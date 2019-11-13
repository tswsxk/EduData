# EduData
Convenient interface for downloading and preprocessing dataset in education.

The dataset includes:

* [KDD Cup 2010](https://pslcdatashop.web.cmu.edu/KDDCup/downloads.jsp)

* [ASSISTments](https://sites.google.com/site/assistmentsdata/)

* [OLI Engineering Statics 2011](https://pslcdatashop.web.cmu.edu/DatasetInfo?datasetId=507)

* [JunyiAcademy Math Practicing Log](https://pslcdatashop.web.cmu.edu/DatasetInfo?datasetId=1198)

* [slepemapy.cz](https://www.fi.muni.cz/adaptivelearning/?a=data)

* [synthetic](https://github.com/chrispiech/DeepKnowledgeTracing/tree/master/data/synthetic)

Your can also visit our datashop [BaseData](http://base.ustc.edu.cn/data/) to get those mentioned-above (most of them) dataset. 

## Tutorial

### Installation
Git and install by `pip`

```shell
pip install -e .
```

### CLI
```shell
edudata $subcommand $parameters1 $parameters2
```

To see the `help` information:
```shell
edudata -- --help
edudata $subcommand --help
```

The cli tools is constructed based on [fire](https://github.com/google/python-fire). 
Refer to the [documentation](https://github.com/google/python-fire/blob/master/docs/using-cli.md) for detailed usage.

#### Download Dataset
Before downloading dataset, first check the available dataset:
```shell
edudata ls
```

Download the dataset by specifying the name of dataset:
```shell
edudata download assistment-2009-2010-skill
```

#### Task Specified Tools

##### Knowledge Tracing

###### Format converter
In Knowledge Tracing task, there is a popular format (we named it `triple line (tl)` format) to represent the interaction sequence records:
```text
5
419,419,419,665,665
1,1,1,0,0
```
which can be found in [Deep Knowledge Tracing](https://github.com/chrispiech/DeepKnowledgeTracing/tree/master/data/assistments).
In this format, three lines are composed of an interaction sequence.
The first line indicates the length of the interaction sequence, 
and the second line represents the exercise id followed by the third line, 
where each elements stands for correct answer (i.e., 1) or wrong answer (i.e., 0) 


In order to deal with the issue that some special symbols are hard to be stored in the mentioned-above format,
we offer another one format, named `json sequence` to represent the interaction sequence records:
```json
[[419, 1], [419, 1], [419, 1], [665, 0], [665, 0]]
```

Each item in the sequence represent one interaction. The first element of the item is the exercise 
(some works call it knowledge unit or knowledge item) id 
and the second one indicates whether the learner correctly answer the exercise, 0 for wrongly while 1 for correctly  
One line, one `json` record, which is corresponded to a learner's interaction sequence.

We provide tools for converting two format:
```shell
# convert tl sequence to json sequence
edudata tl2json $src $tar
# convert json sequence to tl sequence
edudata json2tl $src $tar
```

###### Dataset Preprocess
The cli tools to quickly convert the "raw" data of the dataset into "mature" data for knowledge tracing task. 
The "mature" data is in `json sequence` format 
and can be modeled by [XKT](https://github.com/bigdata-ustc/XKT) and TKT(TBA)

TBA

###### Analysis Dataset
This tool only supports the `json sequence` format. To check the following statical indexes of the dataset:

* knowledge units number
* correct records number
* the number of sequence

```shell
edudata kt_stat $filename
```

#### Evaluation
In order to better verify the effectiveness of model, 
the dataset is usually divided into `train/valid/test` or using `kfold` method.

```shell
edudata train_valid_test $filename1 $filename2 -- --train_ratio 0.8 --valid_ratio 0.1 --test_ratio 0.1
edudata kfold $filename1 $filename2 -- --n_splits 5
```
Refer to [longling](https://longling.readthedocs.io/zh/latest/#dataset) for more tools and detailed information.
