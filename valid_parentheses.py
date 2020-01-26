#!/usr/local/bin/python3

###################
# write a function that returns true is brackets are balanced
# example:
# Input: ()
# Return: True
#
# Input: {}[]()
# Return: True
#
# Input: {[]()
# Return: False

def solution(A):
    p1_left = 0
    p1_right = 0
    p2_left = 0
    p2_right = 0
    p3_left = 0
    p3_right = 0

    if '(' in A:
        p1_left = A.count('(')
    if ')' in A:
        p1_right = A.count(')')

    if '[' in A:
        p2_left = A.count('[')
    if ']' in A:
        p2_right = A.count(']')

    if '{' in A:
        p3_left = A.count('{')
    if '}' in A:
        p3_right = A.count('}')

    if p1_left == p1_right and p2_left == p2_right and p3_left == p3_right:
        return True
    else:
        return False



if __name__ == "__main__":
    A = [')','(','{','}']
    A = ['{','}',']',')']
    print(solution(A))


