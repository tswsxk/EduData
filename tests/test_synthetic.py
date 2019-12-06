# coding: utf-8
# 2019/12/6 @ tongshiwei

from EduData.DataSet.synthetic import transfer_synthetic_dataset
from longling import path_append


def test_synthetic_kt(shared_data_dir):
    src_dir = path_append(shared_data_dir, "synthetic", to_str=True)
    tar_dir = src_dir
    transfer_synthetic_dataset(src_dir, tar_dir)
