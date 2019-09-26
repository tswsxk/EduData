# coding: utf-8
# 2019/8/24 @ tongshiwei

__all__ = ["analysis_records"]

from tqdm import tqdm
import json


def analysis_records(source):
    ku_set = set()
    records_num = 0
    seq_count = 0
    correct_num = 0
    with open(source) as f:
        for line in tqdm(f, "doing statistics"):
            seq_count += 1
            responses = json.loads(line)
            records_num += len(responses)
            correct_num += len([r[1] for r in responses if int(r[1]) == 1])
            ku_set.update(set([_id for _id, _ in responses]))

    print("in %s" % source)
    print("knowledge units number: %s" % len(ku_set))
    print("records number: %s" % records_num)
    print("correct records number: %s" % correct_num)
    print("the number of sequence: %s" % seq_count)
