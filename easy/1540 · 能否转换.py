class Solution:
    """
    @param s: string S
    @param t: string T
    @return: whether S can convert to T
    """
    def can_convert(self, s: str, t: str) -> bool:
        # Write your code here
        if not s and t:
            return False
        if len(t) == 0 and len(s) >= 0:
            return True

        sp, tp = 0, 0
        while True:
            while s[sp] != t[tp]:
                if sp == len(s) - 1:
                    return False
                sp += 1

            if tp == len(t) - 1:
                return True
            tp += 1

            if sp == len(s) - 1:
                return False
            sp += 1


class Solution:
    """
    @param s: string S
    @param t: string T
    @return: whether S can convert to T
    """
    def can_convert(self, s: str, t: str) -> bool:
        # Write your code here
        if not s and t:
            return False
        if len(t) == 0 and len(s) >= 0:
            return True

        tp = 0
        for sp in range(len(s)):
            if s[sp] == t[tp]:
                tp += 1
                if tp == len(t):
                    return True
        return False


class Solution:
    """
    @param s: string S
    @param t: string T
    @return: whether S can convert to T
    """
    def can_convert(self, s: str, t: str) -> bool:
        # Write your code here
        if not s and t:
            return False
        if len(t) == 0 and len(s) >= 0:
            return True

        tp = 0
        for ch in iter(s):
            if ch == t[tp]:
                tp += 1
                if tp == len(t):
                    return True
        return False


class Solution:
    """
    @param s: string S
    @param t: string T
    @return: whether S can convert to T
    """
    def can_convert(self, s: str, t: str) -> bool:
        # Write your code here
        if not s and t:
            return False
        if len(t) == 0 and len(s) >= 0:
            return True

        sp, tp = 0, 0
        while sp < len(s) and tp < len(t):
            if s[sp] == t[tp]:
                sp += 1
                tp += 1
            else:
                sp += 1
        return tp == len(t)
