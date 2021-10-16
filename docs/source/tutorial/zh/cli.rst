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
将 ``.tl`` 格式的数据转化为 :doc:`序列文件 <sequence>`

参数
^^^^^^^^^^^^^^^^^^^^

* ``src*`` : 将要转化的 ``.tl`` 源文件
* ``tar*`` : 输出的序列文件
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
将 :doc:`序列文件 <sequence>` 转化为 ``.tl`` 格式文件

参数
^^^^^^^^^^^^^^^^^^^^

* ``src*`` : 将要转化的序列文件
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
分析一个学生的 :doc:`回答序列 <sequence>`

参数
^^^^^^^^^^^^^^^^^^^^

* ``source*`` : 
    要分析的回答序列文件，可以同时指定多个文件，在分析时会将所有文件中的记录进行拼接

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
将一个数据集文件按行拆分成训练集、验证集、测试集，比例为8:1:1

参数
^^^^^^^^^^^^^^^^^^^^

* ``files*`` : 待拆分的数据集文件，可以同时指定多个
示例
^^^^^^^^^^^^^^^^^^^^

数据集中的每一行代表一个样本，数据集中有30个样本，按照8:1:1的比例划分为训练集、验证集、测试集

.. code-block:: console

    $ cat data.json           
    [0.4086358705691857, 0.5821013717870963, 0.3937663543609674, 0.3596475011511454, 0.6269590610755503, 0.5916270350464593, 0.40039551392826145, 0.175949398164154, 0.7188498245018131, 0.3353656251326548]
    [0.7577482681983009, 0.7823167871569502, 0.7628718209608286, 0.6570446436834679, 0.7895185204556635, 0.5802078440735305, 0.27497800873078715, 0.30383370246383956, 0.9037409494778825, 0.910175518416613]
    [0.408436652871088, 0.3176041020104178, 0.9772468567022291, 0.2958594473962345, 0.9400651897265613, 0.7442828330073002, 0.4328292856489826, 0.48221263297826256, 0.028567228727882088, 0.06838837638379969]
    [0.4367401871654375, 0.9147963293632903, 0.5618913934548003, 0.555425728144243, 0.14801367475302585, 0.4753940552854019, 0.35687531862795085, 0.7848409683542806, 0.6110589151187046, 0.7982670835419365]
    ...
    $ edudata train_valid_test data.json
    dataset, INFO train_valid_test start
    dataset, INFO train_valid_test: data.json -> data.train.json,data.valid.json,data.test.json
    dataset, INFO train_valid_test end
    $ wc -l data.json data.train.json data.valid.json data.test.json 
    30 data.json
    24 data.train.json
    3 data.valid.json
    3 data.test.json
    60 总用量


kfold
---------------------

用法
^^^^^^^^^^^^^^^^^^^^
将数据集按照5折交叉验证划分，可以同时指定多个

参数
^^^^^^^^^^^^^^^^^^^^
* ``files*`` : 待拆分的数据集文件

示例
^^^^^^^^^^^^^^^^^^^^

可以看到数据集被拆分为了五份，每次取其中一份作为测试集，其余作为训练集

.. code-block:: console

    $ edudata kfold data.json             
    dataset, INFO kfold 0 start
    dataset, INFO kfold 1 start
    dataset, INFO kfold 0: data.json -> data.0.train.json,data.0.test.json
    dataset, INFO kfold 2 start
    dataset, INFO kfold 1: data.json -> data.1.train.json,data.1.test.json
    dataset, INFO kfold 2: data.json -> data.2.train.json,data.2.test.json
    ...
    $ wc -l data.*       
    6 data.0.test.json
   24 data.0.train.json
    6 data.1.test.json
   24 data.1.train.json
    6 data.2.test.json
   24 data.2.train.json
    6 data.3.test.json
   24 data.3.train.json
    6 data.4.test.json
   24 data.4.train.json
   30 data.json

dataset.junyi.kt.extract_relations
---------------------
                
用法                   
^^^^^^^^^^^^^^^^^^^^ 
从 ``junyi`` 数据集中抽取出出练习之间的一些关系并将结果序列化为 ``.json`` 文件

                
                
参数                   
^^^^^^^^^^^^^^^^^^^^ 
* ``src_root`` : 数据集所在的源文件夹，默认为 ``../raw_data/junyi/``               
* ``tar_root`` : 结果存放的文件夹，默认为 ``../data/junyi/data/``

示例                   
^^^^^^^^^^^^^^^^^^^^ 
                
.. code-block:: console

    $ edudata dataset junyi kt extract_relations . ./data
    837it [00:00, 130560.17it/s]
    junyi, INFO vertex num: 835
    837it [00:00, 121630.89it/s]
    junyi, INFO prerequisite edges: 985
    junyi, INFO similarity edges: 1954
    junyi, INFO count    1954.000000
    mean        4.979990
    std         2.436923
    min         1.000000
    25%         2.603846
    50%         5.190909
    75%         7.216667
    max         9.000000
    dtype: float64
    junyi, INFO edges: 1954
    junyi, INFO count    1954.000000
    mean        4.511079
    std         1.659825
    min         1.000000
    25%         3.250000
    50%         4.400000
    75%         5.666667
    max         8.750000
    dtype: float64
    $ ls ./data
    difficulty.json    prerequisite.json
    graph_vertex.json  similarity.json
                
