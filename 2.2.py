# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# num = 0
# for i in range(1, 5):
#     for j in range(1, 5):
#         for k in range(1, 5):
#             if (i != j) & (i != k) & (j != k):
#                 print("%d%d%d" % (i, j, k))
#                 num = num + 1
# print("共有", num, "个")

# 👆第一种，👇第二种

from itertools import permutations

num = 0
for x in permutations([1, 2, 3, 4], 3):
    for y in x:
        print(y, end="")
    num = num + 1
    print()
print("共有", num, "个")
