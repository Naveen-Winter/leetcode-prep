import unittest
from valid_prathesis import IsValidSolution


class IsValidSolutionTest(unittest.TestCase):
    def test_something(self):
        instance = IsValidSolution()
        self.assertEqual(True, instance.isValid("{[]}"))  # add assertion here
        self.assertEqual(False, instance.isValid("}}"))  # add assertion here
        self.assertEqual(False, instance.isValid("{"))  # add assertion here
        self.assertEqual(False, instance.isValid("{^"))  # add assertion here


