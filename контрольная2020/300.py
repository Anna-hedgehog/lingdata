lines = []
firstwords = []
with open("300to.txt", "r", encoding = "utf-8") as f:
    for line in f:
        line = line.strip("\ufeff\n \n")
        if line:
            lines.append(line)
    for i in lines:
        i = i.split(' ')
        if i[0]:
            firstwords.append(i[0].strip(","))
            

with open("300tonew01.txt", "w", encoding = "utf-8") as n:
    for word in firstwords:
        n.write(word + "\n")


