import sys

n = int(sys.stdin.readline().strip())
card_list = sys.stdin.readline().strip().split()


def showdown(n, card_list):
    color = []
    size = []
    for k in range(1, n + 1):
        color.append(str(card_list[k - 1][0]))
    for h in range(1, n + 1):
        size5 = str(card_list[h - 1][1:len(card_list[h - 1])])
        if size5 == "J":
            size5 = 11
        elif size5 == "Q":
            size5 = 12
        elif size5 == "K":
            size5 = 13
        elif size5 == "A":
            size5 = 14
        size.append(int(size5))

    size_set = list(set(size))

    # 判断牌

    if len(set(color)) == 1 and max(size) - min(size) == 4 and max(size) == 14:
        print("HuangJiaTongHuaShun")
        exit()
    if len(set(color)) == 1 and max(size) - min(size) == 4:
        print("TongHuaShun")
        exit()
    else:
        if len(size) - 3 == len(size_set):
            for a in range(0, 5):
                for b in range(0, 2):
                    if size[a] == size_set[b]:
                        size[a] = 0
                        size_set[b] = 0
            last = [x for x in size if x != 0]
            if last[0] == last[1] == last[2]:
                print('SiTiao')
                exit()
            else:
                print("HuLu")
                exit()
        if len(set(color)) == 1:
            print("TongHua")
            exit()
        if len(size) - 2 == len(size_set):
            for a in range(0, 5):
                for b in range(0, 3):
                    if size[a] == size_set[b]:
                        size[a] = 0
                        size_set[b] = 0
            last = [x for x in size if x != 0]
            if last[0] == last[1]:
                print('SanTiao')
                exit()
            else:
                print('LiangDui')
                exit()

        if size == list(set(size)) and max(size) - min(size) == 4:
            print('ShunZi')
            exit()
        elif len(size) - 1 == len(size_set):
            print('YiDui')
            exit()




        else:
            print('GaoPai')


showdown(n, card_list)
