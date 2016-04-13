import unittest

import countdown

class TestCountdown(unittest.TestCase):

  def test_exprs_pass(self):
    testlist = [1, 2]
    operators = '+*/-'
    expected = [
        [1, 2, '+'], [1, 2, '*'], [1, 2, '/'], [1, 2, '-']] 
    result = countdown.exprs([], 0, testlist, operators)
    self.assertEqual(list(result), expected)

  def test_exprs_fail(self):
    testlist = [1, 2]
    operators = '+*/-'
    expected = [
        [1, 2, '-'], [1, 2, '*'], [1, 2, '/'], [1, 2, '-']] 
    result = countdown.exprs([], 0, testlist, operators)
    self.assertNotEqual(list(result), expected)

  def test_calculate_pass(self):
    testlist = [1, 2, '+']
    expected = 3
    result = countdown.calculate(testlist)
    self.assertEqual(result, expected)

  def test_calculate_fail(self):
    testlist = [1, 2, '-']
    expected = 3
    result = countdown.calculate(testlist)
    self.assertNotEqual(result, expected)

  def test_make_rpn_pass(self):
    testlist = [1, 2]
    expected = [[[1, 2, '+']], [[2, 1, '+']]] 
    result = countdown.make_rpn(testlist, '+')
    self.assertEqual(result, expected)

  def test_make_rpn_fail(self):
    testlist = [1, 2]
    expected = [[[1, 2, '+']], [[2, 1, '-']]] 
    result = countdown.make_rpn(testlist, '+')
    self.assertNotEqual(result, expected)


if __name__ == '__main__':
  unittest.main()
