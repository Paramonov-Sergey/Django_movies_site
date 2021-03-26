'''Ваша задача-написать функцию, которая увеличивает строку, чтобы создать новую строку.
Если строка уже заканчивается числом, то это число должно быть увеличено на 1.
 Если строка не заканчивается числом. число 1 должно быть добавлено к новой строке.'''


def func(stroka):
    if stroka.isalpha() or stroka == '':
        return stroka + '1'
    else:
        alpha =list(filter(str.isalpha,stroka))
        digits= list(filter(str.isdigit,stroka))
        if len(digits)==1 or digits[0]!='0':
            return ''.join(alpha) + str(int(''.join(digits))+1)

        i = len(digits) - 1
        if digits[i]!='9':
            digits[i]=str(int(digits[i])+1)
            return ''.join(alpha)+''.join(digits)
        else:
            while digits[i]=='9':
                digits[i]='0'
                i-=1
            digits[i]=str(int(digits[i])+1)
            return ''.join(alpha) + ''.join(digits)

print(func('hello001'))
print(func('some'))