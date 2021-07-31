'''两个形参，一个表示尺码，一个表示要印上去的字'''
def make_shirt(size,words):
	print(f"We're going to make a size {size} T-shirt with the words {words}")


# 用位置实参调用函数
make_shirt(35,"'I love Python'")

# 使用关键字实参调用函数
make_shirt(words="'I love Python'",size=35)


	
