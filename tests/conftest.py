# coding: utf-8
# 2019/11/14 @ tongshiwei

from EduData import get_data
from longling import path_append
import functools
import pytest

test_url_dict = {
    "tests":
        "http://base.ustc.edu.cn/data/tests/",
    "junyi":
        "http://base.ustc.edu.cn/data/tests/junyi/",
}

get_data = functools.partial(get_data, url_dict=test_url_dict)


@pytest.fixture(scope="session")
def shared_data_dir(tmp_path_factory):
    tmpdir = tmp_path_factory.mktemp("data")
    try:
        return path_append(get_data("tests", tmpdir, override=True), "tests")
    except Exception as e:
        raise e
