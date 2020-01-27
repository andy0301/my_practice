#!/usr/local/bin/python3

"""
An array A consisting of N integers is given. A triplet (P, Q, R) is triangular if 0 ≤ P < Q < R < N and:

A[P] + A[Q] > A[R],
A[Q] + A[R] > A[P],
A[R] + A[P] > A[Q].
For example, consider array A such that:

  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20
Triplet (0, 2, 4) is triangular.

Write a function:

def solution(A)

that, given an array A consisting of N integers, returns 1 if there exists a triangular triplet for this array and returns 0 otherwise.

For example, given array A such that:

  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20
the function should return 1, as explained above. Given array A such that:

  A[0] = 10    A[1] = 50    A[2] = 5
  A[3] = 1
the function should return 0.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].
"""

def is_triangle(P,Q,R):
    if P + Q > R and Q + R > P and R +  P > Q:
        return 1
    else:
        return 0

def solution(A):
    # sort A
    A.sort()

    for i in range(len(A)-2):
        if is_triangle(A[i],A[i+1],A[i+2]) == 1:
            return 1
            break

    return 0



if __name__ == "__main__":
    A = [10,2,5,1,8,20]
    print(solution(A))

    A = [10,50,5,1]
    print(solution(A))
    