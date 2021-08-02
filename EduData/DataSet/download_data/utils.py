# coding: utf-8
# create by tongshiwei on 2019-8-16
import logging
import tarfile
import zipfile
import rarfile

from longling import flush_print

logger = logging.getLogger("downloader")


def decompress(file):  # pragma: no cover
    for z in [".tar.gz", ".tar.bz2", ".tar.bz", ".tar.tgz", ".tar", ".tgz", ".zip", ".rar"]:
        if file.endswith(z):
            if z == ".zip":
                return un_zip(file)
            elif z == ".rar":
                return un_rar(file)
            else:
                return un_tar(file)
    return file


def get_uz_path(file):  # pragma: no cover
    #  返回解压缩后的文件名
    for i in [".tar.gz", ".tar.bz2", ".tar.bz", ".tar.tgz", ".tar", ".tgz", ".zip", ".rar"]:
        file = file.replace(i, "")
    return file


def un_zip(file):  # pragma: no cover
    zip_file = zipfile.ZipFile(file)
    uz_path = get_uz_path(file)
    logger.info(file + " is unzip to " + uz_path)
    for name in zip_file.namelist():
        zip_file.extract(name, uz_path)
    zip_file.close()
    return uz_path


def un_rar(file):  # pragma: no cover
    rar_file = rarfile.RarFile(file)
    uz_path = get_uz_path(file)
    logger.info(file + " is unrar to " + uz_path)
    rar_file.extractall(uz_path)
    return uz_path


def un_tar(file):  # pragma: no cover
    tar_file = tarfile.open(file)
    uz_path = get_uz_path(file)
    logger.info(file + " is untar to " + uz_path)
    tar_file.extractall(path=uz_path)
    return uz_path


def timestamp2time(time_stamp):
    import time
    time_struct = time.localtime(time_stamp)
    return time.strftime('%a, %d %b %Y %H:%M:%S GMT', time_struct)


def format_sizeof(num, suffix='', divisor=1000):
    """
    Code from tqdm

    Formats a number (greater than unity) with SI Order of Magnitude
    prefixes.

    Parameters
    ----------
    num  : float
        Number ( >= 1) to format.
    suffix  : str, optional
        Post-postfix [default: ''].
    divisor  : float, optional
        Divisor between prefixes [default: 1000].

    Returns
    -------
    out  : str
        Number with Order of Magnitude SI unit postfix.

    Examples
    --------
    >>> format_sizeof(800000)
    '800K'
    >>> format_sizeof(40000000000000)
    '40.0T'
    >>> format_sizeof(1000000000000000000000000000)
    '1000.0Y'
    """
    for unit in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
        if abs(num) < 999.5:
            if abs(num) < 99.95:
                if abs(num) < 9.995:
                    return '{0:1.2f}'.format(num) + unit + suffix
                return '{0:2.1f}'.format(num) + unit + suffix
            return '{0:3.0f}'.format(num) + unit + suffix
        num /= divisor
    return '{0:3.1f}Y'.format(num) + suffix


def format_byte_sizeof(num, suffix='B'):
    """
    Code from longling

    Examples
    --------
    >>> format_byte_sizeof(1024)
    '1.00KB'
    """
    return format_sizeof(num, suffix, divisor=1024)


def reporthook4urlretrieve(blocknum, bs, size):
    """
    Code from longling

    Parameters
    ----------
    blocknum:
        已经下载的数据块
    bs:
        数据块的大小
    size:
        远程文件的大小

    Returns
    -------

    """
    per = 100.0 * (blocknum * bs) / size
    if per > 100:
        per = 100
    flush_print(
        'Downloading %.2f%% : %s | %s' % (
            per,
            format_byte_sizeof(blocknum * bs),
            format_byte_sizeof(size)
        ))
