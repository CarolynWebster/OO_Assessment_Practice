"""
Tests for Part 4.

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

>>> from practice import Question, Exam, Student, Quiz
>>> q = Quiz('quiz')
>>> q.add_question(Question('What is the list method for sorting a list object?', '.sort()'))
>>> _inputs = ['.sort()', 'sorted()']
>>> q.administer()
What is the list method for sorting a list object? > .sort()
1
>>> q.administer()
What is the list method for sorting a list object? > sorted()
0
"""

if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print("\nALL TESTS PASSED. GOOD WORK ON PART 4!\n")
