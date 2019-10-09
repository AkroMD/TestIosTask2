import random

def quicksort(nums):
   if len(nums) <= 1:
       return nums
   else:
       q = random.choice(nums)
   l_nums = [n for n in nums if n < q]
 
   e_nums = [q] * nums.count(q)
   b_nums = [n for n in nums if n > q]
   return quicksort(l_nums) + e_nums + quicksort(b_nums)


def Myquicksort(nums):
    if len(nums) <= 1:
        return nums
    else:
        ref_point = random.choice(nums)
    first_nums = [n for n in nums if n < ref_point] 
    middle_nums = [ref_point] * nums.count(ref_point)
    second_nums = [n for n in nums if n > ref_point]
    return Myquicksort(first_nums) + middle_nums + Myquicksort(second_nums)


def Split3(nums):
    nums_3 = []
    nums_else = []
    for i in nums:
        if i % 3 == 0:
            nums_3.append(i)
        else: 
            nums_else.append(i)
    return Myquicksort(nums_3) + Myquicksort(nums_else)

N = int(input())
nums = [int(s) for s in input().split()]
nums = Split3(nums)
print(*nums, sep=" ")
