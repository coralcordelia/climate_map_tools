import csv
import glob
import os

glob.glob('/')

def open_csv_file(filename):
    with open(filename, "r", newline='') as infile:
        data = csv.DictReader(infile)
        return list(data)
    
def write_csv_file(filename, fields, data):
    # Credit to geeksforgeeks
    with open(filename, "w", newline='') as outfile:
        # creating a csv dict writer object
        writer = csv.DictWriter(outfile, fieldnames=fields)

        # writing headers (field names)
        writer.writeheader()

        # writing data rows
        writer.writerows(data)

def prompt(text, typ):
    output = input(text + '\n')
    try:
        return typ(output)
    except:
        print(f'Invalid response. Please type a {typ}.')
        return prompt(text, typ)
    
def add_iso_code(row):
    row_copy = row.copy()
    row_copy.update({"Country ID": id_by_iso_code[row["Code"]]})
    return row_copy

for filename in os.listdir('raw_data'):
    if filename.endswith(".csv"): 
        print(os.path.join('raw_data/', filename))
        original_data = open_csv_file('raw_data/' + filename)

        mapping = open_csv_file("ISO_to_country_id.csv")

        fields = list(original_data[0].keys()) + ["Country ID"]

        id_by_iso_code = {
            item["ISO Code"]: item["ID"]
            for item in mapping
        }

        output = [
            add_iso_code(row)
            for row in original_data if row["Code"] in id_by_iso_code and int(row["Year"]) >= 1950 and int(row["Year"]) <= 2021
        ]

        write_csv_file('formatted_data/' + filename, fields, output)
    else:
        continue

