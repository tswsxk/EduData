# coding: utf-8
# create by tongshiwei on 2019/7/2

from EduData import get_data, list_resources


def test_download(tmp_path):
    try:
        get_data("toy", tmp_path, override=True)
        assert True
    except Exception as e:
        raise e


def test_list_resources():
    list_resources()
    assert True
