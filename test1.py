"""Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).
Input: s = "aa", p = "a"
Output: false """


"""
Input: s = "aa", p = "*"
Output: true

Input: s = "aa", p = "*"
Output: true


Input: s = "cb", p = "?a"
Output: false

s = "abcaabee", p = "ab*be?"
True
"""

def is_possible(s, p, n, m):

    if m==0:
        return n==0
    
    if n==0:
        for i in range(m):
            if p[i] != "*":
                return False
        return True
    
    if s[n-1]==p[m-1] or p[m-1]=="?":
        return is_possible(s, p, n-1, m-1)
    
    if p[m-1]=="*":
        return is_possible(s,p,n,m-1) or is_possible(s,p,n-1,m)

    return False

s = "abcaa"
p = "ab*"

n = len(s)
m = len(p)

print(is_possible(s, p, n, m))

s = "cb"
p = "?a"
n = len(s)
m = len(p)

print(is_possible(s, p, n, m))

s = "aa"
p = "*"
n = len(s)
m = len(p)

print(is_possible(s, p, n, m))