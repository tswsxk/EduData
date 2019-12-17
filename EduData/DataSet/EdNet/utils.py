# coding: utf-8
# 2019/12/17 @ tongshiwei

import csv


def get_question_id(question_str):
    """
    Examples
    --------
    >>> get_question_id("q123")
    123
    """
    return int(question_str.lstrip("q"))


class Judgement(object):
    def __init__(self, questions_csv):
        self.question = [None] * (18143 + 1)
        with open(questions_csv) as f:
            f.readline()
            for i, line in enumerate(csv.reader(f, delimiter=",")):
                _id = self.get_question_id(line[0])
                correct_answer = line[3]
                self.question[_id] = (i, correct_answer)

    @staticmethod
    def get_question_id(question_id):
        if isinstance(question_id, str):
            question_id = get_question_id(question_id)
        return question_id

    def is_correct(self, question_id: (str, int), user_answer: str):
        question_id = self.get_question_id(question_id)

        if self.question[question_id] is None:
            raise ValueError("Unknown question")

        return True if self.question[question_id][1] == user_answer else False

    def __call__(self, question_id: str, user_answer: str):
        question_id = self.get_question_id(question_id)

        if self.question[question_id] is None:
            raise ValueError("Unknown question")

        _id, ground_truth = self.question[question_id]
        return _id, 1 if ground_truth == user_answer else 0
