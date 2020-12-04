# advent of code day 1

def get_list(file_name):
	with open(file_name, 'r') as f:
		expenses = []
		for line in f:
			expenses.append(int(line))
	return expenses


def test(argument):	
	n = 0
	for i in argument:
		answer = 2020 - argument[n]
		if answer in argument:
			print(answer)
			print(argument[n])
			print(answer * argument[n])
			return answer
			return argument[n]
		else:
			n += 1


test(get_list('day1.txt'))