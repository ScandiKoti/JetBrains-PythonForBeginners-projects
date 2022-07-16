import math
import argparse

parser = argparse.ArgumentParser(description="This program calculate differentiated payments and annuity payment.")
parser.add_argument("--type", choices=['diff', 'annuity'],
                    help="Calculation of differentiated payments or annuity payments.")
parser.add_argument("--interest", type=float,
                    help="Is specified without a percent sign, it must always be provided.")
parser.add_argument("--principal", type=int,
                    help="For differentiated payments you will need 4 parameters (excluding payment). \
                    For annuity payments user will be calculating the number of payments, the payment amount,\
                    or the loan principal.")
parser.add_argument("--payment", type=int)
parser.add_argument("--periods", type=int)
args = parser.parse_args()


def diff_month_payment(interest, principal, periods):
    payments = 0
    i = interest / (12 * 100)
    for m in range(1, periods + 1):
        result = math.ceil((principal / periods) + i * (principal - (principal * (m - 1) / periods)))
        print(f"Month {m}: payment is {result}")
        payments += result
    overpayment = payments - principal
    print(f"Overpayment = {overpayment}")
    return payments


calculation = [args.principal, args.payment, args.periods]

if args.type is None:
    print('Incorrect parameters')
elif args.interest is None or args.interest <= 0:
    print('Incorrect parameters')
elif args.type == 'diff':
    if args.principal is None or args.principal <= 0 or args.periods is None or args.periods <= 0:
        print('Incorrect parameters')
    else:
        diff_month_payment(args.interest, args.principal, args.periods)
elif args.type == 'annuity' and len(calculation) < 2:
    print('Incorrect parameters')

elif args.type == 'annuity':
    if args.principal == None and args.payment > 0 and args.periods > 0:
        i = args.interest / (12 * 100)
        loan_principal = math.ceil(args.payment / ((i * (1 + i) ** args.periods) / ((1 + i) ** args.periods - 1)))
        print(f'Your loan principal = {loan_principal}!')
        overpayment = (args.payment * args.periods) - loan_principal
        print(f"Overpayment = {overpayment}")
    elif args.payment == None and args.principal > 0 and args.periods > 0:
        i = args.interest / (12 * 100)
        annuity_payment = math.ceil(args.principal * ((i * (1 + i) ** args.periods)) / ((1 + i) ** args.periods - 1))
        print(f'Your monthly payment = {annuity_payment}!')
        overpayment = (annuity_payment * args.periods) - args.principal
        print(f"Overpayment = {overpayment}")
    elif args.periods == None and args.principal > 0 and args.payment > 0:
        i = args.interest / (12 * 100)
        x = args.payment / (args.payment - i * args.principal)
        base = 1 + i
        number_of_monthly = math.log(x, base)
        number_of_monthly_payment = math.ceil(number_of_monthly)
        if number_of_monthly_payment == 1:
            print('It will take 1 month to repay this loan!')
        elif number_of_monthly_payment < 12:
            print(f'It will take {number_of_monthly_payment} months to repay this loan!')
        elif number_of_monthly_payment % 12 == 0:
            if number_of_monthly_payment // 12 == 1:
                print('It will take 1 year to repay this loan!')
            else:
                print(f'It will take {number_of_monthly_payment // 12} years to repay this loan!')
        else:
            if number_of_monthly_payment // 12 == 1 and number_of_monthly_payment % 12 == 1:
                print(
                    f'It will take {number_of_monthly_payment // 12} year and {number_of_monthly_payment % 12}'
                    f'month to repay this loan!')
            elif number_of_monthly_payment // 12 == 1 and number_of_monthly_payment % 12 != 1:
                print(
                    f'It will take {number_of_monthly_payment // 12} year and {number_of_monthly_payment % 12} months to repay this loan!')
            elif number_of_monthly_payment // 12 != 1 and number_of_monthly_payment % 12 == 1:
                print(
                    f'It will take {number_of_monthly_payment // 12} years and {number_of_monthly_payment % 12} month to repay this loan!')
            else:
                print(
                    f'It will take {number_of_monthly_payment // 12} years and {number_of_monthly_payment % 12} months to repay this loan!')
        overpayment = (args.payment * number_of_monthly_payment) - args.principal
        print(f"Overpayment = {overpayment}")
    else:
        print('Incorrect parameters')
