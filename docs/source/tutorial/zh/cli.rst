支持的命令
=====================


.. note::

    参数名后带 ``*`` 的参数是用户必须提供的参数，其他参数为可选参数

download
---------------------

用法
^^^^^^^^^^^^^^^^^^^^
用于下载并解压缩一个数据集到指定目录下

参数
^^^^^^^^^^^^^^^^^^^^

* ``dataset*`` : 数据集名
* ``data_dir`` : 数据存储目录，默认为当前目录
* ``override`` : 是否覆盖已存在的文件，默认为False
* ``url_dict`` ： 链接名称与链接映，默认情况下使用预定义的url

示例
^^^^^^^^^^^^^^^^^^^^

下载 ``math23k`` 数据集到当前文件夹

.. code-block:: console

    $ edudata download math23k 
    downloader, INFO http://base.ustc.edu.cn/data/math23k.zip is saved as math23k.zip
    Downloading math23k.zip 100.00%: 2.28MB | 2.28MB
    downloader, INFO math23k.zip is unzip to math23k
    math23k
    $ ls
    math23k  math23k.zip


下载 ``math32k`` 数据集到当前目录的父目录，并覆盖已有的文件

.. code-block:: console

    $ edudata download math23k .. True
    downloader, INFO http://base.ustc.edu.cn/data/math23k.zip is saved as ../math23k.zip
    Downloading ../math23k.zip 100.00%: 2.28MB | 2.28MB
    downloader, INFO ../math23k.zip is unzip to ../math23k
    ../math23k


ls
---------------------

用法
^^^^^^^^^^^^^^^^^^^^
列出当前所支持下载的全部数据集

参数
^^^^^^^^^^^^^^^^^^^^

* 无

示例
^^^^^^^^^^^^^^^^^^^^


.. code-block:: console

    $ Code edudata ls                      
    assistment-2009-2010-skill
    assistment-2012-2013-non-skill
    assistment-2015
    assistment-2017
    junyi
    KDD-CUP-2010
    NIPS-2020
    ...


tl2json
---------------------

用法
^^^^^^^^^^^^^^^^^^^^
将 ``.tl`` 格式的数据转化为 ``.json`` 格式

参数
^^^^^^^^^^^^^^^^^^^^

* ``src*`` : 将要转化的 ``.tl`` 源文件
* ``tar*`` : 输出的 ``.json`` 目标文件
* ``to_int`` : 是否需要将练习的编号转化为 ``int`` 类型，默认为 ``True``
* ``left_shift`` : 是否需要将练习的编号整体减1，默认为 ``False``

示例
^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

    $ cat data.tl                         
    15
    1,1,1,1,7,7,9,10,10,10,10,11,11,45,54
    0,1,1,1,1,1,0,0,1,1,1,1,1,0,0
    $ edudata tl2json data.tl data.json
    1it [00:00, 2610.02it/s]
    $ cat data.json
    [[1, 0], [1, 1], [1, 1], [1, 1], [7, 1], [7, 1], [9, 0], [10, 0], [10, 1], [10, 1], [10, 1], [11, 1], [11, 1], [45, 0], [54, 0]]

json2tl
---------------------

用法
^^^^^^^^^^^^^^^^^^^^
将 ``.json`` 格式的数据转化为 ``.tl`` 格式

参数
^^^^^^^^^^^^^^^^^^^^

* ``src*`` : 将要转化的 ``.json`` 源文件
* ``tar*`` : 输出的 ``.tl`` 目标文件

示例
^^^^^^^^^^^^^^^^^^^^


.. code-block:: console

    $ cat data.json
    [[1, 0], [1, 1], [1, 1], [1, 1], [7, 1], [7, 1], [9, 0], [10, 0], [10, 1], [10, 1], [10, 1], [11, 1], [11, 1], [45, 0], [54, 0]]
    $ edudata json2tl data.json data.tl
    1it [00:00, 8793.09it/s]
    $ data cat data.tl  
    15
    1,1,1,1,7,7,9,10,10,10,10,11,11,45,54
    0,1,1,1,1,1,0,0,1,1,1,1,1,0,0

kt_stat
---------------------

用法
^^^^^^^^^^^^^^^^^^^^
分析一个学生的回答序列

数据格式
^^^^^^^^^^^^^^^^^^^^
学生的回答序列是一系列二元组，二元组的第一个元素代表所答题目的编号，第二个元素代表答案是否正确

参数
^^^^^^^^^^^^^^^^^^^^

