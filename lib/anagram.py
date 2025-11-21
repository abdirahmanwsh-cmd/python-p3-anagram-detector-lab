# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word
        self._key = ''.join(sorted(word.lower()))

    def match(self, candidates):
        matches = []
        for cand in candidates:
            if cand.lower() == self.word.lower():
                continue
            if ''.join(sorted(cand.lower())) == self._key:
                matches.append(cand)
        return matches

