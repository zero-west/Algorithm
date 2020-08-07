from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s)//2):
            s[i], s[-(1+i)] = s[-(i+1)], s[i]

    def reverseString2(self, s: List[str]) -> None:
        s[:] = s[::-1]