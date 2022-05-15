# syntax=docker/dockerfile:1
FROM ubuntu:20.04

RUN export DEBIAN_FRONTEND=noninteractive ; apt update && apt install -y nano vim python3 python3-pip && pip3 install kaitaistruct && pip3 install msgpack
RUN export DEBIAN_FRONTEND=noninteractive ; apt install -y openjdk-11-jdk wget unzip git
RUN cd /usr/local/ ; wget https://github.com/kaitai-io/kaitai_struct_compiler/releases/download/0.9/kaitai-struct-compiler-0.9.zip && unzip kaitai-struct-compiler-0.9.zip
