def merge_rows(first, second):
    merged = []

    for index, element in enumerate(first):
        merged.append(element + max(second[index], second[index + 1]))

    return merged

def get_maximum_path(rows):
    if len(rows) == 1:
        return rows[0][0]

    new = rows[:-2]
    new.append(merge_rows(rows[-2], rows[-1]))

    return get_maximum_path(new)

def parse_string(string): #turns a string like "17 47 82" into [17, 47, 82]
    split = string.split()

    return [int(number) for number in split]

def parse_file(filename): #turns a file containing a text representation of a triangle into a list of lists
    f = open(filename, "r")
    return [parse_string(line.strip()) for line in f]

f = open("./data.txt", "r")
print(get_maximum_path(parse_file("./data.txt")))