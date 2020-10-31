from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        arr = list(set(nums))
        if len(arr) < 3:
            return max(arr)
        else:
            arr.remove(max(arr))
            arr.remove(max(arr))
            return max(arr)


if __name__ == '__main__':
    s = Solution()
    assert s.thirdMax([3, 2, 1]) == 1
    assert s.thirdMax([1, 2]) == 2
    assert s.thirdMax([2, 2, 3, 1]) == 1
    assert s.thirdMax([1, 2, 2, 5, 3, 5]) == 2
