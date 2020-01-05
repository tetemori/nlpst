def ngram(target, w, i):
    #もし、単語のN-gramだった場合
    if(w == 0):
        words = target.split()
    # もし、文字のN-gramだった場合
    else:
        words = list(target)
    return [words[idx:idx + i] for idx in range(len(words) - i + 1)]


#単語のbi-gram
print(ngram("I am an NLPer", 0, 2))
#文字のbi-gram
print(ngram("I am an NLPer", 1, 2))