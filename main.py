from file import *
from number_translator import *


def translate_nums(data):
    translated_data = list()
    for nums in data:
        if type(nums[0]) is int:
            lst = to_roman_nums(nums)
            translated_data.append(lst)
        else:
            translated_data.append(to_arab_nums(nums))
    return translated_data


def main():
    filename = input("Enter name of file: ")
    output_data = translate_nums(read_file(filename))
    output_filename = input("Choose file for output: ")
    write_file(output_filename, output_data)


if __name__ == '__main__':
    main()
