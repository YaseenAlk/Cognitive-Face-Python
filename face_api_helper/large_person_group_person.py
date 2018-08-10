#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: large_person_group_person.py
Description: Large Person Group Person section of the Cognitive Face API.
"""
from . import util
from face_msgs.msg import FaceAPIRequest as req_msg


def create(large_person_group_id, name, user_data=None):
    """Create a new person in a specified large person group. A newly created
    person have no registered face.

    Args:
        large_person_group_id: `large_person_group_id` of the target large
            person group.
        name: Name of the created person, maximum length is 128.
        user_data: Optional user defined data for the person. Length should not
            exceed 16KB.

    Returns:
        A new `person_id` created.
    """
    url = 'largepersongroups/{}/persons'.format(large_person_group_id)
    json = {
        'name': name,
        'userData': user_data,
    }

    util.MostRecentRequest.get().request_type = req_msg.LARGEPERSONGROUPPERSON_CREATE

    return util.request('POST', url, json=json)


def delete(large_person_group_id, person_id):
    """Delete an existing person from a large person group. Persisted face
    images of the person will also be deleted.

    Args:
        large_person_group_id: `large_person_group_id` of the target large
            person group.
        person_id: personId of the target person.

    Returns:
        An empty response body.
    """
    url = 'largepersongroups/{}/persons/{}'.format(large_person_group_id,
                                                   person_id)

    util.MostRecentRequest.get().request_type = req_msg.LARGEPERSONGROUPPERSON_DELETE

    return util.request('DELETE', url)


def get(large_person_group_id, person_id):
    """Retrieve a person's information, including registered persisted faces,
    `name` and `user_data`.

    Args:
        large_person_group_id: `large_person_group_id` of the target large
            person group.
        person_id: Specifying the target person.

    Returns:
        The person's information.
    """
    url = 'largepersongroups/{}/persons/{}'.format(large_person_group_id,
                                                   person_id)

    util.MostRecentRequest.get().request_type = req_msg.LARGEPERSONGROUPPERSON_GET

    return util.request('GET', url)


def list(large_person_group_id, start=None, top=None):
    """List `top` persons in a large person group with `person_id` greater than
    `start`, and retrieve person information (including `person_id`, `name`,
    `user_data` and `persisted_face_ids` of registered faces of the person).

    Args:
        large_person_group_id: `large_person_group_id` of the target large
            person group.
        start: List persons from the least `person_id` greater than this.
        top: The number of persons to list, rangeing in [1, 1000]. Default is
            1000.

    Returns:
        An array of person information that belong to the large person group.
    """
    url = 'largepersongroups/{}/persons'.format(large_person_group_id)
    params = {
        'start': start,
        'top': top,
    }

    util.MostRecentRequest.get().request_type = req_msg.LARGEPERSONGROUPPERSON_LIST

    return util.request('GET', url, params=params)


def update(large_person_group_id, person_id, name=None, user_data=None):
    """Update `name` or `user_data` of a person.

    Args:
        large_person_group_id: `large_person_group_id` of the target large
            person group.
        person_id: `person_id` of the target person.
        name: Name of the created person, maximum length is 128.
        user_data: Optional user defined data for the person. Length should not
            exceed 16KB.

    Returns:
        An empty response body.
    """
    url = 'largepersongroups/{}/persons/{}'.format(large_person_group_id,
                                                   person_id)
    json = {
        'name': name,
        'userData': user_data,
    }

    util.MostRecentRequest.get().request_type = req_msg.LARGEPERSONGROUPPERSON_UPDATE

    return util.request('PATCH', url, json=json)
