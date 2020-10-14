import csv
from Tests.MR import mr_check
from Tests.Ferma import f_check
from Tests.SH import sh_check
from Tests.Leman import l_check
import time

start = time.time()

ranges = {
    0: range(5, pow(2, 7), 2),
    1: range(pow(2, 7) + 1, pow(2, 12), 2),
    2: range(pow(2, 12) + 1, pow(2, 17), 2),
    3: range(pow(2, 17) + 1, pow(2, 20), 2),
    4: range(pow(2, 20) + 1, pow(2, 22), 2),
    5: range(pow(2, 22) + 1, pow(2, 24), 2),
    6: range(pow(2, 24) + 1, pow(2, 26), 2)}

rangess = {
    0: '0 - 2^7',
    1: '2^7 - 2^12',
    2: '2^12 - 2^15',
    3: '2^17 - 2^20',
    4: '2^20 - 2^22',
    5: '2^22 - 2^24',
    6: '2^24 - 2^26'}

data = [['Диапазон', 'Тест', 'Количество вероятно простых', "Время"], ]

mr_time, mr_p_c = mr_check(ranges)
for i in range(7):
    data.append([rangess.get(i), 'Тест Миллера-Рабина', mr_p_c[i], mr_time[i]], )
l_time, l_p_c = l_check(ranges)
for i in range(7):
    data.append([rangess.get(i), 'Тест Лемана', l_p_c[i], l_time[i]], )
f_time, f_p_c = f_check(ranges)
for i in range(7):
    data.append([rangess.get(i), 'Тест Ферма', f_p_c[i], f_time[i]], )
sh_time, sh_p_c = sh_check(ranges)
for i in range(7):
    data.append([rangess.get(i), 'Тест Соловея-Штрассе', sh_p_c[i], sh_time[i]], )

with open('result.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(data)

end = time.time()

print(end-start)