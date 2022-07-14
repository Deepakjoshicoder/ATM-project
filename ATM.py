pin = 2485
account_no = 20336

a = 0
while a<1:

	current_balance = [10000]

	check_pin = int(input('''
			Welcome To SBI Bank.
		Please Enter Your 4 Digit Pin!\n'''))

	if pin == check_pin:
		options = int(input('''		Welcome To SBI Bank.
	      Please Select Your Option.

	1. Cash Withdrawal
	2. Balance Inquery
	3. Cash Deposit
	\n'''))

		if options == 1:
			with_bal = int(input(''' Please Enter How Much Amount Would You Like To WithDraw.
			'''))
			ask  = input(f"Please Confirm ${with_bal} You Would Like To Withdraw! Press 'Y' For Confirm Else Press 'N'!\n")
			if ask == 'Y':
				if with_bal <= current_balance[0]:
					updated_bal = current_balance[0]-with_bal
					with_bal = '{:,}'.format(with_bal)
					upb = '{:,}'.format(updated_bal)
					current_balance.append(updated_bal)
					current_balance.pop(0)
					print(f'''	Transaction Successful!

			Cash Withdrew : Rs. {with_bal}
			Updated Balance :Rs. {upb}''')
				else:
					print("Transaction Declined!Not Enough Balance.")
			else:
				print("Thank You For Using SBI ATM.")
				break
		elif options == 2:
			for x in current_balance:
				a = x
			x = '{:,}'.format(a)
			print(f'''		Your Current Balance is :-
		Rs. {x}
			''')
		
		elif options == 3:
			ac_number = int(input("Please Enter Account Number :- \n"))
			if ac_number == account_no:
				am = int(input("Please Enter How Much Cash You Want to Deposit :- \n"))
				amu = '{:,}'.format(am)
				updated_bal = current_balance[0]+am
				upb = '{:,}'.format(updated_bal)
				current_balance.append(updated_bal)
				current_balance.pop(0)
				print(f'''		Transaction Successful!
			Cash Deposited : Rs. {amu}
			Total Balance : Rs. {upb}
				''')
		else:
			print("Invalid Option Selected.")
		
		ask = input("Press 'Y' If You Want to Continue Else Press 'N'")
		if ask == 'Y':
			continue
		else:
			print("Thank You For Using SBI ATM.")
			break
	else:
		print("Invalid Pin.")
		break