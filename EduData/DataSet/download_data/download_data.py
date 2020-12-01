# coding: utf-8
# create by tongshiwei on 2019/7/2

__all__ = ["URL_DICT", "get_data", "list_resources"]

import os
import re
from urllib.request import urlretrieve

import requests
from bs4 import BeautifulSoup
from longling import config_logging, LogLevel, path_append, flush_print

try:
    from .utils import decompress, reporthook4urlretrieve, yes_no, timestamp2time
except (SystemError, ModuleNotFoundError):  # pragma: no cover
    from utils import decompress, reporthook4urlretrieve, yes_no, timestamp2time

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
    "psychometrics":
        "http://base.ustc.edu.cn/data/psychometrics/",
    "psy":
        "http://base.ustc.edu.cn/data/psychometrics/",
    "pisa2015":
        "http://base.ustc.edu.cn/data/pisa2015_science.zip",
    "workbankr":
        "http://base.ustc.edu.cn/data/wordbankr.zip",
    "critlangacq":
        "http://base.ustc.edu.cn/data/critlangacq.zip",
    "ktbd":
        "http://base.ustc.edu.cn/data/ktbd/",
    "ktbd-a0910":
        "http://base.ustc.edu.cn/data/ktbd/assistment_2009_2010/",
    "ktbd-junyi":
        "http://base.ustc.edu.cn/data/ktbd/junyi/",
    "ktbd-synthetic":
        "http://base.ustc.edu.cn/data/ktbd/synthetic/",
    "ktbd-a0910c":
        "http://base.ustc.edu.cn/data/ktbd/a0910c/",
    "cdbd":
        "http://base.ustc.edu.cn/data/cdbd/",
    "cdbd-lsat":
        "http://base.ustc.edu.cn/data/cdbd/LSAT/",
    "cdbd-a0910":
        "http://base.ustc.edu.cn/data/cdbd/a0910/",
    "math2015":
        "http://staff.ustc.edu.cn/~qiliuql/data/math2015.rar",
    "ednet":
        "http://base.ustc.edu.cn/data/EdNet/",
    "ktbd-ednet":
        "http://base.ustc.edu.cn/data/ktbd/EdNet/"
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


def download_file(url, save_path, override, chunksize=65535):
    downloaded = 0
    if os.path.exists(save_path) and override:
        logger.info(save_path + ' will be overridden.')
    elif os.path.exists(save_path):
        # Resume download
        downloaded = os.stat(save_path).st_size
        local_timestamp = os.path.getctime(save_path)
        logger.info("{} already exists. Send resume request after {} bytes".format(
            save_path, downloaded))
        # raise FileExistsError()
    old_downloaded = downloaded

    headers = {}
    if downloaded:
        headers['Range'] = 'bytes={}-'.format(downloaded)
        headers['If-Unmodified-Since'] = timestamp2time(local_timestamp)

    logger.info(url + ' is saved as ' + save_path)
    res = requests.get(url, headers=headers, stream=True, timeout=15)

    mode = 'wb+'
    content_len = int(res.headers.get('content-length'))
    # Check if server supports range feature, and works as expected.
    if res.status_code == 206:
        # Content range is in format `bytes 327675-43968289/43968290`, check
        # if it starts from where we requested.
        content_range = res.headers.get('content-range')
        # If file is already downloaded, it will reutrn `bytes */43968290`.

        if content_range and \
                int(content_range.split(' ')[-1].split('-')[0]) == downloaded:
            mode = 'ab+'

    elif res.status_code == 416:
        # 416 means Range field not support
        # TODO:需要重新下载吗
        logger.warning("Range not support. Redownloading...")
        urlretrieve(url, save_path, reporthook=reporthook4urlretrieve)
        return

    elif res.status_code == 412:
        # 如果所请求的资源在指定的时间之后发生了修改，那么会返回 412 (Precondition Failed) 错误。
        logger.warning("Resource Changed, should override. Redownloading...")
        urlretrieve(url, save_path, reporthook=reporthook4urlretrieve)
        return

    file_origin_size = content_len + old_downloaded
    with open(save_path, mode) as f:
        for chunk in res.iter_content(chunksize):
            f.write(chunk)
            downloaded += len(chunk)
            # TODO:如何显示下载进度
            flush_print('Downloading %s %.2f%%: %d | %d' % (save_path, downloaded / file_origin_size * 100,
                        downloaded, file_origin_size))

    # urlretrieve(url, save_path, reporthook=reporthook4urlretrieve)
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
    if dataset in url_dict:
        url = url_dict[dataset]
    elif re.match("http(s?)://.*", dataset):
        url = dataset
    else:
        raise ValueError("%s is neither a valid dataset name nor an url" % dataset)

    save_path = path_append(data_dir, url.split('/')[-1], to_str=True)
    # if os.path.exists(save_path):
    #     ans = yes_no("Find File Exist Resume Download (No means Override)?[Y/n]")
    #     override = not ans

    try:
        return download_data(url, data_dir, override)
    except FileExistsError:
        return save_path


def list_resources():
    print("\n".join(URL_DICT))
