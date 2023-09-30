# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, 
# если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  

str1 = input('Напишите стихотворение: ')
phrase_list = str1.split(' ')
dictionary = ['а', 'и', 'е', 'ё', 'о', 'у', 'ы', 'э', 'ю', 'я']
count_list = []
count = 0
for i in range(len(phrase_list)):
    for k in range(len(phrase_list[i])): 
        for j in range(len(dictionary)):
                if phrase_list[i][k] == dictionary[j]:
                        count =+ 1
        count_list.append(count)
        count = 0

count_list2 =[]
count2 = 0

for i in range(len(phrase_list)):
    count_list2.append(count_list[count2:(count2 + (len(phrase_list[i])))])
    count2 = count2 + len(phrase_list[i])

count_list3 = []
for i in range(len(count_list2)):
      count_list3.append(sum(count_list2[i]))

count3 = 0
for i in range(len(count_list3)):
      if count_list3[-1] == count_list3[i]:
            count3 += 1
if count3 == len(count_list3):
      print('Парам пам-пам')
else:
      print('Пам парам')
