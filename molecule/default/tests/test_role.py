import pytest


@pytest.mark.parametrize(
    "path",
    [
        ("/usr/local/bin/innotop"),
    ],
)
def test_innotop_is_installed(host, path):
    path = host.file(path)
    assert path.exists
    assert path.is_file


@pytest.mark.parametrize(
    "command,output",
    [
        ("/usr/local/bin/innotop --version", "innotop  Ver 1.13.0"),
    ],
)
def test_innotop_runs(host, command, output):
    stdout = host.check_output(command)
    assert stdout == output
