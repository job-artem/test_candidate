import csv
import re

filepath = '/home/work/PycharmProjects/test_candidate/test_data/test.csv'


with open(filepath) as csv_file, open(filepath) as csv_file_2, open(filepath) as header_csv:
    header_reader = csv.DictReader(header_csv)
    for num, row in enumerate(header_reader):
        if num == 1:
            header = list(row.keys())
            break
    print(header)
    # reader = csv.reader(csv_file_2, delimiter=' ', quotechar='"', skipinitialspace=True)

    # data_reader = csv.DictReader(csv_file, fieldnames=header, delimiter=',')
    #
    # for num, row in enumerate(data_reader):
    #     if num == 1:
    #         pass
    #     else:
    #         print(row)

    # for num, (line, row) in enumerate(zip(csv_file, reader)):
    #     print(f'{num}  --> {line}{row}\n')

    for num, line in enumerate(csv_file):
        if num != 0:
            # 1
            print(f'{num} --> {line.strip()}')

            # 2
            line_arr = line.split(',')
            print(line_arr)
            # cleaned_arr = [el.strip() for el in line_arr]

            # 3
            cleaned_arr = []
            for el in line_arr:
                cleaned_el = re.sub(r'\"', '', el)
                cleaned_arr.append(cleaned_el)
            print(cleaned_arr)
            data_dict = {}

            # 4
            for key, value in zip(header, cleaned_arr):
                data_dict[key] = value
            print(data_dict, '\n')




