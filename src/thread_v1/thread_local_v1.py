"""
线程本地对象
"""

import threading

# 创建线程本地数据对象
local_data = threading.local()


# 在线程中获取线程本地数据
def get_local_data():
    # return local_data.value
    return getattr(local_data, 'value', None)


# 在线程中设置线程本地数据
def set_local_data(value):
    local_data.value = value


set_local_data('main-haha')

def info():
    set_local_data('hello')
    print('local value is :', get_local_data())

# 创建线程对象
thread = threading.Thread(target=info)
thread.start()
thread.join()

# 通过线程对象获取线程本地数据
data = get_local_data()
print('local data main is:',data)  # 输出: Hello
