#8/16/2026
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        theword = ""
        w1=len(word1)
        w2=len(word2)
        

        for i,j in zip(word1,word2):
        
                theword +=  i
                theword += j
            
        if w1 < w2:
            theword += word2[w1:]
        elif w1 > w2:
            theword += word1[w2:]

        
        return theword



if __name__ == "__main__":

    solution = Solution()

    word1 = "abc"
    word2 = "123"

    result  = solution.mergeAlternately(word1,word2)

    print(result)

    
