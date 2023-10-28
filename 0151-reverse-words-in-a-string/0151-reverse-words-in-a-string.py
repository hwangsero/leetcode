class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()  # 공백을 기준으로 단어를 분리
        reversed_words = words[::-1]  # 단어의 순서를 뒤집음
        return ' '.join(reversed_words) 