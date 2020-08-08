import math
import argparse
import sys


# credit_principal = 'Credit principal: 1000'
# final_output = 'The credit has been repaid!'
# first_month = 'Month 1: paid out 250'
# second_month = 'Month 2: paid out 250'
# third_month = 'Month 3: paid out 500'
#
# # write your code here
#
# #  print(credit_principal)
# #  print(first_month)
# #  print(second_month)
# #  print(third_month)
# #  print(final_output)
#
# print('Enter the credit principal:')
# cp = int(input())
# print('What do you want to calculate?')
# print('type "m" - for count of months,')
# print('type "p - for monthly payments:')
# calc = input()
# if calc == 'm':
#     print('Enter monthly payment:')
#     payment = int(input())
#     months = cp / payment
#     if months == 1:
#         print('It takes 1 month to repay the credit')
#     else:
#         print('It takes '
#               + str(months)
#               + ' months to repay the credit')
# else:
#     print('Enter count of months:')
#     months = int(input())
#     if cp % months == 0:
#         payment = int(cp / months)
#         print('Your monthly payment = '
#               + str(payment))
#     else:
#         payment = int(cp/months + 1)
#         last_payment = cp - ((months - 1) * payment)
#         print('Your monthly payment = '
#               + str(payment)
#               + ' with last month payment = '
#               + str(last_payment))
#
# i = 0.01
#
#
# def main():
#     print('What do you want to calculate?')
#     print('type "n" - for count of months,')
#     print('type "a" - for annuity monthly payment,')
#     print('type "p" - for credit principal:')
#     calc = input()
#     if calc == 'n':
#         number_months()
#     elif calc == 'a':
#         payment()
#     elif calc == 'p':
#         credit_principal()
#     else:
#         main()
#         return
#
#
# def credit_principal():
#     payment = float(input('Enter monthly payment:'))
#     periods = float(input('Enter count of periods:'))
#     interest = float(input('Enter credit interest:')) / (12 * 100)
#     i_formula = (1 + interest) ** periods
#     p = math.ceil(payment / ((interest * i_formula) / (i_formula - 1)))
#     print(f'Your credit principal = {p}!')
#     return
#
#
# def number_months():
#     cp = float(input('Enter credit principal:'))
#     payment = float(input('Enter monthly payment:'))
#     interest = float(input('Enter credit interest:')) / (12 * 100)
#     n = math.ceil(math.log((payment / (payment - interest * cp)), 1 + interest))
#     years = math.floor(n / 12)
#     months = n % 12
#     if n == 1:
#         print(f'You need {months} month to repay this credit!')
#     elif n < 12:
#         print(f'You need {months} months to repay this credit!')
#     elif n == 12:
#         print(f'You need {years} year to repay this credit!')
#     elif n % 12 == 0:
#         print(f'You need {years} years to repay this credit!')
#     else:
#         print(f'You need {years} years and {months} months to repay this credit!')
#     return
#
#
# def payment():
#     cp = float(input('Enter credit principal:'))
#     periods = float(input('Enter count of periods:'))
#     interest = float(input('Enter credit interest:')) / (12 * 100)
#     i_formula = (1 + interest) ** periods
#     a = math.ceil(cp * ((interest * i_formula) / (i_formula - 1)))
#     print(f'Your annuity payment = {a}!')
#
# def differentiated_payment():
#
#
#
# main()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--type', type=str, help='annuity or diff.')
    parser.add_argument('--payment', type=int, help='refers to the monthly payment.')
    parser.add_argument('--principal', type=int, help='refers to the credit principal')
    parser.add_argument('--periods', type=int, help='refers to the number of months.')
    parser.add_argument('--interest', type=float, help='refers to the interest rate\
     without a percentage sign')
    args = parser.parse_args()

    if len(sys.argv) == 5 and negative([args.payment, args.principal, args.periods,
                                        args.interest]):
        if args.type == 'annuity':
            if args.payment is None:
                monthly_payment(args.principal, args.periods, args.interest)
            elif args.principal is None:
                credit_principal(args.payment, args.periods, args.interest)
            elif args.periods is None:
                number_of_months(args.principal, args.payment, args.interest)
            else:
                'Incorrect parameters'
        elif args.type == 'diff':
            differentiated_payment(args.principal, args.interest, args.periods)
        else:
            print('Incorrect parameters')
    else:
        print('Incorrect parameters')
    return


def monthly_payment(cp, periods, interest):
    i = nominal_interest(interest)
    i_formula = (1 + i) ** periods
    a = math.ceil(cp * ((i * i_formula) / (i_formula - 1)))
    print(f'Your annuity payment = {a}!')
    total = a * periods
    overpayment = total - cp
    print('\n' + f'Overpayment = {overpayment}')


def credit_principal(payment, periods, interest):
    i = nominal_interest(interest)
    i_formula = (1 + i) ** periods
    p = math.ceil(payment / ((i * i_formula) / (i_formula - 1)))
    print(f'Your credit principal = {p}!')
    total = payment * periods
    overpayment = total - p
    print('\n' + f'Overpayment = {overpayment}')


def number_of_months(cp, payment, interest):
    i = nominal_interest(interest)
    n = math.ceil(math.log((payment / (payment - i * cp)), 1 + i))
    years = math.floor(n / 12)
    months = n % 12
    if n == 1:
        print(f'You need {months} month to repay this credit!')
    elif n < 12:
        print(f'You need {months} months to repay this credit!')
    elif n == 12:
        print(f'You need {years} year to repay this credit!')
    elif n % 12 == 0:
        print(f'You need {years} years to repay this credit!')
    else:
        print(f'You need {years} years and {months} months to repay this credit!')
    total = payment * n
    overpayment = total - cp
    print('\n' + f'Overpayment = {overpayment}')


def differentiated_payment(cp, interest, periods):
    i = nominal_interest(interest)
    total = 0
    for current_period in range(1, periods + 1):
        payment = math.ceil((cp / periods) + i
                            * (cp - ((cp * (current_period - 1)) / periods)))
        print(f'Month {current_period}: paid out {payment}')
        total = total + payment
    overpayment = total - cp
    print('\n' + f'Overpayment = {overpayment}')


def nominal_interest(interest):
    i = interest / (12 * 100)
    return i


def negative(args):
    for argument in args:
        if argument is not None and argument < 0:
            return False
    return True


main()
