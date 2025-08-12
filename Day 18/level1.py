import re 

#1
paragraph = "I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love."
a = re.findall("\\w+", paragraph)
b = set(a)

get_frequent_word = [(a.count(i), i) for i in b]

frequent_word_sorted = sorted(get_frequent_word, key=lambda x : x[0], reverse=True)

#2
particles_ = ['-12', '-4', '-3', '-1', '0', '4', '8']
get_particles= [re.findall("-?\\d+", i)[0] for i in particles_]
particles = list(map(int, get_particles))

distance = particles[-1] - particles[0]
