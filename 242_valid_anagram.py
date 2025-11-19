class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count_1 = {}
        char_count_2 = {}
        for char1 in s:
            current_count_1 = char_count_1.get(char1,0)
            char_count_1[char1] = current_count_1 + 1
        for char2 in t:
            current_count_2 = char_count_2.get(char2,0)
            char_count_2[char2] = current_count_2 + 1
        return char_count_1 == char_count_2
    
#I can use standard library in leetcode, like sort, counter 