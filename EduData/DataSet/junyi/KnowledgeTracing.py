# coding: utf-8
# create by tongshiwei on 2019-7-5

import csv
import json

from longling import wf_open
from tqdm import tqdm

from EduData.Tools import train_valid_test


def extract_students_log(source, target, ku_dict):
    """require big memory to run this function"""

    outcome = {
        "INCORRECT": 0,
        "CORRECT": 1,
        "HINT": 0,
    }

    students = {}

    with open(ku_dict) as f:
        ku_dict = json.load(f)

    with open(source) as f:
        f.readline()
        for line in tqdm(csv.reader(f, delimiter='\t'), "reading data"):
            student, session, exercise, correct, timestamp = line[0], line[1], ku_dict[line[-5]], \
                                                             outcome[line[10]], line[8]
            if student not in students:
                students[student] = {}
            if session not in students[student]:
                students[student][session] = []

            students[student][session].append([int(timestamp), exercise, correct])

    with wf_open(target) as wf:
        for student_id, sessions in tqdm(students.items(), "sorting"):
            for session_id, exercises in sessions.items():
                exercises.sort(key=lambda x: x[0])
                exercise_response = [(exercise[1], exercise[2]) for exercise in exercises]
                print(json.dumps(exercise_response), file=wf)


def select_n_most_frequent_students(source, target, n=1000):

    pass


if __name__ == '__main__':
    root = "../../"
    student_log_raw_file = root + "raw_data/junyi/junyi_ProblemLog_for_PSLC.txt"
    student_log_file = root + "data/junyi/student_log_kt.json"
    ku_dict_file = root + "data/junyi/graph_vertex.json"
    # extract_students_log(student_log_raw_file, student_log_file, ku_dict_file)

    student_log_file_small = student_log_file + ".small"

    with open(student_log_file) as f, wf_open(student_log_file_small) as wf:
        for i, line in tqdm(enumerate(f)):
            if i > 50000:
                break
            print(line, end="", file=wf)

    print(train_valid_test(
        student_log_file_small,
        valid_ratio=0.,
        test_ratio=0.2,
        root_dir=root + "data/junyi/",
        silent=False,
    ))
