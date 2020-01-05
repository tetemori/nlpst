def ngram(target, w, i):
    #もし、単語のN-gramだった場合
    if(w == 0):
        words = target.split()
    # もし、文字のN-gramだった場合
    else:
        words = list(target)
    return [("".join(words[idx:idx + i])) for idx in range(len(words) - i + 1)]

X = set(ngram("paraparaparadise", 1, 2))
Y = set(ngram("paragraph", 1, 2))

#和集合
print(X | Y)

#積集合
print(X & Y)

#差集合
print(Y - X)

#差集合
print(X - Y)