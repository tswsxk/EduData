# coding: utf-8
# 2019/8/23 @ tongshiwei

import fire

from EduData.DataSet.download_data.download_data import get_data as download, list_resources as ls
from EduData.Task.KnowledgeTracing.format import tl2json, json2tl
from EduData.Task.KnowledgeTracing.statistics import analysis_records as kt_stat
from EduData.Tools.train_valid_test import train_valid_test, KFold as kfold


def cli():
    fire.Fire()


if __name__ == '__main__':
    cli()
