# coding: utf-8
# 2019/12/6 @ tongshiwei

import os
import json
from tqdm import tqdm
from pathlib import PurePath
from longling import wf_open, path_append


def synthetic2json(src, tar):
    with open(src) as f, wf_open(tar) as wf:
        for line in tqdm(f, desc="%s -> %s" % (src, tar)):
            line = line.strip()
            if not line:  # pragma: no cover
                continue
            elems = line.split(",")
            print(json.dumps([[i, int(ans)] for i, ans in enumerate(elems)]), file=wf)


def transfer_synthetic_dataset(src_dir, tar_dir):
    for root, dirs, files in os.walk(src_dir):
        for filename in files:
            src = PurePath(path_append(root, filename))
            if src.suffix != ".csv":  # pragma: no cover
                continue
            tar = path_append(tar_dir, src.with_suffix(".json").name)
            synthetic2json(src, tar)


if __name__ == '__main__':
    transfer_synthetic_dataset("../../../data/synthetic", "./")
