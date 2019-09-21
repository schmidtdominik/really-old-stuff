import sys

header = 'unixtime;air_quality;motion;interf1;interf2;bright_out;bright_top;bright_back;humidity;temp;heat_index;atm_pressure'

with open('samples/' + sys.argv[1], 'r+') as f:
    data = f.read()
    if not data.startswith(header):
        data = header + '\n' + data
        f.seek(0)
        f.write(data)
        print('Done.')
    else:
        print('Header already present in file!')
