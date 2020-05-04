import os.path
import random
import datetime
# create list
list1 = []
list2 = []
list3 = []
list4 = []
# split data as len
with open('jug_words.txt', 'r') as f:
    for i in f.readlines():
        i = i.strip('\n')
        list1 += i
        print(i)
        if len(i) == 2:
            list2.append(i)
        if len(i) == 3:
            list3.append(i)
        if len(i) == 4:
            list4.append(i)
print(len(list2), "list2", list2)
print(len(list3), "list3", list3)
print(len(list4), "list4", list4)
# split list2
list21 = []
list22 = []
for i in list2:
    if i[0] in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']:
        list21.append(i)
    else:
        list22.append(i)
print(len(list21), "list21", list21)
print(len(list22), "list22", list22)
# split list3
list31 = []
list32 = []
list33 = []
list34 = []
list35 = []
for i in list3:
    if i[0] in ['a', 'b', 'c', 'd', 'e']:
        list31.append(i)
    elif i[0] in ['f', 'g', 'h', 'i', 'j']:
        list32.append(i)
    elif i[0] in ['k', 'l', 'm', 'n', 'o']:
        list33.append(i)
    elif i[0] in ['p', 'q', 'r', 's', 't']:
        list34.append(i)
    else:
        list35.append(i)
print(len(list31), "list31", list31)
print(len(list32), "list32", list32)
print(len(list33), "list33", list33)
print(len(list34), "list34", list34)
print(len(list35), "list35", list35)
# split list4
list41 = []
list42 = []
list43 = []
list44 = []
list45 = []
list46 = []
list47 = []
list48 = []
list49 = []
list410 = []
list411 = []
list412 = []
list413 = []
for i in list4:
    if i[0] in ['a', 'b']:
        list41.append(i)
    elif i[0] in ['c', 'd']:
        list42.append(i)
    elif i[0] in ['e', 'f']:
        list43.append(i)
    elif i[0] in ['g', 'h']:
        list44.append(i)
    elif i[0] in ['i', 'j']:
        list45.append(i)
    elif i[0] in ['k', 'l']:
        list46.append(i)
    elif i[0] in ['m', 'n']:
        list47.append(i)
    elif i[0] in ['o', 'p']:
        list48.append(i)
    elif i[0] in ['q', 'r']:
        list49.append(i)
    elif i[0] in ['s', 't']:
        list410.append(i)
    elif i[0] in ['u', 'v']:
        list411.append(i)
    elif i[0] in ['w', 'x']:
        list412.append(i)
    else:
        list413.append(i)
print(len(list41), "list41", list41)
print(len(list42), "list42", list42)
print(len(list43), "list43", list43)
print(len(list44), "list44", list44)
print(len(list45), "list45", list45)
print(len(list46), "list46", list46)
print(len(list47), "list47", list47)
print(len(list48), "list48", list48)
print(len(list49), "list49", list49)
print(len(list410), "list410", list410)
print(len(list411), "list411", list411)
print(len(list412), "list412", list412)
print(len(list413), "list413", list413)
# create data sturture
list2m = {'abcdefghijklm':list21,'nopqrstuvwxyz':list22}
list3m = {'abcde':list31, 'fghij':list32, 'klmno':list33, 'pqrst':list34, 'uvwxyz':list35}
list4m = {'ab':list41, 'cd':list42, 'ef':list43, 'gh':list44, 'ij':list45, 'kl':list46, 'mn':list47, 'op':list48, 'qr':list49, 'st':list410, 'uv':list411, 'wx':list412, 'yz':list413}
dict_main = {2: list2m, 3: list3m, 4: list4m}


totalscore =0
def scorcingsystem(w):
    score = 0
    if len(w) in (2,3):
        score = 1
    elif len(w) == 4:
        score = 2
    elif len(w) == 5:
        score = 4
    elif len(w) in (6,7):
        score = 5
    elif len(w) == 8:
        score = 8
    global totalscore
    totalscore += score
    return [score,totalscore]





def markshengsearchengine(word,letter):
    t1 = 0
    t2 = 0
    worldl = len(word)
    for i in dict_main:
        if i == worldl:
            for k in dict_main[i]:
                if word in dict_main[i][k]:
                    print(word,"exist in jug_word")
                    t1 = 1
    if t1 == 0:
        print("not exist in jug_word")
    for k in word:
        if k not in letter:
            t2 = 1
    if t2 == 1:
        print("not exist in letter")
    else:
        print("exist in letter")
    if t1 ==1 and t2 == 0:
        print("score add",scorcingsystem(word)[0])
    else:
        return False

list_az = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
letter = []
for i in range(8):
    n = random.randint(0,25)
    letter += list_az[n]
    letter = "yardyard"


def run_game():
    game = 0
    for k in range(3):
        if game >= 3:
            game_over()
            break
        print("round",str(k+1)*100,"letter=", letter)
        for i in range(5):
            if markshengsearchengine(input("enter word"),letter) == False:
                game += 1
            if game >= 3:
                break

def game_over():
    print("gameover,you total score is",totalscore)
    file_name = 'high_score.txt'
    with open(file_name, 'a') as file_obj:
        file_obj.writelines(str(datetime.datetime.now())+" totalscore "+str(totalscore)+"\n")

run_game()