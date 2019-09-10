# coding: utf-8
# 2019/8/23 @ tongshiwei

import fire

from EduData.DataSet.download_data.download_data import get_data as download, list_resources as ls
from EduData.Task.KnowledgeTracing.format import tl2json, json2tl

if __name__ == '__main__':
    fire.Fire()
