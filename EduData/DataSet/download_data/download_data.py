# coding: utf-8
# create by tongshiwei on 2019/7/2

__all__ = ["URL_DICT", "get_data", "list_resources"]

import os
from urllib.request import urlretrieve

import requests
from bs4 import BeautifulSoup
from longling import config_logging, LogLevel, path_append

try:
    from .utils import decompress, reporthook4urlretrieve
except (SystemError, ModuleNotFoundError):  # pragma: no cover
    from utils import decompress, reporthook4urlretrieve

DEFAULT_DATADIR = path_append("./", "", to_str=True)

logger = config_logging(logger="downloader", console_log_level=LogLevel.INFO)

prefix = 'http://base.ustc.edu.cn/data/'

URL_DICT = {
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
        "http://base.ustc.edu.cn/data/slepemapy.cz/",
    "synthetic":
        "http://base.ustc.edu.cn/data/synthetic/",
    "ktbd":
        "http://base.ustc.edu.cn/data/ktbd/",
}


def get_dataset_name():  # pragma: no cover
    urls = []
    for i in URL_DICT.values():
        if i not in urls:
            urls.append(i)
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
            temp = prefix + h
            # 避免重复
            if temp not in urls:
                urls.append(temp)
                # 避免ASSISTment和junyi的重复
                if temp not in ['http://base.ustc.edu.cn/data/ASSISTment/',
                                'http://base.ustc.edu.cn/data/JunyiAcademy_Math_Practicing_Log/']:
                    URL_DICT[h[:-1]] = temp


def download_file(url, save_path, override):
    if os.path.exists(save_path) and override:  # pragma: no cover
        os.remove(save_path)
        logger.info(save_path + ' will be overridden.')

    logger.info(url + ' is saved as ' + save_path)
    urlretrieve(url, save_path, reporthook=reporthook4urlretrieve)
    print()
    decompress(save_path)


def download_data(url, data_dir, override, bloom_filter: set = None):
    bloom_filter = set() if bloom_filter is None else bloom_filter

    if url in bloom_filter:  # pragma: no cover
        return

    if url.endswith("/"):  # 以/结尾是文件夹，其余是文件
        _data_dir = path_append(data_dir, url.split('/')[-2], to_str=True)

        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        soup = BeautifulSoup(r.text, "lxml")
        al = soup.find_all('a')
        for a in al:
            # 获得链接名
            h = a.get('href')
            if h[0] != '.':
                url_h = url + h
                if url_h not in bloom_filter:
                    download_data(url_h, _data_dir, override, bloom_filter)
        bloom_filter.add(url)

    else:
        os.makedirs(data_dir, exist_ok=True)
        save_path = path_append(data_dir, url.split('/')[-1], to_str=True)
        download_file(url, save_path, override)
        bloom_filter.add(url)

    return data_dir


def get_data(dataset, data_dir=DEFAULT_DATADIR, override=False, url_dict: dict = None):
    """
    Parameters
    ----------
    dataset: str
        数据集名
    data_dir: str
        数据存储目录
    override: bool
        是否覆盖已存在的文件
    url_dict:
        链接名称与链接映射

    Returns
    -------

    """
    url_dict = URL_DICT if not url_dict else url_dict
    try:
        return download_data(url_dict[dataset], data_dir, override)
    except FileExistsError:  # pragma: no cover
        return path_append(data_dir, url_dict[dataset].split('/')[-1], to_str=True)


def list_resources():
    print("\n".join(URL_DICT))
