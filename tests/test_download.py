# coding: utf-8
# create by tongshiwei on 2019/7/2

import time

import pytest

from EduData.Download import get_data, url_dict


def test_download(tmp_path):
    for url in url_dict:
        get_data(url, tmp_path, override=True)
        time.sleep(1)

    for url in url_dict:
        with pytest.raises(FileExistsError):
            get_data(url, tmp_path, override=False)
        time.sleep(1)
    for url in url_dict:
        get_data(url, tmp_path, override=True)
        time.sleep(1)
