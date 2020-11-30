# coding: utf-8
# 2019/12/13 @ tongshiwei

"""
Using junyi test data as demo testing data
"""

import json

from longling import path_append, as_out_io

from EduData.Task.KnowledgeTracing.graph import (dense_graph,
                                                 correct_transition_count_graph, correct_transition_graph,
                                                 posterior_correct_probability_graph,
                                                 transition_graph, similarity_graph)


def test_graph(shared_data_dir, tmpdir):
    demo_response = [
        [[0, 1], [1, 0], [1, 1], [2, 0]],
        [[0, 0], [0, 0], [0, 1], [2, 0]],
        [[1, 1], [2, 0], [2, 1], [3, 1]],
        [[0, 1], [1, 1], [2, 0], [2, 1]],
        [[2, 0], [1, 0], [0, 1], [1, 1]],
    ]

    tmpfile = path_append(tmpdir, "demo.json", to_str=True)
    with as_out_io(tmpfile) as wf:
        for seq in demo_response:
            print(json.dumps(seq), file=wf)

    dense_graph_path = path_append(tmpdir, "dense_graph.json", to_str=True)
    _dense_graph = dense_graph(4, dense_graph_path)
    assert len(_dense_graph) == 12

    trans_graph = path_append(tmpdir, "transition_graph", to_str=True)
    transition_graph(4, tmpfile, tar=trans_graph)

    ctrans_count_graph = path_append(tmpdir, "correct_transition_count_graph", to_str=True)
    correct_transition_count_graph(4, tmpfile, tar=ctrans_count_graph)

    ctrans_graph = path_append(tmpdir, "correct_transition_graph", to_str=True)
    correct_transition_graph(4, tmpfile, tar=ctrans_graph)

    pcp_graph = path_append(tmpdir, "posterior_correct_probability_graph", to_str=True)
    posterior_correct_probability_graph(4, tmpfile, tar=pcp_graph)

    ctrans_sim = path_append(shared_data_dir, "correct_transition_sim_graph", to_str=True)
    similarity_graph(4, ctrans_graph, ctrans_sim)
