f = open("waww.txt", "r")

all_words = list()
for line in f:
    line = line.strip()
    words = line.split()
    all_words += words

print (all_words)

all_words.sort()

print all_words

counter = 0
for line in open("waww.txt", "r"):
    line = line.strip()
    words = line.split()
    line_list = list()
    for word in words:
        line_list.append(all_words[counter])
        counter += 1
    print " ".join(line_list)


# for line in f:
#     line = line.strip()
#     words = line.split()
#     print words
#     print line