dataset.junyi.kt.build_json_sequence    
---------------------
                
用法                   
^^^^^^^^^^^^^^^^^^^^ 
从数据集中构建出前 ``n`` 活跃学生的 :doc:`回答序列 <sequence>`
                
参数                   
^^^^^^^^^^^^^^^^^^^^ 

* ``src_root*`` : 数据集文件的存放目录
* ``tar_root*`` : 输出文件存放目录
* ``ku_dict_path*`` : 将知识点映射为编号的字典文件
* ``n`` : 要挑选出的前 ``n`` 活跃的学生数，默认为 ``1000``

数据格式
^^^^^^^^^^^^^^^^^^^^ 

文件中的每一行代表一个 ``session`` 中学生的回答序列，而相邻的若干个行代表了一个学生的所有回答情况。

示例                   
^^^^^^^^^^^^^^^^^^^^ 

每一行代表一个 ``session`` ，而每个学生可以在多个 ``session`` 中答题。从结果中可以看到最活跃的 ``1000`` 名学生共进行了 ``59792`` 次 ``session``

.. code-block:: console
                
    $ edudata dataset junyi kt build_json_sequence . ./data ./data/graph_vertex.json     
    reading data: 39462201it [03:28, 189554.01it/s]
    calculating frequency: 100%|█████████████████████████████████████████████████████| 247547/247547 [00:00<00:00, 1011762.99it/s]
    writing -> data/student_log_kt_1000: 100%|███████████████████████████████████████████████| 1000/1000 [00:03<00:00, 321.59it/s]
    $ wc -l student_log_kt_1000   
    59792 student_log_kt_1000


dataset.ednet.kt.build_json_sequence             
---------------------
                
用法                   
^^^^^^^^^^^^^^^^^^^^ 
从 ``EdNet`` 数据集中构建全部学生的 :doc:`回答序列 <sequence>`
                
参数                   
^^^^^^^^^^^^^^^^^^^^ 
* ``users_dir*`` : 数据集所在的目录
* ``questions_csv*`` : 存放问题答案的 ``.csv`` 文件
* ``tar*`` : 输出的回答序列文件
                
                
示例                   
^^^^^^^^^^^^^^^^^^^^ 
                
由于原数据集过大，因此只使用原数据集的一个子集作为演示

.. code-block:: console

    $ edudata dataset ednet kt build_json_sequence KT1_sample EdNet-Contents/contents/questions.csv sequence.json
    building interactions: 100%|████████████████████████████████████████████████████████████████| 10/10 [00:00<00:00, 1240.59it/s]
    $ wc -l sequence.json
    10 sequence.json

                
dataset.ednet.kt.select_n            
---------------------
                
用法                   
^^^^^^^^^^^^^^^^^^^^ 
从全体学生的 :doc:`回答序列 <sequence>` 中挑出前 ``n`` 长的序列
                
参数                   
^^^^^^^^^^^^^^^^^^^^ 
* ``src*`` : 全部学生的回答序列
* ``tar*`` : 前 ``n`` 长的回答序列
* ``n*``
                
                
示例                   
^^^^^^^^^^^^^^^^^^^^ 
                
.. code-block:: console
                
    $ edudata dataset ednet kt select_n sequence.json top5.json 5
    evaluating length of each row: 10it [00:00, 6238.74it/s]
    selecting 5 most active students from sequence.json to top5.json: 10it [00:00, 58254.22it/s]
    $ wc -l top5.json    
    5 top5.json


graph.dense               
---------------------
                
用法                   
^^^^^^^^^^^^^^^^^^^^ 
输出一个含有 ``ku_num`` 个节点的完全图
                
                
参数                   
^^^^^^^^^^^^^^^^^^^^ 
* ``ku_num*`` : 图中节点的个数
* ``tar*`` : 输出的目标文件
* ``undirected`` : 是否输出无向图，默认为 ``False``         
                
示例                   
^^^^^^^^^^^^^^^^^^^^ 
                
.. code-block:: console
    
    $ edudata graph dense 5 graph.json                           
    [0, 1]
    [0, 2]
    [0, 3]
    [0, 4]
    [1, 0]
    ...

graph.con               
---------------------
                
用法                   
^^^^^^^^^^^^^^^^^^^^ 
通过学生的 :doc:`回答序列 <sequence>` 计算两道练习题相邻出现的概率。

输出一个 :doc:`知识点图 <graph>`
                
参数                   
^^^^^^^^^^^^^^^^^^^^ 
* ``ku_num*`` : 总的练习数（节点数）
* ``src*`` : 回答序列文件，可以同时指定多个
* ``tar*`` : 输出的目标
                
示例                   
^^^^^^^^^^^^^^^^^^^^ 
                
