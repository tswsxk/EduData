# coding: utf-8
# create by tongshiwei on 2019/7/2

import codecs
import csv
import json

import networkx as nx
import pandas
from longling import wf_open, config_logging
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


if __name__ == '__main__':
    root = "../../"
    raw_file = root + "raw_data/junyi/junyi_Exercise_table.csv"
    ku_dict_file = root + "data/junyi/graph_vertex.json"
    prerequisite_file = root + "data/junyi/prerequisite.json"
    similarity_raw_files = [
        root + "raw_data/junyi/relationship_annotation_{}.csv".format(name) for name in ["testing", "training"]
    ]
    similarity_raw_file = root + "raw_data/junyi/relationship_annotation.csv"
    similarity_file = root + "data/junyi/similarity.json"

    # merge_relationship_annotation(similarity_raw_files, similarity_raw_file)

    # build_ku_dict(raw_file, ku_dict_file)
    extract_prerequisite(raw_file, prerequisite_file, ku_dict_file)
    # extract_similarity(similarity_raw_file, similarity_file, ku_dict_file)
