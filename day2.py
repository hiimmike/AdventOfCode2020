# advent of code day 2
# part 1

def get_list(file):
	with open(file, 'r') as f:
		items = f.readlines()
		valid_pws = 0
		for line in items:
			lower = int(line.split('-')[0])
			upper = int(line.split('-')[1].split(' ')[0])
			key = line.split(':')[0][-1]
			password = line.split(': ')[-1]
			valid = 0
			for char in password:
				if char == key:
					valid += 1
			if lower <= valid <= upper:
				valid_pws += 1

	return valid_pws

go = get_list('2day.txt')
print(go)