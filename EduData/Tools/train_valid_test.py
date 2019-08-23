# coding: utf-8
# create by tongshiwei on 2019-7-5

__all__ = ["train_valid_test"]

import io
from longling.ML.toolkit.dataset.splitter import train_valid_test
import random
import math


def KFold(filename, train_prefix, valid_prefix, n_splits=5, shuffle=False):
    with open(filename) as f:
        indices = [idx for idx, _ in enumerate(f)]
        sample_num = indices[-1]
    if shuffle is True:
        random.shuffle(indices)

    proportion = sample_num / n_splits
    step = math.floor(proportion * sample_num)
    indices_buckets = [
        (i, i + step) for i in range(0, sample_num, step)
    ]
    train_wfs = [
        io.open(train_prefix + index, "w", encoding="utf-8") for index in range(n_splits)
    ]
    valid_wfs = [
        io.open(valid_prefix + index, "w", encoding="utf-8") for index in range(n_splits)
    ]
    with open(filename) as f:
        for line_no, line in enumerate(f):
            for idx, (start, end) in enumerate(indices_buckets):
                if start <= line_no < end:
                    print(line, end="", file=valid_wfs[idx])
                else:
                    print(line, end="", file=train_wfs[idx])

    for wf in train_wfs + valid_wfs:
        wf.close()
