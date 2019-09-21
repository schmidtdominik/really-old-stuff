items = ["Datetime", "Brightness", "Air Quality", "PIR", "Humidity", "Temperature", "Heat Index", "Air pressure"]

with open("env_mon.txt", "r+") as f:
	data = f.read()
	f.seek(0)

	records = data.split("\n")
	for cnt, rec in enumerate(records):
		records[cnt] = rec.split(";");


	delete = []

	for cnt, rec in enumerate(records):
		if (rec[0][6:10] != "2015"):
			delete.append(cnt)

	for cnt, i in enumerate(delete):
		del records[i - cnt]



	for cnt, rec in enumerate(records):
		records[cnt] = ";".join(rec);

	records = "\n".join(records);

	for cnt, item in enumerate(items):
		f.write(item)
		if (cnt < len(items) - 1):
			f.write(";")

	f.write("\n")

	f.write(records)
	f.truncate()