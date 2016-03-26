__author__ = 'Ismail'

from main.Grading import *
import unittest


class TestGrading(unittest.TestCase):
    def setUp(self):
        self.problem = ['a', 'b', 'c', 'd', 'e']
        self.a = GradingProblem(self.problem)
        self.a.problem_shuffled = ['b', 'a', 'e', 'c', 'd']
        self.user_solution_matrix = [[0 for x in range(len(self.problem))] for x in range(len(self.problem))]
        self.a.user_input = [1, 2, 5, 3, 4]
        self.a.get_user_answer_steps()
        self.a.get_accurate_user_input()
        self.a.populate_user_answer_matrix_diagonal()
        self.a.populate_user_answer_matrix()

        self.problem_answer = [['-',1,1,1,1],
                               [0,'-',1,1,1],
                               [0,0,'-',1,1],
                               [0,0,0,'-',1],
                               [0,0,0,0,'-']]

        self.user_score, self.total_score, self.score_percentage = self.a.get_user_score(self.problem_answer)
        self.notes = self.a.get_user_feedback()

    def test_user_answer_steps(self):
        self.assertEqual(['b', 'a', 'd', 'e', 'c'], self.a.user_answer_steps)

    def test_accurate_user_input(self):
        self.assertEqual([2, 1, 4, 5, 3], self.a.accurate_user_input)

    def test_user_answer_matrix(self):
        self.assertEqual([['-', 0, 1, 1, 1],
                          [1, '-', 1, 1, 1],
                          [0, 0, '-', 0, 0],
                          [0, 0, 1, '-', 1],
                          [0, 0, 1, 0, '-']], self.a.user_answer_matrix)

    def test_user_score(self):
        self.assertEqual(7, self.user_score)
        self.assertEqual(10, self.total_score)
        self.assertEqual(70, self.score_percentage)

    def test_user_feedback(self):
        self.assertEqual(['21', '43', '53'],self.notes)