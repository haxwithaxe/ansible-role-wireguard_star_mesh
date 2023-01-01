import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_wireguard_conf_contains_zero(host, contains_block,
                                      interface_block_regex, shared_values):
    name = 'wireguard-ks-zero'
    address = '10.254.254.10'
    port = 54321
    if host.ansible.get_variables()['inventory_hostname'] == name:
        regex = interface_block_regex(address, port)
    else:
        regex = r'''\[Peer\]
PublicKey=[^\n]*
PresharedKey=[^\n]*
AllowedIPs=10\.254\.254\.10/31,10\.254\.253\.0/24,10\.254\.252\.0/24
Endpoint=wireguard-ks-zero\.testnet:54321'''
    with host.sudo():
        conf = host.file(f'/etc/wireguard/{shared_values.NET_NAME}.conf')
        assert contains_block(regex, conf.content)


def test_wireguard_conf_contains_one(host, contains_block,
                                     interface_block_regex, peer_block_regex,
                                     shared_values):
    name = 'wireguard-ks-one'
    address = '10.254.254.111'
    allowed_ip_cidr = shared_values.ALLOWED_IP_CIDR
    suffix = f'.{shared_values.NET_NAME}'
    port = shared_values.PORT
    if host.ansible.get_variables()['inventory_hostname'] == name:
        regex = interface_block_regex(address, port)
    else:
        regex = peer_block_regex(name, address, allowed_ip_cidr,
                                 port, suffix)
    with host.sudo():
        conf = host.file(f'/etc/wireguard/{shared_values.NET_NAME}.conf')
        assert contains_block(regex, conf.content)


def test_wireguard_conf_contains_two(host, contains_block,
                                     interface_block_regex, peer_block_regex,
                                     shared_values):
    name = 'wireguard-ks-two'
    address = '10.254.254.222'
    allowed_ip_cidr = shared_values.ALLOWED_IP_CIDR
    suffix = f'.{shared_values.NET_NAME}'
    port = shared_values.PORT
    if host.ansible.get_variables()['inventory_hostname'] == name:
        regex = interface_block_regex(address, port)
    else:
        regex = peer_block_regex(name, address, allowed_ip_cidr,
                                  port, suffix)
    with host.sudo():
        conf = host.file(f'/etc/wireguard/{shared_values.NET_NAME}.conf')
        assert contains_block(regex, conf.content)
