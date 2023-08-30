def first_last6(nums):
    index = 1
    for c in nums:
        if c == 6 and index == 1:
            return True
        if c == 6 and index == len(nums):
            return True
        index += 1
    return False

#########################################

def same_first_last(nums):
    if len(nums) > 1:
        if nums[0] == nums[-1]:
            return True
        return False
    if len(nums) == 1:
        return True
    return False

#########################################

def make_pi():
    return [3,1,4]

#########################################

def common_end(a, b):
    if len(a) > 0 and len(b) > 0:
        if a[0] == b[0] or a[-1] == b[-1]:
            return True
    return False

#########################################

def sum3(nums):
    return nums[0] + nums[1] + nums[2]

#########################################

def rotate_left3(nums):
    return [nums[1], nums[2], nums[0]]

#########################################

def reverse3(nums):
    return nums[::-1]

#########################################

def max_end3(nums):
    if nums[0] > nums[-1]:
        return [nums[0], nums[0], nums[0]]
    return [nums[-1], nums[-1], nums[-1]]

#########################################

def sum2(nums):
    if len(nums) >= 2:
        return nums[0] + nums[1]
    if len(nums) == 1:
        return nums[0]
    return 0

#########################################

def middle_way(a, b):
    return [a[1], b[1]]

#########################################

def make_ends(nums):
    if len(nums) >= 1:
        return [nums[0],nums[-1]]
    return nums

#########################################

def has23(nums):
    if 2 in nums or 3 in nums:
        return True
    return False