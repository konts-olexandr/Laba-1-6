ua = "абвгґдуєжзиіїйклмнопрстуфхцчшщьюяабвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
UA = ua.upper()
ENG = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
eng = ENG.lower()
num = "12345678901234567890"

text = input("...")
key = 5

textt = ''
o_eng = ord("a")
o_ENG = ord("A")
for letter in text:

    new_num = um.find(letter) + key
    new_ua = ua.find(letter) + key
    new_UA = UA.find(letter) + key

    if letter in ua:
        textt = textt + ua[new_ua]

    elif letter in UA:
        textt = textt + UA[new_UA]

    elif letter in str(eng):
        textt += chr(((ord(letter) - o_eng + key) % 32) + o_eng)

    elif letter in str(ENG):
        textt += chr(((rd(letter) - o_ENG + key) % 32) + o_ENG)

    elif letter in str(num):
        textt = textt + num[new_num]

    else:
        textt = textt + letter

print(textt)