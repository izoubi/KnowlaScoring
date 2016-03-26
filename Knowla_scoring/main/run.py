__author__ = 'Ismail'


from main.Grading import *
from main import *

used_problem = problem
used_problem_answer = problem_answer
used_problem_feedback = problem_feedback
used_problem_con_steps = problem_consecutive_steps


a = GradingProblem(used_problem,used_problem_answer, used_problem_con_steps)
b = a.shuffle_problem()
a.print_problem(b)
a.get_user_input()
a.get_user_answer_steps()
a.get_accurate_user_input()

a.populate_user_answer_matrix()
a.to_print_matrix(a.user_answer_matrix)

user_score, total_score , score_percentage = a.get_user_score()
print(user_score,'out of', total_score, " with a percentage of ", score_percentage,'%')

notes = a.get_user_feedback()

for note_index in range(len(notes)):
    key = notes[note_index]
    print(used_problem_feedback[key])

