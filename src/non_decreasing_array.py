from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        # detect the last two integers
        if len(nums) in {1, 2}:
            return True
        else:
            count = 0
            for idx, _ in enumerate(nums[1:-1]):
                if ((nums[idx] <= nums[idx + 1] > nums[idx + 2]) and (nums[idx] > nums[idx + 2])) or \
                        nums[idx] > nums[idx + 1] > nums[idx + 2]:
                        count += 1
            else:
                return False if count >= 1 else True


if __name__ == '__main__':
    s = Solution()
    assert s.checkPossibility([4, 2, 3]) == True
    assert s.checkPossibility([4, 2, 1]) == False
    assert s.checkPossibility([3, 4, 2, 3]) == False
    assert s.checkPossibility([-1, 4, 2, 3]) == True
    assert s.checkPossibility([1, 3, 2]) == True
    assert s.checkPossibility([2, 3, 3, 2, 2]) == False
    assert s.checkPossibility([5, 7, 1, 8]) == True
