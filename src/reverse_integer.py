class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        else:
            res = int(str(x)[::-1].replace("-", ""))
            if res >= 2**31:
                return 0
            else:
                if x < 0:
                    return -res
                else:
                    return res


if __name__ == '__main__':
    x = 120
    s = Solution()
    assert s.reverse(x) == 21
    assert s.reverse(123) == 321
    assert s.reverse(-123) == -321
    assert s.reverse(0) == 0