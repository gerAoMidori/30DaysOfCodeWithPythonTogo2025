import re
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching
 m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

def clean_text(sentence):
    return re.sub("[^A-Za-z0-9 ]","" , sentence)

def most_frequent_words(data_ : str):
    data = data_.split()
    items = set(data)
    items_counted =  [(data.count(i), i) for i in items]
    return sorted(items_counted, key = lambda x : x[0], reverse= True)


print(most_frequent_words(clean_text(sentence)))
      
