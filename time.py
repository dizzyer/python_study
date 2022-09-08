import time

scale = 10
print("执行开始".center(scale, '-'))
for i in range(10):
    print("\r{:^3}% [{}]".format((i+1)*10, '*'*(i+1)+' '*(9-i)), end='')
    time.sleep(0.1)
# print('\n')
print('\n' + "执行结束".center(scale, '-'))
