# coding: utf-8
# 2019/11/14 @ tongshiwei

from longling import path_append
from script.junyi_kt import extract_relations, build_json_sequence
from EduData.Task.KnowledgeTracing.format import tl2json, json2tl
from EduData.Task.KnowledgeTracing.statistics import analysis_records


def test_junyi(shared_data_dir):
    src_root = path_append(shared_data_dir, "junyi", to_str=True)
    extract_relations(src_root, path_append(src_root, "data"))
    assert True


def test_junyi_kt(shared_data_dir):
    src_root = path_append(shared_data_dir, "junyi", to_str=True)
    ku_dict_path = path_append(shared_data_dir, "junyi", "data", "graph_vertex.json")
    build_json_sequence(src_root, path_append(src_root, "data", to_str=True), ku_dict_path)
    assert True


def test_json2tl(shared_data_dir):
    src = path_append(shared_data_dir, "junyi", "data", "student_log_kt_1000", to_str=True)
    tl_tar = path_append(shared_data_dir, "junyi", "data", "student_log_kt_1000.tl", to_str=True)
    json_tar = path_append(shared_data_dir, "junyi", "data", "student_log_kt_1000.json", to_str=True)
    json2tl(src, tl_tar)
    tl2json(tl_tar, json_tar)
    assert True


def test_analysis(shared_data_dir):
    src = path_append(shared_data_dir, "junyi", "data", "student_log_kt_1000", to_str=True)
    analysis_records(src)
    assert True
