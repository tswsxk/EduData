# coding: utf-8
# create by tongshiwei on 2019/7/2

__all__ = ["download_data", "get_data"]

from longling import config_logging, LogLevel, path_append
from longling.spider import download_data

DEFAULT_DATADIR = path_append("../", "data/", to_str=True)

config_logging(logger="downloader", console_log_level=LogLevel.INFO)

url_dict = {
    "assistment-2009-2010-skill":
        "https://drive.google.com/file/d/0B2X0QD6q79ZJUFU1cjYtdGhVNjg",
    "assistment-2009-2010-non-skill":
        "https://sites.google.com/site/assistmentsdata/home/assistment-2009-2010-data/non-skill-builder-data-2009-10",
    "assistment-2009-2010":
        "http://teacherwiki.assistment.org/index.php/Assistments_2009-2010_Full_Dataset"
}


def get_data(dataset, data_dir=DEFAULT_DATADIR, override=False):
    try:
        return download_data(url_dict[dataset], data_dir, override)
    except FileExistsError:
        return path_append(data_dir, url_dict[dataset].split('/')[-1], to_str=True)


def list_resources():
    print("\n".join(url_dict))


if __name__ == '__main__':
    get_data("assistment-2009-2010-skill")
