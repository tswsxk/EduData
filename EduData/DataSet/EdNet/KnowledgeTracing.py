# coding: utf-8
# 2019/12/17 @ tongshiwei

import heapq
import json
from longling import path_append, wf_open
import re
import os
import csv
from tqdm import tqdm
from .utils import Judgement

__all__ = ["csv2interactions", "build_interactions"]


def csv2interactions(src: str, judgement: Judgement):
    interactions = []
    with open(src) as f:
        f.readline()
        for line in csv.reader(f, delimiter=","):
            _question_id = line[2]
            _answer = line[3]
            interactions.append(list(judgement(_question_id, _answer)))
    return interactions


def build_interactions(users_dir, questions_csv, tar):
    judgement = Judgement(questions_csv)

    with wf_open(tar) as wf:
        for root, dirs, files in os.walk(users_dir):
            for filename in tqdm(files, "building interactions"):
                if re.match("u.*\.csv", filename):
                    interactions_seq = csv2interactions(path_append(root, filename, to_str=True), judgement)
                    print(json.dumps(interactions_seq), file=wf)


def select_n_most_active(src, tar, n):
    lengths = []
    with open(src) as f:
        for i, line in tqdm(enumerate(f), "evaluating length of each row"):
            lengths.append([i, len(json.loads(line))])

    selected_idx = set(list(zip(*heapq.nlargest(n, lengths, key=lambda x: x[1])))[0])

    with open(src) as f, wf_open(tar) as wf:
        for i, line in tqdm(enumerate(f), "selecting %s most active students from %s to %s" % (n, src, tar)):
            if i not in selected_idx:
                continue
            print(line, end='', file=wf)
