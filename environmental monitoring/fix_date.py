with open("env_mon.txt", "r+") as f:
    data = f.read()
    records = data.split("\n")
    for cnt, rec in enumerate(records):
    	records[cnt] = rec.split(";");

    for cnt, rec in enumerate(records):
    	d = rec[0][0:2]
    	m = rec[0][3:5]
    	records[cnt][0] = m + "/" + d + str(rec[0][5:])

    del records[-1]


    for cnt, rec in enumerate(records):
    	records[cnt] = ";".join(rec);

    records = "\n".join(records);

    f.seek(0)
    f.write(records)