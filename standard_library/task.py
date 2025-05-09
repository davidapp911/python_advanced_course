# You possess a file named "json_program1.json". This file includes numerous entries, each with an individual's
# details - name, birthdate, and gender.
# Your goal is to create a Python scripts that is able to do the following tasks:
#
# 1.- Open and read the file "json_program1.json" using the built-in 'json' module in Python.
# 2.- Process the JSON data to convert it into a usable format within your Python script.
# 3.- Analyze all entries within the JSON data to identify any individuals who are currently
# minors (under 18 years of age). For safety add a few minors in the JSON file.
# 4.- Display the details (name, birthdate, and gender) of all minors identified in step 3 as your output.
#
# In this project, you will be employing the 'os' and 'os.path' modules to perform file operations, 'datetime' to handle
# and manipulate date/time data, and 'json' for processing JSON data.
import json
from datetime import date


def main():
    # Input file path
    filepath = 'json_program1.json'

    with open(filepath, 'r') as file:
        data = json.load(file)


    minors = []

    # for each person in file, check if the age is less than 18
    for person in data:
        person_birthdate = date.fromisoformat(person['birth_date'])
        age = (date.today() - person_birthdate).days // 365

        # if age is less than 18, the person is a minor
        if age < 18:
            print("***********")
            print(f"Name: {person['name']}")
            print(f"Birth date: {person_birthdate}")
            print(f"Gender: {person['gender']}")
            print(f"Age: {age}")

            person["age"] = age
            minors.append(person)

        # stores into json file for further verification
        with open("minors.json", 'w') as file:
            json.dump(minors, file, indent=4)

if __name__ == '__main__':
    main()