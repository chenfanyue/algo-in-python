class Solution:
    """
    @param s: a string
    @param k: an integer
    @return: the number of substrings there are that contain at least k distinct characters
    """
    def k_distinct_characters(self, s: str, k: int) -> int:
        record = [0] * 26
        cnt = 0
        res = 0
        n = len(s)

        j = 0
        for i in range(n):
            offset = ord(s[i]) - ord('a')
            record[offset] += 1
            if record[offset] == 1:
                cnt += 1
            if cnt == k:
                res += n - i
            
            while cnt == k:
                offset = ord(s[j]) - ord('a')
                record[offset] -= 1
                if record[offset] == 0:
                    cnt -= 1
                j += 1
                if cnt == k:
                    res += n - i

        return res
