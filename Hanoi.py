x = []
y = []
z = []

def hanoi(n, i, j, k): #主函数hanoi用来进行汉诺塔的操作，表示将n个盘子从i栈移动到j栈，借助k栈
    if n == 1:         #n == 1 时开始移动，将i（list类型）的末尾元素添加到j后删除
        eval(j+".append("+i+"[-1])")
        eval(i+".pop()")
        print("{} -> {}".format(i, j))
        print(x, y, z)
    else:              #n != 1时先将上面n-1个塔移动到k栈，再把最后一个移动到j栈，最后把k栈上n-1个塔移动到j栈
        hanoi(n-1, i, k, j)
        hanoi(1, i, j, k)
        hanoi(n-1, k, j, i)
    return None

for i in range(3):
    x.append(i)
hanoi(i+1, 'x', 'z', 'y')