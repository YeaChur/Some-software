import pyautogui
import time

time.sleep(3)

zfc_num_end = 0
zfc_num_begin = 0
ls = []
# 以列表形式保存按键
with open('yuanshi_musictxt/未闻花名.txt','r',encoding='utf-8') as rfile:
    for i in rfile.readlines():
        if i != '':
            ls.append(i.strip("\n"))
rfile.close()
TiME = float(ls[0])
ls.pop(0)
for j in ls:
    ls_j = list(map(str,j.strip()))
    ls_j.append(' ')
    ls_j_ls = []
    if ls_j != []:
        while True:
            zfc_num_end = ls_j.index(' ')
            if zfc_num_end != len(ls_j)-1:
                ls_j_ls.append(ls_j[0:zfc_num_end])
                zfc_num_begin = zfc_num_end + 1
                ls_j = ls_j[zfc_num_begin:len(ls_j)]
            else:
                ls_j_ls.append(ls_j[0:zfc_num_end])
                break
    else:
        continue
    for k in ls_j_ls:
        if '(' in k:
            num_index_begin = k.index('(')
            num_index_end = k.index(')')
            if num_index_begin == 0 and num_index_end == len(k) - 1:
                k.remove('(')
                k.remove(')')
                pyautogui.press(k)
                time.sleep(TiME)
            else:
                if num_index_begin == 0:
                    pyautogui.press(k[num_index_begin+1:num_index_end])
                    time.sleep(TiME/2)
                    for new_i in k[num_index_end+1:len(k)]:
                        pyautogui.keyDown(new_i)
                        time.sleep(TiME/2)
                        pyautogui.keyUp(new_i)
                if num_index_begin !=0:
                    for new_i2 in k[0:num_index_begin]:
                        pyautogui.keyDown(new_i2)
                        time.sleep(TiME/2)
                        pyautogui.keyUp(new_i2)
                    pyautogui.press(k[num_index_begin+1:num_index_end])
                    time.sleep(TiME/2)
            # pyautogui.keyDown(k)
            # time.sleep(TiME)
            # pyautogui.keyUp(k)
        else:
            if k == []:
                continue
            num_time = TiME/len(k)
            for ii in k:
                pyautogui.keyDown(ii)
                time.sleep(num_time)
                pyautogui.keyUp(ii)



