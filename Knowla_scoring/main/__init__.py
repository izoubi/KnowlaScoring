__author__ = 'Ismail'

problem = [1, 2, 3, 4, 5]
problem_answer = [['-', 1, 1, 1, 1],
                  [0, '-', 1, 1, 1],
                  [0, 0, '-', 1, 1],
                  [0, 0, 0, '-', 1],
                  [0, 0, 0, 0, '-']]

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

problem_consecutive_steps = {'a': [3, 1, 1, 4],
                             'b': [3, 2, 2, 4],
                             'c': [5, 4, 3, 5],
                             'd': [2, 1]}