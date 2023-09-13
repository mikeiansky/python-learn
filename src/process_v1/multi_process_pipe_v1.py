"""
多进程管道通信
"""
import multiprocessing


def main():
    pipe_send, pipe_recv = multiprocessing.Pipe()
    print(pipe_send)
    print(pipe_recv)

    pipe_send.send('test')
    print('after send')

    # 
    b_result = pipe_recv.recv_bytes()
    print('receive byte data :', b_result)

    # 没有数据接收会阻塞，这个怎么才算接收完成
    result = pipe_recv.recv()
    print('receive data :', result)

    print('main complete ... ')

if __name__ == '__main__':
    main()