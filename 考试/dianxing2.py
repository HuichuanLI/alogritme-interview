for a in range(9):
    for b in range(9):
        for c in range(9):
            for d in range(9):
                if a * 1000 + b * 100 + c * 10 + d + b * 1000 + c * 100 + d * 10 + a == 8888:
                    print(str(a) + " " + str(b) + " " + str(c) + " " + str(d))
