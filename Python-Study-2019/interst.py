# 用来计算复利


def interst():
	rate = 0.15
	sum = 0
	money = 12000
	for i in range(5):
		print(i)
		sum = (sum+money)*(1+rate)
	print(sum)


# 主函数
if __name__ == "__main__":
	interst()
