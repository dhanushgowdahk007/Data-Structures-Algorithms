# https://leetcode.com/problems/longest-substring-without-repeating-characters/

def lengthOfLongestSubstring(s):
    charSet = set()
    left = 0
    maxLength = 0

    for right in range(len(s)):
        while s[right] in charSet:
            charSet.remove(s[left])
            left += 1
        
        charSet.add(s[right])
        maxLength = max(maxLength, right - left + 1)
    
    return maxLength

# Example usage:
s = "abcabcbb"
result = lengthOfLongestSubstring(s)
print(result)  # Output: 3

# Time Complexity: O(N), where N is the length of the input string. We iterate through the string once.
# Space Complexity: O(min(N, M)), where M is the size of the character set. In the worst case, we may need to store all unique characters in the substring.