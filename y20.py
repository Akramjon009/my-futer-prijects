def txt(texts: list):
    if texts != []:
        words = str()
        for i in range(len(texts)):
            if i != len(texts)-1:
                words += texts[i]+", "
            else:
                words = words[:-2]+" and "+texts[i]
        return words + " likes this"
    else:
        return "no one likes this"

lis = input().split()
print(txt(lis))