"""
Making fuel for the LAMBCHOP"s reactor core is a tricky process because of the exotic matter involved. It starts as raw ore
, then during processing, begins randomly changing between forms, eventually reaching a stable form.
There may be multiple stable forms that a sample could ultimately reach, not all of which are useful as fuel.

Commander Lambda has tasked you to help the scientists increase fuel creation efficiency by predicting
the end state of a given ore sample. You have carefully studied the different structures that the ore can take
and which transitions it undergoes. It appears that, while random, the probability of each structure transforming is fixed.
That is, each time the ore is in 1 state, it has the same probabilities of entering the next state (which might be the same state).
You have recorded the observed transitions in a matrix. The others in the lab have hypothesized more exotic
forms that the ore can become, but you haven't seen all of them.

Write a function solution(m) that takes an array of array of nonnegative ints representing how many times that
state has gone to the next state and return an array of ints for each terminal state giving the exact probabilities of
each terminal state, represented as the numerator for each state, then the denominator for all of them at the end and in simplest form.
The matrix is at most 10 by 10. It is guaranteed that no matter which state the ore is in,
there is a path from that state to a terminal state. That is, the processing will always eventually end in a stable state.
The ore starts in state 0. The denominator will fit within a signed 32-bit integer during the calculation,
as long as the fraction is simplified regularly.

For example, consider the matrix m:
[
  [0,1,0,0,0,1],  # s0, the initial state, goes to s1 and s5 with equal probability
  [4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but with different probabilities
  [0,0,0,0,0,0],  # s2 is terminal, and unreachable (never observed in practice)
  [0,0,0,0,0,0],  # s3 is terminal
  [0,0,0,0,0,0],  # s4 is terminal
  [0,0,0,0,0,0],  # s5 is terminal
]
So, we can consider different paths to terminal states, such as:
s0 -> s1 -> s3
s0 -> s1 -> s0 -> s1 -> s0 -> s1 -> s4
s0 -> s1 -> s0 -> s5
Tracing the probabilities of each, we find that
s2 has probability 0
s3 has probability 3/14
s4 has probability 1/7
s5 has probability 9/14
So, putting that together, and making a common denominator, gives an answer in the form of
[s2.numerator, s3.numerator, s4.numerator, s5.numerator, denominator] which is
[0, 3, 2, 9, 14].

"""
import math
from fractions import Fraction

def solution(m):
    size = len(m)
    for i in range(size):
        total = sum(m[i])
        if total == 0:
            m[i][i] = 1
        else:
            for j in range(size):
                m[i][j] = m[i][j] / total
    q, r = [], []
    for i in range(size):
        if all([row[i] == 0 for row in m]):
            r.append(i)
        else:
            q.append(i)
    if not q:
        return [1] + [0] * (size - 1) + [1]
    qt = [m[i][j] for i in q for j in q]
    rt = [m[i][j] for i in q for j in r]
    identity = [1 if i == j else 0 for i in range(len(q))]
    tmp = substract_matrix(identity, qt)
    tmp = invert_matrix(tmp)
    res = multiply_matrices(tmp, rt)
    res = [res[i][0] for i in range(len(res))]
    res += [1 - sum(res)]
    res = [int(frac) for frac in to_simplest_form(res)]
    return res


def substract_matrix(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def invert_matrix(a):
    n = len(a)
    A = [[a[i][j] for j in range(n)] + [1 if j == i else 0 for j in range(n)] for i in range(n)]
    for i in range(n):
        max_row = i
        for j in range(i+1, n):
            if abs(A[j][i]) > abs(A[max_row][i]):
                max_row = j
        A[i], A[max_row] = A[max_row], A[i]
        scale = A[i][i]
        for j in range(i, 2*n):
            A[i][j] /= scale
        for j in range(n):
            if j != i:
                scale = A[j][i]
                for k in range(i, 2*n):
                    A[j][k] -= scale * A[i][k]
    return [[A[i][j+n] for j in range(n)] for i in range(n)]


def multiply_matrices(a, b):
    return [[sum([a[i][k] * b[k][j] for k in range(len(a[0]))]) for j in range(len(b[0]))] for i in range(len(a))]


def to_simplest_form(fractions):
    from fractions import Fraction
    lcm = 1
    for frac in fractions:
        lcm *= frac.denominator // gcd(lcm, frac.denominator)
    return [Fraction(lcm // frac.denominator * frac.numerator, lcm) for frac in fractions]


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a






s = solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]])
print(s)