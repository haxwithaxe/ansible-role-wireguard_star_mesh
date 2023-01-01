#import warnings
#with warnings.catch_warnings():
#    warnings.filterwarnings("ignore", category=DeprecationWarning)
import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_wireguard_service_up(host, shared_values):
    wg_service = host.service(f'wg-quick@{shared_values.NET_NAME}.service')
    assert wg_service.is_running


def test_wireguard_service_enabled(host, shared_values):
    wg_service = host.service(f'wg-quick@{shared_values.NET_NAME}.service')
    assert wg_service.is_enabled
