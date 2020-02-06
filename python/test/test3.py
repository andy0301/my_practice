#!/usr/local/bin/python3

"""
stack:
"13 DUP 4 POP 5 DUP + DUP + -" # Return 7
"5 6 + - " # return -1
"3 DUP - -" # return -1
"""

def solution(S):
    stack = []
    strings = S.split()

    if not int(strings[0]): # if the first is not a integer then return -1 and exit.
        return(-1)
    else:
        stack.append(int(strings[0]))


    for i in range(1,len(strings)):
        #print(strings[i])
        if strings[i] == 'DUP':
            a = stack.pop()
            try:
                if int(a):
                    stack.append(a)
                    stack.append(a)
            except:
                continue
            #print(stack)
        elif strings[i] == 'POP':
            stack.pop()
        elif strings[i] == '+':
            if len(stack) <=1:
                return(-1)
                break
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(a + b)
                #print(stack)
        elif strings[i] == '-':
            if len(stack) <=1:
                return(-1)
                break
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(a - b)
        else:
            stack.append(strings[i])     

    return(stack.pop())      

    


if __name__ == "__main__":
    S = "13 DUP 4 POP 5 DUP + DUP + -"
    print(solution(S))

    S = "5 6 + - "
    print(solution(S))

    S = "3 DUP - -"
    print(solution(S))