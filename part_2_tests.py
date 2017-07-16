"""
Tests for Part 2.

Testing the add_question function.

Since this is interactive, let's have a fake input handler:

>>> import sys
>>> def fake_input(prompt):
...     sys.stdout.write(prompt)
...     v = _inputs.pop(0)
...     print(v)
...     return v

>>> try:
...     import __builtin__ as b    # Python 2
... except ImportError:
...     import builtins as b       # Python 3

>>> b.raw_input = b.input = fake_input

>>> from practice import Question, Exam, Student
>>> e = Exam('test')
>>> q = Question('How are you?', 'Great')
>>> e.add_question(q)
>>> q in e.questions
True
>>> _inputs = ['Fine', 'Great', 'Fine', 'Blue', 'Great', 'Blue', 'Fine', 'Grey']
>>> e.questions[0].ask_and_evaluate()
How are you? > Fine
False
>>> e.questions[0].ask_and_evaluate()
How are you? > Great
True
>>> e.add_question(Question('What color is the sky?', 'Blue'))
>>> e.administer()
How are you? > Fine
What color is the sky? > Blue
0.5
>>> e.administer()
How are you? > Great
What color is the sky? > Blue
1.0
>>> e.administer()
How are you? > Fine
What color is the sky? > Grey
0.0
"""
if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print("\nALL TESTS PASSED. GOOD WORK ON PART 2!\n")