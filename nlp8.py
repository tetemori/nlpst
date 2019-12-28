def cipher(x, y):
    result = ""
    if(y == 0):
        for ans in x:
            if(ans.islower()):
                ans = chr(219 - ord(ans))
            result = result + ans
    if (y == 1):
        for ans in x:
            if(ans.islower()):
                ans = chr(219 - ord(ans))
            result = result + ans
    return result

print(cipher("I Hzev Pvm", 1))