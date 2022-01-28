import random

LOWER_LIMIT = 60
UPPER_LIMIT = 90

print("\n### while ###")
# while 循环
data = random.randrange(0, 100, 1)
while data >= LOWER_LIMIT:
    # 到达90跳出循环
    if data >= UPPER_LIMIT:
        print(f"over, greater than upper, data:{data}")
        break
    # [60~90) 区间内继续
    print(f"continue, in limit, data:{data}")
    data = random.randrange(0, 100, 1)
else:
    # 未达60正常结束
    print(f"over, less than lower, data:{data}")

print("\n### for ###")
# for 循环
for item in ["A", "B", "C", "D", "E"]:
    print(f"grade:{item}")
