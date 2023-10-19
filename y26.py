def Number(lis: list):
    count = 0
    uz_all = 0
    other_all = 0
    for i in range(len(lis)):
        s = lis[i]
        uz, other = map(int, s.split(":"))
        other_all += other
        uz_all += uz
        if uz > other:
            count += 3
        elif uz == other:
            count += 1

    return f'ball: {count}\nscore uzb {uz_all} : other {other_all}'
try:
    nums = input().split()
    score = Number(nums)
except ValueError:
    print("Error")
else:
    print(score)