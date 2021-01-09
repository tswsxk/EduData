# CONTRIBUTE

## Guidance
Thank you for your interest in contributing to EduData! 
Before you begin writing code, it is important that you share your intention to contribute with the team, 
based on the type of contribution:

1. You want to propose a new feature and implement it.
    * Post about your intended feature in an issue, 
    and we shall discuss the design and implementation. 
    Once we agree that the plan looks good, go ahead and implement it.
2. You want to implement a feature or bug-fix for an outstanding issue.
    * Search for your issue in the [EduData issue list](https://github.com/bigdata-ustc/EduData/issues).
    * Pick an issue and comment that you'd like to work on the feature or bug-fix.
    * If you need more context on a particular issue, please ask and we shall provide.
3. You want to add the data analysis or a new dataset

Once you implement and test your feature or bug-fix, 
please submit a Pull Request to [https://github.com/bigdata-ustc/EduData](https://github.com/bigdata-ustc/EduData)

The followings are some helpful guidelines for different types contribution:
 
### Add new dataset

Currently, we only provide the downloading interface for the website http://base.ustc.edu.cn/data/.

If you try to add a new dataset, you should first upload the dataset to the website, and then complete two things:

* create the key-value pair in `URL_DICT` of [`download_data.py`](Edudata/Dataset/download/data/download_data.py)
* run `pytest` to test whether all test cases go well

## FAQ

Q: I have carefully test the code in my local system (all testing passed) but still failed in online ci?
 
A: There are two possible reasons: 
1. the online ci system is different from your local system;
2. there are some network error causing the downloading test failed, which you can find in the ci log.

For the second reason, all you need to do is to retry the test. 
