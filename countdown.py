import itertools
import operator
import postfix
import random
import sys
OPERATORS = {
        '+':  operator.add, '-':  operator.sub,
        '*':  operator.mul, '/':  operator.div}

def make_rpn(input_numbers):
  result = []
  for elem in itertools.permutations(input_numbers):
    result.append(list(postfix._exprs([], 0, elem, '-+*/')))
  return result

def main(n):
  result = {}
  target = 188
  #input_numbers = random.sample(range(1, 101), n) 
  #print 'input numbers %s' % input_numbers
  input_numbers = range(1, 7)[:n]
  for i in range(2, n+1):
    for operator_permutation in make_rpn(input_numbers[:i]):
      for sublist in operator_permutation:
        result[tuple(sublist)] = postfix.calculate(sublist)
  return result

if __name__ == '__main__':
  print  len(main(int(sys.argv[1])))
