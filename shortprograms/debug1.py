han = open('mbox-short.txt')

for line in han:
    line = line.rstrip()
    words = line.split()
    print('words:',words)
    # Guardian partner
    #if len(words) < 3 or words[0] != 'From':
    if len(words) < 3:
        continue
    if words[0] != 'From':
        continue
    print(words[2])