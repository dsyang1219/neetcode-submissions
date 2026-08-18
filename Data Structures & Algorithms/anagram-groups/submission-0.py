class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {}

        for word in strs:
            anagram = "".join(sorted(word))
            if anagram in groups.keys():
                anagram_list = groups[anagram]
                anagram_list.append(word)
                
            else:
               anagram_list = [] 
               anagram_list.append(word)
            
            groups[anagram] = anagram_list

        return list(groups.values())