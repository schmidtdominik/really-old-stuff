import os
 
index = 0

data_file = open('primes_data', 'a+')

if os.path.isfile('index'):
	index_file = open('index', 'w+')
	index = int(data_file.read().strip())

def store(output):
	for number in output:
		data_file.write(str(number) + ';')
		output = []

	index_file.write(str(index))

def get_task():
	global index
	task = index
	index += 1
	return task

def receive_results(id, result):
	print(id, result)
	return "done"