.. code-block:: console

    $ cat data.json      
    [[0, 1], [1, 0], [1, 1], [2, 0]]
    [[0, 1], [1, 1], [2, 0], [4, 1]]
    [[0, 1], [2, 1], [3, 0], [2, 1]]
    $ edudata graph con 5 data.json --tar graph.json
    /home/huzr/.local/lib/python3.9/site-packages/EduData/Task/KnowledgeTracing/graph.py:529: UserWarning: do not use this function due to the lack of support from theory
    warnings.warn("do not use this function due to the lack of support from theory")
    constructing concurrence graph: 3it [00:00, 8701.88it/s]
    $ cat graph.json       
    [
    [
        0,
        1,
        0.21049203852953075
    ],
    [
        0,
        2,
        0.07743569350528148
    ],
    ...
                
graph.trans               
---------------------
                
用法                   
^^^^^^^^^^^^^^^^^^^^ 
通过学生的 :doc:`回答序列 <sequence>` 计算在遇到一个知识点之后，另外一个知识点出现的概率

输出一个 :doc:`知识点图 <graph>`
                
                
参数                   
^^^^^^^^^^^^^^^^^^^^ 
* ``ku_num*`` : 总的练习数（节点数）
* ``src*`` : 回答序列文件，可以同时指定多个
* ``tar*`` : 输出的目标图
                
                
示例                   
^^^^^^^^^^^^^^^^^^^^ 
                
.. code-block:: console


    $ cat data.json
    [[0, 1], [1, 0], [1, 1], [2, 1]]
    [[2, 0], [1, 0], [0, 1], [2, 1]]
    $ edudata graph trans 3 data.json -tar result.json
    constructing transition graph: 2it [00:00, 6765.01it/s]
    [0.0, 0.5, 0.5]
    [0.5, 0.0, 0.5]
    [0.0, 1.0, 0.0]
                

graph.ctrans              
---------------------
                
用法                   
^^^^^^^^^^^^^^^^^^^^ 
通过学生的 :doc:`回答序列 <sequence>` 计算在一个知识点掌握之后，另外一个知识点也随之掌握的概率

输出一个 :doc:`知识点图 <graph>`
                
                
参数                   
^^^^^^^^^^^^^^^^^^^^ 
* ``ku_num*`` : 总的练习数（节点数）
* ``src*`` : 存有回答序列的文件，可以同时指定多个
* ``tar*`` : 输出的目标
                
                
示例                   
^^^^^^^^^^^^^^^^^^^^ 
                
.. code-block:: console
                
    $ cat data.json
    [[0, 1], [1, 0], [1, 1], [2, 1]]
    [[2, 0], [1, 0], [0, 1], [2, 1]]
    $ edudata graph ctrans 3 data.json --tar result.json
    constructing coorect transition graph: 2it [00:00, 11351.30it/s]
    [0.0, 0.0, 1.0]
    [0.0, 0.0, 1.0]
    [0.0, 0.0, 0.0]

graph.sim               
---------------------
                
用法                   
^^^^^^^^^^^^^^^^^^^^ 
根据一个已有的 :doc:`知识点图 <graph>` 计算图中节点之间的余弦相似度
                
参数                   
^^^^^^^^^^^^^^^^^^^^ 
* ``ku_num*`` ：图中节点的个数
* ``src_graph*`` ： 存放图的文件
* ``tar*`` : 输出文件
                
                
示例                   
^^^^^^^^^^^^^^^^^^^^ 
                
.. code-block:: console
                
    $ edudata graph sim 5 graph.json result.json
    $ cat result.json
    [
        [
            0,
            1,
            0.2618280790565648
        ],
        [
            0,
            2,
            0.7264881146529072
        ],
        [
            0,
            3,
            0.4690365472434528
        ],
    ...

graph.ccon            
---------------------
                
用法                   
^^^^^^^^^^^^^^^^^^^^ 
通过学生的回答序列计算知识点之间的互影响

输出一个 :doc:`知识点图 <graph>`
                
                
参数                   
^^^^^^^^^^^^^^^^^^^^ 
* ``ku_num*`` : 总的练习数（节点数）
* ``src*`` : 存有回答序列的文件，可以同时指定多个
* ``tar*`` : 输出的目标
                
示例                   
^^^^^^^^^^^^^^^^^^^^ 
                
.. code-block:: console
    
    $ cat data.json        
    [[0, 1], [1, 0], [1, 1], [2, 0]]
    [[0, 1], [1, 1], [2, 0], [2, 1]]
    [[2, 1], [2, 1], [1, 1], [2, 0]]
    [[1, 0], [0, 1], [0, 1], [2, 0]]
    [[2, 0], [1, 1], [0, 1], [2, 1]]
    $ edudata graph ccon 3 data.json --tar result.json  
    /home/huzr/.local/lib/python3.9/site-packages/EduData/Task/KnowledgeTracing/graph.py:510: UserWarning: do not use this function due to the lack of support from theory
    warnings.warn("do not use this function due to the lack of support from theory")
    constructing coorect transition graph: 5it [00:00, 18927.36it/s]
    [[0. 1. 0.]
    [1. 0. 0.]
    [0. 0. 0.]]