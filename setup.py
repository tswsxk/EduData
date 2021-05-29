# coding: utf-8
# create by tongshiwei on 2019/6/25

from setuptools import setup, find_packages

test_deps = [
    'pytest>=4',
    'pytest-cov>=2.6.0',
    'pytest-flake8',
]

setup(
    name='EduData',
    version='0.0.14',
    extras_require={
        'test': test_deps,
    },
    packages=find_packages(),
    python_requires='>=3.6',
    long_description='Refer to full documentation https://github.com/bigdata-ustc/EduData/blob/master/README.md'
                     ' for detailed information.',
    description='This project aims to '
                'provide convenient interfaces for downloading and preprocessing dataset in education.',
    install_requires=[
        'tqdm',
        'networkx',
        'longling[ml]>=1.3.15',
        'requests',
        'bs4',
        'rarfile',
        'pandas',
        'fire',
        'lxml',
        'numpy>=1.16.5',
        'scipy>=1.2.0',
        'scikit-learn>=0.23.2',
    ],  # And any other dependencies foo needs
    entry_points={
        "console_scripts": [
            "edudata = EduData.main:cli",
        ],
    },
    classifier=[
        "Programming Language :: Python :: 3",
    ]
)
