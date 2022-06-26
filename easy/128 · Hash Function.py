class Solution:
    """
    @param key: A string you should hash
    @param hash_size: An integer
    @return: An integer
    """
    def hash_code(self, key: str, hash_size: int) -> int:
        # write your code here
        code = 0
        for ch in key:
            code = (code * 33 + ord(ch)) % hash_size
        
        return code
