# syntax=docker/dockerfile:1
FROM ubuntu:20.04

RUN apt update && apt install -y nano vim python3 python3-pip && pip3 install kaitaistruct && pip3 install msgpack
