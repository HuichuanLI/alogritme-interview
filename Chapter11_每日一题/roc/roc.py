def get_roc(data, pos, neg):
    data = sorted(data, key=lambda x: x[0], reverse=True)
    roc_arr = []
    tp = fp = 0
    for sample in data:
        tp += (1 if sample[1] == 1 else 0)
        fp += (1 if sample[1] == 0 else 0)
        roc_arr.append((fp / neg, tp / pos))
    return roc_arr


print(get_roc([[0.1, 1], [0.6, 1], [0.1, 0]], 1, 1))
