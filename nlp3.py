alp = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
ry = alp.replace(".", "").replace(",", "")
ry = ry.split()
ans: str = ""
for y in ry:
    ans = ans + str(len(y))

print(ans)