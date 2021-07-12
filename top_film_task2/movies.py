import re
import argparse
import csv


def reading_csv_file(file_path: str, columns: list = None) -> list:
    data = []
    with open(file_path) as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        if columns:
            for line in reader:
                data_line = {col: line.get(col) for col in columns}
                data.append(data_line)
        else:
            data = [row for row in reader]
    return data


def get_arguments() -> dict:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--N", type=int, help=" top № films ")
    ap.add_argument("--genres", type=str, help=" genre filter. (example: "'Comedy|Drama'"")
    ap.add_argument("--year_from", type=int, help=" year filter (example: 1999)")
    ap.add_argument("--year_to", type=int, help=" year filter (example: 2000)")
    ap.add_argument("--regexp", type=str, help="filter on name(example: Story)")
    return vars(ap.parse_args())


def getting_the_year_from_the_name(data: list, column: str, new_column: str, re_data: str, new_re_data: str) -> list:
    for row in data:
        if re.search(new_re_data, row[column]):  # looking for a year with regular degeneration
            new_col_val = re.search(new_re_data, row[column]).group()
        else:
            new_col_val = None

        row[new_column] = new_col_val
        row[column] = re.sub(re_data, '', row[column])
        # replace the found value in the
        # original with an empty character
    return data


def filter_data_by_year(data: list, column: str, start=None, end=None) -> list:
    filtered_data = []
    if start and end:
        if start > end:
            start, end = end, start

        for line in data:
            if not line[column]:
                continue
            val = int(line[column])
            if val >= start and val <= end:
                filtered_data.append(line)

    elif start:
        for line in data:
            if not line[column]:
                continue

            if start <= int(line[column]):
                filtered_data.append(line)
    elif end:
        for line in data:
            if not line[column]:
                continue

            if int(line[column]) <= end:
                filtered_data.append(line)
    else:
        return data

    return filtered_data


def sort_by_match(data: list, column: str, sort_text: str) -> list:
    filtered_data = []

    for line in data:
        if re.search(sort_text, line[column]):
            filtered_data.append(line)

    return filtered_data


def print_data_csv(data: list, n_rows=None):
    if n_rows and len(data) >= n_rows:
        data = data[:n_rows]

    print(', '.join(getting_a_column(data)))

    for row in data:
        csv_row = ''
        for x, y in row.items():
            csv_row += ',' + str(y)
        csv_row = csv_row[1:]
        print(csv_row)


def function_sorted_data(data: list, sort_by: str, reverse=True) -> list:
    return sorted(data, key=lambda k: (k[sort_by] is not None, k[sort_by]), reverse=reverse)


def getting_an_average_rating_for_a_movie(file_path: str, id_grop: str, rating: str) -> list:
    data = []
    with open(file_path) as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')

        group_val = {}
        for line in reader:
            val_gr = line.get(id_grop)
            rait_val = float(line.get(rating))

            if val_gr in group_val.keys():
                group_val[val_gr] += [rait_val]
            else:
                group_val[val_gr] = [rait_val]

        for k, v in group_val.items():
            data.append({id_grop: k, rating: round(sum(v) / len(v), 2)})

    return data


def getting_a_column(data: list) -> list:
    columns = data[0].keys()
    return columns


def devided_data(data: list, start=None, end=None) -> list:
    if start:
        data = data[start:]
    if end:
        data = data[:end]
    return data


def merging_dictionaries(movies: list, ratings: list, connection: str) -> list:
    merged_list = []
    count = 0
    for movie in movies:
        for item in range(count, len(ratings)):
            if movie[connection] == ratings[item][connection]:
                dct = dict(movie, **ratings[item])
                merged_list.append(dct)
                count += 1
                break

    return merged_list


def main():
    args = get_arguments()  # get arguments
    movies = reading_csv_file('movies.csv')  # reading from file
    movies = getting_the_year_from_the_name(movies, 'title', 'year', "\d\d\d\d", "\d\d\d\d")

    movies = filter_data_by_year(  # sorting data by year
        movies, 'year',
        start=args['year_from'],
        end=args['year_to']
    )

    if args['regexp']:
        movies = sort_by_match(movies, 'title', args['regexp'])

    movies = function_sorted_data(movies, 'movieId', reverse=False)

    ratings = getting_an_average_rating_for_a_movie('ratings.csv', 'movieId', 'rating')
    ratings = function_sorted_data(ratings, 'movieId', reverse=False)

    data = merging_dictionaries(movies, ratings, 'movieId')
    data = function_sorted_data(data, 'rating', reverse=True)

    if args['genres']:
        genres_data = []
        genres = args['genres'].split('|')
        for genre in genres:
            genres_data.extend(
                devided_data(
                    sort_by_match(data, 'genres', genre), end=args['N']))

        print_data_csv(genres_data)
    else:
        print_data_csv(data, n_rows=args['N'])


if __name__ == "__main__":
    main()
