# coding: utf-8
# create by tongshiwei on 2019-8-14

from EduData.Task.kt_data import tl2json, json2tl


def test_json2tl(tmp_path):
    src = "../data/junyi/student_log_kt.json.small.test"
    tl_tar = tmp_path / "student_log_kt.json.small.test.tl"
    json_tar = tmp_path / "student_log_kt.json.small.test.json"
    json2tl(src, tl_tar)
    tl2json(tl_tar, json_tar)
