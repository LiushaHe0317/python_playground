import math


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or x > 2**31 or x <= -2**31:
            return False
        else:
            splitted_x = tuple((x//(10**i))%10 for i in range((math.floor(math.log10(x)) if x != 0 else 0), -1, -1))
            return splitted_x == splitted_x[::-1]


if __name__ == '__main__':
    s = Solution()

    s.isPalindrome(121)

    assert s.isPalindrome(121) == True
    assert s.isPalindrome(-121) == False
    assert s.isPalindrome(10) == False
    assert s.isPalindrome(-101) == False

    print(s.isPalindrome(22))
