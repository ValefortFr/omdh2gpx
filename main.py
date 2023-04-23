from datetime import datetime, timedelta

gpx = '<gpx creator="Moi" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.topogr' \
      'afix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd" version="1.1" xmlns="http://www.topografix.com/GPX' \
      '/1/1"><trk><trkseg>'

file_name = 'ACT_0000'

with open(f"{file_name}.OMH", 'rb') as file:
    data = file.read()

time_point = datetime(2000 + int(data[14]), data[15], data[16], data[17], data[18], data[19])

with open(f"{file_name}.OMD", 'rb') as file:
    data = file.read()

position = 60  # skip header
while len(data) > position:
    lat1 = int.from_bytes(data[position:position + 4], "little") / 10 ** 6
    lon1 = (int.from_bytes(data[position + 4:position + 8], "little") - 2 ** 32) / 10 ** 6

    lat2 = int.from_bytes(data[position + 20:position + 24], "little") / 10 ** 6
    lon2 = (int.from_bytes(data[position + 24:position + 28], "little") - 2 ** 32) / 10 ** 6

    gpx += f'<trkpt lat="{lat1}" lon="{lon1}"><time>' \
           f'{datetime.strftime(time_point, "%Y-%m-%dT%H:%M:%SZ")}</time></trkpt>' \
           f'<trkpt lat="{lat2}" lon="{lon2}"><time>' \
           f'{datetime.strftime(time_point + timedelta(seconds=5), "%Y-%m-%dT%H:%M:%SZ")}</time></trkpt>'

    time_point += timedelta(seconds=10)
    position += 60

gpx += '</trkseg></trk></gpx>'

with open(f'{file_name}.gpx', "w") as file:
    file.write(gpx)
