# https://docs.python.org/3/library/unittest.html
import test_case_1
import test_case_2

import unittest

# initialize the test suite
loader = unittest.TestLoader()
suite  = unittest.TestSuite()

# add tests to the test suite
suite.addTests(loader.loadTestsFromModule(test_case_1.TestCase1))
suite.addTests(loader.loadTestsFromModule(test_case_2.TestCase2))

# initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
