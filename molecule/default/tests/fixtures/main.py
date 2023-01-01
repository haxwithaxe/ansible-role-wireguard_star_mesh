import pytest

class WGSharedValues:

    ALLOWED_IP_CIDR = 32
    NET_NAME = 'wg0'
    PORT = 51820


@pytest.fixture
def shared_values():
    return WGSharedValues
