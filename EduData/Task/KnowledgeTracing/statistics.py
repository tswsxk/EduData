# coding: utf-8
# 2019/8/24 @ tongshiwei

__all__ = ["analysis_records"]

import networkx as nx
import numpy as np
import pandas as pd
import fileinput
from tqdm import tqdm
import json


def _report(total, correct):
    keep_ids, total_first_answer_num = list(zip(*[[i, n] for i, n in enumerate(total) if n > 0]))
    total_correctly_first_answer_num = [n for i, n in enumerate(correct) if i in keep_ids]
    total_first_answer_num = np.asarray(total_first_answer_num)
    total_correctly_first_answer_num = np.asarray(total_correctly_first_answer_num)
    correctly_answer_portion = total_correctly_first_answer_num / total_first_answer_num
    print(total_first_answer_num.sum())
    print(total_correctly_first_answer_num.sum())
    print(total_correctly_first_answer_num.sum() / total_first_answer_num.sum())
    print(correctly_answer_portion.max(), correctly_answer_portion.min(),
          correctly_answer_portion.sum() / len(correctly_answer_portion))


def correctly_answer(ku_num, *filenames, prerequsite_graph=None, similarity_graph=None):
    total_first_answer_num = [0] * ku_num
    total_correctly_first_answer_num = [0] * ku_num

    pre_total_first_answer_num = [0] * ku_num
    pre_total_correctly_first_answer_num = [0] * ku_num

    sim_total_first_answer_num = [0] * ku_num
    sim_total_correctly_first_answer_num = [0] * ku_num

    graph_total_first_answer_num = [0] * ku_num
    graph_total_correctly_first_answer_num = [0] * ku_num

    with open(prerequsite_graph) as f:
        pgraph = nx.DiGraph()
        pgraph.add_nodes_from([i for i in range(ku_num)])
        pgraph.add_edges_from(json.load(f))
        pre_path = nx.shortest_path(pgraph)

    with open(similarity_graph) as f:
        sgraph = nx.Graph()
        sgraph.add_nodes_from([i for i in range(ku_num)])
        sgraph.add_edges_from([edge[:2] for edge in json.load(f) if edge[2] >= 5.0])
        sim_path = nx.shortest_path(sgraph)

    with fileinput.input(files=filenames) as f:
        for line in tqdm(f):
            records = json.loads(line)
            pre_set = set()
            pc_set = set()
            pre_ku = None
            for _id, _c in records:
                if pre_ku is None:
                    total_first_answer_num[_id] += 1
                    if _c == 1:
                        total_correctly_first_answer_num[_id] += 1
                elif _id != pre_ku:
                    total_first_answer_num[_id] += 1
                    if _c == 1:
                        total_correctly_first_answer_num[_id] += 1

                    in_pre = False
                    in_sim = False
                    for pre in pc_set:
                        if in_pre and in_sim:
                            break
                        if _id in pre_path[pre] and len(pre_path[pre][_id]) <= 2:
                            in_pre = True
                        if _id in sim_path[pre] and len(sim_path[pre][_id]) <= 2:
                            in_sim = True
                    if in_pre:
                        pre_total_first_answer_num[_id] += 1
                        if _c == 1:
                            pre_total_correctly_first_answer_num[_id] += 1
                    if in_sim:
                        sim_total_first_answer_num[_id] += 1
                        if _c == 1:
                            sim_total_correctly_first_answer_num[_id] += 1
                    if in_pre or in_sim:
                        graph_total_first_answer_num[_id] += 1
                        if _c == 1:
                            graph_total_correctly_first_answer_num[_id] += 1

                    pre_set.add(_id)
                    if _c == 1:
                        pc_set.add(_id)
                pre_ku = _id
    print("total")
    _report(total_first_answer_num, total_correctly_first_answer_num)
    print("pre")
    _report(pre_total_first_answer_num, pre_total_correctly_first_answer_num)
    print("sim")
    _report(sim_total_first_answer_num, sim_total_correctly_first_answer_num)
    print("graph")
    _report(graph_total_first_answer_num, graph_total_correctly_first_answer_num)


