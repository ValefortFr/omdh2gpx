import argparse
from datetime import datetime, timedelta


def main():
    parser = argparse.ArgumentParser(description="Process an OMD and OMH file to produce a gpx one.")
    parser.add_argument("input_file", help="Base name of the OMD and OMH files (required, it is assumed they share the same stem)")

    args = parser.parse_args()
    file_name = args.input_file

    gpx = '<gpx creator="Moi" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd" version="1.1" xmlns="http://www.topografix.com/GPX/1/1"><trk><trkseg>'
    try:
        with open(f"{file_name}.OMH", 'rb') as file:
            data = file.read()
    except FileNotFoundError:
        print(f"Error: Input file '{file_name}' not found.")
        return

    time_point = datetime(2000 + int(data[14]), data[15], data[16], data[17], data[18])
    try:
        with open(f"{file_name}.OMD", 'rb') as file:
            data = file.read()
    except FileNotFoundError:
        print(f"Error: Input file '{file_name}' not found.")
        return

    position = 0
    while len(data) > position + 20:
        latitude = int.from_bytes(data[position:position + 4], byteorder='little', signed=True) / 10 ** 6
        longitude = int.from_bytes(data[position + 4:position + 8], byteorder='little', signed=True) / 10 ** 6

        gpx += f'<trkpt lat="{latitude}" lon="{longitude}"><time>{datetime.strftime(time_point, "%Y-%m-%dT%H:%M:%SZ")}</time></trkpt>'

        time_point += timedelta(seconds=5)
        position += 40 if position % 3 else 20

    gpx += '</trkseg></trk></gpx>'

    with open(f'{file_name}.gpx', "w") as file:
        file.write(gpx)

    print(f'{file_name}.gpx written')

if __name__ == "__main__":
    main()
