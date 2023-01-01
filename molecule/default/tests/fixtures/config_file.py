
import re

import pytest


@pytest.fixture
def interface_block_regex():
    def _interface_block_regex(address, port):
        return rf'''\[Interface\]
ListenPort={port}
PrivateKey=[^\n]*
Address={address}'''
    return _interface_block_regex


@pytest.fixture
def peer_block_regex():
    def _peer_block_regex(name, address, allowed_ip_cidr, port, suffix):
        return rf'''\[Peer\]
PublicKey=[^\n]*
PresharedKey=[^\n]*
AllowedIPs={address}/{allowed_ip_cidr}
Endpoint={name}{suffix}:{port}'''
    return _peer_block_regex


@pytest.fixture
def contains_block():
    def _contains_block(regex, text_bytes):
        found = re.search(regex, text_bytes.decode(), re.M)
        return found is not None
    return _contains_block
