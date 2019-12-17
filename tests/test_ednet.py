# coding: utf-8
# 2019/12/17 @ tongshiwei

import json
import pytest
from longling import path_append
from EduData.DataSet.EdNet.utils import Judgement
from EduData.DataSet.EdNet.KnowledgeTracing import build_interactions, csv2interactions, select_n_most_active


def test_utils(shared_data_dir):
    question_csv_path = path_append(shared_data_dir, "tests", "EdNet", "contents", "questions.csv")

    judgement = Judgement(question_csv_path)

    assert judgement.is_correct("q1", "b") is True
    assert judgement.is_correct("1", "c") is False

    with pytest.raises(ValueError):
        judgement.is_correct("q12000", "d")

    with pytest.raises(ValueError):
        judgement("q12000", "a")

    assert judgement("q1", "b") == (0, 1)


def test_build_interactions(shared_data_dir):
    question_csv_path = path_append(shared_data_dir, "tests", "EdNet", "contents", "questions.csv")
    users_dir = path_append(shared_data_dir, "tests", "EdNet", "KT1")

    user_csv = path_append(users_dir, "u1.csv")

    judgement = Judgement(question_csv_path)

    interactions = csv2interactions(user_csv, judgement)

    assert interactions[0] == [5011, 0]

    tar = path_append(shared_data_dir, "tests", "EdNet", "KT1", "data", "kt.json")
    build_interactions(users_dir, question_csv_path, tar)

    with open(tar) as f:
        assert json.loads(f.readline())[0] == [5011, 0]
        assert len(json.loads(f.readline())) == 16

    tar2 = path_append(tar, to_str=True) + ".%s" % 1
    select_n_most_active(tar, tar2, 1)

    with open(tar2) as f:
        assert json.loads(f.readline())[0] == [5011, 0]
