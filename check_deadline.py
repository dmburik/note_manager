from datetime import date

# вывод даты в обратной последовательности(День - Месяц - Год)
current_date=date.today()
date_for_print=current_date.strftime('%d-%m-%Y')
print ("Текущая дата : "+ date_for_print)
# запрос даты от пользователя с дальнейшей конвертацией
check_issue_date = input("введите дату дэдлайна в формате ДД-ММ-ГГГГ")
# конвертация полученной даты в формат date и запрос даты в случае не правильной даты
def check_date():
    check_issue_date2=check_issue_date
    local_issue_date=0
    while local_issue_date==0:
        try:
            local_issue_date=date(int(check_issue_date2[6:11]),int(check_issue_date2[3:5]),int(check_issue_date2[0:2]))
        except ValueError:
            try:
                local_issue_date=date(int(check_issue_date2[0:4]),int(check_issue_date2[5:7]),int(check_issue_date2[8:10]))
            except ValueError:
                print("не корректный формат даты / не существующая дата")
                check_issue_date2 = input("введите дату дэдлайна в формате ДД-ММ-ГГГГ")
    return local_issue_date
# блок для определения написания день/дня/дней
issue_date=check_date()
time_left=issue_date - current_date
string_time_left=str(time_left.days)
print(string_time_left)
def dni_dney():
    symbols=len(string_time_left)
    print(symbols)
    if string_time_left[symbols-1] == '1'and string_time_left[symbols-2] == "1":
        local_dni = "дней"
    elif (string_time_left[symbols-1] == '2' or string_time_left[symbols-1] == "3" or string_time_left[symbols-1] == "4"
          and string_time_left[symbols-2]!="1"):
        local_dni="дня"
    elif string_time_left[symbols-1] == "1" :
        local_dni="день"
    elif string_time_left[symbols-1] == "2" or string_time_left[symbols-1] == "3" or string_time_left[symbols-1] == "4":
        local_dni="дня"
    else:
        local_dni="дней"
    return local_dni
dni=dni_dney()
# вывод дэдлайн истек/до дэдлайна осталось
if int(string_time_left) > 0:
    print("до дэдлайна осталось " + string_time_left + " " + dni)
elif int(string_time_left) == 0:
    print("дэдлайн сегодня!!!")
else:
    print("внимание! Дэдлайн истек "+string_time_left + " " + dni + " назад")