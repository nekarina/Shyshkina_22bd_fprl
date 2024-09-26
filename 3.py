def word(w):
    if len(w) < 2:
        return w
    word = w[:2] +"..." + w[:2] + "..." + w + "?"
    return word
w = "Today weather is incredible"
word_s = word(w)
print(word_s)