# 前指针作主指针, recommended
class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def length_of_longest_substring_k_distinct(self, s: str, k: int) -> int:
        if not s or not k:
            return 0
        n = len(s)
        if k >= n:
            return n
        
        res = 0
        i = 0
        sub_len = 1
        hashmap = {s[0]: 1}
        
        j = 1
        while j < n:
            hashmap[s[j]] = hashmap.get(s[j], 0) + 1
            if len(hashmap) <= k:
                sub_len += 1
                j += 1
                continue
            
            hashmap.pop(s[j])
            res = max(res, sub_len)

            if hashmap[s[i]] > 1:
                hashmap[s[i]] -= 1
            else:
                del hashmap[s[i]]
            i += 1
            sub_len -= 1

        return max(res, sub_len)


# 后指针作主指针, not recommended
class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def length_of_longest_substring_k_distinct(self, s: str, k: int) -> int:
        if not s or not k:
            return 0
        n = len(s)
        if k >= n:
            return n
        
        res = 0
        j = 1
        sub_len = 1
        hashmap = {s[0]: 1}
        
        for i in range(n):
            while j < n:
                hashmap[s[j]] = hashmap.get(s[j], 0) + 1
                if len(hashmap) > k:
                    hashmap.pop(s[j])
                    res = max(res, sub_len)
                    break
                sub_len += 1
                j += 1
            if j == n:
                return max(res, sub_len)
            if hashmap[s[i]] > 1:
                hashmap[s[i]] -= 1
            else:
                del hashmap[s[i]]
            sub_len -= 1



from collections import OrderedDict
class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def length_of_longest_substring_k_distinct(self, s: str, k: int) -> int:
        if not s or not k:
            return 0
        n = len(s)
        if k >= n:
            return n

        i = 0
        hashmap = OrderedDict()
        res = 1

        for j in range(n):
            ch = s[j]
            if ch in hashmap:
                del hashmap[ch]
            hashmap[ch] = j

            if len(hashmap) > k:
                leftmost = hashmap.popitem(last=False)[1]
                i = leftmost + 1
            
            if (sub_len := j - i + 1) > res:
                res = sub_len
        
        return res
