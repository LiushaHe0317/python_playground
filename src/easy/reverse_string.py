from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        temp = s[::-1]
        s[:] = temp


if __name__ == '__main__':
    s = Solution()
    arr1 = ["h","e","l","l","o"]
    s.reverseString(arr1)
    assert arr1 == ["o","l","l","e","h"]

    arr2 = ["H","a","n","n","a","h"]
    s.reverseString(arr2)
    assert arr2 == ["h","a","n","n","a","H"]
