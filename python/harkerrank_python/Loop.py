#!/usr/local/bin/python3

"""
Task
Read an integer . For all non-negative integers , print . See the sample for details.

Input Format

The first and only line contains the integer, .

Constraints


Output Format

Print  lines, one corresponding to each .
"""

if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        print(i ** 2)