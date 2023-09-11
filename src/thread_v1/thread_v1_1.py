"""
这里是线程
"""

import threading

ld = threading.local()
ld.left = 189

print("current thread name ", threading.current_thread().name)
print("main ld left : ", ld.left)
print("type ld : ", type(ld))
print('on main has attr left', hasattr(ld, 'left'))

def info(msg):
    
    ild = threading.local()
    tn = threading.current_thread().name

    print(tn, ' info is ', msg)
    if not hasattr(ild, 'left') :
        print('have not left attr , thread name is ', tn)
        ild.left = 299
    
    print("this is thread name is ", tn)
    # print("type ild : ", type(ild))
    print("thread local left is ", ild.left)

t1 = threading.Thread(target=info, args=('ttt---->11',))

t2 = threading.Thread(target=info, args=('ttt---->22',))

t1.start()
t2.start()
t1.join()
t2.join()

print('complete')
