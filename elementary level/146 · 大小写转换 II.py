class Solution:
    """
    @param letters: A string
    @return: A string
    """
    def lowercase_to_uppercase2(self, letters: str) -> str:
        # write your code here
        arr = list(letters)
        a, z = ord('a'), ord('z')
        gap = ord('a') - ord('A')
        for i in range(len(arr)):
            if a <= ord(arr[i]) <= z:
                arr[i] = chr(ord(arr[i]) - gap)
        return ''.join(arr)
