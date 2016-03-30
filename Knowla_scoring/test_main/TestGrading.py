__author__ = 'Ismail'

from main.Grading import *
import unittest


class TestGrading(unittest.TestCase):
    def setUp(self):
        self.problem = [1, 2, 3, 4, 5]

        self.problem_answer = [['-',1,1,1,1],
                               [0,'-',1,1,1],
                               [0,0,'-',1,1],
                               [0,0,0,'-',1],
                               [0,0,0,0,'-']]

        self.consecutive_steps = {'a': [3, 1, 1, 4],
                                  'b': [3, 2, 2, 4],
                                  'c': [5, 4, 3, 5]}

        self.a = GradingProblem(self.problem, self.problem_answer, self.consecutive_steps)

        self.user_solution_matrix = [[0 for x in range(len(self.problem))] for x in range(len(self.problem))]
        self.a.user_input = [1, 2, 3, 4, 5]
        self.a.populate_user_answer_matrix_diagonal()
        self.a.populate_user_answer_matrix()
        self.user_score, self.total_score, self.score_percentage = self.a.get_user_score()
        self.notes = self.a.get_user_feedback()

    def test_user_answer_steps(self):
        self.assertEqual([1, 2, 3, 4, 5], self.a.user_input)


    def test_user_answer_matrix(self):
        self.assertEqual([['-', 1, 1, 1, 1],
                          [0, '-', 1, 1, 1],
                          [0, 0, '-', 1, 1],
                          [0, 0, 0, '-', 1],
                          [0, 0, 0, 0, '-']], self.a.user_answer_matrix)

    def test_user_score(self):
        self.assertEqual(10, self.user_score)
        self.assertEqual(10, self.total_score)
        self.assertEqual(100, self.score_percentage)

    def test_user_feedback(self):
        self.assertEqual([], self.notes)