"""
Role tests
"""

import pytest
import os
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_netdata_user(host):
    """
    Ensure netdata user exists
    """

    user = host.user('netdata')

    assert user.group == 'netdata'
    assert user.home == '/var/lib/netdata'
    assert user.shell == '/usr/sbin/nologin'


@pytest.mark.parametrize('item_type,path,user,group,mode', [
    ('dir', '/etc/netdata', 'root', 'netdata', 0o755),
    ('file', '/etc/netdata/netdata.conf', 'netdata', 'root', 0o640),
    ('file', '/etc/netdata/apps_groups.conf', 'root', 'netdata', 0o640),
    ('file', '/etc/netdata/charts.d.conf', 'root', 'netdata', 0o640),
    ('file', '/etc/netdata/fping.conf', 'root', 'netdata', 0o640),
    (
        'file',
        '/etc/netdata/health_alarm_notify.conf',
        'root',
        'netdata',
        0o640
    ),
    (
        'file',
        '/etc/netdata/health_email_recipients.conf',
        'root',
        'netdata',
        0o640
    ),
    ('file', '/etc/netdata/node.d.conf', 'root', 'netdata', 0o640),
    ('file', '/etc/netdata/python.d.conf', 'root', 'netdata', 0o640),
    ('file', '/etc/netdata/stream.conf', 'root', 'netdata', 0o640),
    ('dir', '/var/lib/netdata', 'netdata', 'netdata', 0o775),
    ('dir', '/var/log/netdata', 'netdata', 'root', 0o755),
])
def test_netdata_paths(host, item_type, path, user, group, mode):
    """
    Ensure path exists and have expected properties
    """

    current_path = host.file(path)

    if item_type == 'file':
        assert current_path.is_file
    elif item_type == 'dir':
        assert current_path.is_directory

    assert current_path.exists
    assert current_path.user == user
    assert current_path.group == group
    assert current_path.mode == mode


@pytest.mark.parametrize('path,pattern', [
    ('/etc/netdata/netdata.conf', '.*\s*history\s*=\s*7992.*'),
    ('/etc/netdata/python.d.conf', '.*\s*example\s*:\s*[tT]rue.*'),
])
def test_config_content(host, path, pattern):
    """
    Check custom configuration values
    """

    assert host.file(path).contains(pattern)


def test_netdata_service(host):
    """
    Check service state
    """

    assert host.service('netdata').is_enabled
    assert host.service('netdata').is_running


def test_netdata_port(host):
    """
    Check listening port
    """

    assert host.socket('tcp://19999').is_listening
