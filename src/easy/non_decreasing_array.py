from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        def isChangeable(left_arr, right_arr):
            left_possible = True
            right_possible = True

            # if changeable from left end
            if len(left_arr) > 1:
                if left_arr[-2] > right_arr[0]:
                    left_possible = False

            # if changeable from right end
            if len(right_arr) > 1:
                if left_arr[-1] > right_arr[1]:
                    right_possible = False

            if left_possible or right_possible:
                return True
            else:
                return False

        # detect the last two integers
        if len(nums) in {1, 2}:
            return True
        else:
            count = 0
            for idx, _ in enumerate(nums[:-1]):
                left = nums[idx]
                right = nums[idx + 1]
                if left > right:
                    count += 1
                    if not isChangeable(nums[:idx + 1], nums[idx + 1:]):
                        return False
            else:
                return False if count > 1 else True


if __name__ == '__main__':
    s = Solution()
    assert s.checkPossibility([4, 2, 3]) == True
    assert s.checkPossibility([4, 2, 1]) == False
    assert s.checkPossibility([3, 4, 2, 3]) == False
    assert s.checkPossibility([-1, 4, 2, 3]) == True
    assert s.checkPossibility([1, 3, 2]) == True
    assert s.checkPossibility([2, 3, 3, 2, 2]) == False
    assert s.checkPossibility([5, 7, 1, 8]) == True
    assert s.checkPossibility([1,5,4,6,7,10,8,9]) == False
    assert s.checkPossibility([12,8,15,11,13,14]) == False
    assert s.checkPossibility([1,2,3,5,4]) == True