#!/usr/local/bin/python3

"""
A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:

S is empty;
S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.
For example, the string "{[()()]}" is properly nested but "([)()]" is not.

Write a function:

def solution(S)

that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..200,000];
string S consists only of the following characters: "(", "{", "[", "]", "}" and/or ")".
"""

def solution(A): # this is not a correct one,because it didn't consider brackets orders
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

def solution_correct(S):
    brackets = list(S)

    stack = [] # init a stack
    for bracket in brackets:
        if bracket == '{' or bracket == '(' or bracket == '[': #  if find open bracket then stack.push()
            stack.append(bracket)
         # if find close bracket and stack is empty, then return 0; break loop
         # if find close bracket and stack is not empty, then stack.pop()
        if bracket == '}' and not stack:
            return 0
            break
        elif bracket == '}' and stack[-1] == '{':
            stack.pop()    
        if bracket == ')' and not stack:
            return 0
            break
        elif bracket == ')' and stack[-1] == '(':
            stack.pop()
        if  bracket == ']' and not stack:
            return 0
            break
        elif bracket == ']' and stack[-1] == '[':
            stack.pop()

    if not stack:
        return 1
    else:
        return 0

    

if __name__ == "__main__":
    A = [')','(','{','}']
    A = ['{','}',']',')']
    A = ["(","[",")","]"]
    print(solution(A))

    S = "{[()()]}"
    print(solution_correct(S))

    S = "([)()]"
    print(solution_correct(S))

    S = ")("
    print(solution_correct(S))

    S = "{[()()][]][}"
    print(solution_correct(S))




