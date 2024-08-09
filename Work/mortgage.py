# mortgage.py
#
# Exercise 1.7
# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
total_month = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    payment_for_this_month = payment 
    if  extra_payment_start_month <= total_month <= extra_payment_end_month: 
        payment_for_this_month = payment + extra_payment
    
    if payment_for_this_month > principal * ( 1 + rate/12) :
        payment_for_this_month = principal * ( 1 + rate/12)

    principal = principal * (1+rate/12) - payment_for_this_month
    total_paid = total_paid + payment_for_this_month

    total_month += 1
    
    print(f'{total_month:3d} {total_paid:10.2f} {principal:10.2f}')

print('Total paid', round(total_paid, 2))
print('Months', total_month)
