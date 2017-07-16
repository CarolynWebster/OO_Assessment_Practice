"""
Tests for part 1.

Testing the student class

>>> from practice import Student, Question, Exam
>>> s = Student('Jane', 'Hacks', '555 Main St.')
>>> s.first_name == 'Jane'
True
>>> s.last_name == 'Hacks'
True
>>> s.address == '555 Main St.'
True

Testing the question class

>>> q = Question('What color is the sky?', 'Blue')
>>> q.question == 'What color is the sky?'
True
>>> q.correct_answer == 'Blue'
True

Testing the exam class

>>> e = Exam('test')
>>> e.name.lower() == 'test'
True
>>> e.questions == []
True
"""

if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print("\nALL TESTS PASSED. GOOD WORK ON PART 1!\n")
