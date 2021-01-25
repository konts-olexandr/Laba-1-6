from collections import Counter
txt = 'текст хелоу воролд<. /буквы три текст'
word_list = []
var_select= input('1 Підрахувати кількість слів\n2 Підрахувати кількість букв')
while var_select =='1':

 for word in txt.split():
    clear_word = ''
    for letter in word:
        if letter.isalpha():
            clear_word+=letter.lower()
    word_list.append(clear_word)
    a=(Counter(word_list))
    print(a)
 break
while var_select =='2':
    t = 'Абв гіфвфаа'
    t = t.lower()
    t = t.replace(' ', '')
    c = Counter(t)
    for letter, count in sorted(c.items()):
        print('{letter}: {count}'.format(letter=letter, count=count))
    break





