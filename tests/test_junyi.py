# coding: utf-8
# 2019/11/14 @ tongshiwei

from longling import path_append
from EduData.DataSet.junyi import extract_relations, build_json_sequence
from EduData.Task.KnowledgeTracing.format import tl2json, json2tl
from EduData.Task.KnowledgeTracing.statistics import analysis_records, analysis_edges
from EduData.Task.KnowledgeTracing.graph import dense_graph, transition_graph, correct_transition_graph
from EduData.Task.KnowledgeTracing.graph import similarity_graph


def test_junyi(shared_data_dir):
    src_root = path_append(shared_data_dir, "junyi", to_str=True)
    extract_relations(src_root, path_append(src_root, "data"))


def test_junyi_kt(shared_data_dir):
    src_root = path_append(shared_data_dir, "junyi", to_str=True)
    ku_dict_path = path_append(shared_data_dir, "junyi", "data", "graph_vertex.json")
    build_json_sequence(src_root, path_append(src_root, "data", to_str=True), ku_dict_path)


def test_json2tl(shared_data_dir):
    src = path_append(shared_data_dir, "junyi", "data", "student_log_kt_1000", to_str=True)
    tl_tar = path_append(shared_data_dir, "junyi", "data", "student_log_kt_1000.tl", to_str=True)
    json_tar = path_append(shared_data_dir, "junyi", "data", "student_log_kt_1000.json", to_str=True)
    json2tl(src, tl_tar)
    tl2json(tl_tar, json_tar, to_int=False)
    tl2json(tl_tar, json_tar, to_int=True)


def test_graph(shared_data_dir):
    json_src = path_append(shared_data_dir, "junyi", "data", "student_log_kt_1000.json", to_str=True)

    dense_graph(835, path_append(shared_data_dir, "dense_graph", to_str=True))
    trans_graph = path_append(shared_data_dir, "transition_graph", to_str=True)
    transition_graph(835, json_src, tar=trans_graph)
    ctrans_graph = path_append(shared_data_dir, "correct_transition_graph", to_str=True)
    correct_transition_graph(835, json_src, tar=ctrans_graph)

    ctrans_sim = path_append(shared_data_dir, "correct_transition_sim_graph", to_str=True)
    similarity_graph(835, ctrans_graph, ctrans_sim)


def test_analysis(shared_data_dir):
    src = path_append(shared_data_dir, "junyi", "data", "student_log_kt_1000", to_str=True)
    analysis_records(src)

    graph_src = path_append(shared_data_dir, "dense_graph", to_str=True)
    analysis_edges(graph_src)

    graph_src = path_append(shared_data_dir, "transition_graph", to_str=True)
    analysis_edges(graph_src, threshold=0.5)
    analysis_edges(graph_src, threshold=None)
