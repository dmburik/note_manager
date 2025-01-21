from datetime import date, datetime

# вывод даты в обратной последовательности(День - Месяц - Год)
current_date=date.today()
print(current_date)
date_for_print=current_date.strftime('%d-%m-%Y')
print ("Текущая дата : "+ date_for_print)
# запрос даты от пользователя с дальнейшей конвертацией
check_issue_date = input("введите дату дэдлайна в формате ДД-ММ-ГГГГ")
check_year_date=check_issue_date
check_lenth_date=check_issue_date
answer_yes = ["y","yes","Y","YES","Yes","да","ДА","Д","д"]
answer_no = ["нет","н","НЕТ","Нет","Н","N","NO","n","No"]
first_check_done = False
jan=('январь',"января","янв","jan","january")
feb=('feb',"february","февраль","февраля","фев")
mar=("march","mar","март","мар","марта")
apr=("apr","april","апр","апрель","апреля")
may=("may","май","мая")
jun=("jun","june","июнь","июня","июн")
jul=("jul","july","июль","июля","июл")
aug=("aug","august","август","авг","августа")
sep=('sep',"september","сен","сент","сентябрь","сентября")
octo=('oct',"october","окт","октябрь","октября")
nov=("nov","november","ноя","нояб","ноябрь","ноября")
dec=("dec","december","дек","декабрь","декабря")
month=[jan,feb,mar,apr,may,jun,jul,aug,sep,octo,nov,dec]
days_count_checked=0
month_count=0
year_count=0
def find_sep():
    check_lenth_sep = check_issue_date
    for i in range(0, len(check_lenth_sep) - 1):
        # print("i"+str(i))
        sepa = [' ', ',', '.', '/', '-', ';', ':']
        if check_lenth_sep[i] in sepa:
            first_sep = i
            break
        else:
            i += 1

    for l in range(first_sep + 1, len(check_lenth_sep) - 1):
        # print("l"+str(l))
        sepa = [' ', ',', '.', '/', '-', ';', ':']
        if check_lenth_sep[l] in sepa:
            second_sep = l
            break
        else:
            l += 1
    return first_sep,second_sep
def check_days():
    #print(2)
    check_month_date=check_issue_date

    if    first_sep_glob ==1:
        while not check_month_date[0].isdigit():
            print("в дате могут быть только'-' и цифры")
            check_month_date = input("введите дату дэдлайна в формате ДД-ММ-ГГГГ")
            first_sep, second_sep = find_sep()
        day_count="0"+check_month_date[0]

    elif     first_sep_glob==2:
        while not check_month_date[0:1].isdigit():
            print("в дате могут быть только'-' и цифры")
            check_month_date = input("введите дату дэдлайна в формате ДД-ММ-ГГГГ")
            first_sep, second_sep = find_sep()
        day_count=check_month_date[0]+check_month_date[1]
    else:
        check_month_date=input("не корректо задана дата, введите дату дэдлайна в формате ДД-ММ-ГГГГ" )
    first_sep, second_sep = find_sep()
    return day_count, check_month_date,first_sep,second_sep
def check_days_in_month():
    inp_days=check_issue_date[0:first_sep_glob]
    inp_month=month_count
    days_in_month=[31,28,31,30,31,30,31,31,30,31,30,31]
    if days_in_month[int(month_count)-1]>=int(inp_days):
        issue_date=year_count+"-"+month_count+"-"+inp_days
    elif int(month_count)==2 and int(inp_days) == 29 and int(year_count)%4==0:
        issue_date = year_count + "-" + month_count + "-" + inp_days
    else:
        while int(inp_days)>int(days_in_month[int(month_count)-1]):

            print("в месяце"+str(inp_month)+" - "+str(days_in_month[int(month_count)-1])+"дней")
            inp_days=input("введите правильную дату в форматеДД")
            while not inp_days.isdigit():
                inp_days = input("введите правильную дату в форматеДД")
        issue_date = year_count + "-" + month_count + "-" + inp_days
    return inp_days,issue_date

def check_month():
    check_lenth_date=check_issue_date
    if second_sep_glob == 3 and first_sep_glob == 1:
        while not check_lenth_date[2].isdigit():
            print("в дате могут быть только'-' и цифры")
            check_lenth_date = input("введите дату дэдлайна в формате ДД-ММ-ГГГГ")
            find_sep()
        month_count = "0" + check_lenth_date[2]
    elif second_sep_glob == 4 and first_sep_glob == 1:
        if check_lenth_date[2:4].isdigit():
            tr = int(check_lenth_date[2:4]) <= 12
        else:
            tr = False
        while not check_lenth_date[2:4].isdigit() and tr:
            print("в дате могут быть только'-' и цифры, месяцы <=12")
            check_lenth_date = input("введите дату дэдлайна в формате ДД-ММ-ГГГГ")
            find_sep()
            if check_lenth_date[2:4].isdigit():
                tr = int(check_lenth_date[2:4]) <= 12
            else:
                tr = False
        month_count = check_lenth_date[2] + check_lenth_date[3]
    elif second_sep_glob == 4 and first_sep_glob == 2:
        while not check_lenth_date[3].isdigit():
            print("в дате могут быть только'-' и цифры")
            check_lenth_date = input("введите дату дэдлайна в формате ДД-ММ-ГГГГ")
            find_sep()
        month_count = "0" + check_lenth_date[3]
    elif second_sep_glob == 5 and first_sep_glob == 2:
        if check_lenth_date[3:5].isdigit():
            tr=int(check_lenth_date[3:5]) <= 12
        else:
            tr=False
        while not (check_lenth_date[3:5].isdigit() and tr):
            # данная проверка не нужна при отсутствии названий месяцев в 2 и менее символов
            #          for l in range(0, 12):
            #             if check_lenth_date[first_sep + 1: second_sep] in month[l][0:10]:
            #                month_count = "0" + str(l + 1)
            #               print(month_count)
            #              break
            #         else:
            #             l+=1
            #              if l==13:
            # при наличии названий в 2 символа следующие 2 строки уходят в блок else
            print("в дате могут быть только'-' и цифры, месяцы <=12")
            check_lenth_date = input("введите дату дэдлайна в формате ДД-ММ-ГГГГ")
            find_sep()
            if check_lenth_date[3:5].isdigit():
                tr = int(check_lenth_date[3:5]) <= 12
            else:
                tr = False
        month_count = check_lenth_date[3] + check_lenth_date[4]
    else:
        for l in range(0, 12):
            if check_lenth_date[first_sep_glob + 1: second_sep_glob] in month[l][0:10]:
                month_count = "0" + str(l + 1)
                break
            else:
                l += 1
                if l == 12:
                    print("не правильный формат даты")
                    print(check_lenth_date[first_sep_glob + 1:second_sep_glob])
    return month_count,check_lenth_date
