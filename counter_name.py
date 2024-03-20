from collections import Counter

# def count_names(first_file, second_file):
#     # Read the names from the first file
#     with open(first_file, 'r') as file:
#         names = file.read().splitlines()

#     # Read the content of the second file
#     with open(second_file, 'r') as file:
#         content = file.read()

#     # Count the occurrences of each name in the second file
#     name_counts = Counter(names)

#     # Print the lines containing the name and count
#     for name in name_counts:
#         count = name_counts[name]
#         lines = [line.strip() for line in content if name in line]
#         print(f"Name: {name} | Count: {count}")
#         print("Lines:")
#         for line in lines:
#             print(line)
#         print()

# def count_names(first_file, second_file):
#     # Read the names from the first file
#     with open(first_file, 'r') as file:
#         names = file.read().splitlines()

#     # Read the content of the second file
#     with open(second_file, 'r') as file:
#         content = file.read()


#     # Count the occurrences of each name in the second file
#     name_counts = Counter(names)

#     # Print the name, count, and exact occurrences in the second file
#     for name in name_counts:
#         occurrences = content.count(name)
#         print(f"Name: {name} | Occurrences: {occurrences}")


# def count_names(first_file, second_file, output_file):
#     # Read the names from the first file
#     with open(first_file, 'r') as file:
#         names = file.read().splitlines()

#     # Read the content of the second file
#     with open(second_file, 'r') as file:
#         content = file.read()

#     # Count the occurrences of each name in the second file
#     name_counts = Counter(names)

#     # Prepare the output content
#     output = ""
#     for name in name_counts:
#         occurrences = content.count(name)
#         output += f"Name: {name} | Occurrences: {occurrences}\n"

#     # Write the output to the file
#     with open(output_file, 'w') as file:
#         file.write(output)


# def count_names(first_file, second_file, output_file):
#     # Read the names from the first file
#     with open(first_file, 'r') as file:
#         names_first = file.read().splitlines()

#     # Read the names from the second file
#     with open(second_file, 'r') as file:
#         names_second = file.read().splitlines()

#     # Find the common names between the two files
#     common_names = set(names_first) & set(names_second)

#     # Prepare the output content
#     output = ""
#     for name in common_names:
#         # count = names_second.count(name)
#         output += f"{name}\n"
#         # for line in names_second:
#         #     if line == name:
#         #         output += line + "\n"

#     # Write the output to the file
#     with open(output_file, 'w') as file:
#         file.write(output)


def count_names(first_file, second_file, output_file):
    # Read the names from the first file
    with open(first_file, 'r') as file:
        names_first = file.read().splitlines()

    # Read the names from the second file
    with open(second_file, 'r') as file:
        names_second = file.read().splitlines()

    # Find the names that appear in the first file but not in the second file
    names_only_in_first = list(set(names_first) - set(names_second))

    # Prepare the output content
    output = ""
    for name in names_only_in_first:
        output += f"{name}\n"

    # Write the output to the file
    with open(output_file, 'w') as file:
        file.write(output)

# Usage example
count_names("import1.txt","useInService_removeDupicate.txt","counter_file.txt")