import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def get_payment(n, pv, fv, r):
    r = r / 100
    month_r = r / 12

    pmt = (pv * month_r) / ( 1 - ( 1 / (1+month_r) ) ** n )

    return pmt

def get_payment_interest_sensitivity(n, pv, fv, min_r=0, max_r=10, grid=100, monthly_rent=None):

    r = np.linspace(min_r, max_r, grid)
    pmt = get_payment(n, pv, fv, r) 

    plt.plot(r, pmt)    
    if monthly_rent:
        plt.hlines(monthly_rent, xmin=min_r, xmax=max_r, color="r")
    plt.xlabel("Interest Rate (%)")
    plt.ylabel("Monthly Payment (w)")
    plt.show()

    return r, pmt

def main():

    mode = input("1. Parameter calibration\n2. Parameter sensitivity\nWhat mode do you want to use: ")

    if mode == "1":
        print(" \
        1. Number of payment\n \
        2. Present value\n \
        3. Future value\n \
        4. Interest rate(annually, in percentage)\n \
        5. Monthly payment")
    
        mode = input("What factor do you want to calculate:")
    
        n  = int(input("Number of payment: "))
        pv = float(input("Present value: "))
        fv = float(input("Future value: "))
        r  = float(input("Interest rate(annually, in percentage): "))
    
        pmt = get_payment(n, pv, fv, r)
        print(f"Monthly payment: {pmt}")
    
    elif mode == "2":
        n     = int(  input("Number of payment: "))
        pv    = float(input("Present value: "))
        fv    = float(input("Future value: "))
        min_r = float(input("Minimum interest rate: "))
        max_r = float(input("Maximum interest rate: "))
        grid  = int(  input("Grid numbers: "))

        r, pmt = get_payment_interest_sensitivity(n, pv, fv, min_r, max_r, grid)

if __name__ == "__main__":
    main()

