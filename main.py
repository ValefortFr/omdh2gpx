from datetime import datetime, timedelta

gpx = '<gpx creator="Moi" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd" version="1.1" xmlns="http://www.topografix.com/GPX/1/1"><trk><trkseg>'

file_name = 'ACT_0000'

with open(f"{file_name}.OMH", 'rb') as file:
    data = file.read()

time_point = datetime(2000 + int(data[14]), data[15], data[16], data[17], data[18], data[19])

with open(f"{file_name}.OMD", 'rb') as file:
    data = file.read()

position = 0
while len(data) > position:
    latitude = int.from_bytes(data[position:position + 4], "little") / 10 ** 6
    longitude = (int.from_bytes(data[position + 4:position + 8], "little") - 2 ** 32) / 10 ** 6

    gpx += f'<trkpt lat="{latitude}" lon="{longitude}"><time>{datetime.strftime(time_point, "%Y-%m-%dT%H:%M:%SZ")}</time></trkpt>' \

    time_point += timedelta(seconds=5)
    position += 40 if position % 3 else 20

gpx += '</trkseg></trk></gpx>'

with open(f'{file_name}.gpx', "w") as file:
    file.write(gpx)
