# coding: utf-8
# create by tongshiwei on 2019/7/2

import time

import pytest

from EduData import get_data
from EduData.DataSet.download_data import url_dict


def test_download(tmp_path):
    for url in url_dict:
        get_data(url, tmp_path, override=True)
        time.sleep(1)


if __name__ == '__main__':
    from EduData.DataSet.download_data.utils import reporthook4urlretrieve
    from urllib.request import urlretrieve

    urlretrieve(
        "http://base.ustc.edu.cn/data/ASSISTment/2015_100_skill_builders_main_problems.zip",
        "../data/temp",
        reporthook=reporthook4urlretrieve
    )
