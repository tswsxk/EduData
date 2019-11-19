# coding: utf-8
# create by tongshiwei on 2019/7/2

from EduData import list_resources
from .conftest import get_data, test_url_dict


def test_download(shared_data_dir):
    try:
        get_data("tests", shared_data_dir, url_dict=test_url_dict)
        assert True
    except Exception as e:
        raise e


def test_list_resources():
    list_resources()
    assert True
