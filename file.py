import re


def read_file(filename: str):
    nums = list()
    with open(f"input/{filename}.txt") as file_object:
        lines = file_object.readlines()
    lines = filter(lambda x: x.strip(), lines)
    for line in lines:
        if len(re.findall('[0-9]', line)) != 0:
            nums.append(list(map(int, re.split('; |, | ', line))))
        else:
            str_list = list(re.split('; |, | ', line))
            nums.append([str_val.rstrip() for str_val in str_list])

    return nums


def write_file(filename: str, data: list):
    with open(f"output/{filename}.txt", 'w') as file_object:
        for row in data:
            file_object.write(' '.join([str(a) for a in row]) + '\n')
