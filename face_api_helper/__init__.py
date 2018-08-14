#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: __init__.py
Description: Python SDK of the Cognitive Face API.
"""

from . import face
from . import face_list
from . import large_face_list
from . import large_face_list_face
from . import large_person_group
from . import large_person_group_person
from . import large_person_group_person_face
from . import person
from . import person_group
from . import util
from .util import CognitiveFaceException
from .util import Key
from .util import BaseUrl
from .util import MostRecentRequest
from .util import MostRecentResponse
from face_msgs.msg import FaceAPIRequest as req_msg
from face_msgs.msg import FaceAPIResponse as resp_msg

_key_ = None
_baseurl_ = util.DEFAULT_BASE_URL

FACE_MSG_NUM_TO_FUNC = {
    req_msg.FACE_DETECT: face.detect,
	req_msg.FACE_FINDSIMILAR: face.find_similars,
	req_msg.FACE_GROUP: face.group,
	req_msg.FACE_IDENTIFY: face.identify,
	req_msg.FACE_VERIFY: face.verify,

	req_msg.FACELIST_ADDFACE: face_list.add_face,
	req_msg.FACELIST_CREATE: face_list.create,
	req_msg.FACELIST_DELETE: face_list.delete,
	req_msg.FACELIST_DELETEFACE: face_list.delete_face,
	req_msg.FACELIST_GET: face_list.get,
	req_msg.FACELIST_LIST: face_list.lists,
	req_msg.FACELIST_UPDATE: face_list.update,

	req_msg.LARGEFACELIST_ADDFACE: large_face_list_face.add,
	req_msg.LARGEFACELIST_CREATE: large_face_list.create,
	req_msg.LARGEFACELIST_DELETE: large_face_list.delete,
	req_msg.LARGEFACELIST_DELETEFACE: large_face_list_face.delete,
	req_msg.LARGEFACELIST_GET: large_face_list.get,
	req_msg.LARGEFACELIST_GETFACE: large_face_list_face.get,
	req_msg.LARGEFACELIST_GETTRAININGSTATUS: large_face_list.get_status,
	req_msg.LARGEFACELIST_LIST: large_face_list.list,
	req_msg.LARGEFACELIST_LISTFACE: large_face_list_face.list,
	req_msg.LARGEFACELIST_TRAIN: large_face_list.train,
	req_msg.LARGEFACELIST_UPDATE: large_face_list.update,
	req_msg.LARGEFACELIST_UPDATEFACE: large_face_list_face.update,

	req_msg.LARGEPERSONGROUP_CREATE: large_person_group.create,
	req_msg.LARGEPERSONGROUP_DELETE: large_person_group.delete,
	req_msg.LARGEPERSONGROUP_GET: large_person_group.get,
	req_msg.LARGEPERSONGROUP_GETTRAININGSTATUS: large_person_group.get_status,
	req_msg.LARGEPERSONGROUP_LIST: large_person_group.list,
	req_msg.LARGEPERSONGROUP_TRAIN: large_person_group.train,
	req_msg.LARGEPERSONGROUP_UPDATE: large_person_group.update,

	req_msg.LARGEPERSONGROUPPERSON_ADDFACE: large_person_group_person_face.add,
	req_msg.LARGEPERSONGROUPPERSON_CREATE: large_person_group_person.create,
	req_msg.LARGEPERSONGROUPPERSON_DELETE: large_person_group_person.delete,
	req_msg.LARGEPERSONGROUPPERSON_DELETEFACE: large_person_group_person_face.delete,
	req_msg.LARGEPERSONGROUPPERSON_GET: large_person_group_person.get,
	req_msg.LARGEPERSONGROUPPERSON_GETFACE: large_person_group_person_face.get,
	req_msg.LARGEPERSONGROUPPERSON_LIST: large_person_group_person.list,
	req_msg.LARGEPERSONGROUPPERSON_UPDATE: large_person_group_person.update,
	req_msg.LARGEPERSONGROUPPERSON_UPDATEFACE: large_person_group_person_face.update,

	req_msg.PERSONGROUP_CREATE: person_group.create,
	req_msg.PERSONGROUP_DELETE: person_group.delete,
	req_msg.PERSONGROUP_GET: person_group.get,
	req_msg.PERSONGROUP_GETTRAININGSTATUS: person_group.get_status,
	req_msg.PERSONGROUP_LIST: person_group.lists,
	req_msg.PERSONGROUP_TRAIN: person_group.train,
	req_msg.PERSONGROUP_UPDATE: person_group.update,

	req_msg.PERSONGROUPPERSON_ADDFACE: person.add_face,
	req_msg.PERSONGROUPPERSON_CREATE: person.create,
	req_msg.PERSONGROUPPERSON_DELETE: person.delete,
	req_msg.PERSONGROUPPERSON_DELETEFACE: person.delete_face,
	req_msg.PERSONGROUPPERSON_GET: person.get,
	req_msg.PERSONGROUPPERSON_GETFACE: person.get_face,
	req_msg.PERSONGROUPPERSON_LIST: person.lists,
	req_msg.PERSONGROUPPERSON_UPDATE: person.update,
	req_msg.PERSONGROUPPERSON_UPDATEFACE: person.update_face
}