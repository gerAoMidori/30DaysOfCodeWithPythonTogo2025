import re
import time
texte = "stephen.mar.quard@uct.ac.za"
texte_ = "<postmaster@collab.sakaiproject.org>"

#4
with open("email_exchanges_big.txt", "r", encoding="utf-8") as f:
    content = f.read()

emails = re.findall("[a-z0-9.]+@[a-z0-9.]+", content)

#5
def most_common_words(filename, top):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    a = re.findall("\\w+", content)
    b = set(a)

    get_common_word = [(a.count(i), i) for i in b]
    common_word_sorted = sorted(get_common_word, key=lambda x : x[0], reverse=True)

    return common_word_sorted[:top]


#rint(most_common_words("donald_speech.txt", 10))