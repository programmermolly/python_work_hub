# invitation=['施一公', '特朗普', '郑强', '奥巴马', '杨振宁', '罗翔']

invitation=['特朗普','奥巴马','杨振宁']
message1=f'请{invitation[0]}于今晚和我共进晚餐'
message2=f'请{invitation[1]}于今晚和我共进晚餐'
message3=f'请{invitation[2]}于今晚和我共进晚餐'

print(message1)
print(message2)
print(message3)

print('我们可以邀请更多人，今天买了一张大餐桌')
invitation.insert(0,'施一公')
invitation.insert(2,'郑强')
invitation.append('罗翔')
message4=f'请{invitation[3]}于今晚和我共进晚餐'
message5=f'请{invitation[4]}于今晚和我共进晚餐'
message6=f'请{invitation[5]}于今晚和我共进晚餐'
print(invitation)
print(message4)
print(message5)
print(message6)


print('由于餐桌无法及时送达，所以只能邀请两位嘉宾')


print(f'{invitation.pop(0)}我很抱歉，无法邀请您来共进晚餐')
print(f'{invitation.pop(0)}我很抱歉，无法邀请您来共进晚餐')
print(f'{invitation.pop(0)}我很抱歉，无法邀请您来共进晚餐')
print(f'{invitation.pop(0)}我很抱歉，无法邀请您来共进晚餐')


print(f'{invitation[0]}，您仍被邀请')
print(f'{invitation[1]}，您仍被邀请')

del invitation[0]
del invitation[0]

print(f'最后结果为{invitation}')


