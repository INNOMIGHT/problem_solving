"""
Write a function that reverses a string.
The input string is given as an array of characters char[].
Do not allocate extra space for another array,
you must do this by modifying the input array in-place with O(1) extra memory.
"""


class Solution:

    def reverse_string(self, s):
        for i in range(len(s)//2):
            tmp = s[i]
            s[i] = s[-1 - i]
            s[-1 - i] = tmp
        return s

        # Another Solution With 2 Pointers -
        # p, q = 0, len(s)-1
        # while p<q:
        #     s[p],s[q] = s[q],s[p]
        #     p+=1
        #     q-=1
