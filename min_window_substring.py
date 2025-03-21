# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")
from collections import Counter
"""
    Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

    Input: s = “timetopractice”, t = “toc”
    Output: toprac
    
    
    Input: s = "a", t = "aa"
    Output: ""

    
    Input: s = “zoomlazapzo”, t = “oza”
    Output: apzo

    Input: s = "ADOBECODEBANC", t = "ABC"
    Output: "BANC"
    
    contrains:
    1 <= m, n <= 10^5
    t should be less than or equal to s


"""


def min_window(s, t):
    
    if not s or not t:
        return ""

    if len(t)> len(s):
        return ""
    
    t_freq = Counter(t)
    left = 0
    right = 0
    
    window_freq = Counter()
    formed = 0
    
    min_length = float("inf")
    min_window = [0,0]
    
    while right < len(s):
        
        window_freq[s[right]] += 1
        
        if s[right] in t_freq and window_freq[s[right]]== t_freq[s[right]]:
            formed += 1
        
        while left <= right and formed == len(t_freq):
            window_size = right - left + 1
            if window_size < min_length:
                min_length = window_size
                min_window = [left, right]
            
            window_freq[s[left]] -= 1
            if s[left] in t_freq and window_freq[s[left]] < t_freq[s[left]]:
                formed -= 1
            
            left+= 1
            
        right+=1
    
    left_window = min_window[0]
    right_window = min_window[1]
    
    return s[left_window: right_window+1]
            

s = "ADOBECODEBANC"
t = "ABC"

print(min_window(s,t))

s = "zoomlazapzo"
t = "oza"

print(min_window(s,t))
s = "a" 
t = "aa"
print(min_window(s,t))

s = "timetopractice"
t = "toc"
print(min_window(s,t))

s = "BAC"
t = "ABC"

print(min_window(s,t))
