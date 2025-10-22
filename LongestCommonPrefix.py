class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        prefix = strs[0]
        for kelime in strs[1:]:
            while not kelime.startswith(prefix):
                prefix = prefix[:-1] 
                if prefix == "":
                    return ""
        return prefix

