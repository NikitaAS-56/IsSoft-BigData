# import csv
# import re
# import sys
# import argparse
#
#
# def mapping(regexp=None, year_from=None, year_to=None) -> list:
#     for movieId, title, genres in csv.reader(sys.stdin):
#         if re.search(r'\d\d\d\d', title):
#            year = int(re.search(r'\d\d\d\d', title).group())
#         else:
#             year = None
#         title = re.sub(r'\s\(\d\d\d\d\)', '', title)
#         genres = genres.split('|')
#
#         if check_year(year_from, year_to, year) and check_regexp(title, regexp):
#             for genre in genres:
#                 yield dict({genre: (title, year)})
#         # if args['genres']:
#         #     genres = args['genres'].split('|')
#         #     d = []
#         #     for row in movies:
#         #         value = (row["title"], row["year"],)
#         #         keys = row["genres"].split('|')
#         #         for genre in genres:
#         #             for key, value in map(keys, value):
#         #                 if key == genre:
#         #                     d.append((key, value))
#         # else:
#         #     d = []
#         #     for row in movies:
#         #         value = (row["title"], row["year"],)
#         #         keys = row["genres"].split('|')
#         #         for key, value in map(keys, value):
#         #             d.append((key, value))
#
#         # sorted_key_value_data = sorted(d, key=lambda k: (k[0], k[1]))
#         # if args['regexp']:
#         #     sorted_key_value_data = sort_by_match(sorted_key_value_data, args['regexp'])
#         # filter_data_by_year(sorted_key_value_data, args["year_from"], args["year_to"])
#         return d
#
#
# def map(keys, value):
#     for key in keys:
#         yield key, value
#
#
# def sort_by_match(data: list, sort_text: str) -> list:
#     filtered_data = []
#
#     for line in data:
#         if re.search(sort_text, line[1][0]):
#             filtered_data.append(line)
#
#     return filtered_data
#
# def get_arguments() -> dict:
#     ap = argparse.ArgumentParser(description=__doc__)
#     ap.add_argument("--genres", type=str, help=" genre filter. (example: "'Comedy|Drama'"")
#     ap.add_argument("--year_from", type=int, help=" year filter (example: 1999)")
#     ap.add_argument("--year_to", type=int, help=" year filter (example: 2000)")
#     ap.add_argument("--regexp", type=str, help="filter on name(example: Story)")
#     return vars(ap.parse_args())
# #
# # def getting_the_year_from_the_name(data: list, column: str, new_column: str, re_data: str, new_re_data: str) -> list:
# #     for row in data:
# #         if re.search(new_re_data, row[column]):
# #             new_col_val = re.search(new_re_data, row[column]).group()
# #         else:
# #             new_col_val = None
# #         row[new_column] = new_col_val
# #         row[column] = re.sub(re_data, '', row[column])
# #     return data
#
# def filter_data_by_year(data: list, start=None, end=None) -> list:
#     filtered_data = []
#     if start and end:
#         if start > end:
#             start, end = end, start
#
#         for line in data:
#             if not line[1][1]:
#                 continue
#             val = int(line[1][1])
#             if val >= start and val <= end:
#                 filtered_data.append(line)
#
#     elif start:
#         for line in data:
#             if not line[1][1]:
#                 continue
#
#             if start <= int(line[1][1]):
#                 filtered_data.append(line)
#     elif end:
#         for line in data:
#             if not line[1][1]:
#                 continue
#
#             if int(line[1][1]) <= end:
#                 filtered_data.append(line)
#     else:
#         return data
#
#     return filtered_data
#
# # def reading( columns: list = None) -> list:
# #         data = []
# #         reader = csv.DictReader(sys.stdin, delimiter=',')
# #         if columns:
# #             for line in reader:
# #                 data_line = {col: line.get(col) for col in columns}
# #
# #                 data.append(data_line)
# #         else:
# #             data = [row for row in reader]
# #
# #         return data
#
# def main():
#     args = get_arguments()
#     # movies = reading()  # reading from file
#     # movies = getting_the_year_from_the_name(movies, 'title', 'year', '\(\d\d\d\d\)', '\d\d\d\d')
#
#     for x in mapping(args['regexp'], args['year_from'], args['year_to']):
#         key, value = x[0], x[1]
#         print(dict({key:(value)}))
#         # print("{}\t{}".format(key, value))
#
#
# if __name__ == '__main__':
#     main()
#

import csv
import sys
import re
import argparse


def get_arguments() -> dict:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--genres", type=str, help=" genre filter. (example: "'Comedy|Drama'"")
    ap.add_argument("--year_from", type=int, help=" year filter (example: 1999)")
    ap.add_argument("--year_to", type=int, help=" year filter (example: 2000)")
    ap.add_argument("--regexp", type=str, help="filter on name(example: Story)")
    return vars(ap.parse_args())

def filter_by_regexp(title, regexp):
    if regexp:
        return True if re.search(regexp, title) else False

    return True


def sort_genre(g, genres):
    if genres:
        genres = genres.split("|")
        for genre in genres:
            return True if genre == g else False
    return True


def map(regexp=None, year_from=None, year_to=None):
    for movieId, title, genres in csv.reader(sys.stdin):

        if re.search(r'\d\d\d\d', title):
            year = int(re.search(r'\d\d\d\d', title).group())
        else:
            year = None

        title = re.sub(r'\s\(\d\d\d\d\)', '', title)
        genres = genres.split('|')

        if filter_by_year(year_from, year_to, year) and filter_by_regexp(title, regexp):
            for genre in genres:
                key = genre
                value = title, year
                yield key, value

def filter_by_year(year_from, year_to, year):
    if year_to and year_from and year:
        return True if (year_from <= year <= year_to) else False

    elif year_to and year:
        return True if (year <= year_to) else False

    elif year_from and year:
        return True if (year >= year_from) else False

    return True


def main():
    args = get_arguments()

    for k in map(args['regexp'], args['year_from'], args['year_to']):
        if args['genres']:
            for genre in args['genres'].split("|"):
                if sort_genre(k[0], genre):
                    key, value = k[0], k[1]
                    print("{}\t{}".format(key, value))
                    # print(dict({key: (value)}))
        else:
            key, value = k[0], k[1]
            # print(dict({key: (value)}))
            print("{}\t{}".format(key, value))

if __name__ == '__main__':
    main()