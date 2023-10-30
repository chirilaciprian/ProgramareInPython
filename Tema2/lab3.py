# Cate cuvinte contine fisierul 'intrare.txt', un cuvant este format doar din litere A-Z, a-z cu lungime cel putin 1
f = open("input.txt","r")
data = f.readlines()
cuvinte = []
for cuv in data:
    tmp = cuv.replace('\n','')
    if tmp.isalpha():
        cuvinte.append(tmp)
print(cuvinte,len(cuvinte))