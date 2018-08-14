#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: util.py
Description: Shared utilities for the Python SDK of the Cognitive Face API.
"""
import sys
import os.path
import time

import json as json_lib
import requests

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

import face_api_helper as CF

from face_msgs.msg import FaceAPIRequest as req_msg
from face_msgs.msg import FaceAPIResponse as resp_msg

DEFAULT_BASE_URL = 'https://westus.api.cognitive.microsoft.com/face/v1.0/'

TIME_SLEEP = 1


class CognitiveFaceException(Exception):
    """Custom Exception for the python SDK of the Cognitive Face API.

    Attributes:
        status_code: HTTP response status code.
        code: error code.
        msg: error message.
    """

    def __init__(self, status_code, code, msg):
        super(CognitiveFaceException, self).__init__()
        self.status_code = status_code
        self.code = code
        self.msg = msg

    def __str__(self):
        return ('Error when calling Cognitive Face API:\n'
                '\tstatus_code: {}\n'
                '\tcode: {}\n'
                '\tmessage: {}\n').format(self.status_code, self.code,
                                          self.msg)


class Key(object):
    """Manage Subscription Key."""

    @classmethod
    def set(cls, key):
        """Set the Subscription Key."""
        cls.key = key
        MostRecentRequest.get().api_subscription_key = key
        CF._key_ = key

    @classmethod
    def get(cls):
        """Get the Subscription Key."""
        if not hasattr(cls, 'key'):
            cls.key = None
        return cls.key


class BaseUrl(object):
    @classmethod
    def set(cls, base_url):
        if not base_url.endswith('/'):
            base_url += '/'
        cls.base_url = base_url
        MostRecentRequest.get().location = base_url
        CF._baseurl_ = base_url

    @classmethod
    def get(cls):
        if not hasattr(cls, 'base_url') or not cls.base_url:
            cls.base_url = DEFAULT_BASE_URL
        return cls.base_url

class MostRecentRequest(object):
    @classmethod
    def get(cls):
        if not hasattr(cls, 'most_recent_request') or not cls.most_recent_request:
            cls.most_recent_request = req_msg()
        return cls.most_recent_request

class MostRecentResponse(object):
    @classmethod
    def get(cls):
        if not hasattr(cls, 'most_recent_response') or not cls.most_recent_response:
            cls.most_recent_response = resp_msg()
        return cls.most_recent_response


def init_from_json_str(json_str):
    Key.set(read_json_param_from_str(json_str, "subscriptionKey"))
    BaseUrl.set(read_json_param_from_str(json_str, "uriBase"))

def read_json_param_from_str(string, param):
        dictionary = json_lib.loads(string)
        return dictionary[param]

def is_json_str(string):
    try:
        json_lib.loads(string)
        return True
    except ValueError:
        return False

def bytearr_to_json_str(arr):
    my_json = arr.decode('utf8').replace("'", '"')
    data = json_lib.loads(my_json)
    return json_lib.dumps(data)
    
def make_req_using_ros_msg(msg_request):
    req_params = get_params_from_ros_msg(msg_request)
    converted_body = bytearr_to_json_str(msg_request.request_body) if is_json_str(msg_request.request_body.decode('utf8').replace("'", '"')) else msg_request.request_body
    func_to_exec = CF.FACE_MSG_NUM_TO_FUNC.get(msg_request.request_type, None)

    if func_to_exec is None:
        raise ValueError("Unknown API request type... Make sure you are passing in a valid FaceAPIRequest msg")
    
    func_arguments = func_to_exec.__code__.co_varnames[:func_to_exec.__code__.co_argcount]
    passed_args = {}
    for arg in func_arguments:
        passed_args[arg] = None
    passed_args['ros_msg_params'] = req_params
    passed_args['ros_msg_body'] = json_lib.loads(converted_body)
    
    return func_to_exec(**passed_args)

def get_params_from_ros_msg(msg_request, params_to_get=None):
    msg_params = json_lib.loads(msg_request.request_parameters)
    returned_dict = {}
    if params_to_get is not None:
        for p in params_to_get:
            val = msg_params.get(p, None)
            if val is not None:
                returned_dict[p] = val
    else:
        returned_dict = msg_params
    return returned_dict

def request(method, url, data=None, json=None, headers=None, params=None):
    # pylint: disable=too-many-arguments
    """Universal interface for request."""

    # Make it possible to call only with short name (without BaseUrl).
    if not url.startswith('https://'):
        url = CF._baseurl_ + url

    # Setup the headers with default Content-Type and Subscription Key.
    headers = headers or {}
    if 'Content-Type' not in headers:
        headers['Content-Type'] = 'application/json'
    headers['Ocp-Apim-Subscription-Key'] = CF._key_

    req_msg_method = -1

    if method.lower() == 'post':
        req_msg_method = req_msg.HTTP_POST
    elif method.lower() == 'put':
        req_msg_method = req_msg.HTTP_PUT
    elif method.lower() == 'delete':
        req_msg_method = req_msg.HTTP_DELETE
    elif method.lower() == 'get':
        req_msg_method = req_msg.HTTP_GET
    elif method.lower() == 'patch':
        req_msg_method = req_msg.HTTP_PATCH
    
    MostRecentRequest.get().request_method = req_msg_method
    MostRecentRequest.get().content_type = headers['Content-Type']
    MostRecentRequest.get().request_body = data if headers['Content-Type'] == 'application/octet-stream' else json_lib.dumps(json).encode('utf-8')
    
    response = requests.request(
        method,
        url,
        params=params,
        data=data,
        json=json,
        headers=headers)

    MostRecentResponse.get().response_type = response.status_code
    MostRecentResponse.get().response = response.text

    # Handle result and raise custom exception when something wrong.
    result = None
    # `person_group.train` return 202 status code for success.
    if response.status_code not in (200, 202):
        try:
            error_msg = response.json()['error']
        except:
            raise CognitiveFaceException(response.status_code,
                                         response.status_code, response.text)
        raise CognitiveFaceException(response.status_code,
                                     error_msg.get('code'),
                                     error_msg.get('message'))

    # Prevent `response.json()` complains about empty response.
    if response.text:
        result = response.json()
    else:
        result = {}

    return result


def parse_image(image):
    """Parse the image smartly and return metadata for request.

    First check whether the image is a URL or a file path or a file-like object
    and return corresponding metadata.

    Args:
        image: A URL or a file path or a file-like object represents an image.

    Returns:
        a three-item tuple consist of HTTP headers, binary data and json data
        for POST.
    """
    if hasattr(image, 'read'):  # When image is a file-like object.
        headers = {'Content-Type': 'application/octet-stream'}
        data = image.read()
        return headers, data, None
    elif os.path.isfile(image):  # When image is a file path.
        headers = {'Content-Type': 'application/octet-stream'}
        data = open(image, 'rb').read()
        return headers, data, None
    elif is_json_str(image) and "url" in json_lib.loads(image).keys():
        return parse_image(json_lib.loads(image)["url"])
    else:  # Default treat it as a URL (string).
        headers = {'Content-Type': 'application/json'}
        json = {'url': image}
        return headers, None, json


def wait_for_person_group_training(person_group_id):
    """Wait for the finish of person group training."""
    idx = 1
    while True:
        res = CF.person_group.get_status(person_group_id)
        if res['status'] in ('succeeded', 'failed'):
            break
        print('The training of Person Group {} is onging: #{}'.format(
            person_group_id, idx))
        time.sleep(2**idx)
        idx += 1


def wait_for_large_face_list_training(large_face_list_id):
    """Wait for the finish of large face list training."""
    idx = 1
    while True:
        res = CF.large_face_list.get_status(large_face_list_id)
        if res['status'] in ('succeeded', 'failed'):
            break
        print('The training of Large Face List {} is onging: #{}'.format(
            large_face_list_id, idx))
        time.sleep(2**idx)
        idx += 1


def wait_for_large_person_group_training(large_person_group_id):
    """Wait for the finish of large person group training."""
    idx = 1
    while True:
        res = CF.large_person_group.get_status(large_person_group_id)
        if res['status'] in ('succeeded', 'failed'):
            break
        print('The training of Large Person Group {} is onging: #{}'.format(
            large_person_group_id, idx))
        time.sleep(2**idx)
        idx += 1


def clear_face_lists():
    """[Dangerous] Clear all the face lists and all related persisted data."""
    face_lists = CF.face_list.lists()
    time.sleep(TIME_SLEEP)
    for face_list in face_lists:
        face_list_id = face_list['faceListId']
        CF.face_list.delete(face_list_id)
        print('Deleting Face List {}'.format(face_list_id))
        time.sleep(TIME_SLEEP)


def clear_person_groups():
    """[Dangerous] Clear all the person groups and all related persisted data.
    """
    person_groups = CF.person_group.lists()
    time.sleep(TIME_SLEEP)
    for person_group in person_groups:
        person_group_id = person_group['personGroupId']
        CF.person_group.delete(person_group_id)
        print('Deleting Person Group {}'.format(person_group_id))
        time.sleep(TIME_SLEEP)


def clear_large_face_lists():
    """[Dangerous] Clear all the large face lists and all related persisted
    data.
    """
    large_face_lists = CF.large_face_list.list()
    time.sleep(TIME_SLEEP)
    for large_face_list in large_face_lists:
        large_face_list_id = large_face_list['largeFaceListId']
        CF.large_face_list.delete(large_face_list_id)
        print('Deleting Large Face List {}'.format(large_face_list_id))
        time.sleep(TIME_SLEEP)


def clear_large_person_groups():
    """[Dangerous] Clear all the large person groups and all related persisted
    data.
    """
    large_person_groups = CF.large_person_group.list()
    time.sleep(TIME_SLEEP)
    for large_person_group in large_person_groups:
        large_person_group_id = large_person_group['largePersonGroupId']
        CF.large_person_group.delete(large_person_group_id)
        print('Deleting Large Person Group {}'.format(large_person_group_id))
        time.sleep(TIME_SLEEP)
