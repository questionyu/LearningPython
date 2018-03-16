# 输出2-100之间的素数
for i in range(2, 101):
    for j in range(2, i):
        if not (i % j):         # 如果 i 整除 j（i 不是素数）
            break                   # 跳出循环
    else:
        print(i, "是素数")
