import csv
import re
import sys
import argparse


def pairing(movies,args) -> list:
    if args['genres']:
        genres = args['genres'].split('|')
        d = []
        for row in movies:
            value = (row["title"], row["year"],)
            keys = row["genres"].split('|')
            for genre in genres:
                for key, value in map(keys, value):
                    if key == genre:
                        d.append((key, value))
    else:
        d = []
        for row in movies:
            value = (row["title"], row["year"],)
            keys = row["genres"].split('|')
            for key, value in map(keys, value):
                d.append((key, value))

    sorted_key_value_data = sorted(d, key=lambda k: (k[0], k[1]))
    if args['regexp']:
        sorted_key_value_data = sort_by_match(sorted_key_value_data, args['regexp'])

    return filter_data_by_year(sorted_key_value_data,args["year_from"],args["year_to"])


def map(keys, value):
    for key in keys:
        yield key, value


def sort_by_match(data: list, sort_text: str) -> list:
    filtered_data = []

    for line in data:
        if re.search(sort_text, line[1][0]):
            filtered_data.append(line)

    return filtered_data

def get_arguments() -> dict:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--genres", type=str, help=" genre filter. (example: "'Comedy|Drama'"")
    ap.add_argument("--year_from", type=int, help=" year filter (example: 1999)")
    ap.add_argument("--year_to", type=int, help=" year filter (example: 2000)")
    ap.add_argument("--regexp", type=str, help="filter on name(example: Story)")
    return vars(ap.parse_args())

def getting_the_year_from_the_name(data: list, column: str, new_column: str, re_data: str, new_re_data: str) -> list:
    for row in data:
        if re.search(new_re_data, row[column]):
            new_col_val = re.search(new_re_data, row[column]).group()
        else:
            new_col_val = None
        row[new_column] = new_col_val
        row[column] = re.sub(re_data, '', row[column])
    return data

def filter_data_by_year(data: list, start=None, end=None) -> list:
    filtered_data = []
    if start and end:
        if start > end:
            start, end = end, start

        for line in data:
            if not line[1][1]:
                continue
            val = int(line[1][1])
            if val >= start and val <= end:
                filtered_data.append(line)

    elif start:
        for line in data:
            if not line[1][1]:
                continue

            if start <= int(line[1][1]):
                filtered_data.append(line)
    elif end:
        for line in data:
            if not line[1][1]:
                continue

            if int(line[1][1]) <= end:
                filtered_data.append(line)
    else:
        return data

    return filtered_data

def reading( columns: list = None) -> list:
        data = []
        reader = csv.DictReader(sys.stdin, delimiter=',')
        if columns:
            for line in reader:
                data_line = {col: line.get(col) for col in columns}

                data.append(data_line)
        else:
            data = [row for row in reader]

        return data

def main():
    args = get_arguments()
    movies = reading()  # reading from file
    movies = getting_the_year_from_the_name(movies, 'title', 'year', '\(\d\d\d\d\)', '\d\d\d\d')

    for x in pairing(movies, args):
        key, value = x[0], '; '.join(x[1])
        print("{}\t{}".format(key, value))

       # for group in sh.shuffle(pairing(movies,args)):
    #
    #     for key, values in group:
    #         # print(key,values)
    #         result_key, result_value = rd.reduce(key, values, args["N"])
    #
    #         for i in range(args["N"]):
    #             print(result_key + "\t", (x for x in result_value[i]))
if __name__ == '__main__':
    main()
