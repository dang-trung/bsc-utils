import pytest

from bsc_utils.config import config


def pytest_addoption(parser):
    parser.addoption(
        '--runall',
        action='store_true',
        dest='nonskip',
        default=False,
        help='run all the tests even the default skipped ones'
    )


@pytest.fixture(scope='session', autouse=True)
def set_env_dev():
    config.configure(FORCE_ENV_FOR_DYNACONF='dev')