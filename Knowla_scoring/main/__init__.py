__author__ = 'Ismail'

problem = [1, 2, 3, 4, 5]
problem_answer = [['-', 1, 1, 1, 1],
                  [0, '-', 1, 1, 1],
                  [0, 0, '-', 1, 1],
                  [0, 0, 0, '-', 1],
                  [0, 0, 0, 0, '-']]

problem_total_grade = 10

problem_feedback = {'21': 'this is because you chose 2 before 1',
                    '31': 'this is because you chose 3 before 1',
                    '41': 'this is because you chose 4 before 1',
                    '51': 'this is because you chose 5 before 1',
                    '32': 'this is because you chose 3 before 2',
                    '42': 'this is because you chose 4 before 2',
                    '52': 'this is because you chose 5 before 2',
                    '43': 'this is because you chose 4 before 3',
                    '53': 'this is because you chose 5 before 3',
                    '54': 'this is because you chose 5 before 4'}


problem_consecutive_steps = {'a': [3, 1, 1, 4, 1.2],
                             'b': [3, 2, 2, 4, 1.3],
                             'c': [5, 4, 3, 5, 2],
                             'd': [2, 1, 0.3]}
# 'a' if user selects step 3 before 1, and 1 before 4, his/her grade is minimized by 1.2
# 'b' if user selects step 3 before 2, and 2 before 4, his/her grade is minimized by 1.3
# 'c' if user selects step 5 before 4, and 3 before 5, his/her grade is minimized by 2
# 'd' if user selects step 2, his/her grade is minimized by 0.3

#################################################

second_problem = [1, 2, 3, 4, 5, 6, 7]

second_problem_answer = [['-', 1, 1, 1, 0, 0, 0],
                         [0, '-', 1, 1, 0, 0, 0],
                         [0, 0, '-', 1, 0, 0, 0],
                         [0, 0, 0, '-', 0, 0, 0],
                         [0, 0, 0, 'a', '-', 0, 0],
                         [0, 0, 0, 0, 0, '-', 0],
                         [0, 0, 0, 0, 0, 0, '-']]

second_problem_total_grade = 6

second_problem_consecutive_steps = {'a': [5, 4, 6]}
# 'a' if user selects step 5 before 4 his/her grade is minimized by 6
second_problem_feedback = {'21': 'this is because you chose 2 before 1',
                           '31': 'this is because you chose 3 before 1',
                           '41': 'this is because you chose 4 before 1',
                           '51': 'this is because you chose 5 before 1',
                           '61': 'this is because you chose 6 before 1',
                           '71': 'this is because you chose 7 before 1',
                           '32': 'this is because you chose 3 before 2',
                           '42': 'this is because you chose 4 before 2',
                           '52': 'this is because you chose 5 before 2',
                           '62': 'this is because you chose 6 before 2',
                           '72': 'this is because you chose 7 before 2',
                           '43': 'this is because you chose 4 before 3',
                           '53': 'this is because you chose 5 before 3',
                           '63': 'this is because you chose 6 before 3',
                           '73': 'this is because you chose 7 before 3',
                           '54': 'this is because you chose 5 before 4',
                           '64': 'this is because you chose 6 before 4',
                           '74': 'this is because you chose 7 before 4',
                           '65': 'this is because you chose 6 before 5',
                           '75': 'this is because you chose 7 before 5',
                           '76': 'this is because you chose 7 before 6'}
###########################
# the next is the third problem

c = [1, 2, 3, 4, 5, 6, 7]

c_answer = [['-', 1, 1, 1, -0.5, -0.5, -0.5],
            [0, '-', 1, 1, -0.5, -0.5, -0.5],
            [0, 0, '-', 1, -0.5, -0.5, -0.5],
            [0, 0, 0, '-', -0.5, -0.5, -0.5],
            [-0.5, -0.5, -0.5, -0.5, '-', -0.5, -0.5],
            [-0.5, -0.5, -0.5, -0.5, -0.5, '-', -0.5],
            [-0.5, -0.5, -0.5, -0.5, -0.5, -0.5, '-']]

c_total_grade = 6
c_consecutive_steps = {'a': [5, 1, 0.5],
                       'b': [6, 1, 0.5],
                       'c': [7, 1, 0.5],
                       'd': [5, 2, 0.5],
                       'e': [6, 2, 0.5],
                       'f': [7, 2, 0.5],
                       'g': [5, 3, 0.5],
                       'h': [6, 3, 0.5],
                       'i': [7, 3, 0.5],
                       'j': [5, 4, 0.5],
                       'k': [6, 4, 0.5],
                       'l': [7, 4, 0.5],
                       'm': [6, 5, 0.5],
                       'n': [7, 5, 0.5],
                       'o': [7, 6, 0.5]}
c_feedback = {'21': 'this is because you chose 2 before 1',
              '31': 'this is because you chose 3 before 1',
              '41': 'this is because you chose 4 before 1',
              '51': 'this is because you chose 5 before 1',
              '61': 'this is because you chose 6 before 1',
              '71': 'this is because you chose 7 before 1',
              '32': 'this is because you chose 3 before 2',
              '42': 'this is because you chose 4 before 2',
              '52': 'this is because you chose 5 before 2',
              '62': 'this is because you chose 6 before 2',
              '72': 'this is because you chose 7 before 2',
              '43': 'this is because you chose 4 before 3',
              '53': 'this is because you chose 5 before 3',
              '63': 'this is because you chose 6 before 3',
              '73': 'this is because you chose 7 before 3',
              '54': 'this is because you chose 5 before 4',
              '64': 'this is because you chose 6 before 4',
              '74': 'this is because you chose 7 before 4',
              '65': 'this is because you chose 6 before 5',
              '75': 'this is because you chose 7 before 5',
              '76': 'this is because you chose 7 before 6'}