# coding: utf-8
# 2019/8/23 @ tongshiwei

import fire

from EduData.DataSet.download_data.download_data import get_data, list_resources
from EduData.Task.KnowledgeTracing.format import tl2json, json2tl
from EduData.Task.KnowledgeTracing.statistics import analysis_records
from longling.ML.toolkit.dataset import train_valid_test, kfold
from EduData.DataSet.junyi import extract_relations, build_json_sequence


def cli():  # pragma: no cover
    fire.Fire(
        {
            "download": get_data,
            "ls": list_resources,
            "tl2json": tl2json,
            "json2tl": json2tl,
            "kt_stat": analysis_records,
            "train_valid_test": train_valid_test,
            "kfold": kfold,
            "dataset": {
                "junyi": {
                    "kt": {
                        "extract_relations": extract_relations,
                        "build_json_sequence": build_json_sequence,
                    }
                }
            }
        }
    )
