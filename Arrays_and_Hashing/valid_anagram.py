# https://leetcode.com/problems/valid-anagram

def isAnagram(s, t):
    if len(s) != len(t):
        return False
    
    char_count = {}

    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    for char in t:
        if char not in char_count or char_count[char] == 0:
            return False
        char_count[char] -= 1

    return True

# Example usage:
s = "anagram"
t = "nagaram"

result = isAnagram(s, t)
print(result)  # Output: True

# Time Complexity: O(N), where N is the length of the strings. We iterate through both strings once, and each lookup and update in the hash map takes O(1) time on average.
# Space Complexity: O(N), where N is the length of the strings. We store the character counts in a hash map, which takes up space proportional to the number of unique characters in the strings.