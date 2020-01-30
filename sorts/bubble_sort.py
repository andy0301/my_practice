#!/usr/local/bin/python3

"""
Bubble sort.

if A[i] > A[i+1], then A[i] = A[i+1]

[2,1,4,5,6,8,11,9,17,13,29]
"""

import random

def test(A, B):
    if A == B:
        return "Sorted"
    else:
        return "Unsorted"

def solution(A):
    for i in range(len(A)):
        for j in range(i+1,len(A) - i):
            if A[i] > A[j]:
                temp = A[i]
                A[i] = A[j]
                A[j] = temp
        
    return(A)
 

if __name__ == "__main__":
    A = [2,1,4,5,6,8,11,9,17,13,29]
    print(solution(A))

    A = random.sample(range(1,2000),100)
    B = solution(A)
    A.sort()
    print(test(A, B))