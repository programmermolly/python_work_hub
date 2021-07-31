def show_messages(messages):
	for message in messages:
		print(message)




def send_messages(messages):
	current_message=messages.pop()
	sent_messages.append(current_message)
	print(sent_messages)

# 函数调用
sent_messages=[]
messages=['Hello','你好']

show_messages(messages)
send_messages(messages[:])