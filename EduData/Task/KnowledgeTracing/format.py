# coding: utf-8
# create by tongshiwei on 2019-8-14

import io
import json

from tqdm import tqdm

__all__ = ["tl2json", "json2tl"]


def tl2json(src: str, tar: str):
    """
    convert the dataset in `tl` sequence into `json` sequence

    .tl format
    The first line is the number of exercises a student attempted.
    The second line is the exercise tag sequence.
    The third line is the response sequence. ::

        15
        1,1,1,1,7,7,9,10,10,10,10,11,11,45,54
        0,1,1,1,1,1,0,0,1,1,1,1,1,0,0

    .json format
    Each sample contains several response elements, and each element is a two-element list.
    The first is the exercise tag and the second is the response. ::

        [[1,0],[1,1],[1,1],[1,1],[7,1],[7,1],[9,0],[10,0],[10,1],[10,1],[10,1],[11,1],[11,1],[45,0],[54,0]]

    """
    with open(src) as f, io.open(tar, "w", encoding="utf-8") as wf:
        for _ in tqdm(f):
            exercise_tags = f.readline().strip().strip(",").split(",")
            response_sequence = f.readline().strip().strip(",").split(",")
            responses = list(zip(exercise_tags, response_sequence))
            print(json.dumps(responses), file=wf)


def json2tl(src, tar):
    with open(src) as f, io.open(tar, "w", encoding="utf-8") as wf:
        for line in tqdm(f):
            responses = json.loads(line)
            exercise_tags, response_sequence = zip(*responses)
            print(len(exercise_tags), file=wf)
            print(",".join(list(map(str, exercise_tags))), file=wf)
            print(",".join(list(map(str, response_sequence))), file=wf)


if __name__ == '__main__':
    json2tl("../data/junyi/student_log_kt.json.small.train", "../data/junyi/student_log_kt.json.small.train.tl")
    json2tl("../data/junyi/student_log_kt.json.small.test", "../data/junyi/student_log_kt.json.small.test.tl")
