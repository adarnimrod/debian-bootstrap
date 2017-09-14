from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_example(host):
    assert host.run('uname').rc == 0


def test_root(host):
    with host.sudo():
        assert host.run('whoami').stdout.strip() == 'root'
