# coding: utf-8
# 2019/11/20 @ tongshiwei


__all__ = ["extract_relations", "build_json_sequence"]

from longling import path_append
from .junyi import build_knowledge_graph
from .KnowledgeTracing import select_n_most_frequent_students


def extract_relations(src_root: str = "../raw_data/junyi/", tar_root: str = "../data/junyi/data/"):
    build_knowledge_graph(
        src_root, tar_root,
        ku_dict_path="graph_vertex.json",
        prerequisite_path="prerequisite.json",
        similarity_path="similarity.json",
        difficulty_path="difficulty.json",
    )


def build_json_sequence(src_root: str = "../raw_data/junyi/", tar_root: str = "../data/junyi/data/",
                        ku_dict_path: str = "../data/junyi/data/graph_vertex.json", n: int = 1000):
    select_n_most_frequent_students(
        path_append(src_root, "junyi_ProblemLog_for_PSLC.txt", to_str=True),
        path_append(tar_root, "student_log_kt_", to_str=True),
        ku_dict_path,
        n,
    )
