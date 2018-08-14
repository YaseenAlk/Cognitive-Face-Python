#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: person_group.py
Description: Person Group section of the Cognitive Face API.
"""
from . import util
from face_msgs.msg import FaceAPIRequest as req_msg


def create(person_group_id, name=None, user_data=None, ros_msg_params=None, ros_msg_body=None):
    """Create a new person group with specified `person_group_id`, `name` and
    user-provided `user_data`.

    Args:
        person_group_id: User-provided `person_group_id` as a string. The valid
            characters include numbers, English letters in lower case, '-' and
            '_'.  The maximum length of the personGroupId is 64.i
        name: Person group display name. The maximum length is 128.
        user_data: User-provided data attached to the person group. The size
            limit is 16KB.

    Returns:
        An empty response body.
    """
    if ros_msg_params is not None:
        person_group_id = ros_msg_params.get("personGroupId", None)
    
    if ros_msg_body is not None:
        name = ros_msg_body.get("name", None)
        user_data = ros_msg_body.get("userData", None)

    name = name or person_group_id
    url = 'persongroups/{}'.format(person_group_id)
    json = {
        'name': name,
        'userData': user_data,
    }

    util.MostRecentRequest.get().request_type = req_msg.PERSONGROUP_CREATE

    return util.request('PUT', url, json=json)


def delete(person_group_id, ros_msg_params=None, ros_msg_body=None):
    """Delete an existing person group. Persisted face images of all people in
    the person group will also be deleted.

    Args:
        person_group_id: The `person_group_id` of the person group to be
            deleted.

    Returns:
        An empty response body.
    """
    if ros_msg_params is not None:
        person_group_id = ros_msg_params.get("personGroupId", None)

    url = 'persongroups/{}'.format(person_group_id)

    util.MostRecentRequest.get().request_type = req_msg.PERSONGROUP_DELETE

    return util.request('DELETE', url)


def get(person_group_id, ros_msg_params=None, ros_msg_body=None):
    """Retrieve the information of a person group, including its `name` and
    `user_data`. This API returns person group information only, use
    `person.lists` instead to retrieve person information under the person
    group.

    Args:
        person_group_id: `person_group_id` of the target person group.

    Returns:
        The person group's information.
    """
    if ros_msg_params is not None:
        person_group_id = ros_msg_params.get("personGroupId", None)

    url = 'persongroups/{}'.format(person_group_id)

    util.MostRecentRequest.get().request_type = req_msg.PERSONGROUP_GET

    return util.request('GET', url)


def get_status(person_group_id, ros_msg_params=None, ros_msg_body=None):
    """Retrieve the training status of a person group (completed or ongoing).
    Training can be triggered by `person_group.train`. The training will
    process for a while on the server side.

    Args:
        person_group_id: `person_group_id` of the target person group.

    Returns:
        The person group's training status.
    """
    if ros_msg_params is not None:
        person_group_id = ros_msg_params.get("personGroupId", None)

    url = 'persongroups/{}/training'.format(person_group_id)

    util.MostRecentRequest.get().request_type = req_msg.PERSONGROUP_GETTRAININGSTATUS

    return util.request('GET', url)


def lists(start=None, top=None, ros_msg_params=None, ros_msg_body=None):
    """List person groups and their information.

    Args:
        start: Optional parameter. List person groups from the least
            `person_group_id` greater than the "start". It contains no more
            than 64 characters. Default is empty.
        top: The number of person groups to list, ranging in [1, 1000]. Default
            is 1000.

    Returns:
        An array of person groups and their information (`person_group_id`,
        `name` and `user_data`).
    """
    if ros_msg_params is not None:
        start = ros_msg_params.get("start", None)
        top = ros_msg_params.get("top", None)

    url = 'persongroups'
    params = {
        'start': start,
        'top': top,
    }

    util.MostRecentRequest.get().request_type = req_msg.PERSONGROUP_LIST

    return util.request('GET', url, params=params)


def train(person_group_id, ros_msg_params=None, ros_msg_body=None):
    """Queue a person group training task, the training task may not be started
    immediately.

    Args:
        person_group_id: Target person group to be trained.

    Returns:
        An empty JSON body.
    """
    if ros_msg_params is not None:
        person_group_id = ros_msg_params.get("personGroupId", None)

    url = 'persongroups/{}/train'.format(person_group_id)

    util.MostRecentRequest.get().request_type = req_msg.PERSONGROUP_TRAIN

    return util.request('POST', url)


def update(person_group_id, name=None, user_data=None, ros_msg_params=None, ros_msg_body=None):
    """Update an existing person group's display `name` and `user_data`. The
    properties which does not appear in request body will not be updated.

    Args:
        person_group_id: `person_group_id` of the person group to be updated.
        name: Optional parameter. Person group display name. The maximum length
            is 128.
        user_data: Optional parameter. User-provided data attached to the
            person group. The size limit is 16KB.

    Returns:
        An empty response body.
    """
    if ros_msg_params is not None:
        person_group_id = ros_msg_params.get("personGroupId", None)
    
    if ros_msg_body is not None:
        name = ros_msg_body.get("name", None)
        user_data = ros_msg_body.get("userData", None)

    url = 'persongroups/{}'.format(person_group_id)
    json = {
        'name': name,
        'userData': user_data,
    }

    util.MostRecentRequest.get().request_type = req_msg.PERSONGROUP_UPDATE

    return util.request('PATCH', url, json=json)