* ``source*`` : 
    要分析的回答序列文件，格式为 ``.json``。可以同时指定多个文件，在分析时会将所有文件中的记录进行拼接

示例
^^^^^^^^^^^^^^^^^^^^


.. code-block:: console

    $ cat data.json
    [[1, 0], [1, 1], [1, 1], [1, 1], [7, 1], [7, 1], [9, 0], [10, 0], [10, 1], [10, 1], [10, 1], [11, 1], [11, 1], [45, 0], [54, 0]]
    $ edudata kt_stat data.json           
    doing statistics: 1it [00:00, 6159.04it/s]
    in ['data.json']
    knowledge units number: 7
    min index: 1; max index: 54
    records number: 15
    correct records number: 10
    the number of sequence: 1

同时分析两个文件

.. code-block:: console

    $ edudata kt_stat data.json data1.json
    doing statistics: 2it [00:00, 9218.25it/s]
    in ['data.json', 'data1.json']
    knowledge units number: 7
    min index: 1; max index: 54
    records number: 30
    correct records number: 20
    the number of sequence: 2


edge_stat
---------------------

用法
^^^^^^^^^^^^^^^^^^^^
分析一个图中的边

参数
^^^^^^^^^^^^^^^^^^^^

* ``src*`` : 
    要分析的图，保存格式为 ``.json``
* ``threshold`` :
    若边有权值，则只有权值超过 ``threshold`` 的边会被计入总数，默认为 ``None``

示例
^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

    $ cat sample_graph.json
    [[1, 2, 2], [2, 4, 10], [1, 3, 5], [4, 3, 6], [5, 3, 1]]
    $ edudata edge_stat sample_graph.json
    in sample_graph.json
    5 edges
    count     5.000000
    mean      4.800000
    std       3.563706
    min       1.000000
    25%       2.000000
    50%       5.000000
    75%       6.000000
    max      10.000000
    dtype: float64

可以看到当 ``threshold=3`` 时有几条边因为权值不够没有计入总数

.. code-block:: console

    $ edudata edge_stat sample_graph.json 3
    in sample_graph.json
    3 edges

train_valid_test
---------------------

用法
^^^^^^^^^^^^^^^^^^^^
将一个数据集文件拆分成训练集、验证集、测试集

参数
^^^^^^^^^^^^^^^^^^^^

* ``files*`` : 待拆分的数据集文件
* ``train_size`` : 训练集的比例，默认为0.8
    : float, int, or None, (default=0.8)
        Represent the proportion of the dataset to include in the train split.
    valid_size: float, int, or None, (default=0.1)
        Represent the proportion of the dataset to include in the valid split.
    test_size: float, int, or None
        Represent the proportion of the dataset to include in the test split.
    random_state: int, RandomState instance or None, optional (default=None)
        If int, random_state is the seed used by the random number generator;
        If RandomState instance, random_state is the random number generator;
        If None, the random number generator is the RandomState instance used by np.random.
    shuffle: boolean, optional (default=True)
        Whether or not to shuffle the data before splitting. If shuffle=False then stratify must be None

示例
^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

    $ cat sample_graph.json
    [[1, 2, 2], [2, 4, 10], [1, 3, 5], [4, 3, 6], [5, 3, 1]]
    $ edudata edge_stat sample_graph.json
    in sample_graph.json
    5 edges
    count     5.000000
    mean      4.800000
    std       3.563706
    min       1.000000
    25%       2.000000
    50%       5.000000
    75%       6.000000
    max      10.000000
    dtype: float64

可以看到当 ``threshold=3`` 时有几条边因为权值不够没有计入总数

.. code-block:: console

    $ edudata edge_stat sample_graph.json 3
    in sample_graph.json
    3 edges

.."download": get_data,
    "ls": list_resources,
    "tl2json": tl2json,
    "json2tl": json2tl,
    "kt_stat": analysis_records,
    "edge_stat": analysis_edges,
    "train_valid_test": train_valid_test,
    "kfold": kfold,
    "dataset": {
        "junyi": {
            "kt": {
                "extract_relations": extract_relations,
                "build_json_sequence": build_json_sequence,
            }
        },
        "ednet": {
            "kt": {
                "build_json_sequence": build_interactions,
                "select_n": select_n_most_active,
            }
        }
    },
    "graph": {
        "ccon": correct_co_influence_graph,
        "con": concurrence_graph,
        "dense": dense_graph,
        "trans": transition_graph,
        "ctrans": correct_transition_graph,
        "sim": similarity_graph,
    }