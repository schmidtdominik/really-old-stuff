def is_prime(n):
	for x in range(2, n):
		if n % x == 0:
			return False
	return True


def get_result(task):
	output = []

	for x in range(task*1000, task*1000+1000): # with filter
		if is_prime(x):
			output.append(str(x))

	return ';'.join(output)