# climate_map_tools
Tools for uploading files onto MIT STRESS platform

This is a collection of some tools that I use that help for uploading things to the STRESS platform. 

The file formatting_atmospheric_data/format_data.py formats data that comes from CSV files with country ISO codes and columns and each row corresponding to a certain year number. Notice that, in order for the program to work, you must first delete the row with the country name. It outputs a CSV file with each country-year pair as a row, included with the Country ID corresponding to the ISO code of that country as well as the value assigned to that country (usually climate projections.) It also only uses years from 2023 onwards to only include projections; to change this, edit line 60. To use the tool, first load all of the files you want to format into formatting_atmospheric_data/raw_data/, and running the program will add the formatted versions of these files into formatting_atmospheric_data/formatted_data/.

The file formatting_global_data/format_data.py takes data downloaded in CSV form in the format provided by Our World In Data, and simply adds the Country ID column with the value corresponding to the ISO code value (if the Country ID exists, otherwise it removes the row) and removes years before 1950 and after 2021 (very recent data often has reporting issues.) To use it, put all downloaded CSV files from Our World In Data that you want to format into formatting_global_data/raw_data/ and the formatted versions of these files will be outputted into formatting_global_data/formatted_data/.

The file shapefile_generator.py generates shapefiles of half-degree by half-degree grid units that can be imported into ArcGIS. After running it, it outputs a file called shapefiles.json.
