"""
参数传递的测试v1版本
"""

def append(l):
    l.append('end')

def test_trans():
    ll = ['java', 'oracle', 'python']
    print('before append ll',ll)    
    append(ll)
    print('after append ll',ll)

if __name__ == "__main__":
    test_trans()