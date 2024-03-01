import re

# Sample array of student names
students = ["John Doe", "Alice Smith", "Bob Johnson", "Jane Doe", "Mary Johnson"]

# Given name to search for
given_name = "Johnson"

# Define a regular expression pattern to match the given name
pattern = re.compile(r'\b{}\b'.format(given_name))

# Use filter and lambda function to select students with the given name
selected_students = list(filter(lambda x: pattern.search(x), students))

# Print the selected students
print("Students with the name '{}':".format(given_name))
for student in selected_students:
    print(student)
