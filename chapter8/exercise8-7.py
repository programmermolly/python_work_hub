def make_album(name_singer,name_album,num=None):
	album_info={name_singer:name_album,'num':num}
	if num:
		album_info['num']=num
	return album_info

# 函数调用
res1=make_album('刘欢','好汉歌',7)
print(res1)

res2=make_album('薛之谦','演员')
print(res2)

res3=make_album('萧全','走着走着就散了')
print(res3)


