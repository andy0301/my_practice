#!/usr/local/bin/python3

"""
Given an integer n, return any array containing n unique integers such that they add up to 0.
eg:
N = 2: [-1,1]
N = 3: [-1,1,0]
N = 4: [-1,1,-2,2]
N = 5: [-1,1,-2,2,0]

if N is even then need add 0
if N is odd then no need add 0
"""
def is_even(N):
    if N % 2 == 0:
        return 1
    else:
        return 0

def solution(N):
    positive = []
    negative = []
    if is_even(N):
        # gen array no need add 0
        # array will be like [-x,x]
        X = N // 2
        for i in range(1,X+1):
            print(i)
            positive.append(i)
        negative = [-x for x in positive]
        return(positive + negative)
    else:
        X = N // 2
        for i in range(1,X+1):
            positive.append(i)
        negative = [-x for x in positive]
        negative.append(0) # N = odd need add '0'
        return(positive + negative)




if __name__ == "__main__":
    N = 3
    print(solution(N))

    N = 4
    print(solution(N))

    N = 5
    print(solution(N))

    N = 16
    print(solution(N))
    print(sum(solution(N)))

    N = 29
    print(solution(N))
    print(sum(solution(N)))
