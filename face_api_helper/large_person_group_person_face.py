#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: large_person_group_person_face.py
Description: Large Person Group Person Face section of the Cognitive Face API.
"""
from . import util
from face_msgs.msg import FaceAPIRequest as req_msg


def add(image,
        large_person_group_id,
        person_id,
        user_data=None,
        target_face=None, ros_msg_params=None, ros_msg_body=None):
    """Add a representative face to a person for identification. The input face
    is specified as an image with a `target_face` rectangle. It returns a
    `persisted_face_id` representing the added face and this
    `persisted_face_id` will not expire.

    Args:
        image: A URL or a file path or a file-like object represents an image.
        large_person_group_id: `large_person_group_id` of the target large
            person group.
        person_id: `person_id` of the target person.
        user_data: Optional parameter. User-specified data about the face list
            for any purpose. The maximum length is 1KB.
        target_face: Optional parameter. A face rectangle to specify the target
            face to be added into the face list, in the format of
            "left,top,width,height". E.g. "10,10,100,100". If there are more
            than one faces in the image, `target_face` is required to specify
            which face to add. No `target_face` means there is only one face
            detected in the entire image.

    Returns:
        A new `persisted_face_id`.
    """
    if ros_msg_params is not None:
        large_person_group_id = ros_msg_params.get("largePersonGroupId", None)
        person_id = ros_msg_params.get("personId", None)
        user_data = ros_msg_params.get("userData", None)
        target_face = ros_msg_params.get("targetFace", None)

    util.MostRecentRequest.get().request_parameters = util.json_lib.dumps({'largePersonGroupId': large_person_group_id, 'personId': person_id, 'userData': user_data, 'targetFace': target_face})

    url = 'largepersongroups/{}/persons/{}/persistedFaces'.format(
        large_person_group_id, person_id)
    headers, data, json = util.parse_image(image if ros_msg_body is None else ros_msg_body)
    params = {
        'userData': user_data,
        'targetFace': target_face,
    }

    util.MostRecentRequest.get().request_type = req_msg.LARGEPERSONGROUPPERSON_ADDFACE

    return util.request(
        'POST', url, headers=headers, params=params, json=json, data=data)


def delete(large_person_group_id, person_id, persisted_face_id, ros_msg_params=None, ros_msg_body=None):
    """Delete a face from a person. Relative image for the persisted face will
    also be deleted.

    Args:
        large_person_group_id: `large_person_group_id` of the target large
            person group.
        person_id: `person_id` of the target person.
        persisted_face_id: The persisted face to remove.

    Returns:
        An empty response body.
    """
    if ros_msg_params is not None:
        large_person_group_id = ros_msg_params.get("largePersonGroupId", None)
        person_id = ros_msg_params.get("personId", None)
        persisted_face_id = ros_msg_params.get("persistedFaceId", None)

    util.MostRecentRequest.get().request_parameters = util.json_lib.dumps({'largePersonGroupId': large_person_group_id, 'personId': person_id, 'persistedFaceId': persisted_face_id})

    url = 'largepersongroups/{}/persons/{}/persistedFaces/{}'.format(
        large_person_group_id, person_id, persisted_face_id)

    util.MostRecentRequest.get().request_type = req_msg.LARGEPERSONGROUPPERSON_DELETEFACE

    return util.request('DELETE', url)


def get(large_person_group_id, person_id, persisted_face_id, ros_msg_params=None, ros_msg_body=None):
    """Retrieve information about a persisted face (specified by
    `persisted_face_ids`, `person_id` and its belonging
    `large_person_group_id`).

    Args:
        large_person_group_id: `large_person_group_id` of the target large
            person group.
        person_id: `person_id` of the target person.
        persisted_face_id: The `persisted_face_id` of the target persisted face
            of the person.

    Returns:
        The target persisted face's information (`persisted_face_id` and
        `user_data`).
    """
    if ros_msg_params is not None:
        large_person_group_id = ros_msg_params.get("largePersonGroupId", None)
        person_id = ros_msg_params.get("personId", None)
        persisted_face_id = ros_msg_params.get("persistedFaceId", None)

    util.MostRecentRequest.get().request_parameters = util.json_lib.dumps({'largePersonGroupId': large_person_group_id, 'personId': person_id, 'persistedFaceId': persisted_face_id})

    url = 'largepersongroups/{}/persons/{}/persistedFaces/{}'.format(
        large_person_group_id, person_id, persisted_face_id)

    util.MostRecentRequest.get().request_type = req_msg.LARGEPERSONGROUPPERSON_GETFACE

    return util.request('GET', url)


def update(large_person_group_id, person_id, persisted_face_id, user_data, ros_msg_params=None, ros_msg_body=None):
    """Update a person persisted face's `user_data` field.

    Args:
        large_person_group_id: `large_person_group_id` of the target large
            person group.
        person_id: `person_id` of the target person.
        persisted_face_id: The `persisted_face_id` of the target persisted face
            of the person.
        user_data: Attach `user_data` to person's persisted face. The size
            limit is 1KB.

    Returns:
        An empty response body.
    """
    if ros_msg_params is not None:
        large_person_group_id = ros_msg_params.get("largePersonGroupId", None)
        person_id = ros_msg_params.get("personId", None)
        persisted_face_id = ros_msg_params.get("persistedFaceId", None)

    if ros_msg_body is not None:
        user_data = ros_msg_body.get("userData", None)

    util.MostRecentRequest.get().request_parameters = util.json_lib.dumps({'largePersonGroupId': large_person_group_id, 'personId': person_id, 'persistedFaceId': persisted_face_id})

    url = 'largepersongroups/{}/persons/{}/persistedFaces/{}'.format(
        large_person_group_id, person_id, persisted_face_id)
    json = {
        'userData': user_data,
    }

    util.MostRecentRequest.get().request_type = req_msg.LARGEPERSONGROUPPERSON_UPDATEFACE

    return util.request('PATCH', url, json=json)
