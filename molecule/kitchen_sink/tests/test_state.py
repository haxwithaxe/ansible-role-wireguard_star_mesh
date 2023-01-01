import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_wireguard_interface_ip(host, shared_values):
    wg_ip = host.interface(shared_values.NET_NAME, 'inet').addresses[0]
    assert wg_ip == host.ansible.get_variables()['wireguard_ip']
