card_no = '5610591081018250'
odd_sum = 0
even_sum = 0
double_list= []
number= list(card_no)

for (idx,val) in enumerate(number):
    if idx%2 == 1:
        odd_sum += int(val)
    else:
        double_list.append(int(val)*2)
    
double_string = ''
for x in double_list:
    double_string += str(x)

double_list = list(double_string)

for x in double_list:
    even_sum += int(x)

total_sum = odd_sum + even_sum

if total_sum % 10 == 0:
    print('Valid card!')
else:
    print('Invalid card!')
