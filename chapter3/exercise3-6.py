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