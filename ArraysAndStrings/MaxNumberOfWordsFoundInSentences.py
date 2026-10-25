#2114. Maximum Number of Words Found in Sentences

class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        max_words = 0
        for sentence in sentences:
            count = 1
            for char in sentence:
                if char == ' ':
                    count += 1
            max_words = max(count, max_words)
        
        return max_words