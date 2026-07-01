# leetcode 49 : https://leetcode.com/problems/group-anagrams/

from collections import defaultdict

def groupAnagrams(strs):
    anagram_map = defaultdict(list)

    for s in strs:
        # Sort the string to use as a key
        sorted_str = tuple(sorted(s))
        anagram_map[sorted_str].append(s)

    return list(anagram_map.values())

# Example usage:
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = groupAnagrams(strs)
print(result)  # Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

# Time Complexity: O(N * K log K), where N is the number of strings in the input list and K is the maximum length of a string. Sorting each string takes O(K log K) time, and we do this for each of the N strings.
# Space Complexity: O(N * K), where N is the number of strings in the input list and K is the maximum length of a string. We store all the strings in the output list, which takes up space proportional to the total number of characters in all the strings.