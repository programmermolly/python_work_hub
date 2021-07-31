def make_album(name_singer,name_album,num=None):
	album_info={name_singer:name_album,'num':num}
	if num:
		album_info['num']=num
	return album_info
usr_album=''
while True:
	usr_singer=input('请输入歌手名： ')
	if usr_singer=='quit':
		break
	usr_album=input('请输入专辑名： ')
	9
	if usr_album=='quit':
		break
res=make_album(usr_singer,usr_album)
if usr_singer!='quit' and usr_album!='quit':
	print(res)


