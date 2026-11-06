class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.split()
        answer=[]
        for item in words:
            answer.append(item[::-1])
        
        return " ".join(answer)
