def lengthOfLongestSubstring(s):
    sol = 0
    en_uzun = 0
    karakterler = set()

    for sag in range(len(s)):
        while s[sag] in karakterler:
            karakterler.remove(s[sol])
            sol += 1

        karakterler.add(s[sag])
        en_uzun = max(en_uzun, sag - sol + 1)

    return en_uzun