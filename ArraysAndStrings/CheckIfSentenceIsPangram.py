#1832. Check if the Sentence is Pangram

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        set_ = set()
        for c in sentence:
            set_.add(c)
        if len(set_) != 26:
            return False
        return True