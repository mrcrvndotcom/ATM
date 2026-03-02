RiveraBalance = 1000
RiveraIsActive = True

print("------------------------------")
print(" ATM ")
print("------------------------------")

while RiveraIsActive:
    print("--- MAIN MENU ---")
    print("1. View Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    RiveraChoice = input("Please select (1-4): ")

    if RiveraChoice == '1':
        print(f"Current Balance: ₱{RiveraBalance}")

    elif RiveraChoice == '2':
        RiveraDeposit = int(input("Enter amount to deposit: "))
        if RiveraDeposit <= 0:
            print("Error: Invalid Amount.")
        else:
            RiveraBalance = RiveraBalance + RiveraDeposit
            print(f"Success! ₱{RiveraDeposit} added.")

    elif RiveraChoice == '3':
        RiveraWithdraw = int(input("Enter amount to withdraw: "))
        if RiveraWithdraw <= 0:
            print("Error: Invalid Amount.")
        elif RiveraWithdraw < 20:
            print("Error: Minimum withdrawal amount is ₱20.")
        elif RiveraWithdraw > RiveraBalance:
            print("Error: Insufficient funds!")
        else:
            RiveraBalance = RiveraBalance - RiveraWithdraw
            print(f"Success! ₱{RiveraWithdraw} withdrawn.")

    elif RiveraChoice == '4':
        print("Thank you!")
        RiveraIsActive = False

    else:
        print("Invalid choice. Please try again.")