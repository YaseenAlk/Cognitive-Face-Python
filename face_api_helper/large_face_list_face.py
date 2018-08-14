#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: large_face_list_face.py
Description: Large Face List Face section of the Cognitive Face API.
"""
from . import util
from face_msgs.msg import FaceAPIRequest as req_msg


def add(image, large_face_list_id, user_data=None, target_face=None, ros_msg_params=None, ros_msg_body=None):
    """Add a face to a large face list.

    The input face is specified as an image with a `target_face` rectangle. It
    returns a `persisted_face_id` representing the added face, and
    `persisted_face_id` will not expire.

    Args:
        image: A URL or a file path or a file-like object represents an image.
        large_face_list_id: Valid character is letter in lower case or digit or
            '-' or '_', maximum length is 64.
        user_data: Optional parameter. User-specified data about the large face
            list for any purpose. The maximum length is 1KB.
        target_face: Optional parameter. A face rectangle to specify the target
            face to be added into the large face list, in the format of
            "left,top,width,height". E.g. "10,10,100,100". If there are more
            than one faces in the image, `target_face` is required to specify
            which face to add. No `target_face` means there is only one face
            detected in the entire image.

    Returns:
        A new `persisted_face_id`.
    """
    if ros_msg_params is not None:
        large_face_list_id = ros_msg_params.get("largeFaceListId", None)
        user_data = ros_msg_params.get("userData", None)
        target_face = ros_msg_params.get("targetFace", None)
    
    url = 'largefacelists/{}/persistedFaces'.format(large_face_list_id)
    headers, data, json = util.parse_image(image if ros_msg_body is None else ros_msg_body)
    params = {
        'userData': user_data,
        'targetFace': target_face,
    }

    util.MostRecentRequest.get().request_type = req_msg.LARGEFACELIST_ADDFACE

    return util.request(
        'POST', url, headers=headers, params=params, json=json, data=data)


def delete(large_face_list_id, persisted_face_id, ros_msg_params=None, ros_msg_body=None):
    """Delete an existing face from a large face list (given by a
    `persisted_face_id` and a `large_face_list_id`). Persisted image related to
    the face will also be deleted.

    Args:
        large_face_list_id: Valid character is letter in lower case or digit or
            '-' or '_', maximum length is 64.
        persisted_face_id: `persisted_face_id` of an existing face. Valid
            character is letter in lower case or digit or '-' or '_', maximum
            length is 64.

    Returns:
        An empty response body.
    """
    if ros_msg_params is not None:
        large_face_list_id = ros_msg_params.get("largeFaceListId", None)
        persisted_face_id = ros_msg_params.get("persistedFaceId", None)
    
    url = 'largefacelists/{}/persistedFaces/{}'.format(large_face_list_id,
                                                       persisted_face_id)

    util.MostRecentRequest.get().request_type = req_msg.LARGEFACELIST_DELETEFACE

    return util.request('DELETE', url)


def get(large_face_list_id, persisted_face_id, ros_msg_params=None, ros_msg_body=None):
    """Retrieve information about a persisted face (specified by
    `persisted_face_id` and a `large_face_list_id`).

    Args:
        large_face_list_id: Valid character is letter in lower case or digit or
            '-' or '_', maximum length is 64.
        persisted_face_id: `persisted_face_id` of an existing face. Valid
            character is letter in lower case or digit or '-' or '_', maximum
            length is 64.

    Returns:
        The target persisted face's information (`persisted_face_id` and
        `user_data`).
    """
    if ros_msg_params is not None:
        large_face_list_id = ros_msg_params.get("largeFaceListId", None)
        persisted_face_id = ros_msg_params.get("persistedFaceId", None)

    url = 'largefacelists/{}/persistedFaces/{}'.format(large_face_list_id,
                                                       persisted_face_id)

    util.MostRecentRequest.get().request_type = req_msg.LARGEFACELIST_GETFACE

    return util.request('GET', url)


def list(large_face_list_id, start=None, top=None, ros_msg_params=None, ros_msg_body=None):
    """Retrieve information (`persisted_face_id` and `user_data`) about
    existing persisted faces in a large face list.

    Args:
        start: Optional parameter. List large face lists from the least
            `large_face_list_id` greater than the "start". It contains no more
            than 64 characters. Default is empty.
        top: The number of large face lists to list, ranging in [1, 1000].
            Default is 1000.

    Returns:
        An array of persisted faces and their information (`persisted_face_id`
        and `user_data`).
    """
    if ros_msg_params is not None:
        large_face_list_id = ros_msg_params.get("largeFaceListId", None)
        start = ros_msg_params.get("start", None)
        top = ros_msg_params.get("top", None)

    url = 'largefacelists/{}/persistedFaces'.format(large_face_list_id)
    params = {
        'start': start,
        'top': top,
    }

    util.MostRecentRequest.get().request_type = req_msg.LARGEFACELIST_LISTFACE

    return util.request('GET', url, params=params)


def update(large_face_list_id, persisted_face_id, user_data=None, ros_msg_params=None, ros_msg_body=None):
    """Update a persisted face's `user_data` field in a large face list.

    Args:
        large_face_list_id: largeFaceListId of an existing large face list.
            person.
        person_id: `person_id` of the target person.
        persisted_face_id: `persisted_face_id` of the target face, which is
            persisted and will not expire.
        user_data: Optional parameter. Attach `user_data` to person's
            persisted face. The size limit is 1KB.

    Returns:
        An empty response body.
    """
    if ros_msg_params is not None:
        large_face_list_id = ros_msg_params.get("largeFaceListId", None)
        persisted_face_id = ros_msg_params.get("persistedFaceId", None)
    
    if ros_msg_body is not None:
        user_data = ros_msg_body.get("userData", None)

    url = 'largefacelists/{}/persistedFaces/{}'.format(large_face_list_id,
                                                       persisted_face_id)
    json = {
        'userData': user_data,
    }

    util.MostRecentRequest.get().request_type = req_msg.LARGEFACELIST_UPDATEFACE

    return util.request('PATCH', url, json=json)
