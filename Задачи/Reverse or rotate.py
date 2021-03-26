'''Входные данные-это строка str из цифр. Разрежьте строку на куски (кусок здесь-это подстрока исходной строки) размера sz (игнорируйте последний кусок, если его размер меньше sz).

Если кусок представляет собой целое число, например сумма кубов его цифр делится на 2, переверните этот кусок; в противном случае поверните его влево на одну позицию. Соберите эти измененные фрагменты и верните результат в виде строки.

Если sz является <= 0 или если str является empty Возврат ""

sz больше (>) чем длина str нельзя взять кусок размером sz отсюда и возвращение"".'''

def revrot(string,sz):
    if not string or sz<=0 or sz>len(string):
        return ""
    else:
        i=sz
        spisok=[]
        k=0
        while k<len(string):
            new=[int(i) for i in string[k:i]]
            if len(new)==sz:
                if sum(new)%2!=0:
                    new.pop(0)
                    new.append(int(string[k]))
                    spisok.append(''.join([str(i) for i in new]))
                else:
                    spisok.append(''.join([str(i) for i in new])[::-1])
            k+=sz
            i+=sz
        return ''.join(spisok)




print(revrot("563000655734469485", 4))
print(revrot("123456987654", 6))
print(revrot("123456987653", 6) )
print(revrot("66443875", 4))
print(revrot("66443875", 8))
print(revrot("664438769", 8))
print(revrot("123456779", 8))
print(revrot("", 8))
print(revrot("123456779", 0))
print(revrot("563000655734469485", 4))