"""
Parts 1-4
Create your classes and class methods here according to the practice instructions.
As you are working on Parts 1, 2, and 4, you can run the test python file
corresponding to that section to verify that you are completing the problem
correctly.
ex: python part_1_tests.py.
"""


class Student(object):
    """A class for student objects"""

    #assign instance attributes when student is created
    def __init__(self, first_name, last_name, address):
        """Assigns instance attributes to newly created question"""
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):
    """A class for holding Question/answer pairs"""

    #assign instance attributes when question is created
    def __init__(self, question, answer):
        """Assigns instance attributes to newly created question"""

        self.question = question

        # stores answer in lowercase to reduce wrong answers based on capitzliation
        self.correct_answer = answer

        # had to remove bc it caused error in part 1 test
        # self.correct_answer = answer.lower()

    # asks a question and checks if the answer is correct
    def ask_and_evaluate(self):
        """A method to evaluate if answers to questions"""

        #take in raw input of user answer
        answer = raw_input(self.question + " > ")

        # makes answer lowercase to reduce wrong answers based on capitalization
        # had to remove bc it caused error in part 1 test
        # answer = answer.lower()

        #create var to check if answer is right or wrong
        result = False

        # if the answer matches the provided answer, result is true
        if answer == self.correct_answer:
            result = True

        #pass back True or False result
        return result


class Exam(object):
    """A class for exams"""

    def __init__(self, name):
        """Assigns instance attributes to newly created exam"""

        self.name = name
        self.questions = []

    def add_question(self, question):
        """A method for adding questions to the exam"""

        # appends a new question to the question list
        self.questions.append(question)

    def administer(self):
        """A method for administering a list of questions and returning score"""

        # create a var to hold the number of questions they get right
        correct_answers = 0

        # loop through the questions in the exam
        for question in self.questions:
            #store the True/False result when the question is asked
            result = question.ask_and_evaluate()
            # if the student got the question right, add point to the total score
            if result is True:
                correct_answers += 1

        # get the percent score by dividing the total number of right answers
        # against the total number of questions
        final_score = float(correct_answers)/len(self.questions)
        return final_score


class Quiz(Exam):
    """A type of exam with a pass/fail result"""

    def administer(self):
        # get the final score from the exam administer function
        quiz_result = super(Quiz, self).administer()

        # if the result is greater than or equal to 50% - it's a pass
        if quiz_result >= 0.5:
            return 1
        else:
            return 0


class StudentExam(object):
    """Stores a student, an exam, and the students score from that exam"""

    def __init__(self, student, exam):
        """sets instance attributes for the student and exam"""
        self.student = student
        self.exam = exam
        self.student_score = None

    def take_test(self):
        """Administers questions from exam and returns the score"""

        # use adminster method from the exam class
        self.student_score = self.exam.administer()

        #print the score for the student
        print "Your score is {}".format(self.student_score)


class StudentQuiz(StudentExam):
    """Store a student, a quiz, and the students result from that quiz"""

    def take_test(self):
        """Administers questions from quiz and returns pass or fail message"""

        # no real need to re-establish a init method to change var name
        # from exam to quiz - we call it exam here, but if a quiz is passed
        # through it will use the quiz class administer method

        # use adminster method from the quiz class
        self.student_score = self.exam.administer()

        if self.student_score == 1:
            print "Great job! You passed the quiz!"
        else:
            print "Sorry, you failed the quiz."


def example():
    """An example of a student taking an exam"""

    # create an example exam
    exam = Exam("example_exam")

    # add questions to the exam
    exam.add_question(Question('How cute are cats?', 'Very cute'))
    exam.add_question(Question('What is the square root of 2?', '4'))
    exam.add_question(Question('What is Carol\'s favorite color?', 'Blue'))

    # create a student to take the exam
    student = Student("Johnny", "Studentstein", "419 Guerrero St.")

    # pass the student and exam into StudentExam instance
    student_exam = StudentExam(student, exam)

    #use the take_test method to administer the test
    student_exam.take_test()

#call the example function if running practice.py
if __name__ == '__main__':
    example()
