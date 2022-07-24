from collections import defaultdict

class Solution:
    """
    @param secret: An string
    @param guess: An string
    @return: An string
    """
    def get_hint(self, secret: str, guess: str) -> str:
        cnt = defaultdict(int)
        for v in guess:
            cnt[v] += 1

        bulls = cows = 0
        bulls_set = set()
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
                bulls_set.add(i)
                cnt[secret[i]] -= 1
        
        for i in range(len(secret)):
            if i in bulls_set:
                continue
            if secret[i] in cnt and cnt[secret[i]] > 0:
                cows += 1
                cnt[secret[i]] -= 1
        
        return str(bulls) + 'A' + str(cows) + 'B'


class Solution:
    """
    @param secret: An string
    @param guess: An string
    @return: An string
    """
    def get_hint(self, secret: str, guess: str) -> str:
        cnt = defaultdict(int)
        for v in guess:
            cnt[v] += 1

        bulls = cows = 0
        bulls_set = set()
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
                bulls_set.add(i)
                cnt[secret[i]] -= 1
                if cnt[secret[i]] == 0:
                    del cnt[secret[i]]
        
        for i in range(len(secret)):
            if i in bulls_set:
                continue
            if secret[i] in cnt:
                cows += 1
                cnt[secret[i]] -= 1
                if cnt[secret[i]] == 0:
                    del cnt[secret[i]]
        
        return str(bulls) + 'A' + str(cows) + 'B'






