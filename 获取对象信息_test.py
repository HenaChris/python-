print(dir("ABC"))


class MyDog(object):
	def __len__(self):
		return 100
dog = MyDog()
print(dog.__len__())
print(len(dog))


class MyObject(object):
	def __init__(self):
		self.x = 9
	def power(self):
		return self.x*self.x

obj = MyObject()

#判断类
print(isinstance(obj,MyObject))

#是否有该属性
print(hasattr(obj,'x'))
print(obj.x)

#设置属性
print(hasattr(obj,'y'))
setattr(obj,'y',19)
print(hasattr(obj,'y'))

#获取属性
print(getattr(obj,'z',404))

#获取对象方法
print(hasattr(obj,'power'))
getattr(obj,'power')
fn = getattr(obj,'power')
print(fn())