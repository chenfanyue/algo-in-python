class Solution:
    """
    @param s: a string
    @param k: a integer
    @return: return a integer
    """
    def character_replacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        
        res = 0
        n = len(s)
        left = right = 0
        cnt = {}
        cnt_max = 0

        while right < n:
            cnt[s[right]] = cnt.get(s[right], 0) + 1
            if cnt[s[right]] > cnt_max:
                cnt_max = cnt[s[right]]
            
            if right - left + 1 - cnt_max > k:
                cnt[s[right]] -= 1
                res = max(res, right - left)
                
                cnt[s[left]] -= 1
                cnt_max = max(cnt.values())
                left += 1
                continue

            right += 1
        
        return max(res, right - left)


class Solution:
    """
    @param s: a string
    @param k: a integer
    @return: return a integer
    """
    def character_replacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        
        n = len(s)
        left = right = 0
        cnt = {}
        cnt_max = 0

        while right < n:
            cnt[s[right]] = cnt.get(s[right], 0) + 1
            if cnt[s[right]] > cnt_max:
                cnt_max = cnt[s[right]]
            
            if right - left + 1 - cnt_max > k:
                cnt[s[left]] -= 1
                cnt_max = max(cnt.values())
                left += 1
            
            right += 1
        
        return right - left

