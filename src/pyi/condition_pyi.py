import condition_v1

def no_over():
    print('no over running ... ')



def all_hold():
    print('all_hold running ... ')


if condition_v1.cond == 'mike':
    def exit_hold():
        print('exit_hold running ... ')
else:
    def no_exit_hold():
        print('no_exit_hold running ... ')