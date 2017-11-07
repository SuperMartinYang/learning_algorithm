s = ''
with open('C:\\Users\\81082\\Desktop\\DDL.txt', mode='r', encoding='ANSI') as f:
    for line in f:
        s += line


with open('C:\\Users\\81082\\Desktop\\DDL_up.txt', mode='w', encoding='ANSI') as f1:
    f1.write(s.upper())