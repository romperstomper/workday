import itertools
import time;
import operator
import random
import sys


def exprs(expr, stack_depth, vals, ops):
  """ Generate postfix expressions recursively.

  Args:
    expr: (list) is the expression so far, a list of values and operators.
    stack_depth: (int) is the depth of the stack created by expr.
    vals: (list) is a list of values remaining to add to the expression.
    ops: (str) possible operators to choose from.

  Yields:
    (list) expression in postfix notation.
  """
  if stack_depth == 1 and not vals:
    # This is a valid expression.
    yield expr
  if stack_depth > 1:
    # Try using an operator
    for o in ops:
      for e in exprs(expr+[o], stack_depth-1, vals, ops):
        yield e
  if vals:
    # Vals are available, push one on the stack
    for e in exprs(expr+[vals[0]], stack_depth+1, vals[1:], ops):
      yield e


def calculate(inputs):
  """Calculate the value of the expression passed in.

  Args:
    input: (list) expression in postfix to evaluate.

  Returns:
    (int) total calculated or 0.
  """
  stack = []
  for a in inputs:
    if type(a) is int:
        stack.append(a)
        continue
    if len(stack) > 1:
      op1, op2 = stack.pop(), stack.pop()
    else:
      return 0

    if a == '+':
        stack.append(op2 + op1)
    elif a == '*':
        stack.append(op2 * op1)
    elif a == '-':
      if op2 - op1 != 0:
        stack.append(op2 - op1)
      else:
        return 0
    elif a == '/' and op1 != 0 and op2 != 0:
      if op2 % op1 == 0:
        stack.append(op2 / op1)
      else:
        return 0

  if stack:
    return stack.pop()
  else:
    return 0


def make_rpn(input_numbers):
  """Calculate the value of the expression passed in.

  Args:
    input: (list) expression in postfix to evaluate.

  Returns:
    (int) total calculated or 0.
  """
  result = []
  for elem in itertools.permutations(input_numbers):
    result.append(list(exprs([], 0, elem, '+*/-')))
  return result

def main(n):
  result = {}
  best = (0, [])
  target = random.choice(range(101, 1000))
  input_numbers = random.sample(range(1, 101), n) 
  for i in range(2, n+1):
    for operator_permutation in make_rpn(input_numbers[:i]):
      for expression in operator_permutation:
        value = calculate(expression)
        if value == target:
          return value, expression, len(result)
        if value:  # No op if value is 0.
          result[tuple(expression)] = value 

  return len(result)


if __name__ == '__main__':
  t0 = time.time()
  print  main(int(sys.argv[1])), time.time() - t0
