#Write a method/function that takes a string and swaps characters, e.g.:
#Given the input of "ABCDEF" it should return "BADCFE"

def swapFun(S,i,j):
    if not S:
        return S

    S_arr = list(S)
    S_arr[i], S_arr[j] = S_arr[j], S_arr[i]
    return ''.join(S_arr)


if __name__ == "__main__":
    S="ABCDEF"
    s_arr=list(S)
    for i in range(len(s_arr)):
        if i % 2 != 0:
            S = swapFun(S,i-1,i)
        s_arr=list(S)
    print(S)

#requests.get('http://10.0.0.1', timeout=10)
#what happen for this?
