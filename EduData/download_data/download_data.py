# coding: utf-8
# create by tongshiwei on 2019/7/2

__all__ = ["url_dict", "get_data"]
import os
from urllib.request import urlretrieve

import requests
from bs4 import BeautifulSoup
from longling import config_logging, LogLevel, path_append
from longling.spider import download_data

from .utils import decompress

DEFAULT_DATADIR = path_append("../", "data/", to_str=True)

config_logging(logger="downloader", console_log_level=LogLevel.INFO)

prefix = 'http://base.ustc.edu.cn/data/'

url_dict = {
    "assistment-2009-2010-skill":
        "http://base.ustc.edu.cn/data/ASSISTment/2009_skill_builder_data_corrected.zip",
    "assistment-2012-2013-non-skill":
        "http://base.ustc.edu.cn/data/ASSISTment/2012-2013-data-with-predictions-4-final.zip",
    "assistment-2015":
        "http://base.ustc.edu.cn/data/ASSISTment/2015_100_skill_builders_main_problems.zip",
    "junyi":
        "http://base.ustc.edu.cn/data/JunyiAcademy_Math_Practicing_Log/junyi.rar",
    "KDD-CUP-2010":
        "http://base.ustc.edu.cn/data/KDD_Cup_2010/",
    "slepemapy.cz":
        "http://base.ustc.edu.cn/data/slepemapy.cz/"
}


def get_dataset_name():
    urls = []
    url = prefix
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.text, "lxml")
    al = soup.find_all('a')
    for a in al:
        # 获得各个数据集名称
        h = a.get('href')
        if h[0] != '.':
            temp = 'http://base.ustc.edu.cn/data/' + h + '\n'
            # 避免重复
            if temp not in urls:
                urls.append(temp)
    return urls


def download():
    count = 0
    os.makedirs('./data/', exist_ok=True)
    lines = get_dataset_name()
    urls = []
    for line in lines:
        line = line.strip()
        os.makedirs('./data/' + line[29:-1], exist_ok=True)
        count += 1
        r = requests.get(line, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        soup = BeautifulSoup(r.text, "lxml")
        al = soup.find_all('a')
        for a in al:
            # 获得文件名
            h = a.get('href')
            if h[0] != '.':
                temp = line + h
                # 避免重复
                if temp not in urls:
                    urls.append(temp)
                    file_path = './data/' + line[29:] + h
                    print(temp + ' is saved as ' + file_path)
                    # 下载
                    urlretrieve(temp, file_path)
                    # 解压
                    decompress(file_path)


def get_data(dataset, data_dir=DEFAULT_DATADIR, override=False):
    try:
        return download_data(url_dict[dataset], data_dir, override)
    except FileExistsError:
        return path_append(data_dir, url_dict[dataset].split('/')[-1], to_str=True)


def list_resources():
    print("\n".join(url_dict))


if __name__ == '__main__':
    get_data("assistment-2009-2010-skill")
