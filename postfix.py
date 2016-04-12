# Enumerate postfix expressions

def _exprs(expr, stack_depth, vals, ops):
    """ Generate postfix expressions recursively.
        `expr` is the expression so far, a list of values and operators.
        `stack_depth` is the depth of the stack created by expr.
        `vals` is a list of values remaining to add to the expression.
        `ops` is a list of possible operators to choose from.
    """
    if stack_depth == 1 and not vals:
        # This is a valid expression.
        yield expr
    if stack_depth > 1:
        # Try using an operator
        for o in ops:
            for e in _exprs(expr+[o], stack_depth-1, vals, ops):
                yield e
    if vals:
        # Vals are available, push one on the stack
        for e in _exprs(expr+[vals[0]], stack_depth+1, vals[1:], ops):
            yield e

def exprs(vals, ops):
    """ Generate postfix expressions created from `vals`, the list of values
        to use, and `ops`, the possible operators to combine them with.
    """
    result = []
    for v in vals:
      result.append(_exprs([], 0, v, ops))
    return result

def all_exprs(n, ops='+'):
     return [ " ".join(e) for e in exprs(n, ops) ]

def calculate(inputs):
    stack = []
    try:
      for a in inputs:
          if type(a) is int:
              stack.append(a)
              continue
          op1, op2 = stack.pop(), stack.pop()
          if a == '+':
              stack.append(op2 + op1)
          elif a == '-':
              stack.append(op2 - op1)
          elif a == '*':
              stack.append(op2 * op1)
          elif a == '/':
              stack.append(op2 / op1)
    except ZeroDivisionError:
      return 0
    return stack.pop()


#for i in range(2, 7):
    #ndyck = len(all_exprs(i))
    #print "%2d: %7d expressions" % (i, ndyck)
