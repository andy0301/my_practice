#!/usr/local/bin/python3

"""
Permutations:

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

def solution(A):
    # A has N integer, then should return N! = N * (N-1) * (N-2) * (N-3) ... * 3 * 2 * 1
    n = 1
    for i in range(1,len(A)+1):
        n = n * i

    results = []
    for j in range(n):
        A = A[-1:] + A[:-1]
        results.append(A)
    return(results)

if __name__ == "__main__":
    A = [1,2,3]
    print(solution(A))

    A = [3,4,5,6]
    print(solution(A))