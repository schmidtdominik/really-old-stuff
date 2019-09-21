with open("env_mon.txt", "r+") as f:
	data = f.read()
	f.seek(0)

	records = data.split("\n")

	for cnt, rec in enumerate(records):
		records[cnt] = rec.split(";");
	del records[-1]


	for cnt, rec in enumerate(records):
		records[cnt][2] = str(float(records[cnt][2]) * 2)
		records[cnt][3] = str(float(records[cnt][3]) * 100)
		records[cnt][4] = str(float(records[cnt][4]) * 10)
		records[cnt][5] = str(float(records[cnt][5]) * 10)
		records[cnt][6] = str(float(records[cnt][6]) * 10)
		#records[cnt][7] = str(float(records[cnt][7]) / 4)

	for cnt, rec in enumerate(records):
		records[cnt] = ";".join(rec);

	records = "\n".join(records);

			
	f.write(records)