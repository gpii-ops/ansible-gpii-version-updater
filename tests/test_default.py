import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_docker_runs(Command):
    assert Command("docker images").rc == 0


def test_ssh_known_hosts_configured(File, Sudo):
    with Sudo():
        ff = File("/home/depoy/gpii-ci-ssh/known_hosts")
        # Existence check seems superfluous but it produces a more helpful
        # error message than .contains() when file does not exist.
        assert ff.exists
        assert ff.contains("github.com")


def test_ssh_config_configured(File, Sudo):
    with Sudo():
        ff = File("/home/gpii-ci-ssh/.ssh/config")
        # Existence check seems superfluous but it produces a more helpful
        # error message than .contains() when file does not exist.
        assert ff.exists
        assert ff.contains("github.com")
