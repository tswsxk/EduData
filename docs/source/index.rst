.. EduNLP documentation master file, created by
   sphinx-quickstart on Sat Aug  7 19:55:39 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

=================================================
Welcome to EduData's Tutorials and Documentation
=================================================
.. Logo
.. image:: _static/EduData.png
   :width: 200px
   :align: center

.. Badges
.. image:: https://img.shields.io/pypi/v/EduData.svg
   :target: https://pypi.python.org/pypi/EduData
   :alt: PyPI

.. image:: https://github.com/bigdata-ustc/EduData/actions/workflows/python-test.yml/badge.svg?branch=master
   :target: https://github.com/bigdata-ustc/EduData/actions/workflows/python-test.yml
   :alt: test

.. image:: https://codecov.io/gh/bigdata-ustc/EduData/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/bigdata-ustc/EduData
   :alt: codecov

.. image:: https://img.shields.io/pypi/dm/EduData.svg?style=flat
   :target: https://pypi.python.org/pypi/EduData
   :alt: Download

.. image:: https://img.shields.io/github/license/bigdata-ustc/EduData
   :target: https://edudata.readthedocs.io/en/latest/?badge=latest
   :alt: License

.. image:: https://zenodo.org/badge/195198356.svg
   :target: https://zenodo.org/badge/latestdoi/195198356
   :alt: DOI



Convenient interface for downloading and preprocessing datasets in education.

The datasets include:

* `ASSISTments (2009-2010, 2012-2013, 2015, 2017) <https://sites.google.com/site/assistmentsdata/>`_ `[Analysis] <https://github.com/bigdata-ustc/EduData/tree/master/docs/ASSISTments>`_

* `KDD Cup 2010 <https://pslcdatashop.web.cmu.edu/KDDCup/downloads.jsp>`_  `[Analysis] <build/blitz/KDD_Cup_2010.ipynb>`_

* `OLI Engineering Statics 2011 <https://pslcdatashop.web.cmu.edu/DatasetInfo?datasetId=507>`_  `[Analysis] <https://github.com/bigdata-ustc/EduData/tree/master/docs/OLI_Fall2011>`_

* `JunyiAcademy Math Practicing Log <https://pslcdatashop.web.cmu.edu/DatasetInfo?datasetId=1198>`_  `[Analysis] <build/blitz/junyi/junyi.ipynb>`_

* `slepemapy.cz <https://www.fi.muni.cz/adaptivelearning/?a=data>`_

* `synthetic <https://github.com/chrispiech/DeepKnowledgeTracing/tree/master/data/synthetic>`_

* `math2015 <http://staff.ustc.edu.cn/~qiliuql/files/Publications/Qi-Liu-TIST2018.pdf>`_  `[Analysis] <https://github.com/bigdata-ustc/EduData/tree/master/docs/math2015>`_

* `EdNet <https://github.com/riiid/ednet>`_  `[Analysis] <build/blitz/EdNet_KT1/EdNet_KT1.ipynb>`_

* `pisa2015math <https://drive.google.com/drive/folders/1ja9P5yzeUDyzzm748p5JObAEs_Evysgc>`_  

* `workbankr <https://drive.google.com/drive/folders/1ja9P5yzeUDyzzm748p5JObAEs_Evysgc>`_

* `critlangacq <https://drive.google.com/drive/folders/1ja9P5yzeUDyzzm748p5JObAEs_Evysgc>`_

* `math23k <http://base.ustc.edu.cn/data/math23k.zip>`_  `[Analysis] <build/blitz/Math23k_Analysis_Report.ipynb>`_

* `MOOCCube <http://moocdata.cn/data/MOOCCube>`_  `[Analysis] <build/blitz/MOOCCube.md>`_  

* `NIPS2020 <https://www.microsoft.com/en-us/research/academic-program/diagnostic-questions/>`_

* `OpenLUNA <http://base.ustc.edu.cn/data/OpenLUNA/>`_

Your can also visit our datashop `BaseData <http://base.ustc.edu.cn/data/>`_  to get those mentioned-above (most of them) datasets.

Except those mentioned-above dataset, we also provide some benchmark dataset for some specified task, which is listed as follows:

* `knowledge tracing benchmark dataset <http://base.ustc.edu.cn/data/ktbd/>`_
* `cognitive diagnosis benchmark dataset <http://base.ustc.edu.cn/data/cdbd/>`_

Installation
=================

Git and install by ``pip``

::

 pip install -e .


or install from ``pypi``:

::

 pip install EduData

CLI
==========

::

 edudata $subcommand $parameters1 $parameters2

To see the ``help`` information:

::

 edudata -- --help
 edudata $subcommand --help

The cli tools is constructed based on `fire <https://github.com/google/python-fire>`_ .
Refer to the `documentation <https://github.com/google/python-fire/blob/master/docs/using-cli.md>`_ for detailed usage.

