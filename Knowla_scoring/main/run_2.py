__author__ = 'Ismail'


from main.Grading import *
from main import *

used_problem = c
used_problem_answer = c_answer
used_problem_feedback = c_feedback
used_problem_con_steps = c_consecutive_steps

a = GradingProblem(used_problem, used_problem_answer, used_problem_con_steps)

a.print_problem(a.problem)
a.get_user_input()


a.populate_user_answer_matrix()
a.to_print_matrix(a.user_answer_matrix)

user_score = a.get_user_score()

total_score = c_total_grade
score_percentage = float(user_score / total_score * 100)
score_percentage = round(score_percentage, 2)

print(user_score, 'out of', total_score, " with a percentage of ", score_percentage,'%')

notes = a.get_user_feedback()

for note_index in range(len(notes)):
    key = notes[note_index]
    print(used_problem_feedback[key])

