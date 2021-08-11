"""
The main purpose of this program is to take the file of csv and convert them
to a json file in order to reduce the amount of time that needs to convert it 
manually.
"""
# Abraham Morales Arroyo 
# 8/11/2021
# Marc's data
# All credit goes to https://www.geeksforgeeks.org/convert-csv-to-json-using-python/
import csv
import json


# Function to convert a CSV to JSON
# Takes the file paths as arguments
def make_json(csvFilePath, jsonFilePath):
	
	# create a dictionary
	data = {}
	
	# Open a csv reader called DictReader
	with open(csvFilePath, encoding='utf-8') as csvf:
		csvReader = csv.DictReader(csvf)
		
		# Convert each row into a dictionary
		# and add it to data
		for rows in csvReader:
			
			# Assuming a column named 'No' to
			# be the primary key
			key = rows['No']
			data[key] = rows

	# Open a json writer, and use the json.dumps()
	# function to dump data
	with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
		jsonf.write(json.dumps(data, indent=4))
		
# Driver Code

# Decide the two file paths according to your
# computer system
csvFilePath = r'stocks.csv'
jsonFilePath = r'stocks.json'

# Call the make_json function
make_json(csvFilePath, jsonFilePath)
