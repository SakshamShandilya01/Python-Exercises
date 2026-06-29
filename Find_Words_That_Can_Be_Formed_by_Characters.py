class Solution:
    def countCharacters(self, words, chars):

        total = 0

        charsCount = {}

        for ch in chars:
            charsCount[ch] = charsCount.get(ch, 0) + 1

        for word in words:

            wordCount = {}

            for ch in word:
                wordCount[ch] = wordCount.get(ch, 0) + 1

            if wordCount == {}:
                continue

            possible = True

            for ch in wordCount:
                if ch not in charsCount or wordCount[ch] > charsCount[ch]:
                    possible = False
                    break

            if possible:
                total += len(word)

        return total