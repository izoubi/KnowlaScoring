__author__ = 'Ismail'


class GradingProblem:
    def __init__(self, a_problem, a_problem_answer, a_problem_cons_steps):
        self.problem = a_problem
        self.correct_answer_matrix = a_problem_answer
        self.consecutive_steps = a_problem_cons_steps
        self.user_input = []  # user answer in numbers
        self.user_answer_matrix = [[0 for x in range(len(self.problem))] for x in range(len(self.problem))]
        self.populate_user_answer_matrix_diagonal()
        self.user_score = 0.0
        self._where_notes = []

    def populate_user_answer_matrix_diagonal(self):
        # precondition: user_answer_matrix is declared
        # postcondition: diagonal of user_answer_matrix is populated with '-'
        for i in range(len(self.user_answer_matrix)):
            for j in range(len(self.user_answer_matrix[i])):
                if i == j:
                    self.user_answer_matrix[i][j] = '-'
                else:
                    pass

    def get_user_input(self):
        # precondition: none.
        # postcondition: user input is collected and saved in user_input
        print("enter your answer from 1 to {}".format(len(self.problem)),
              ' in the correct order separated by a comma')
        self.user_input = input()
        self.user_input = self.user_input.split(',')  # to get the numbers of user answer

        self.user_input = [int(i) for i in self.user_input]  # convert the user input into integers

    def populate_user_answer_matrix(self):
        # precondition: user_answer_matrix is declared
        # postcondition:  user_answer_matrix is populated based on his/her answer
        for index_one in range(0, len(self.user_input)-1):
            key1 = self.user_input[index_one]
            for index_two in range(index_one + 1, len(self.user_input)):
                key2 = self.user_input[index_two]
                if key1 < key2:
                    self.user_answer_matrix[key1-1][key2-1] = 1  # for grades triangle
                    self.user_answer_matrix[key2-1][key1-1] = 0  # for notes triangle
                else:
                    self.user_answer_matrix[key2-1][key1-1] = 0  # for grades triangle
                    self.user_answer_matrix[key1-1][key2-1] = 1  # for notes triangle

    def get_user_score(self):
        # precondition : the user_answer_matrix is populated, and the correct_answer_matrix is received.
        # postcondition : user_score, total_score,  and score_percentage are calculated and returned
        for i in range(len(self.user_answer_matrix)):
            for j in range(i+1, len(self.user_answer_matrix[i])):
                self.user_score += float(self.user_answer_matrix[i][j] * self.correct_answer_matrix[i][j])
                # multiply each element in the user answer matrix in grades triangle with the identical element in
                # the correct answer matrix  grades triangle

        print("user answer before deduction if there is any", self.user_score) # this line would be deleted after
        self.check_consecutive_steps()  # check if the user has mistakes in the consecutive steps

        self.user_score = round(self.user_score, 2)

        return self.user_score

    def check_consecutive_steps(self):
        for a in self.consecutive_steps:
            check = self.consecutive_steps[a]
            if len(check) == 3:
                try:
                    step_a = int(self.user_input.index(check[0]))
                    step_b = int(self.user_input.index(check[1]))
                    penalty = float(check[2])
                    if step_a < step_b:
                        self.user_score -= penalty
                    else:
                        pass
                except:
                    pass

            elif len(check) == 5:
                step_a = int(self.user_input.index(check[0]))
                step_b = int(self.user_input.index(check[1]))
                step_c = int(self.user_input.index(check[2]))
                step_d = int(self.user_input.index(check[3]))
                penalty = float(check[4])
                if step_a < step_b and step_c < step_d:
                    self.user_score -= penalty
                else:
                    pass

    def get_user_feedback(self):
        # precondition : user_answer_matrix is populated
        # postcondition : wherever user has errors user_answer_matrix, errors are returned.
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








