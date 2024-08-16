import json


def write_json_file(data, filename):
    with open(filename, "w") as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)
        print(f"Data saved to {filename}")


southernmost_lat_values = [a * 0.5 for a in range(-180, 180)]
westernmost_long_values = [a * 0.5 for a in range(-360, 360)]

all_shapefiles = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "id": int((long * 2 + 360) + (lat * 2 + 180) * 720),
            "geometry": {
                "type": "Polygon",
                "coordinates": [[
                    [long, lat],
                    [long + 0.5, lat],
                    [long + 0.5, lat + 0.5],
                    [long, lat + 0.5],
                    [long, lat],
                ]],
            },
            "properties": {
                "FID": int((long * 2 + 360) + (lat * 2 + 180) * 720),
                "NORTHMOST LATITUDE": lat,
                "SOUTHMOST LATITUDE": lat + 0.5,
                "WESTMOST LONGITUDE": long,
                "EASTMOST LONGITUDE": long + 0.5,
            },
        }
        for long in westernmost_long_values
        for lat in southernmost_lat_values
    ],
}
write_json_file(all_shapefiles, "shapefiles.json")
