import random


""" Shows all available groups and lets the user view details of each group and choose one to join. """
def view_group():
    while True:
        print("\nPaluwagan Groups:") # Group 1-3
        print("1. Low Pay") 
        print("2. Mid Pay")
        print("3. Mid Pay but High Reward!")

        user_choice = input("\nUser Choice (Q to Back): ").lower()

        group_name = ""
        handler = ""
        members = []
        contribution = 0
        est_rate = None 
        interval = 0
        duration = 0
        safe = ""

        if user_choice in ["1", "low pay"]:
            group_name = "Russell Paylow"
            handler = "Russel Fellow"
            members = ["Russell", "Felix", "Otto", "Belomont", "Marcos",
                       "Rachins", "Helaine", "Julius", "Kiritaka"]
            contribution = 100
            interval = 7
            duration = 70
            safe = "Safe!"

        elif user_choice in ["2", "mid pay"]:
            group_name = "Hoshin Pay"
            handler = "Anastasia Hoshin"
            members = ["Hoshin", "Subaru", "Crusch", "Emilia",
                       "Reinhard", "Priscilla", "Aldebaran"]
            contribution = 250
            interval = 7
            duration = 56
            safe = "Safe!"

        elif user_choice in ["3", "mid pay but high reward"]:
            group_name = "Roswaal Credit Association (ROSCA)"
            handler = "Roswaal Mathers"
            members = ["Roswaal", "Rem", "Clind", "Ram", "Echidna"]
            contribution = 500
            est_rate = 30
            interval = 7
            duration = 42
            safe = "High Risk High Reward!"

        elif user_choice in ["q", "quit"]:
            return

        else:
            print(f"Invalid Choice: '{user_choice}'")
            continue

        # Display group info
        print("\n--- GROUP INFO ---")
        print(f"Group: {group_name}")
        print(f"Handler: {handler}")
        print(f"Members: {len(members)}")

        for m in members:
            print(f"- {m}")

        print(f"Contribution: PHP {contribution}")

        if est_rate is not None:
            print(f"Interest Rate: {est_rate}%")

        print(f"Interval: {interval} Days")
        print(f"Duration: {duration} Days")
        print(f"Status: {safe}")

        while True:
            join = input(f'\nJoin "{group_name}" group? (y/n): ').lower()

            if join in ["y", "yes"]:
                while True:
                    user_fullname = input("Fullname: ").title()

                    if user_fullname == "" or user_fullname == " ":
                        print("Invalid Input, Name shouldnt be empty")
                        continue

                    # DATE VALIDATION ADDED HERE
                    while True:
                        join_date = input("Date of joining (MM/DD/YYYY): ")

                        if len(join_date) != 10:
                            print("Invalid format. Use MM/DD/YYYY")
                            continue

                        if join_date[2] != "/" or join_date[5] != "/":
                            print("Invalid format. Use MM/DD/YYYY")
                            continue

                        mm = join_date[0:2]
                        dd = join_date[3:5]
                        yyyy = join_date[6:10]

                        # SIMPLE DIGIT CHECK
                        valid_chars = "0123456789"
                        valid = True

                        for i in mm:
                            if i not in valid_chars:
                                valid = False

                        for i in dd:
                            if i not in valid_chars:
                                valid = False

                        for i in yyyy:
                            if i not in valid_chars:
                                valid = False

                        if valid == False:
                            print("Invalid input. Numbers only allowed.")
                            continue

                        break

                    print(f"\nWelcome to {group_name}!")

                    return (group_name, handler, est_rate, members,
                            contribution, interval, duration,
                            user_fullname, join_date)

            elif join in ["n", "no"]:
                break

            else:
                print(f"Invalid Choice: '{join}'")


""" Asks the user if they contributed on the scheduled day. 
Returns: 1 if payment was made, 0 if missed. """
def contribution_day():
    while True:
        pay = input("Did you contribute? (y/n): ").lower()

        if pay in ["y", "yes"]:
            print("Payment Recorded!")
            return 1

        elif pay in ["n", "no"]:
            print("Missed Payment Recorded!")
            return 0

        else:
            print(f"Invalid input: '{pay}'")


