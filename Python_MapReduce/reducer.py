# import argparse
# import sys
#
#
# def shuffle():
#     num_reducers = 1
#     shuffled_items = []
#     prev_key = None
#     values = []
#     try:
#         for slice in sys.stdin:
#
#                 key, value = slice.split("\t")
#                 if key != prev_key and prev_key != None:
#                     shuffled_items.append((prev_key, values))
#                     values = []
#
#                 prev_key = key
#                 values.append(value)
#
#     except:
#         pass
#     finally:
#         if prev_key != None:
#             shuffled_items.append((key, values))
#
#     result = []
#     num_items_per_reducer = len(shuffled_items) // num_reducers
#     if len(shuffled_items) / num_reducers != num_items_per_reducer:
#         num_items_per_reducer += 1
#     for i in range(num_reducers):
#         result.append(shuffled_items[num_items_per_reducer*i:num_items_per_reducer*(i+1)])
#     return result
#
# def get_arguments() -> dict:
#     ap = argparse.ArgumentParser(description=__doc__)
#     ap.add_argument("--N", type=int, help=" top № films ")
#     return vars(ap.parse_args())
#
#
# def reduce(name, values,args):
#     return name, values[:args]
#
#
# def main():
#     args = get_arguments()
#     for group in shuffle():
#         for slice in group:
#             key, values = slice[0], slice[1]
#             result_key, result_value = reduce(key, values,args["N"])
#
#             if args["N"]:
#                 for x in range(args["N"]):
#                     print(result_key + "\t"+result_value[x],end='')
#             else:
#                 for x in result_value:
#                     print(result_key + "\t" + str(x),end='')
#
#
# if __name__ == '__main__':
#     main()

import argparse
import sys


def argument_parser() -> dict:
    parser = argparse.ArgumentParser()
    parser.add_argument("--N", type=int,
                        help="Number of top rated movies for each genre")
    return vars(parser.parse_args())



def shuffle():
    shuffled_items = []
    prev_key = None
    values = []
    try:
        for slice in sys.stdin:

                key, value = slice.split("\t")
                if key != prev_key and prev_key != None:
                    shuffled_items.append((prev_key, values))
                    values = []
                prev_key = key
                values.append(value)

    except:
        pass
    finally:
        if prev_key != None:
            shuffled_items.append((key, values))

    return shuffled_items

def reduce(key, value, n=None):
    if n:
        for v in value[:n]:
            print(f"{key},{v}")

    else:
        for v in value:
            print(f"{key},'{v}")


def main():
    args = argument_parser()
    print('genre,title,year')
    for key, value in shuffle():
        reduce(key, value, args['N'])


if __name__ == '__main__':
    main()