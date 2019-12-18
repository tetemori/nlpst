alp = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
alp = alp.split()
numc = [1, 5, 6, 7, 8, 9, 15, 16, 19]
d = {}
for i, name in enumerate(alp):
    if(i+1 in numc):
        name = name[0]
    else:
        name = name[0:2]
    d[str(i+1)] = name

print(d)
