import sys
def shuffle():
    num_reducers = 1
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

    result = []
    num_items_per_reducer = len(shuffled_items) // num_reducers
    if len(shuffled_items) / num_reducers != num_items_per_reducer:
        num_items_per_reducer += 1
    for i in range(num_reducers):
        result.append(shuffled_items[num_items_per_reducer*i:num_items_per_reducer*(i+1)])
    return result
