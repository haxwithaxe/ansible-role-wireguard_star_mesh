import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_wireguard_conf_contains_zero(host, contains_block,
                                      interface_block_regex, peer_block_regex,
                                      shared_values):
    name = 'wireguard-defaults-zero'
    address = '10.254.254.10'
    allowed_ip_cidr = shared_values.ALLOWED_IP_CIDR
    port = shared_values.PORT
    if host.ansible.get_variables()['inventory_hostname'] == name:
        regex = interface_block_regex(address, port)
    else:
        regex = peer_block_regex(name, address, allowed_ip_cidr,
                                 port, '')
    with host.sudo():
        conf = host.file(f'/etc/wireguard/{shared_values.NET_NAME}.conf')
        assert contains_block(regex, conf.content)


def test_wireguard_conf_contains_one(host, contains_block,
                                     interface_block_regex, peer_block_regex,
                                     shared_values):
    name = 'wireguard-defaults-one'
    address = '10.254.254.111'
    allowed_ip_cidr = shared_values.ALLOWED_IP_CIDR
    port = shared_values.PORT
    if host.ansible.get_variables()['inventory_hostname'] == name:
        regex = interface_block_regex(address, port)
    else:
        regex = peer_block_regex(name, address, allowed_ip_cidr,
                                 port, '')
    with host.sudo():
        conf = host.file(f'/etc/wireguard/{shared_values.NET_NAME}.conf')
        assert contains_block(regex, conf.content)


def test_wireguard_conf_contains_two(host, contains_block,
                                     interface_block_regex, peer_block_regex,
                                     shared_values):
    name = 'wireguard-defaults-two'
    address = '10.254.254.222'
    allowed_ip_cidr = shared_values.ALLOWED_IP_CIDR
    port = shared_values.PORT
    if host.ansible.get_variables()['inventory_hostname'] == name:
        regex = interface_block_regex(address, port)
    else:
        regex = peer_block_regex(name, address, allowed_ip_cidr,
                                  port, '')
    with host.sudo():
        conf = host.file(f'/etc/wireguard/{shared_values.NET_NAME}.conf')
        assert contains_block(regex, conf.content)
