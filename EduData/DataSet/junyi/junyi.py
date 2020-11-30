# coding: utf-8
# create by tongshiwei on 2019/7/2

"""
This script is used to build the map dict (ku_name -> idx) extract some relations from the original junyi dataset.
"""
__all__ = ["build_knowledge_graph"]

import codecs
import csv
import json

import networkx as nx
import pandas
from longling import wf_open, config_logging, path_append
from tqdm import tqdm

logger = config_logging(logger="junyi", console_log_level="info")


def build_ku_dict(source, target):
    with codecs.open(source, encoding="utf-8") as f, wf_open(target) as wf:
        f.readline()
        idx = 0
        vertex_dict = {}
        for line in tqdm(csv.reader(f)):
            if line[0] not in vertex_dict:
                vertex_dict[line[0]] = idx
                idx += 1
        logger.info("vertex num: %s" % len(vertex_dict))
        json.dump(vertex_dict, wf, indent=2)


def extract_prerequisite(source, target, ku_dict):
    """in target: (A, B) means predecessor --> successor"""
    with codecs.open(source, encoding="utf-8") as f, open(ku_dict) as kf, wf_open(target) as wf:
        ku_dict = json.load(kf)

        prerequisite_edges = []
        f.readline()
        for line in tqdm(csv.reader(f)):
            if not line[2]:
                continue
            successor = ku_dict[line[0]]
            for prerequisite in line[2].split(','):
                predecessor = ku_dict[prerequisite]
                if predecessor == successor:
                    continue
                if predecessor == 61 and successor == 498:
                    # there is a loop 498 -> 510 -> 61 -> 498 in original data
                    continue
                prerequisite_edges.append((predecessor, successor))

        logger.info("prerequisite edges: %s" % len(prerequisite_edges))

        # clean the loop in prerequisite graph

        graph = nx.DiGraph()
        graph.add_edges_from(prerequisite_edges)
        assert not list(nx.algorithms.simple_cycles(graph)), "loop in DiGraph"

        json.dump(prerequisite_edges, wf, indent=2)


def merge_relationship_annotation(sources, target):
    with wf_open(target) as wf:
        with codecs.open(sources[0]) as f:
            for line in f:
                wf.write(line)
        with codecs.open(sources[1]) as f:
            f.readline()
            for line in f:
                wf.write(line)
    return target


def extract_similarity(source, target, ku_dict):
    """
    In target: (A, B, v) means A is similar with B in v degree.
    If v is small, A and B should be considered as not similar.
    """
    similarity = []
    with codecs.open(source, encoding="utf-8") as f, open(ku_dict) as kf, wf_open(target) as wf:
        f.readline()
        ku_dict = json.load(kf)
        for line in csv.reader(f):
            similarity.append((ku_dict[line[0]], ku_dict[line[1]], float(line[2])))

        logger.info("similarity edges: %s" % len(similarity))

        logger.info(pandas.Series([sim[-1] for sim in similarity]).describe())
        json.dump(similarity, wf, indent=2)


def extract_difficulty(source, target, ku_dict):
    """
    In target: (A, B, v) means A is similar with B in v degree.
    If v is small, A and B should be considered as not similar.
    """
    difficulty = []
    with codecs.open(source, encoding="utf-8") as f, open(ku_dict) as kf, wf_open(target) as wf:
        f.readline()
        ku_dict = json.load(kf)
        for line in csv.reader(f):
            difficulty.append((ku_dict[line[0]], ku_dict[line[1]], float(line[4])))

        logger.info("edges: %s" % len(difficulty))

        logger.info(pandas.Series([sim[-1] for sim in difficulty]).describe())
        json.dump(difficulty, wf, indent=2)


def build_knowledge_graph(src_root: str, tar_root: (str, None) = None,
                          ku_dict_path: str = None,
                          prerequisite_path: (str, None) = None,
                          similarity_path: (str, None) = None,
                          difficulty_path: (str, None) = None):
    tar_root = tar_root if tar_root is not None else src_root
    exercise_src = path_append(src_root, "junyi_Exercise_table.csv")

    assert ku_dict_path is not None

    relation_src = merge_relationship_annotation(
        [path_append(src_root, "relationship_annotation_{}.csv".format(name)) for name in ["testing", "training"]],
        path_append(src_root, "relationship_annotation.csv")
    )
    ku_dict_path = path_append(tar_root, ku_dict_path)
    build_ku_dict(exercise_src, ku_dict_path)

    if prerequisite_path is not None:
        prerequisite_path = path_append(tar_root, prerequisite_path)
        extract_prerequisite(exercise_src, prerequisite_path, ku_dict_path)

    if similarity_path is not None:
        similarity_path = path_append(tar_root, "similarity.json")
        extract_similarity(relation_src, similarity_path, ku_dict_path)

    if difficulty_path is not None:
        difficulty_path = path_append(tar_root, "difficulty.json")
        extract_difficulty(relation_src, difficulty_path, ku_dict_path)
