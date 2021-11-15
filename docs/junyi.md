## junyi数据集说明
[data source](https://pslcdatashop.web.cmu.edu/Files?datasetId=1198)

### Authorization
	Any form of commercial usage is not allowed!
	Please cite the following paper if you publish your work:

	Haw-Shiuan Chang, Hwai-Jung Hsu and Kuan-Ta Chen,
	"Modeling Exercise Relationships in E-Learning: A Unified Approach,"
	International Conference on Educational Data Mining (EDM), 2015.

### Introduction
The dataset contains the problem log and exercise-related information on the Junyi Academy ( http://www.junyiacademy.org/ ), an E-learning platform established in 2012 on the basis of the open-source code released by Khan Academy. In addition, the annotations of exercise relationship we collected for building models are also available. 

### Meaning of Fields
#### junyi_Exercise_table.csv:
字段名 | 说明
------ | ----
name   | Exercise name (The name is also an id of exercise, so each name is unique in the dataset). If you want to access the exercise on the website, please append this name after url, http://www.junyiacademy.org/exercise/ (e.g., http://www.junyiacademy.org/exercise/similar_triangles_1 ). Please note that Junyi Academy are constantly changing their contents as Khan Academy did, so some url of exercises might be unavaible when you access them.
live   |Whether the exercise is still accessible on the website on Jan. 2015
prerequisite|	Indicate its prerequisite exericse (parent shown in its knowledge map)
h_position|	The coordiate on the x axis of the knowledge map
v_position|	The coordiate on the y axis of the knowledge map
creation_date|	The date this exercise is created
seconds_per_fast_problem|	The website judge a student finish the exercise fast if he/she takes less then this time to answer the question. The number is manually assigned by the experts in Junyi Academy.
pretty_display_name|	The chinese name of exercise shown in the knowledge map (Please use UTF-8 to decode the chinese characters)
short_display_name|	Another chinese name of exercise (Please use UTF-8 to decode the chinese characters)
topic|	The topic of each exercise, and the topic would be shown as a larger node in the knowledge map.
area:| The area of each exercise (Each area contains several topics)

* Example

name|live|prerequisites|h_position|v_position|creation_date|seconds_per_fast_problem|pretty_display_name|short_display_name|topic|area
---|---|---|---|---|---|---|---|---|---|---
parabola_intuition_1|TRUE|recognizing_conic_sections|47|2|2012-10-11 17:55:24.8056 UTC|13|?物線直覺 1|?物線直覺1|conic-sections|algebra
circles_and_arcs|TRUE||40|-20|2012-10-11 17:55:33.41014 UTC|27|圓與弧|圓與弧|area-perimeter-and-volume|geometry


#### relationship_annotation_training.csv / relationship_annotation_testing.csv
字段名 | 说明
----|---
Exercise_A, Exercise_B|	The exercise names being compared
Similarity_avg, Difficulty_avg, Prequesite_avg|	The mean opinion scores of different relationships. This is also the ground truth we used to train/test our model.
Similarity_raw, Difficulty_raw, Prequesite_raw|	The raw scores given by workers (delimiter is "_")

* Example

Exercise_A|Exercise_B|Similarity_avg|Similarity_raw|Difficulty_avg|Difficulty_raw|Prerequisite_avg|Prerequisite_raw
---|---|---|---|---|---|---|---
radius_diameter_and_circumference|arithmetic_word_problems_1|1.857142857|1_4_1_1_1_1_2_1_1_1_3_1_3_5|2.857142857|4_5_1_1_1_1_7_1_1_4_2_5_2_5|3|1_6_1_1_1_3_2_1_9_2_3_2_8_2
radius_diameter_and_circumference|parts_of_circles|6.785714286|6_9_6_6_7_8_7_8_8_8_4_6_5_7|2.428571429|3_5_1_3_2_1_5_1_1_1_1_2_5_3|7.285714286|6_7_7_6_8_8_9_5_9_9_7_7_5_9


#### junyi_ProblemLog_original.csv
字段名 | 说明
------ | ----
user_id|	An number represents an user
exercise|	Exercise name
problem_type|	Some exercises would record what template of problem this student encounters at this time
problem_number|	How many times this student practices this exercise (e.g., the number would be 1 if the student tries to answer this exercise at the first time)
topic_mode| Whether the student is assigned this exercise by clicking the topic icon (This function has been closed now)
suggested|	Whether the exercise is suggested by the system according to prerequisite relationships on the knowledge map
review_mode|	Whether the exercise is done by the student after he/she earn proficiency
time_done|		Unix timestamp in microsecends
time_taken|		Second the student spend on this exercise
time_taken_attempts|	Seconds the student spend on each answering attempt 
correct|	Whether the student's first attempt is correct, and the field would be false if any hint is requested
count_attempts|	How many times student attempt to answer the problem
hint_used|	Whether student request hints
count_hints|	How many times student request hints
hint_time_taken_list|	Seconds the student spend on each requested hints
earned_proficiency|	Whether the student reaches proficiency. Please refer to http://david-hu.com/2011/11/02/how-khan-academy-is-using-machine-learning-to-assess-student-mastery.html for the algorithm of determining proficiency 
points_earned|	How many points students earn for this practice

* Example

user_id|exercise|problem_type|problem_number|topic_mode|suggested|review_mode|time_done|time_taken|time_taken_attempts|correct|count_attempts|hint_used|count_hints|hint_time_taken_list|earned_proficiency|points_earned
---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---
12884|time_terminology|analog_word|1|false|false|false|1420714810324490|4|3&1|false|2|false|0|null|false|0
239464|multiplication_1|0|6|false|false|false|1403098400836660|2|2|true|1|false|0|null|false|14

#### junyi_ProblemLog_for_PSLC.csv
The tab delimited format used in PSLC datashop, please refer to their document ( https://pslcdatashop.web.cmu.edu/help?page=importFormatTd )
The size of the text file is too large (9.1 GB) to analyze using tools of websites, so we compress the text file and put it as an extra file of the dataset. We also upload a small subset of data into the website for the illustration purpose. Note that there are some assumptions when converting the data into this format, please read the description of our dataset for more details.
* Example

Anon Student Id|Session Id|Time|Student Response Type|Tutor Response Type|Level (Unit)|Level (Section)|Problem Name|Problem Start Time|Step Name|Outcome|Condition Name|Condition Type|Selection|Action|Input|KC (Exercise)|KC (Topic)|KC (Area)|CF (points_earned)|CF (earned_proficiency)
---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---
12884|148691|1420714809324|ATTEMPT|RESULT|telling-time|time_terminology|time_terminology--analog_word|1420714806324|time_terminology--analog_word|INCORRECT|Choose_Exercise|NA|NA|NA|NA|time_terminology|telling-time|arithmetic|0|0
12884|148691|1420714810324|ATTEMPT|RESULT|telling-time|time_terminology|time_terminology--analog_word|1420714809324|time_terminology--analog_word|INCORRECT|Choose_Exercise|NA|NA|NA|NA|time_terminology|telling-time|arithmetic|0|0
239464|93497|1403098400837|ATTEMPT|RESULT|multiplication-division|multiplication_1|multiplication_1--0|1403098398837|multiplication_1--0|CORRECT|Choose_Exercise|NA|NA|NA|NA|multiplication_1|multiplication-division|arithmetic|14|0

### Questions and Collaboration:
	1. If you have any question to this dataset, please e-mail to hschang@cs.umass.edu.
	2. If you have intention to acquire more data which fit your research purpose, please contact Junyi Academy directly for discussing the further cooperation opportunites by emailing to support@junyiacademy.org
### Note:
	1. The dataset we used in our paper (Modeling Exercise Relationships in E-Learning: A Unified Approach) is extracted from Junyi Academy on July 2014, and this dataset is extracted on Jan 2015. After applying our method on the new dataset, we got similar observation with that in our paper, even though this dataset contains more users and exercises. 
	2. After uncompress the original problem log and problem log using PLSC format, the text files will take around 2.6 GB and 9.1 GB respectively. Please prepare enough space in your disk.
	
### Annotaion:
1. PSLC数据集是对original数据集做了处理以后生成的数据，拆分的字段为time_taken_attempts，因此PSLC数据集的条目数比original的多


### Analysis
#### 每个用户的练习次数及对应的知识点数(50000 session 抽样)
||exercise_length|exercise_num
|---|---|---
|count|8246.000000|8246.000000
|mean|167.808513|9.569367
|std|616.725544|21.860770
|min|1.000000|1.000000
|25%|7.000000|1.000000
|50%|19.000000|3.000000
|75%|85.000000|9.000000
|90%|335.000000|23.000000
|max|16111.000000|517.000000

#### 每个用户的session数(50000 session 抽样)
||session_num
|---|---
|count|8246.000000
|mean|6.063789
|std|18.974000
|min|1.000000
|10%|1.000000
|25%|1.000000
|50%|1.000000
|75%|4.000000
|90%|12.000000
|max|521.000000

#### 每个session对应的练习次数、知识点数、session的近似持续时间(50000 session 抽样)
||exercise_length|exercise_num|last_time
|---|---|---|---
|count|50002.000000|50002.000000|50002.00000
|mean|27.673873|2.833487|386.93766
|std|42.860613|3.816037|518.76202
|min|1.000000|1.000000|0.00000
|10%|1.000000|1.000000|0.00000
|25%|4.000000|1.000000|48.95350
|50%|11.000000|1.000000|201.17450
|75%|33.000000|3.000000|518.81725
|90%|72.000000|6.000000|1024.00000
|max|1107.000000|143.000000|7573.38600