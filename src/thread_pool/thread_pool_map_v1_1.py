"""
threading 模块 map 用法
"""

import concurrent.futures

# 定义一个可调用函数
def square(x):
    return x ** 2

# 创建 ThreadPoolExecutor 对象
with concurrent.futures.ThreadPoolExecutor() as executor:
    # 使用 map() 方法应用函数到多个输入
    inputs = [1, 2, 3, 4, 5]
    results = executor.map(square, inputs)

    # 打印结果
    for result in results:
        print(result)
