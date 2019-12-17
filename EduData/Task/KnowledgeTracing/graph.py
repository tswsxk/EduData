# coding: utf-8
# 2019/12/12 @ tongshiwei

import json
from longling import wf_open
from tqdm import tqdm
import numpy as np
from scipy.spatial.distance import cdist

__all__ = ["dense_graph", "correct_transition_graph", "transition_graph", "similarity_graph"]


def dense_graph(ku_num, tar):
    _graph = []

    for i in range(ku_num):
        for j in range(ku_num):
            if i != j:
                _graph.append([i, j])

    with wf_open(tar) as wf:
        json.dump(_graph, wf, indent=2)


def _count_to_probability(count_graph):
    _transition_graph = np.asarray(count_graph)

    _transition_graph = (_transition_graph.T / _transition_graph.sum(axis=-1)).T

    return _transition_graph.tolist()


def _output_graph(graph, tar):
    ku_num = len(graph)

    _graph = []

    for i in range(ku_num):
        for j in range(ku_num):
            if i != j and graph[i][j] > 0:
                _graph.append([i, j, graph[i][j]])

    with wf_open(tar) as wf:
        json.dump(_graph, wf, indent=2)


def correct_transition_graph(ku_num, *src, tar):
    count_graph = [[0] * ku_num for _ in range(ku_num)]

    for filename in src:
        with open(filename) as f:
            for line in tqdm(f, "constructing transition graph"):
                if not line.strip():  # pragma: no cover
                    continue
                seq = json.loads(line)
                pre_c = None
                for eid, r in seq:
                    if pre_c is not None:
                        if eid != pre_c and r == 1:
                            count_graph[pre_c][eid] += 1
                        elif r == 1:
                            # count_graph[pre_c][eid] += 1
                            pass
                    if r == 1:
                        pre_c = eid
                    else:
                        pre_c = None

    _transition_graph = _count_to_probability(count_graph)

    _output_graph(_transition_graph, tar)


def transition_graph(ku_num, *src, tar):
    count_graph = [[0] * ku_num for _ in range(ku_num)]

    for filename in src:
        with open(filename) as f:
            for line in tqdm(f, "constructing transition graph"):
                if not line.strip():  # pragma: no cover
                    continue
                seq = json.loads(line)
                pre = None
                for eid, _ in seq:
                    if pre is not None:
                        if eid != pre:
                            count_graph[pre][eid] += 1
                        else:
                            # count_graph[pre][eid] += 1
                            pass
                    pre = eid

    _transition_graph = _count_to_probability(count_graph)
    _output_graph(_transition_graph, tar)


def similarity_graph(ku_num, src_graph, tar):
    """construct similarity graph based on transition graph"""
    with open(src_graph) as f:
        _transitions = json.load(f)

    _transition_graph = [[0] * ku_num for _ in range(ku_num)]

    for id1, id2, value in _transitions:
        _transition_graph[id1][id2] = float(value)

    _transition_graph = np.asarray(_transition_graph)
    _dist_graph = 1 - cdist(_transition_graph, _transition_graph, 'cosine')

    _dist_graph[np.isnan(_dist_graph)] = 0
    _similarity_graph = (_dist_graph - _dist_graph.min()) / (_dist_graph.max() - _dist_graph.min())
    _output_graph(_similarity_graph, tar)


if __name__ == '__main__':
    similarity_graph(
        124,
        "../../../data/assistment_2009_2010/transition_graph.json",
        "../../../data/assistment_2009_2010/trans_sim.json"
    )
    similarity_graph(
        124,
        "../../../data/assistment_2009_2010/correct_transition_graph.json",
        "../../../data/assistment_2009_2010/ctrans_sim.json"
    )
