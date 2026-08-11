from collections import defaultdict


class Solution:

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_map = defaultdict(list)

        for s in strs:
            # Sort characters to create a unique key for all anagrams of this word
            key = "".join(sorted(s))
            anagram_map[key].append(s)

        return list(anagram_map.values())