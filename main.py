import os
import random
os.system('cls')

list_ = ['염소', '염소', '스포츠카']
random.shuffle(list_)
sportscar_index = str(list_.index('스포츠카'))
print(list_)


print('montyhall in python 0/1/2')
number = str(input(">"))
print(type(number))



open_goat = ["0", "1" ,"2"]
if number == sportscar_index:
    open_goat.remove(number)
else:
    open_goat.remove(number)
    open_goat.remove(sportscar_index)
print(f'염소가 있는 방의 문은 {open_goat[0]}.')
choice = input('바꾸시겠습니까?y/n>')
if choice == 'y':
    change = ["0", "1", "2"]
    change.remove(number)
    change.remove(open_goat[0])
    final_choice = change[0]
else:
    final_choice = number

print(f'당신의 최종으로 선택한 문은 {final_choice}번 문입니다.')
print(f'{final_choice}문 뒤에는 {list_[int(final_choice)]} 이가 있었습니다.')
