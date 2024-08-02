from tqdm import tqdm
import time

# 设置总步数为 100
total_steps = 100

# 使用 with 语句创建一个 tqdm 进度条对象
with tqdm(total=total_steps, ncols=80) as pbar:
    # 模拟耗时的操作
    for i in range(total_steps):
        time.sleep(0.1)
        pbar.update(1)  # 更新进度条，步长为 1

import time

# 设置总步数为 50
total_steps = 50

# 模拟耗时的操作
for i in range(total_steps):
    time.sleep(0.1)
    progress = "*" * int((i + 1) / total_steps * 30)
    print("\r[{}] {:.2%}".format(progress.ljust(30), (i + 1) / total_steps), end="")
