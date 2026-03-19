def fltr(sentence, x_words):
    words = sentence.split()
    FLTRD = ""
    for word in words:
        if word in x_words:
            FLTRD += "*" * len(word) + " "
        else:
            FLTRD += word + " "
    return FLTRD.strip()


sentence = input("Enter a sentence: ")
x_words_input = input("Enter bad words separated by commas: ")

x_words = x_words_input.split(",")


FLTRD = fltr(sentence, x_words)
print("Filtered sentence:", FLTRD)
