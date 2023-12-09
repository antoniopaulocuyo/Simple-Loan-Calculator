import math
import argparse
import sys


def command_line_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--payment", default=False, type=int)
    parser.add_argument("--principal", default=False, type=float)
    parser.add_argument("--periods", default=False, type=int)
    parser.add_argument("--type", default=False)
    parser.add_argument("--interest", default=False, type=float)

    args = parser.parse_args()

    payment, principal, periods, interest = args.payment, args.principal, args.periods, args.interest
    pay_type = args.type

    interest = interest / (12 * 100)
    return payment, principal, periods, interest, pay_type


def condition(payment, principal, periods, interest, pay_type):
    loan_options = ["diff", "annuity"]

    # Conditions
    if len(sys.argv) != 5:
        return "Incorrect parameters"
    if not pay_type:
        return "Incorrect parameters"
    elif pay_type not in loan_options:
        return "Incorrect parameters"
    elif pay_type == "diff" and (principal and payment):
        return "Incorrect parameters"

    if not interest or interest < 0:
        return "Incorrect parameters"
    elif principal < 0:
        return "Incorrect parameters"
    elif payment < 0:
        return "Incorrect parameters"
    elif payment < 0:
        return "Incorrect parameters"
    elif periods < 0:
        return "Incorrect parameters"
    else:
        return 0


def annual_payment_calculation(principal, periods, interest):
    interest_growth = math.pow(1 + interest, periods)
    return math.ceil(principal * ((interest * interest_growth) / (interest_growth - 1)))


def annual_principal_calculation(payment, periods, interest):
    interest_growth = math.pow(1 + interest, periods)
    return math.ceil(payment/((interest * interest_growth)/(interest_growth - 1)))


def annual_period_calculation(principal, payment, interest):
    return math.ceil(math.log(payment/(payment - (interest * principal)), 1 + interest))


def annuity_payments(payment, principal, periods, interest):
    return_list = []

    if not payment:
        payment = annual_payment_calculation(principal, periods, interest)
        return_list.append(f"Your monthly payment = {payment}!")
        return_list.append(f"Overpayment = {math.ceil(payment * periods - principal)}")
        return return_list
    elif not principal:
        principal = annual_principal_calculation(payment, periods, interest)
        return_list.append(f"Your loan principal = {math.ceil(principal)}!")
        return_list.append(f"Overpayment = {math.ceil(payment * periods - principal)}")
        return return_list
    elif not periods:
        periods = math.ceil(annual_period_calculation(principal, payment, interest))
        if periods < 12:
            return_list.append(f"It will take {periods} months to repay this loan!")
            return_list.append(f"Overpayment = {math.ceil(payment * periods - principal)}")
            return return_list
        elif math.ceil(periods % 12) == 0:
            years = math.ceil(periods // 12)
            return_list.append(f"It will take {years} years to repay this loan!")
            return_list.append(f"Overpayment = {math.ceil(payment * periods - principal)}")
            return return_list
        else:
            years = periods // 12
            months = math.ceil(periods % 12)
            return_list.append(f"It will take {years} years and {months} months to repay this loan!")
            return_list.append(f"Overpayment = {math.ceil(payment * periods - principal)}")
            return return_list


def diff_equation(current_month, period, principal):
    return (principal * (current_month - 1)) / period


def differential_payments(principal, periods, interest):
    over_payment = 0
    return_list = []

    for months in range(periods):
        current_month = months + 1
        diff_payment = math.ceil((principal / periods) + interest * (principal - diff_equation(current_month, periods,
                                                                                               principal)))
        return_list.append(f"Month {current_month}: payment is {diff_payment}")
        over_payment += diff_payment
    return_list.append("")
    return_list.append(f"Overpayment = {int(over_payment - principal)}")
    return return_list


def main():
    payment, principal, periods, interest, payment_type = command_line_arguments()

    if condition(payment, principal, periods, interest, payment_type):
        print("Incorrect parameters")
    else:
        if payment_type == "annuity":
            for month in annuity_payments(payment, principal, periods, interest):
                print(month)
        else:
            for month in differential_payments(principal, periods, interest):
                print(month)


if __name__ == "__main__":
    main()
