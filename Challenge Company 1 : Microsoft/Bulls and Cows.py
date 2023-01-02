https://leetcode.com/problems/bulls-and-cows/
  
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bag = collections.Counter(secret)
        bulls, cows = 0, 0
 
        # bulls pass
        for a, b in zip(secret, guess):
            if a == b:
                bulls += 1
                bag[b] -= 1

        # cows pass
        for a, b in zip(secret, guess):
            if a!= b and bag[b] > 0:
                cows += 1
                bag[b] -= 1

        return f'{bulls}A{cows}B'
        
