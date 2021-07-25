invitation=['特朗普','奥巴马','杨振宁']
message1=f'请{invitation[0]}于今晚和我共进晚餐'
message2=f'请{invitation[1]}于今晚和我共进晚餐'
message3=f'请{invitation[2]}于今晚和我共进晚餐'

print(message1)
print(message2)
print(message3)


print(invitation.pop()+'无法赴约')

invitation.append('施一公')
print(invitation)
message1=f'请{invitation[0]}于今晚和我共进晚餐'
message2=f'请{invitation[1]}于今晚和我共进晚餐'
message4=f'请{invitation[2]}于今晚和我共进晚餐'
print(message1)
print(message2)
print(message4)
