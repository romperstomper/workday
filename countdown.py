import itertools
import operator
import random

def make_expressions(target = 188):
  operators = [operator.mul, operator.add, operator.sub, operator.div]
  # We get the cartisan product of the operators as they can repeat.
  operator_permutations = [x for x in itertools.product(operators, repeat = 5)]
  input_numbers = random.sample(range(1, 101), 6)
  input_permutations = [
      # We will use at least one and maximum 6 numbers.
      list(itertools.permutations(input_numbers, x)) for x in range(2, 7)
      ]
  return input_permutations

print [len(x) for x in make_expressions()]
