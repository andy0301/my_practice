#!/usr/local/bin/python3

"""
Write a function

def solution(A)

that, given an array A consisting of N integers, returns the number of distinct values in array A.

For example, given array A consisting of six elements such that:

 A[0] = 2    A[1] = 1    A[2] = 1
 A[3] = 2    A[4] = 3    A[5] = 1
the function should return 3, because there are 3 distinct values appearing in array A, namely 1, 2 and 3.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
"""

def solution(A):
    A_dict = {}
     # loop array A then put the value to A_dict[key]
    for a in A:
        try:
            A_dict[a] = True
        except:
            continue

     # return A_dict.keys() count, this should be the number for distinct values from A
    return(len(A_dict.keys()))

def solution_using_set(A):
    A_set = set(A)
    return(len(A_set))

if __name__ == "__main__":
    A = [2,1,1,2,3,1]
    print(solution(A))
    print(solution_using_set(A))

    A = [2,1,1,2,3,1,4,5,6,4,5,6]
    print(solution(A))
    print(solution_using_set(A))