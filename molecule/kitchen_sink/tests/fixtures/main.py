import pytest

class WGSharedValues:

    ALLOWED_IP_CIDR = 31
    NET_NAME = 'testnet'
    PORT = 12345


@pytest.fixture
def shared_values():
    return WGSharedValues
