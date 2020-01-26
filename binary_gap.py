#!/usr/local/bin/python3

###################
# A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

# For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.

# Write a function:

# def solution(N)

# that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

# For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..2,147,483,647].

def solution(N):
    bin_N = str(bin(N)[2:])
    n_list = (list(bin_N))
    n_list_1_count = n_list.count('1')
     # if '1' count <= 1, then there is no binary gap
    if n_list_1_count <= 1:
        return(0)
    else:
        gap_list=[]
        for i in range(len(n_list)):
            if n_list[i] == '1':
                gap_list.append(i)

        gap_num = gap_list[1] - gap_list[0] - 1
        for j in range(len(gap_list)):
            if j == len(gap_list) - 1:
                break
            else:
                if gap_list[j+1] - gap_list[j] -1 >= gap_num:
                    gap_num =  gap_list[j+1] - gap_list[j] -1
        return(gap_num)

if __name__ == "__main__":
    N = 32
    print(solution(N))

    N = 1024
    print(solution(N))

    N = 28889910
    print(solution(N))

    N = 1041
    print(solution(N))

    N = 529
    print(solution(N))

    N = 9
    print(solution(N))

    N = 805306369
    print(solution(N))

    N = 1610612737
    print(solution(N))