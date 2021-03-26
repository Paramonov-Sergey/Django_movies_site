'''Учитывая строку str, переверните ее, опуская все неалфавитные символы.'''

def reverse_letter(string):
    k = ''.join([i for i in string[::-1] if i.isalpha()])
    return k
print(reverse_letter("ab23c"))