import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_docker_container_runs(Command, Sudo):
    with Sudo():
        cmd = Command("docker ps")
    assert cmd.rc == 0
    # We don't want the version-updater to really run and push changes during
    # testing. Fortunately, the container won't get far because (in testing) it
    # won't have real a real ssh key to use with Github.
    assert "gpii/version-updater" in cmd.stdout


def test_ssh_known_hosts_configured(File, Sudo):
    with Sudo():
        ff = File("/home/deploy/gpii-ci-ssh/known_hosts")
        # Existence check seems superfluous but it produces a more helpful
        # error message than .contains() when file does not exist.
        assert ff.exists
        assert ff.contains("github.com")


def test_ssh_config_configured(File, Sudo):
    with Sudo():
        ff = File("/home/deploy/gpii-ci-ssh/config")
        # Existence check seems superfluous but it produces a more helpful
        # error message than .contains() when file does not exist.
        assert ff.exists
        assert ff.contains("github.com")
