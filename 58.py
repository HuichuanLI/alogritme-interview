import sys


def entityRecogProcess(text):
    dict1, phrases, entity = text.split(";")
    dict2 = {}
    res = ""
    for elem in dict1.split(","):
        english, chinese = elem.split(":")
        dict2[chinese] = english
    Flag = False
    entity = entity.rstrip()
    history = ""
    history2 = ""
    for elema, elemb in zip(phrases, entity.split()):
        elemb = elemb.strip()
        if elemb == 'O':
            Flag = False
        else:
            if not Flag:
                if res:
                    res += "," + dict2[elemb] + ":" + elema
                else:
                    res += "" + dict2[elemb] + ":" + elema
                Flag = True
                history = dict2[elemb]
            else:
                if history and dict2[elemb] != history:
                    res += "," + dict2[elemb] + ":"
                    history = dict2[elemb]

                res += elema
    return res


if __name__ == "__main__":
    for line in sys.stdin:
        print(entityRecogProcess(line))
