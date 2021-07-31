# "carmaker"意为“汽车制造商” "car model"意为“汽车型号”
def make_car(carmaker,car_model,**car_dict):
	car_dict['制造商']=carmaker
	car_dict['型号']=car_model
	return car_dict


# 函数调.用
car=make_car('subaru','outback',color='blue',tow_package=True)
print(car)
	