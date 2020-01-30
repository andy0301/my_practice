#!/usr/local/bin/python3

###################
# given sorted list A of integers, then return a sorted list of the squares of those integers
#

def solution(A):
    # calc squares for list A
    for i in range(len(A)):
        A[i] = A[i] * A[i]

    A.sort()
    return(A)

if __name__ == "__main__":
    A = [1,2,3,4,5,6]
    A = [6,8,9,11,22,44]
    print(solution(A))
        