def correctly_answer2(ku_num, *filenames, prerequsite_graph=None, similarity_graph=None):
    total_first_answer_num = [0] * ku_num
    total_correctly_first_answer_num = [0] * ku_num

    pre_total_first_answer_num = [0] * ku_num
    pre_total_correctly_first_answer_num = [0] * ku_num

    sim_total_first_answer_num = [0] * ku_num
    sim_total_correctly_first_answer_num = [0] * ku_num

    graph_total_first_answer_num = [0] * ku_num
    graph_total_correctly_first_answer_num = [0] * ku_num

    with open(prerequsite_graph) as f:
        pgraph = nx.DiGraph()
        pgraph.add_nodes_from([i for i in range(ku_num)])
        pgraph.add_edges_from(json.load(f))
        pre_path = nx.shortest_path(pgraph)

    with open(similarity_graph) as f:
        sgraph = nx.Graph()
        sgraph.add_nodes_from([i for i in range(ku_num)])
        sgraph.add_edges_from([edge[:2] for edge in json.load(f) if edge[2] >= 5.0])
        sim_path = nx.shortest_path(sgraph)

    with fileinput.input(files=filenames) as f:
        for line in tqdm(f):
            records = json.loads(line)
            pre = None
            pre_c = None
            for _id, _c in records:
                if pre is None:
                    total_first_answer_num[_id] += 1
                    if _c == 1:
                        total_correctly_first_answer_num[_id] += 1
                elif _id != pre:
                    total_first_answer_num[_id] += 1
                    if _c == 1:
                        total_correctly_first_answer_num[_id] += 1

                    if pre_c == 1:
                        in_graph = False
                        if _id in pre_path[pre] and len(pre_path[pre][_id]) <= 2:
                            in_graph = True
                            pre_total_first_answer_num[_id] += 1
                            if _c == 1:
                                pre_total_correctly_first_answer_num[_id] += 1
                        if _id in sim_path[pre] and len(sim_path[pre][_id]) <= 2:
                            in_graph = True
                            sim_total_first_answer_num[_id] += 1
                            if _c == 1:
                                sim_total_correctly_first_answer_num[_id] += 1
                        if in_graph:
                            graph_total_first_answer_num[_id] += 1
                            if _c == 1:
                                graph_total_correctly_first_answer_num[_id] += 1
                pre = _id
                pre_c = _c

    print("total")
    _report(total_first_answer_num, total_correctly_first_answer_num)
    print("pre")
    _report(pre_total_first_answer_num, pre_total_correctly_first_answer_num)
    print("sim")
    _report(sim_total_first_answer_num, sim_total_correctly_first_answer_num)
    print("graph")
    _report(graph_total_first_answer_num, graph_total_correctly_first_answer_num)


def analysis_records(*source):
    ku_set = set()
    records_num = 0
    seq_count = 0
    correct_num = 0
    with fileinput.input(files=source) as f:
        for line in tqdm(f, "doing statistics"):
            seq_count += 1
            responses = json.loads(line)
            records_num += len(responses)
            correct_num += len([r[1] for r in responses if int(r[1]) == 1])
            ku_set.update(set([_id for _id, _ in responses]))

    print("in %s" % list(source))
    print("knowledge units number: %s" % len(ku_set))
    print("min index: %s; max index: %s" % (min(ku_set), max(ku_set)))
    print("records number: %s" % records_num)
    print("correct records number: %s" % correct_num)
    print("the number of sequence: %s" % seq_count)


def analysis_edges(src, threshold=None):
    edge_num = 0
    average_weight = []

    with open(src) as f:
        graph_edges = json.load(f)

    for edge in graph_edges:
        if len(edge) == 2:
            edge_num += 1
        elif len(edge) >= 3:
            if threshold is None:
                edge_num += 1
                average_weight.append(edge[2])
            elif edge[2] >= threshold:
                edge_num += 1
        else:  # pragma: no cover
            raise ValueError("each edge in src should have at least two element")

    print("in %s" % src)
    print("%s edges" % edge_num)
    if average_weight:
        print(pd.Series(average_weight).describe())


if __name__ == '__main__':
    root = "../../../data/junyi/"
    correctly_answer(
        835,
        root + "train.json", root + "test.json",
        prerequsite_graph=root + "prerequisite.json",
        similarity_graph=root + "similarity.json"
    )
