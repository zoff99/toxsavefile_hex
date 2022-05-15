doc: |
  
  Toxcore save file parser (wip)
  
  Copyright https://github.com/Green-Sky
  

meta:
  id: tox_save
  license: GPL-3.0
  ks-version: 0.9
  endian: le
  imports:
    - /serialization/msgpack

seq:
  - id: magic
    contents: [0x00, 0x00, 0x00, 0x00, 0x1f, 0x1b, 0xed, 0x15]
  - id: states
    type: state
    repeat: until
    repeat-until: _.type == state_type::end or _io.eof

types:
  state:
    seq:
      - id: sub_length
        type: u4
      - id: type
        type: u2
        enum: state_type
      - id: cookie # magic
        contents: [0xce, 0x01]
      - id: data
        size: sub_length
        type:
          switch-on: type
          cases:
            'state_type::name': state_name
            'state_type::groups': state_groups
  state_name:
    seq:
      - id: name
        type: str
        encoding: UTF-8
        size-eos: true
  state_groups:
    seq:
      - id: pack
        type: msgpack
        size-eos: true

enums:
  state_type:
    1: nospamkeys
    2: dht
    3: friends
    4: name
    5: statusmessage
    6: status
    7: groups
    10: tcp_relay
    11: path_node
    20: conferences
    255: end

  
