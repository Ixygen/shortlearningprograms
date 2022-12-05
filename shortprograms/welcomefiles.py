f_handle = open('mbox-short.txt')
#print(f_handle)

for text in f_handle:
    space_rm = text.rstrip()
    print(space_rm.upper())