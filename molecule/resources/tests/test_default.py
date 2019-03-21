import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_influxdb_repo_added(host):
    repo = host.file('/etc/yum.repos.d/influxdb.repo')
    assert repo.exists
    assert repo.user == 'root'
    assert repo.group == 'root'
    assert repo.mode == 0o644


def test_influxdb_is_installed(host):
    influxdb = host.package("influxdb")
    assert influxdb.is_installed


def test_influxdb_running_and_enabled(host):
    influxdb = host.service("influxdb")
    assert influxdb.is_running
    assert influxdb.is_enabled


def test_grafana_repo_added(host):
    repo = host.file('/etc/yum.repos.d/grafana.repo')
    assert repo.exists
    assert repo.user == 'root'
    assert repo.group == 'root'
    assert repo.mode == 0o644


def test_grafana_is_installed(host):
    grafana = host.package("grafana")
    assert grafana.is_installed


def test_grafana_running_and_enabled(host):
    grafana = host.service("grafana")
    assert grafana.is_running
    assert grafana.is_enabled
