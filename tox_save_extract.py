#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright https://github.com/Green-Sky
#
from tox_save import ToxSave
import msgpack
import json
import base64
import string

save = ToxSave.from_file("./tox_save.tox")

def is_container_printable(obj):
    for i in obj:
        if chr(i) not in string.printable:
            return False
    return True

def json_serialiser(byte_obj):
    if isinstance(byte_obj, (bytes, bytearray)):
        if is_container_printable(byte_obj):
            return byte_obj.decode('utf-8')
        else:
            # Bytes to Base64 Bytes then to String
            return base64.b64encode(byte_obj).decode('utf-8')
    raise ValueError('No encoding handler for data type ' + type(byte_obj))

for state in save.states:
    print(state.type)
    if state.type == ToxSave.StateType.groups:
        unpacked_save = msgpack.unpackb(state.data.pack, raw=False)
        print(json.dumps(unpacked_save, default=json_serialiser, indent=2))
