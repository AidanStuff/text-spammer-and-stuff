#by Aidan 2021 08 Apr 2021 V1
import random, string

amount = int(input(' how many lines of text: '))
value = 1
while value <= amount:
    code = "lol" + ('').join(random.choices(string.ascii_letters + string.digits, k=16))
    f = open('spam.txt', "a+")
    f.write(f'{code}\n')
    f.close()
    print(f'[new line spamed] {code}')
    value += 1
