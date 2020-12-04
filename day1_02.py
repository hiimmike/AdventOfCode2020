# advent of code day 1

def get_list(file_name):
	with open(file_name, 'r') as f:
		expenses = []
		for line in f:
			expenses.append(int(line))
	return expenses


def test(argument):	
	for i in argument:
		for x in argument:
			answer = 2020 - x - i
			if answer in argument:
				print(answer * i * x)
				print(i)
				print(x)
				print(answer)
				return answer
				return i
				return x				

test(get_list('day1.txt'))