def check_year():
    find_sep()
    check_year_date=check_issue_date
    while  not check_year_date[second_sep_glob+1:20].isdigit() :
        print("в дате могут быть только'-' и цифры")
        check_year_date=input("введите дату дэдлайна в формате ДД-ММ-ГГГГ")

    if int(check_year_date[second_sep_glob+1:20]) > 1991:
        year_check2 = check_year_date[second_sep_glob+1:20]
    elif 100 <= int(check_year_date[second_sep_glob+1:20]) <= 1991:
        yes_no_question = input(
            "ваш год меньше года создания python вы уверены что правильно указали год? введите Y/N")
        i = 0
        while i == 0:
            if yes_no_question in answer_yes:
                year_check2 = check_year_date[second_sep_glob+1:20]
                i += 1
            elif yes_no_question in answer_no:
                year_check2 = input("введите правильный год в формате ГГГГ")
                while int(year_check2) < 1991:
                    year_check2 = input("введите правильный год в формате ГГГГ")
                i += 1
            else:
                print("на вопрос можно ответь только 'Y'(да) или 'N'(нет)")
                while yes_no_question in answer_yes or yes_no_question in answer_no:
                    yes_no_question = input(
                        "ваш год меньше года создания python вы уверены что правильно указали год? введите Y/N")
    elif int(check_year_date[second_sep_glob+1:20]) < 100:
        yes_no_question = input(
            'вы ввели ' + check_year_date[second_sep_glob+1:20] + " , вы имели ввиду 20" +
            check_year_date[second_sep_glob+1:20] + '? Y/N')
        i = 0
        while i == 0:
            if yes_no_question in answer_yes:
                year_check2 = '20' + check_year_date[second_sep_glob+1:20]
                i += 1
                #print(yes_no_question)
            elif yes_no_question in answer_no:
                year_check2 = input("введите дату 4мя цифрами в формате ГГГГ")
                while int(year_check2) <= 1991:
                    yes_no_question_2 = input(
                        "ваш год меньше года создания python вы уверены что правильно указали год? введите Y/N")
                    n = 0
                    while n == 0:
                        if yes_no_question_2 in answer_yes:
                            year_check2 = check_year_date[second_sep_glob+1:20]
                            n += 1
                        elif yes_no_question_2 in answer_no:
                            year_check2 = input("введите правильный год в формате ГГГГ")
                            while int(year_check2) <= 1991:
                                year_check2 = input("введите правильный год в формате ГГГГ")
                            n += 1
                        else:
                            while yes_no_question_2 not in answer_yes and yes_no_question_2 not in answer_no:
                                print("на вопрос можно ответь только 'Y'(да) или 'N'(нет)")
                                yes_no_question_2 = input(
                                    "ваш год меньше года создания python вы уверены что правильно указали год? введите Y/N")
            else:
                 while yes_no_question not in answer_yes and yes_no_question not in answer_no:
                    print("на вопрос можно ответь только 'Y'(да) или 'N'(нет)")
                    yes_no_question = input(
                        'вы ввели ' + check_year_date[second_sep_glob+1:20] + " , вы имели ввиду 20" +
                        check_year_date[second_sep_glob+1:9] + '? Y/N')
            i+=1
    else:
        print("формат года введен не верно")
        year_check2=input("введите год 4мя цифрами в формате ГГГГ")
    check_year_date=check_year_date[0:second_sep_glob+1]+year_check2
    return year_check2,check_year_date
while  days_count_checked==0 or month_count==0 or year_count==0:
    first_sep_glob,second_sep_glob=find_sep()
    days_count,check_issue_date,first_sep_glob,second_sep_glob=check_days()
    first_sep_glob,second_sep_glob=find_sep()
    month_count,check_issue_date=check_month()
    year_count,check_issue_date=check_year()
    days_count_checked,check_issue_date=check_days_in_month()


print(check_issue_date)
time_left=date(int(year_count),int(month_count),int(days_count_checked)) - current_date
string_time_left=str(time_left.days)
symbols=len(string_time_left)
print(string_time_left)
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
if int(string_time_left) > 0:
    print("до дэдлайна осталось " + string_time_left + " " + dni)
else:
    print("внимание! Дэдлайн истек "+string_time_left + " " + dni + " назад")
print(time_left)
