
# class Student:
# 	def __init__(self, name, age, grade):
# 		self.name = name
# 		self.age = age
# 		self.grade = grade	# 0 - 100

# 	def get_grade(self):
# 		return self.grade 


# class Course:
# 	def __init__(self, name, max_students):
# 		self.name = name
# 		self.max_students = max_students

# 		self.students = []

# 	def add_student(self, student):
# 		if len(self.students) < self.max_students:
# 			self.students.append(student)
# 			return True
# 		return False

# 	def get_average_grade(self):
# 		value = 0
# 		for student in self.students:
# 			value += student.get_grade()

# 		return value / len(self.students)



# s1 = Student('Islombek', 21, 95)
# s2 = Student('Josh', 32, 75)
# s3 = Student('Timber', 42, 80)

# course = Course('Science', 2)
# course.add_student(s1)
# course.add_student(s2)

# # print(course.students[0].name)

# print(course.add_student(s3))

# print(course.get_average_grade())


#------------------------------------------------------------

					# Inheritance

# class Car1(object):
# 	def __init__(self, brand, c_type, cost):
# 		self.brand = brand
# 		self.c_type = c_type
# 		self.cost = cost

# 	def info(self):
# 		print("This is {}, type of the car is {}, and it costs ${}"
# 			.format(self.brand, self.c_type, self.cost))

# 	def mark(self):
# 		print(5)

# class Car2(Car1):

# 	def __init__(self, brand, c_type, cost, color):

# 		super(Car2, self).__init__(brand, c_type, cost)
# 		self.color = color
	
# 	def mark(self):
# 		print(1)

# 	def info(self):
# 		print('This is {}, type of the car is {}, and it costs ${} and the color is {}'.format(self.brand, self.c_type, self.cost, self.color))



# class Car3(Car1):
	
# 	def mark(self):
# 		print(3)


# c1 = Car1('Mustang', 'Sport', 12000)
# c1.info()
# # c1.mark()

# c2 = Car2('BMW', 'Sport', 15000, 'Green')
# c2.info()
# c2.mark()


# c3 = Car3('Rolls Royce', 'Classic', 20000)
# c3.info()
# c3.mark()



#------------------------------------------------------------------------


# class Animal(object):
# 	def __init__(self, name, age):
# 		self.n = name 
# 		self.a = age

# 	def print_all(self):
# 		print(f"My name is {self.n}, I'm {self.a} y.o.")


# class Dog(Animal):
# 	def data(self, name, age, color):
# 		super(Dog, self).data(name, age)
# 		self.c = color

# 	def print_all(self):
# 		print(f"My name is {self.n}, I'm {self.a} y.o. and I'm {self.c}")


# a = Animal('Lion', 7)
# a.data('Lion', 7)
# a.print_all()
# print(a.a)

# d = Dog()
# d.data('Dog', 3, 'White')
# d.print_all()
# print(d.color)


#------------------------------------------------------------------------

#						 @CLASSMETHOD
# class Person:
# 	num_people = 0

# 	def __init__(self, name):
# 		self.n = name
# 		Person.add_person()

# 	@classmethod
# 	def num_people_(cls):
# 		return cls.num_people

# 	@classmethod
# 	def add_person(cls):
# 		cls.num_people += 1


# p1 = Person('Tim')
# p2 = Person('Bill')

# print(Person.num_people_())

#------------------------------------------------------------------------
				
#				@STATICMETHOD 		
# class Math:

# 	@staticmethod
# 	def add5(x):
# 		return x + 5


# print(Math.add5(10))

#------------------------------------------------------------------------

#					ENCAPSULATION

# class Islom():
# 	def __init__(self):
# 		self.__n = 'Islombek '
# 		self.a = '21'

# 	def info(self):
# 		return self.__n + self.a


# a = Islom()

# print(a._Islom__n)  # to private variable we can access via _ClassName(UnderscoreClassName)
# print(a.a)
# print(a.info())

						# Getter & Setter
						

# class Islom():
# 	def __init__(self):
# 		self.__name = 'Islombek '
# 		self.age = '21'

# 	def info(self):
# 		return self.__name + self.age

# 	def get__name(self):
# 		return self.__name

# 	def set__name(self, n):
# 		self.__name = n 


# a = Islom()

# a.set__name('Joshua ')
# print(a.get__name())

# # print(a._Islom__name)  # to private variable we can access via _ClassName(UnderscoreClassName)
# # print(a.age)
# print(a.info())


# ----------------------------------------------------------------------------

# 						POLYMORPHISM


# class Math1:
# 	def number(self):
# 		return 5


# class Math2(Math1):
# 	# def number(self):
# 	# 	return 15


# a = Math1()
# print(a.number())

# b = Math2()
# print(b.number())







