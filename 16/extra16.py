# Nested_list = [[12, 34, 56, 67], [34, 68, 78]]
# Write a code that generates a list of the following numbers from
# the nested list above – 34, 67, 78. Your output should be another
# list:
# [34, 67, 78]. The list output should not have duplicates.

def generate_list():
    Nested_list = [[12, 34, 56, 67], [34, 68, 78]]
    values = [34, 67, 78]
    result = []
    for sublist in Nested_list:
        for item in sublist:
            if item in values:
                if item not in result:
                    result.append(item)

    return result


# Test
print(generate_list())
