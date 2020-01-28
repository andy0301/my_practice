#!/usr/local/bin/python3

"""
K = 14
'Codility We test coders' - this should return 'Codility We' as J=11 more close to K=14

K = 100
'Why not' - string length less than K, so return whole string
"""

def solution(message, K):
    # if K >= len(message), then return message
    if K >= len(list(message)):
        return (message)
    else:
        # return (message[0:K])
        # trying split build in funtion to get each word from the string
        split_list = message.split() # split by space
        results = ""
        space_cnt = message.count(' ') # get space count from the message
        K = K - space_cnt + 2 # redefine K
        for str in split_list:
            if len(str) < K:
                K = K - len(str)
                results = results + str + " "
            else:
                break
        return(results.rstrip())
            
        


if __name__ == "__main__":
    message = "Codility We test coders"
    K = 14
    print(solution(message, K))

    message = "Why not"
    K = 100
    print(solution(message, K))

    message = "The quick brown fox jumps over the lazy dog"
    K = 39
    print(solution(message, K))