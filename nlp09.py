import random

target = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
target = target.split()

result = []

for i in target:
    if(len(i) <= 4):
        result.append(i)
    else:
        onf = list(i[1:-1])
        random.shuffle(onf)
        result.append(i[0] + "".join(onf) + i[-1])

print(" ".join(result))