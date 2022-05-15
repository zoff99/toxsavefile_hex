#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright https://github.com/Green-Sky
#
# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
#
from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class ToxSave(KaitaiStruct):
    """Toxcore save file parser (wip)
    """

    class StateType(Enum):
        nospamkeys = 1
        dht = 2
        friends = 3
        name = 4
        statusmessage = 5
        status = 6
        groups = 7
        tcp_relay = 10
        path_node = 11
        conferences = 20
        end = 255
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.magic = self._io.read_bytes(8)
        if not self.magic == b"\x00\x00\x00\x00\x1F\x1B\xED\x15":
            raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00\x1F\x1B\xED\x15", self.magic, self._io, u"/seq/0")
        self.states = []
        i = 0
        while True:
            _ = ToxSave.State(self._io, self, self._root)
            self.states.append(_)
            if  ((_.type == ToxSave.StateType.end) or (self._io.is_eof())) :
                break
            i += 1

    class State(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.sub_length = self._io.read_u4le()
            self.type = KaitaiStream.resolve_enum(ToxSave.StateType, self._io.read_u2le())
            self.cookie = self._io.read_bytes(2)
            if not self.cookie == b"\xCE\x01":
                raise kaitaistruct.ValidationNotEqualError(b"\xCE\x01", self.cookie, self._io, u"/types/state/seq/2")
            _on = self.type
            if _on == ToxSave.StateType.name:
                self._raw_data = self._io.read_bytes(self.sub_length)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = ToxSave.StateName(_io__raw_data, self, self._root)
            elif _on == ToxSave.StateType.groups:
                self._raw_data = self._io.read_bytes(self.sub_length)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = ToxSave.StateGroups(_io__raw_data, self, self._root)
            else:
                self.data = self._io.read_bytes(self.sub_length)


    class StateName(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.name = (self._io.read_bytes_full()).decode(u"UTF-8")


    class StateGroups(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.pack = self._io.read_bytes_full()


