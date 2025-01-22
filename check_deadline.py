from datetime import date

# вывод даты в обратной последовательности(День - Месяц - Год)
current_date=date.today()
date_for_print=current_date.strftime('%d-%m-%Y')
print ("Текущая дата : "+ date_for_print)
# запрос даты от пользователя с дальнейшей конвертацией
check_issue_date = input("введите дату дэдлайна в формате ДД-ММ-ГГГГ")
# конвертация полученной даты в формат date и запрос даты в случае не правильной даты
issue_date=0
while issue_date==0:
    try:
        issue_date=date(int(check_issue_date[6:11]),int(check_issue_date[3:5]),int(check_issue_date[0:2]))
    except ValueError:
        print("не корректный формат даты / не существующая дата")
        check_issue_date = input("введите дату дэдлайна в формате ДД-ММ-ГГГГ")
# блок для определения написания день/дня/дней
time_left=issue_date - current_date
string_time_left=str(time_left.days)
symbols=len(string_time_left)
if string_time_left[symbols-1]=='1':
    dni = "день"
elif string_time_left[symbols-1]=='2' or string_time_left[symbols-1]=="3" or string_time_left[symbols-1]=="4":
    dni="дня"
elif string_time_left[symbols-1]=="1" and string_time_left[symbols]!="1":
    dni="день"
elif (string_time_left[symbols-1]=="2" or string_time_left[symbols-1]=="3" or string_time_left[symbols-1]=="4"
      and string_time_left[symbols]!="1"):
    dni="дня"
else:
    dni="дней"
# вывод дэдлайн истек/до дэдлайна осталось
if int(string_time_left) > 0:
    print("до дэдлайна осталось " + string_time_left + " " + dni)
elif int(string_time_left) == 0:
    print("дэдлайн сегодня!!!")
else:
    print("внимание! Дэдлайн истек "+string_time_left + " " + dni + " назад")