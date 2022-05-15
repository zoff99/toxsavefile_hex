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
    binary_file = open("./tox_dump." + str(state.type).split(".")[1] + ".dat", "wb")
    if (type(state.data) == bytes):
        binary_file.write(state.data)
    else:
        if (type(state.data) != ToxSave.StateName):
            binary_file.write(state.data.pack)
        else:
            binary_file.write(state._raw_data)
    binary_file.close()

    if state.type == ToxSave.StateType.groups:
        try:
            unpacked_save = msgpack.unpackb(state.data.pack, raw=False)
            print(json.dumps(unpacked_save, default=json_serialiser, indent=2))
        except:
            print("Error with group unpacking")


