def hanoi(n, a='A', b='B', c='C'): 
	'''汉诺塔'''
    if n == 1:
        print('move', a, '-->', c)
        return

    # 要把A的前n-1个饼全移到B，A剩一个饼，再把这个饼移到C
    hanoi(n-1, a, c, b)
    print('move', a, '-->', c)

    # 现在把B看作第一个塔，问题就变成了把B的所有饼移到C，形成递归
    hanoi(n-1, b, a, c)

if __name__ == '__main__':
	print(hanoi(5))

'''Stack Version
from Stack import Stack

def HanoiWithStack(n, a, b, c):
	if a.size() == 0:
		for i in range(n, 0, -1):
			a.push(i)
	if n == 1:
		c.push(a.pop())
		return
	HanoiWithStack(n - 1, a, c, b)
	c.push(a.pop())
	HanoiWithStack(n - 1, b, a, c)


if __name__ == '__main__':
	a = Stack()
	b = Stack()
	c = Stack()
	HanoiWithStack(5, a, b, c)
	for i in range(c.size()):
		print(c.pop())
'''