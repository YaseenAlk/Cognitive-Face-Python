#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: large_person_group.py
Description: Large Person Group section of the Cognitive Face API.
"""
from . import util
from face_msgs.msg import FaceAPIRequest as req_msg


def create(large_person_group_id, name=None, user_data=None, ros_msg_params=None, ros_msg_body=None):
    """Create a new large person group with specified `large_person_group_id`,
    `name` and user-provided `user_data`.

    Args:
        large_person_group_id: User-provided `large_person_group_id` as a
            string. The valid characters include numbers, English letters in
            lower case, '-' and '_'.  The maximum length is 64.
        name: Name of the created large person group, maximum length is 128.
        user_data: Optional user defined data for the large person group.
            Length should not exceed 16KB.

    Returns:
        An empty response body.
    """
    if ros_msg_params is not None:
        large_person_group_id = ros_msg_params.get("largePersonGroupId", None)
    
    if ros_msg_body is not None:
        name = ros_msg_body.get("name", None)
        user_data = ros_msg_body.get("userData", None)

    util.MostRecentRequest.get().request_parameters = util.json_lib.dumps({'largePersonGroupId': large_person_group_id})

    name = name or large_person_group_id
    url = 'largepersongroups/{}'.format(large_person_group_id)
    json = {
        'name': name,
        'userData': user_data,
    }

    util.MostRecentRequest.get().request_type = req_msg.LARGEPERSONGROUP_CREATE

    return util.request('PUT', url, json=json)


def delete(large_person_group_id, ros_msg_params=None, ros_msg_body=None):
    """Delete an existing large person group. Persisted face images of all
    people in the large person group will also be deleted.

    Args:
        large_person_group_id: The `large_person_group_id` of the large person
            group to be deleted.

    Returns:
        An empty response body.
    """
    if ros_msg_params is not None:
        large_person_group_id = ros_msg_params.get("largePersonGroupId", None)

    util.MostRecentRequest.get().request_parameters = util.json_lib.dumps({'largePersonGroupId': large_person_group_id})

    url = 'largepersongroups/{}'.format(large_person_group_id)

    util.MostRecentRequest.get().request_type = req_msg.LARGEPERSONGROUP_DELETE

    return util.request('DELETE', url)


def get(large_person_group_id, ros_msg_params=None, ros_msg_body=None):
    """Retrieve the information of a large person group, including its `name`
    and `user_data`.

    Args:
        large_person_group_id: `large_person_group_id` of the target large
            person group.

    Returns:
        The large person group's information.
    """
    if ros_msg_params is not None:
        large_person_group_id = ros_msg_params.get("largePersonGroupId", None)

    util.MostRecentRequest.get().request_parameters = util.json_lib.dumps({'largePersonGroupId': large_person_group_id})

    url = 'largepersongroups/{}'.format(large_person_group_id)

    util.MostRecentRequest.get().request_type = req_msg.LARGEPERSONGROUP_GET

    return util.request('GET', url)


def get_status(large_person_group_id, ros_msg_params=None, ros_msg_body=None):
    """Retrieve the training status of the large person group (completed or
    ongoing).  Training can be triggered by `large_person_group.train`. The
    training will process for a while on the server side.

    Args:
        large_person_group_id: `large_person_group_id` of the target large
            person group.

    Returns:
        The large person group's training status.
    """
    if ros_msg_params is not None:
        large_person_group_id = ros_msg_params.get("largePersonGroupId", None)

    util.MostRecentRequest.get().request_parameters = util.json_lib.dumps({'largePersonGroupId': large_person_group_id})

    url = 'largepersongroups/{}/training'.format(large_person_group_id)

    util.MostRecentRequest.get().request_type = req_msg.LARGEPERSONGROUP_GETTRAININGSTATUS

    return util.request('GET', url)


def list(start=None, top=None, ros_msg_params=None, ros_msg_body=None):
    """List large person groups and their information.

    Args:
        start: Optional parameter. List large person groups from the least
            `large_person_group_id` greater than the "start". It contains no
            more than 64 characters. Default is empty.
        top: The number of large person groups to list, ranging in [1, 1000].
            Default is 1000.

    Returns:
        An array of large person groups and their information
        (`large_person_group_id`, `name` and `user_data`).
    """
    if ros_msg_params is not None:
        start = ros_msg_params.get("start", None)
        top = ros_msg_params.get("top", None)

    util.MostRecentRequest.get().request_parameters = util.json_lib.dumps({'start':start, 'top':top})

    url = 'largepersongroups'
    params = {
        'start': start,
        'top': top,
    }

    util.MostRecentRequest.get().request_type = req_msg.LARGEPERSONGROUP_LIST

    return util.request('GET', url, params=params)


def train(large_person_group_id, ros_msg_params=None, ros_msg_body=None):
    """Queue a large person group training task, the training task may not be
        started immediately.

    Args:
        large_person_group_id: Target large person group to be trained.

    Returns:
        An empty JSON body.
    """
    if ros_msg_params is not None:
        large_person_group_id = ros_msg_params.get("largePersonGroupId", None)

    util.MostRecentRequest.get().request_parameters = util.json_lib.dumps({'largePersonGroupId': large_person_group_id})

    url = 'largepersongroups/{}/train'.format(large_person_group_id)

    util.MostRecentRequest.get().request_type = req_msg.LARGEPERSONGROUP_TRAIN

    return util.request('POST', url)


def update(large_person_group_id, name=None, user_data=None, ros_msg_params=None, ros_msg_body=None):
    """Update an existing large person group's `name` and `user_data`. The
    properties which does not appear in request body will not be updated.

    Args:
        large_person_group_id: `large_person_group_id` of the large person
            group to be updated.
        name: Optional parameter. Large person group display name. The maximum
            length is 128.
        user_data: Optional parameter. User-provided data attached to the large
            person group. The size limit is 16KB.

    Returns:
        An empty response body.
    """
    if ros_msg_params is not None:
        large_person_group_id = ros_msg_params.get("largePersonGroupId", None)
    
    if ros_msg_body is not None:
        name = ros_msg_body.get("name", None)
        user_data = ros_msg_body.get("userData", None)

    util.MostRecentRequest.get().request_parameters = util.json_lib.dumps({'largePersonGroupId': large_person_group_id})

    url = 'largepersongroups/{}'.format(large_person_group_id)
    json = {
        'name': name,
        'userData': user_data,
    }

    util.MostRecentRequest.get().request_type = req_msg.LARGEPERSONGROUP_UPDATE

    return util.request('PATCH', url, json=json)