""" Simulates a standard paluwagan group with fixed contributions. """
def low_mid_simulation(group_name, handler, members,
                       contribution, interval, duration,
                       user_fullname, join_date):

    members = members.copy()
    members.append(user_fullname)
    random.shuffle(members)

    print("\n--- PAYOUT ORDER ---")
    for i, m in enumerate(members):
        print(f"{i + 1}. {m}")

    base_payout = contribution * len(members)
    penalty_rate = contribution * 0.30

    missed = 0
    penalty_total = 0
    user_received_payout = False

    day = 1

    while day <= duration:

        if day % interval == 0:

            print(f"\nDay {day} - Contribution Day!")
            result = contribution_day()

            if result == 0:
                missed += 1
                penalty_total += penalty_rate

            round_num = day // interval

            if round_num <= len(members):

                receiver = members[round_num - 1]

                if receiver == user_fullname:
                    current_payout = base_payout - penalty_total
                    print(f"{receiver} received PHP {current_payout:.2f}")
                    user_received_payout = True

                else:
                    print(f"{receiver} received PHP {base_payout:.2f}")

        day += 1

    if user_received_payout:

        final_payout = base_payout - penalty_total

        print("\nYOU RECEIVED YOUR PAYOUT!")
        print(f"Missed Payments: {missed}")
        print(f"Total Deduction: PHP {penalty_total:.2f}")
        print(f"Final Payout: PHP {final_payout:.2f}")

        save_history(group_name, handler, user_fullname,
                     join_date, final_payout)


def scam_group(group_name, est_rate, members,
               contribution, interval, duration,
               user_fullname, join_date):

    members = members.copy()
    members.append(user_fullname)

    print("\n--- PAYOUT ORDER ---")
    for i, m in enumerate(members):
        print(f"{i + 1}. {m}")

    day = 1
    round_num = 0
    miss_count = 0
    status = "SAFE"

    interest = est_rate / 100
    base_pool = contribution * len(members)
    payout = base_pool + (base_pool * interest)

    while day <= duration:

        if day % interval == 0:
            round_num += 1
            print(f"\nDay {day} - Contribution Day!")

            while True:
                pay = input("Did you contribute? (y/n): ").lower()

                if pay in ["y", "yes"]:
                    print("Payment Recorded!")
                    break

                elif pay in ["n", "no"]:
                    miss_count += 1
                    print("Warning! Missing payment recorded")

                    if miss_count >= 10:
                        status = "KICKED OUT"
                        print("\nYOU GOT KICKED OUT")
                        save_scam_history(group_name, user_fullname, join_date, status)
                        return

                else:
                    print(f"Invalid input: '{pay}'")

            if round_num <= len(members):
                receiver = members[round_num - 1]

                if receiver == user_fullname:
                    print(".....")
                    status = "SCAMMED"
                    print("YOU WERE REMOVED BEFORE PAYOUT")
                    save_scam_history(group_name, user_fullname, join_date, status)
                    return

                print(f"{receiver} received PHP {payout:.2f}")

        day += 1

    save_scam_history(group_name, user_fullname, join_date, status)


def save_history(group_name, handler, user_fullname, join_date, payout):
    file = open("transaction_history.txt", "a")
    file.write("\n--- TRANSACTION HISTORY ---\n")
    file.write(f"Group Name: {group_name}\n")
    file.write(f"Handler: {handler}\n")
    file.write(f"Fullname: {user_fullname}\n")
    file.write(f"Join Date: {join_date}\n")
    file.write(f"Payout: PHP {payout:.2f}\n")
    file.close()


def save_scam_history(group_name, user_fullname, join_date, status):
    file = open("transaction_history.txt", "a")
    file.write("\n--- TRANSACTION HISTORY ---\n")
    file.write(f"Group Name: {group_name}\n")
    file.write("Handler: ?\n")
    file.write(f"Fullname: {user_fullname}\n")
    file.write(f"Join Date: {join_date}\n")
    file.write(f"Status: {status}\n")
    file.write("Payout: ?\n")
    file.close()


def main():
    while True:

        print("\n1. View Groups")
        print("2. Quit")

        choice = input("Choice: ")

        if choice == "1":
            result = view_group()

            if result:
                (group_name, handler, est_rate, members,
                 contribution, interval, duration,
                 user_fullname, join_date) = result

                if contribution < 500:
                    low_mid_simulation(group_name, handler,
                                       members, contribution, interval,
                                       duration, user_fullname, join_date)

                else:
                    scam_group(group_name, est_rate, members,
                               contribution, interval, duration,
                               user_fullname, join_date)

        elif choice == "2":
            print("Bye!")
            break

        else:
            print("Invalid Choice")


main()