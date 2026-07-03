# https://leetcode.com/problems/longest-repeating-character-replacement/

def characterReplacement(s, k): 
    
    count = {}
    max_count = 0
    left = 0
    max_length = 0

    for right in range(len(s)):
        count[s[right]] = count.get(s[right], 0) + 1
        max_count = max(max_count, count[s[right]])

        while (right - left + 1) - max_count > k:
            count[s[left]] -= 1
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length

# Example usage:
s = "AABABBA"
k = 1
result = characterReplacement(s, k)
print(result)  # Output: 4

# Time Complexity: O(N), where N is the length of the input string. We iterate through the string once.
# Space Complexity: O(1), as we are using a fixed-size dictionary to store character counts, which is limited to the number of unique characters in the input string (at most 26 for uppercase English letters).