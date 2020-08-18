#!/usr/bin/env python3
line = "-" * 35

a = ('Distinction','A')
b = ('Merit','B')
c = ('Credit','C')
d = ('Satisfactory', ' D')
f = ('UnSatisfactory', 'F')

def unpacker(values):
	for item in values:
		print(item)
	print(line)

def calculator(paper_mark = 0, pupil_mark = 0):
	percent = (pupil_mark / paper_mark) * 100
	return round(percent)

def invalid_value():
	print("Invalid value!")
	print(line)

def decider(percentage = 0):
	if (percentage < 1) | (percentage > 100):
		invalid_value()
	elif percentage >= 75:
		print(str(percentage) + '%')
		unpacker(a)
	elif percentage >= 65:
		print(str(percentage) + '%')
		unpacker(b)
	elif percentage >= 40:
		print(str(percentage) + '%')
		unpacker(c)
	elif percentage >= 30:
		print(str(percentage) + '%')
		unpacker(d)
	elif percentage < 30:
		print(str(percentage) + '%')
		unpacker(f)

try:
	paper = int(input("Paper's Mark: "))

	while True:
		pupil = int(input("Pupil's Mark: "))
		if pupil == 0:
			print("Good Bye!")
			break
		decider(calculator(paper, pupil))
except:
	pass