__author__ = 'Ismail'

import random


class GradingProblem:
    def __init__(self, a_problem, a_problem_answer, a_problem_cons_steps):
        self.problem = a_problem
        self.correct_answer_matrix = a_problem_answer
        self.consecutive_steps = a_problem_cons_steps
        self.problem_shuffled = self.problem.copy()
        self.user_input =[]  # user answer in numbers
        self.user_answer_steps = []  # user answer in steps same as problem steps
        self.accurate_user_input = []  # user answer in numbers (comparing his/her input_steps to the problem steps)
        self.user_answer_matrix =[[0 for x in range(len(self.problem))] for x in range(len(self.problem))]
        self.populate_user_answer_matrix_diagonal()
        self.user_score, self.total_score, self.score_percentage = 0, 0, 0
        self._where_notes = []

    def populate_user_answer_matrix_diagonal(self):
        for i in range(len(self.user_answer_matrix)):
            for j in range(len(self.user_answer_matrix[i])):
                if i == j:
                    self.user_answer_matrix[i][j] = '-'
                else:
                    pass

    def shuffle_problem(self):
        random.shuffle(self.problem_shuffled)
        return self.problem_shuffled

    def get_user_input(self):
        # precondition: none.
        # postcondition: user input is collected
        print("enter your answer from 1 to {}".format(len(self.problem_shuffled)),
              ' in the correct order separated by a comma')
        self.user_input = input()
        self.user_input = self.user_input.split(',')  # to get the numbers of user answer

    def get_user_answer_steps(self):
        # precondition: user inserted his/her answer
        # postcondition: user's answer in form of steps is found
        for i in range(len(self.user_input)):
            key = int(self.user_input[i])
            self.user_answer_steps.append(self.problem_shuffled[key-1])

    def get_accurate_user_input(self):
        # precondition : user's answer in form of steps is known + the correct problem before shuffling it is known too
        # postcondition : accurate user input in form of numbers from 1 to the number of steps is found

        for user_input_index in range(0, len(self.user_answer_steps)):
            key = self.user_answer_steps[user_input_index]
            for correct_answer_index in range(0, len(self.problem)):
                if (self.problem[correct_answer_index]) == key:
                    # compare each element in the correct answer against user's input
                    self.accurate_user_input.append(correct_answer_index+1)
                    break  # terminate the internal loop if the condition is TRUE

    def populate_user_answer_matrix(self):
        # precondition: accurate user answer is found, user answer matrix is declared
        # postcondition:  user answer matrix is populated based on his/her answer
        for index_one in range(0, len(self.accurate_user_input)-1):
            key1 = self.accurate_user_input[index_one]
            for index_two in range(index_one + 1, len(self.accurate_user_input)):
                key2 = self.accurate_user_input[index_two]
                if key1 < key2:
                    self.user_answer_matrix[key1-1][key2-1] = 1  # for grades triangle
                    self.user_answer_matrix[key2-1][key1-1] = 0  # for notes triangle
                else:
                    self.user_answer_matrix[key2-1][key1-1] = 0  # for grades triangle
                    self.user_answer_matrix[key1-1][key2-1] = 1  # for notes triangle

    def get_user_score(self):
        # precondition : the user answer matrix is populated, and the correct answer matrix is received.
        # postcondition : user score and the total score are calculated

        for i in range(len(self.user_answer_matrix)):
            for j in range(i+1, len(self.user_answer_matrix[i])):
                self.user_score += int(self.user_answer_matrix[i][j] * self.correct_answer_matrix[i][j])  # (returned user score)
                # multiply each element in the user answer matrix in grades triangle with the identical element in
                # the correct answer matrix  grades triangle
                self.total_score += int(self.correct_answer_matrix[i][j])  # returned total score

        print("user answer before deduction if there is any", self.user_score) # this line would be deleted after
        self.check_consecutive_steps()
        self.score_percentage = int(self.user_score / self.total_score * 100)

        return self.user_score, self.total_score, self.score_percentage

    def check_consecutive_steps(self):
        for a in self.consecutive_steps:
            check = self.consecutive_steps[a]
            if self.accurate_user_input.index(check[0]) < self.accurate_user_input.index(check[1]) and \
                            self.accurate_user_input.index(check[2]) < self.accurate_user_input.index(check[3]):
                self.user_score -= 1
            else:
                pass

    def get_user_feedback(self):
        # precondition : user answer matrix is populated
        # postcondition : where user had errors (notes) are returned.
        for i in range(len(self.user_answer_matrix)):
            for j in range(i):  # loop through the notes triangle only.
                if self.user_answer_matrix[i][j] == 1:
                    key = str(i+1)+str(j+1)  # append the accurate indexes of where the error is.
                    self._where_notes.append(key)
        return self._where_notes

    @staticmethod
    def print_problem( to_print):
        for i in range(len(to_print)):
            print(str(i+1)+'.', to_print[i])

    @staticmethod
    def to_print_matrix(a_matrix):
        for i in range(len(a_matrix)):
            for j in range(len(a_matrix[i])):
                print(a_matrix[i][j], end=' ')
            print(end='\n')








