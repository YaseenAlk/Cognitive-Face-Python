#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: large_face_list.py
Description: Large Face List section of the Cognitive Face API.
"""
from . import util
from face_msgs.msg import FaceAPIRequest as req_msg


def create(large_face_list_id, name=None, user_data=None, ros_msg_params=None, ros_msg_body=None):
    """Create an empty large face list with user-specified
    `large_face_list_id`, `name` and an optional `user_data`.

    Args:
        large_face_list_id: Valid character is letter in lower case or digit or
            '-' or '_', maximum length is 64.
        name: Name of the created large face list, maximum length is 128.
        user_data: Optional parameter. User-defined data for the large face
            list.  Length should not exceed 16KB.

    Returns:
        An empty response body.
    """
    if ros_msg_params is not None:
        large_face_list_id = ros_msg_params.get("largeFaceListId", None)
    
    if ros_msg_body is not None:
        name = ros_msg_body.get("name", None)
        user_data = ros_msg_body.get("userData", None)

    util.MostRecentRequest.get().request_parameters = util.json_lib.dumps({'largeFaceListId': large_face_list_id})

    name = name or large_face_list_id
    url = 'largefacelists/{}'.format(large_face_list_id)
    json = {
        'name': name,
        'userData': user_data,
    }

    util.MostRecentRequest.get().request_type = req_msg.LARGEFACELIST_CREATE

    return util.request('PUT', url, json=json)


def delete(large_face_list_id, ros_msg_params=None, ros_msg_body=None):
    """Delete an existing large face list according to `large_face_list_id`.
    Persisted face images in the large face list will also be deleted.

    Args:
        large_face_list_id: Valid character is letter in lower case or digit or
            '-' or '_', maximum length is 64.

    Returns:
        An empty response body.
    """
    if ros_msg_params is not None:
        large_face_list_id = ros_msg_params.get("largeFaceListId", None)

    util.MostRecentRequest.get().request_parameters = util.json_lib.dumps({'largeFaceListId': large_face_list_id})

    url = 'largefacelists/{}'.format(large_face_list_id)

    util.MostRecentRequest.get().request_type = req_msg.LARGEFACELIST_DELETE

    return util.request('DELETE', url)


def get(large_face_list_id, ros_msg_params=None, ros_msg_body=None):
    """Retrieve a large face list's information, including
    `large_face_list_id`, `name`, `user_data`. Large face list simply
    represents a list of faces, and could be treated as a searchable data
    source in `face.find_similars`.

    Args:
        large_face_list_id: Valid character is letter in lower case or digit or
            '-' or '_', maximum length is 64.

    Returns:
        The large face list's information.
    """
    if ros_msg_params is not None:
        large_face_list_id = ros_msg_params.get("largeFaceListId", None)

    util.MostRecentRequest.get().request_parameters = util.json_lib.dumps({'largeFaceListId': large_face_list_id})

    url = 'largefacelists/{}'.format(large_face_list_id)

    util.MostRecentRequest.get().request_type = req_msg.LARGEFACELIST_GET

    return util.request('GET', url)


def get_status(large_face_list_id, ros_msg_params=None, ros_msg_body=None):
    """Retrieve the training status of a large face list (completed or
    ongoing). Training can be triggered by `large_face_list.train`. The
    training will process for a while on the server side.

    Args:
        large_face_list_id: `large_face_list_id` of the target large face list.

    Returns:
        The large face list's training status.
    """
    if ros_msg_params is not None:
        large_face_list_id = ros_msg_params.get("largeFaceListId", None)

    util.MostRecentRequest.get().request_parameters = util.json_lib.dumps({'largeFaceListId': large_face_list_id})

    url = 'largefacelists/{}/training'.format(large_face_list_id)

    util.MostRecentRequest.get().request_type = req_msg.LARGEFACELIST_GETTRAININGSTATUS

    return util.request('GET', url)


def list(start=None, top=None, ros_msg_params=None, ros_msg_body=None):
    """Retrieve information about all existing large face lists. Only
    `large_face_list_id`, `name` and `user_data` will be returned.

    Args:
        start: Optional parameter. List large face lists from the least
            `large_face_list_id` greater than the "start". It contains no more
            than 64 characters. Default is empty.
        top: The number of large face lists to list, ranging in [1, 1000].
            Default is 1000.

    Returns:
        An array of large face lists.
    """
    if ros_msg_params is not None:
        start = ros_msg_params.get("start", None)
        top = ros_msg_params.get("top", None)

    util.MostRecentRequest.get().request_parameters = util.json_lib.dumps({'start': start, 'top': top})

    url = 'largefacelists'
    params = {
        'start': start,
        'top': top,
    }

    util.MostRecentRequest.get().request_type = req_msg.LARGEFACELIST_LIST

    return util.request('GET', url, params=params)


def train(large_face_list_id, ros_msg_params=None, ros_msg_body=None):
    """Queue a large face list training task, the training task may not be
    started immediately.

    Args:
        large_face_list_id: Target large face list to be trained.

    Returns:
        An empty JSON body.
    """
    if ros_msg_params is not None:
        large_face_list_id = ros_msg_params.get("largeFaceListId", None)

    util.MostRecentRequest.get().request_parameters = util.json_lib.dumps({'largeFaceListId': large_face_list_id})

    url = 'largefacelists/{}/train'.format(large_face_list_id)

    util.MostRecentRequest.get().request_type = req_msg.LARGEFACELIST_TRAIN

    return util.request('POST', url)


def update(large_face_list_id, name=None, user_data=None, ros_msg_params=None, ros_msg_body=None):
    """Update information of a large face list, including `name` and `user_data`.

    Args:
        large_face_list_id: Valid character is letter in lower case or digit or
            '-' or '_', maximum length is 64.
        name: Name of the created large face list, maximum length is 128.
        user_data: Optional parameter. User-defined data for the large face
            list. Length should not exceed 16KB.

    Returns:
        An empty response body.
    """
    if ros_msg_params is not None:
        large_face_list_id = ros_msg_params.get("largeFaceListId", None)
    
    if ros_msg_body is not None:
        name = ros_msg_body.get("name", None)
        user_data = ros_msg_body.get("userData", None)

    util.MostRecentRequest.get().request_parameters = util.json_lib.dumps({'largeFaceListId': large_face_list_id})

    url = 'largefacelists/{}'.format(large_face_list_id)
    json = {
        'name': name,
        'userData': user_data,
    }

    util.MostRecentRequest.get().request_type = req_msg.LARGEFACELIST_UPDATE

    return util.request('PATCH', url, json=json)
