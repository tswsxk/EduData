# coding: utf-8
# create by tongshiwei on 2019/7/2

import pytest
from EduData import list_resources
from .conftest import get_data, test_url_dict


def test_download(shared_data_dir):
    get_data("tests", shared_data_dir, url_dict=test_url_dict)
    with pytest.raises(ValueError):
        get_data("*&53$#@")


def test_override(shared_data_dir):
    get_data(
        "http://base.ustc.edu.cn/data/tests/synthetic/naive_c5_q50_s4000_v0.csv",
        shared_data_dir,
    )
    get_data(
        "http://base.ustc.edu.cn/data/tests/synthetic/naive_c5_q50_s4000_v0.csv",
        shared_data_dir,
        override=True
    )
    get_data(
        "http://base.ustc.edu.cn/data/tests/synthetic/naive_c5_q50_s4000_v0.csv",
        shared_data_dir,
        override=False
    )


def test_list_resources():
    list_resources()