Download Dataset
==================

Before downloading dataset, first check the available dataset:

::

 edudata ls

and get:

::
 assistment-2009-2010-skill
 assistment-2012-2013-non-skill
 assistment-2015
 junyi
 ...
 ktbd
 ktbd-a0910
 ktbd-junyi
 ktbd-synthetic
 ...


Download the dataset by specifying the name of dataset:

::

 edudata download assistment-2009-2010-skill


In order to change the storing directory, use the following order:

::

 edudata download assistment-2009-2010-skill $dir


For detailed information of each dataset, refer to the docs

Task Specified Tools
============================

Knowledge Tracing
-----------------------



Format converter
----------------------

In Knowledge Tracing task, there is a popular format (we named it ``triple line (tl)`` format) to represent the interaction sequence records:

::

 5
 419,419,419,665,665
 1,1,1,0,0

which can be found in `Deep Knowledge Tracing <https://github.com/chrispiech/DeepKnowledgeTracing/tree/master/data/assistments>`_ .
In this format, three lines are composed of an interaction sequence.
The first line indicates the length of the interaction sequence,
and the second line represents the exercise id followed by the third line,
where each elements stands for correct answer (i.e., 1) or wrong answer (i.e., 0)


In order to deal with the issue that some special symbols are hard to be stored in the mentioned-above format,
we offer another one format, named ``json sequence`` to represent the interaction sequence records:

::

 [[419, 1], [419, 1], [419, 1], [665, 0], [665, 0]]


Each item in the sequence represent one interaction. The first element of the item is the exercise
id (in some works, the exercise id is not one-to-one mapped to one knowledge unit(ku)/concept,
but in junyi, one exercise contains one ku)
and the second one indicates whether the learner correctly answer the exercise, 0 for wrongly while 1 for correctly  
One line, one `json` record, which is corresponded to a learner's interaction sequence.

We provide tools for converting two format:

::

 # convert tl sequence to json sequence, by default, the exercise tag and answer will be converted into int type
 edudata tl2json $src $tar
 # convert tl sequence to json sequence without converting
 edudata tl2json $src $tar False
 # convert json sequence to tl sequence
 edudata json2tl $src $tar


Dataset Preprocess
---------------------

The cli tools to quickly convert the "raw" data of the dataset into "mature" data for knowledge tracing task.
The "mature" data is in ``json sequence`` format
and can be modeled by `XKT <https://github.com/bigdata-ustc/XKT>`_ and TKT(TBA)

junyi
------------

::

 # download junyi dataset to junyi/
 >>> edudata download junyi
 # build knolwedge graph
 >>> edudata dataset junyi kt extract_relations junyi/ junyi/data/
 # prepare dataset for knwoeldge tracing task, which is represented in json sequence
 >>> edudata dataset junyi kt build_json_sequence junyi/ junyi/data/ junyi/data/graph_vertex.json 1000
 # after preprocessing, a json sequence file, named student_log_kt_1000, can be found in junyi/data/
 # further preprocessing like spliting dataset into train and test can be performed
 >>> edudata train_valid_test junyi/data/student_log_kt_1000 -- --train_ratio 0.8 --valid_ratio 0.1 --test_ratio 0.1


Analysis Dataset
---------------------

This tool only supports the `json sequence` format. To check the following statical indexes of the dataset:

* knowledge units number
* correct records number
* the number of sequence

::

 edudata kt_stat $filename


Evaluation
--------------

In order to better verify the effectiveness of model,
the dataset is usually divided into ``train/valid/test`` or using ``kfold`` method.

::

 edudata train_valid_test $filename1 $filename2 --train_ratio 0.8 --valid_ratio 0.1 --test_ratio 0.1
 edudata kfold $filename1 $filename2 --n_splits 5

Refer to `longling <https://longling.readthedocs.io/zh/latest/#dataset>`_ for more tools and detailed information.

Citation
================

If this repository is helpful for you, please cite our work

::

 @misc{bigdata2021edudata,
 title={EduData},
 author={bigdata-ustc},
 publisher = {GitHub},
 journal = {GitHub repository},
 year = {2021},
 howpublished = {\url{https://github.com/bigdata-ustc/EduData}},
 }


More works
===============

Refer to our `website <http://base.ustc.edu.cn/>`_ and `github <https://github.com/bigdata-ustc>`_ for our publications and more projects



.. toctree::
   :caption: Introduction
   :hidden:

   self

.. toctree::
   :maxdepth: 1
   :caption: Tutorial
   :hidden:
   :glob:

   tutorial/en/index

.. toctree::
   :maxdepth: 1
   :caption: 用户指南
   :hidden:

   tutorial/zh/index
   tutorial/zh/DataSet
   tutorial/zh/Task


.. toctree::
   :maxdepth: 2
   :caption: API Reference
   :hidden:
   :glob:

   api/dataset
   api/task