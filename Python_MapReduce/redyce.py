import argparse
import shafling as sh


def get_arguments() -> dict:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--N", type=int, help=" top № films ")
    return vars(ap.parse_args())


def reduce(name, values,args):
    return name, values[:args]


def main():
    args = get_arguments()

    for group in sh.shuffle():
        for slice in group:
            key, values = slice[0], slice[1]
            result_key, result_value = reduce(key, values,args["N"])

            if args["N"]:
                for x in range(args["N"]):
                    print(result_key + "\t"+result_value[x],end='')
            else:
                for x in result_value:
                    print(result_key + "\t" + str(x),end='')


if __name__ == '__main__':
    main()












           # print(r"{}; {}".format(result_key, str(x)))
            # print(result_key + "\t" + str(result_value))
    #print(group[0])
    # for group in csv.reader(sys.stdin.readlines()):

        # for key, values in group:
        #     # print(key,values)
        #     result_key, result_value = reduce(key, values, args["N"])
        #
        #     for i in range(args["N"]):
        #         print(result_key + "\t", result_value)
