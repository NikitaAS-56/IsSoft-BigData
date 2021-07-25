import argparse
from config import *
from mysql.connector import connection


def get_movies_data(conn, n=None, regexp=None, year_from=None, year_to=None, genres=None):
    cursor = conn.cursor()
    if not n:
        n = 'NULL'
    if not regexp:
        regexp = 'NULL'
    else:
        regexp = f"'{regexp}'"
    if not year_from:
        year_from = 'NULL'
    if not year_to:
        year_to = 'NULL'
    if not genres:
        genres = 'NULL'
    else:
        genres = f"'{genres}'"

    try:

        query_string = f"CALL usp_find_top_rated_movies({n}, {regexp}, {year_from}, {year_to}, {genres});"
        data = []
        for result in cursor.execute(query_string, multi=True):
            if result.with_rows:
                for row in result.fetchall():
                    data.append(row)

        return data
    except Exception as e:
        print(e)

    cursor.close()


def print_movies(conn, n=None, regexp=None, year_from=None, year_to=None, genres=None, ) -> None:

    try:
        column = ['movieId', 'title', 'genres', 'year', 'rating']
        head = ', '.join(column)
        print(head)

        for row in get_movies_data(conn, n, regexp, year_from, year_to, genres):

            csv_row = ''
            for attribute in row:
                csv_row += "," + str(attribute)

            csv_row = csv_row[1:]
            print(csv_row)
    except Exception as e:
        print(e)


def argument_parser() -> dict:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-n", "--topN", type=int,
                        help="Number of top rated movies for each genre")
    parser.add_argument("-g", "--genres", type=str,
                        help="Filter movies by genre")
    parser.add_argument("-f", "--year_from", type=int,
                        help="Filter movies by year starting from --year_from")
    parser.add_argument("-t", "--year_to", type=int,
                        help="Filter movies by year ending --year_to")
    parser.add_argument("-r", "--regexp", type=str,
                        help="Filter movies by name")

    return vars(parser.parse_args())


def main():

    args = argument_parser()
    try:
        conn = connection.MySQLConnection(**CONFIG['db_connect'])
        print_movies(conn, args['topN'], args['regexp'], args['year_from'], args['year_to'], args['genres'])

    except Exception as e:
        print(e)

    conn.close()


if __name__ == "__main__":
    main()

