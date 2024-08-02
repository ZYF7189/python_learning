# # # # x = int(input())
# # # # if x < 2:
# # # #     print(x)
# # # # else:
# # # #     left = 1
# # # #     right = x // 2
# # # #     while left <= right:
# # # #         mid = left + (right - left) // 2
# # # #         square = mid * mid
# # # #         if square == x:
# # # #             print(mid)
# # # #             break
# # # #         elif square > x:
# # # #             right = mid - 1
# # # #         else:
# # # #             left = mid + 1
# # # #     else:
# # # #         print(right)
# # # nums = [1,2,2,0,3,4,8,6,5,6]
# # # val = int(input())
# # # i, l = 0, len(nums)
# # # while i < l:
# # #     if nums[i] == val:  # 找到等于目标值的节点
# # #         for j in range(i + 1, l):  # 移除该元素，并将后面元素向前平移
# # #             nums[j - 1] = nums[j]
# # #         l -= 1
# # #         i -= 1
# # #     i += 1
# # # print(l,nums)
# # nums = [1,2,2,3,4,5,2,6,7]
# # fast = 0
# # slow = 0
# # while fast < len(nums):
# #     flag = 1
# #     for i in range(slow):
# #         if nums[fast] == nums[i]:
# #             flag = -1
# #             break
# #     if flag == 1:
# #         nums[slow] = nums[fast]
# #         slow += 1
# #     fast += 1
# # print(slow)
# nums = [1,0,0,0,3,4,5]
# # num = len(nums)
# # for i in range(num):
# #     if nums[i] == 0:
# #         j = i + 1
# #         while j < num:
# #             if nums[j] != 0:
# #                 t = nums[i]
# #                 nums[i] = nums[j]
# #                 nums[j] = t
# #                 break
# #             else:
# #                 j += 1
# n = len(nums)
# left = right = 0
# while right < n:
#     if nums[right] != 0:
#         nums[left], nums[right] = nums[right], nums[left]
#         left += 1
#     right += 1
# print(nums)
#
# while True:
#     f = float(input("f="))
#     v = float(input("v="))
#     out = float(37580 / f * v)
#     print("%.2f" % out)
#
#

import math


def calculate_octagon_footprint(r):
    footprint = []
    for i in range(8):
        angle = math.radians(i * 45)  # 将角度转换为弧度
        x = r * math.cos(angle)
        x = round(x, 3)
        y = r * math.sin(angle)
        y = round(y, 3)
        footprint.append([x, y])
    return footprint


r = 0.21  # 机器人半径
octagon_footprint = calculate_octagon_footprint(r)
print(octagon_footprint)
