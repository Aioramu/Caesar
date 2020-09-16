import random,re,string
a=open("tom.txt","r")
tom=list(a.read())

a.close()

lang=[c for c in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя']
#LANG=[c for c in 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ']
key=random.randint(0,32)
a=0
for i in tom:
    if i in lang:
        tom[a]=lang[lang.index(i)+key]
    #elif i in LANG:
    #    tom[a]=LANG[LANG.index(i)+key]
    #a=a+1
tom=''.join(tom)
with open('enc.txt','w') as file_oject:
    file_oject.write(tom)
#прочитать весь новый файл,узнать сколько в нём БУКВ,далее поиск всех букв и составление частот в словарь.проделать тоже самое со всей ВиМ.
hz={'а':0,'б':0,'в':0,'г':0,'д':0,'е':0,'ё':0,'ж':0,'з':0,'и':0,'й':0,'к':0,'л':0,'м':0,'н':0,'о':0,'п':0,'р':0,'с':0,'т':0,'у':0,'ф':0,'х':0,'ц':0,'ч':0,'ш':0,'щ':0,'ъ':0,'ы':0,'ь':0,'э':0,'ю':0,'я':0}
hz1={'а':0,'б':0,'в':0,'г':0,'д':0,'е':0,'ё':0,'ж':0,'з':0,'и':0,'й':0,'к':0,'л':0,'м':0,'н':0,'о':0,'п':0,'р':0,'с':0,'т':0,'у':0,'ф':0,'х':0,'ц':0,'ч':0,'ш':0,'щ':0,'ъ':0,'ы':0,'ь':0,'э':0,'ю':0,'я':0}

b=open("voina-i-mir.txt")
book=list(b.read())
b.close()
def count(book):
    count=0
    for word in book:
        if word in hz.keys():
            count+=1
    return(count)
allw=count(book)
def similar(book,hz,allw):
    for i in hz.keys():
        count=0
        for word in book:
            if i==word:
                count+=1
                hz[word]=count/allw
    return(hz)
fullb=similar(book,hz,allw)#table of hz of full book
c=open("enc.txt","r")
tom=list(c.read())#Enrypted chapter
c.close()

allw=count(tom)

chapter=similar(tom,hz1,allw)#table of hz of one encryted chapter
#print("тaблица частот всей книги:",fullb,'\n',"Tаблица частот главы",chapter)
list_c = list(chapter.items())
list_c.sort(key=lambda i: i[1])
dict_numbers = {}
for i in list_c:
    dict_numbers[i[0]] = i[1]

list_b = list(fullb.items())
list_b.sort(key=lambda i: i[1])
dict_full = {}
for i in list_b:
    dict_full[i[0]] = i[1]
a=[]
for n in dict_full.keys():
    a.append(n)
print()
#print(dict_full,'\n',a,'\n',dict_numbers)
tom=''.join(tom)
count=0
for i in dict_numbers.keys():
    print(i,a[count],type(i),type(a[count]))
    tom=tom.replace(str(i),str(a[count]))
    count+=1
print(tom)
