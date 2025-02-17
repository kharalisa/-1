#Вариант 31.
Целые восьмеричные числа, начинающиеся с нечетных цифр и не превышающие 5 цифр. Четные цифры выводить словами.

slovar = {
    '0': 'ноль',
    '2': 'два',
    '4': 'четыре',
    '6': 'шесть'
}

def octal(c): 
    return c in '01234567'

def chet(c): 
    return c in '1357'

def replace_num(num): 
    a = [] 
    for d in num: 
        if d in slovar:
            a.append(slovar[d]) 
        else:
            a.append(d)
    return ' '.join(a) 

def read_file(file, size=1024): 
    with open(file, 'r') as f: 
        data = '' 
        while True: 
            block = f.read(size)
            if not block: 
                break
            data += block 
            while ' ' in data: 
                pos = data.index(' ') 
                leksema = data[:pos] 
                data = data[pos+1:]
                if len(leksema) <= 5 and all(octal(c) for c in leksema) and chet(leksema[0]):
                    print(replace_num(leksema))

read_file('numbers.txt')
    
    

