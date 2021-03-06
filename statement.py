# 条件语句的使用
# 1.if ... elif ... else 条件判断语句
boolVal = 0;
if boolVal:
	print('its true');
elif not(boolVal): # 使用not(bool)函数作为逻辑非
	print('its false');
else :
	print('what is it?');

# 2.for 循环语句
# Python的for循环跟C的基础for循环不一样
arr = ['chaoshen', 'shasha', 'lijie'];
for item in arr:
	print(item);
# 当我们要对一个遍历的数组进行修改操作时，最好遍历该数组的副本（拷贝后的），放置发生无限循环
for w in arr[:]:
	if len(w) > 6:
		arr.insert(0, w);
print(arr);

# 3.range函数
# 遍历一些列的数字
for num in range(5): # 0 - <5
	print(num);

for num in range(5, 10): # 5 - <10
	print(num);

for num in range(12, 100, 10): # 12 - <100 其中筛选出12 + 10*i的数据
	print(num);

iteArr = ['jinchao','shanshan','chaoshen','shasha'];
for num in range(len(iteArr)):
	print(num,iteArr[num]);
# 注：range(num) 函数返回的是一个对象，虽然跟List对象很相似，因为它能够被遍历，但是它并不是List对象
print(range(5));
print(list(range(5)));

# 4.break continue 和 else(用于循环的正常退出判断)
# break 用于终止 for 和 while 循环
for num in range(1, 10):
	print(num);
	# if num > 6:
	# 	break;
	# 用于循环的正常退出判断，即非break,continue 和 异常导致的循环退出
else: 
	print('loop is end');
# 5.pass
# pass语句没有任何含义
while False:
	pass

# function 函数
def fib(n):
	a, b = 0, 1;
	result = [];
	while a < n:
		print(a, end = ' ');
		result.append(a);
		a, b = b, a + b;
	print();
	return result;
print(fib(15));