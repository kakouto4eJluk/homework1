'''
Реализовать функцию int_func(), принимающую слово из маленьких
латинских букв и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать
строка из слов, разделенных пробелом. Каждое слово состоит
из латинских букв в нижнем регистре. Сделать вывод исходной
строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
'''
def int_func (*args):
    word = input('Введите слова: ')
    print(word.title())
    return

int_func()

def my_func (*args):
    line = input('Введите слова: ')
    words = line.split()
    n = 0
    new_list = list()

    while n < len(words):
        words_str = list(words[n])
        new_word = chr(ord(words_str[0]) - 32)
        words_str.pop(0)
        words_str.insert(0, new_word)
        words_str.append(' ')
        new_list += words_str
        n += 1

    my_str = ''.join(new_list)

    print(my_str)


my_func()