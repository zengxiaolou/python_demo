"""
AUTHOR:         zeng_xiao_yu
GITHUB:         https://github.com/zengxiaolou
EMAIL:          zengevent@gmail.com
TIME:           2020/7/25-11:06
INSTRUCTIONS:   文件简介
"""


class SuitableSum(object):
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def suitable_sum(self):
        for i in range(0, len(self.nums)):
            if i < self.target:
                for j in range(i+1, len(self.nums)):
                    if self.nums[j] < self.target:
                        if self.nums[i] + self.nums[j] == self.target:
                            return i, j


