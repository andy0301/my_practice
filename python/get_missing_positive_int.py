#!/usr/local/bin/python3

###################
# that given an array A of N integers, returns the smallest positive integer (greater than 0)
# that does not occur in A.
# example:
#   A = [1,3,6,4,1,2] return 5
#   A = [-1,-3] return 1
#   A = [1,2,3] return 4
# Write an efficient algorithm for the following assumptions:
# N is an integer within the range [1..100,000]
# each element of array A is an integer within [-1,000,000..1,000,000]

import sys

def solution(A):
    alen = len(A)
     # gen a sorted list from 1 to alen
    sorted_list = []
    for i in range(1,alen+2):
        sorted_list.append(i)

    for missing_int in sorted_list:
        if missing_int not in list(A):
            return(missing_int)


if __name__ == "__main__":
    #A = [1,2,3]
    A = [1,3,6,4,1,2]
    for i in range(-2000,100000):
        A.append(i)
    A.remove(888)
    #A.remove(20)
    print(solution(A))
        