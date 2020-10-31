class Solution:
    def mySqrt(self, x: int) -> int:
        return int(x**0.5)


if __name__ == '__main__':
    s = Solution()
    assert s.mySqrt(4) == 2
    assert s.mySqrt(8) == 2
