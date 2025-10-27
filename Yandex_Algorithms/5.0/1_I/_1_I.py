N = int(input())

year = int(input())

day = []
month = []

day_month = []
for i in range(N):
    s1, s2 = input().split()
    day.append(s1)

    month.append(s2)

    day_month.append([int(s1),s2])

day_of_week = input()

MonthYear = {'January' : 31, 
             'February':28, 
             'March':31,
             'April':30,
             'May':31,
             'June':30,
             'July':31,
             'August':31,
             'September':30,
             'October':31,
             'November' :30,
             'December' : 31}

DayMonth = {'Monday':1,
            'Tuesday':2,
            'Wednesday':3,
            'Thursday':4,
            'Friday':5,
            'Saturday':6,
            'Sunday':7}

count_days = 365

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    MonthYear['February'] +=1
    count_days+=1

for i in DayMonth.keys():
    if day_of_week == i:
        number_first_day = DayMonth[i]
    #DayMonth[i] = 0

a = 8*[0]

b = 8*[0]
now = 1
n = number_first_day

numb_days = 0
numb_month = 0


the_days = 0

the_days_in_month = 1
keys = list(MonthYear.keys())
#print(keys)

now_month = keys[numb_month]
while now <= count_days:

    #a[n]+=1
    #n+=1
    #if n > 7:
    #    n = 1


    #now+=1

    if now>the_days:

        now_month = keys[numb_month]

        the_days +=MonthYear[now_month]

        numb_month +=1

        the_days_in_month = 1

        #print(the_days, numb_month)

    #now+=1

    #the_days_in_month +=1

    #print([the_days_in_month, now_month], n)
    if [the_days_in_month, now_month] in day_month:
        b[n] += 1

    now+=1

    the_days_in_month +=1

    a[n]+=1

    n+=1
    if n > 7:
        n = 1

a_b = 7*[0]
for i in range(1,len(a)):
    a_b[i-1] = a[i] - b[i]

#print(a_b)

max_value = max(a_b)
max_index = a_b.index(max_value)
 
min_value = min(a_b)
min_index = a_b.index(min_value)

for i in DayMonth.keys():
    if min_index+1 == DayMonth[i]:
        min_day = i

    if max_index+1 == DayMonth[i]:
        max_day = i

print(max_day,min_day)

#print(min_index) 
#print(day_month)
#print('a',a)
#print(number_first_day)
#print(DayMonth)
#print('b',b)
