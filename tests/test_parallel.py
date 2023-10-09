import pytest

from bsc_utils.parallel import (
    ProcessPoolExecutor, ThreadPoolExecutor, parallel
)


def f(x, y):
    return x**2


@pytest.fixture(scope='module', autouse=True)
def params_list():
    return [{'x': n, 'y': n} for n in list(range(100))]


def test_multi_thread(params_list):
    res = parallel(f, params_list, executor_type=ThreadPoolExecutor)
    assert len(res) == len(params_list)


def test_multi_process(params_list):
    res = parallel(f, params_list, executor_type=ProcessPoolExecutor)
    assert len(res) == len(params_list)
