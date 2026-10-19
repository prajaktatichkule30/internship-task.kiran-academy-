import random

while True:
    print("\n===== CAB BOOKING CHATBOT =====")
    print("1. Book Ride")
    print("2. Exit")

    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == "1":

        print("\n===== SELECT CAB TYPE =====")
        print("1. Auto - Rs.12/km")
        print("2. Sedan - Rs.18/km")
        print("3. SUV - Rs.25/km")

        cab_choice = input("Select cab (1-3): ").strip()

        if cab_choice == "1":
            cab = "Auto"
            rate = 12
        elif cab_choice == "2":
            cab = "Sedan"
            rate = 18
        elif cab_choice == "3":
            cab = "SUV"
            rate = 25
        else:
            print("Invalid cab choice! Please select 1, 2, or 3.")
            continue

        print("\n===== SELECT ROUTE =====")
        print("1. Pune Station to Shivajinagar - 5 km")
        print("2. Swargate to Kothrud - 8 km")
        print("3. Hinjawadi to Wakad - 10 km")

        route_choice = input("Select route (1-3): ").strip()

        if route_choice == "1":
            source = "Pune Station"
            destination = "Shivajinagar"
            distance = 5
        elif route_choice == "2":
            source = "Swargate"
            destination = "Kothrud"
            distance = 8
        elif route_choice == "3":
            source = "Hinjawadi"
            destination = "Wakad"
            distance = 10
        else:
            print("Invalid route choice! Please select 1, 2, or 3.")
            continue

        fare = rate * distance

        print("\n===== RIDE DETAILS =====")
        print("Cab Type:", cab)
        print("Source:", source)
        print("Destination:", destination)
        print("Distance:", distance, "km")
        print("Rate per km: Rs.", rate)
        print("Total Fare: Rs.", fare)

        print("\n1. Confirm & Share OTP")
        print("2. Cancel Ride")

        confirm = input("Enter your choice (1 or 2): ").strip()

        if confirm == "1":
            otp = random.randint(1000, 9999)
            print("\nYour OTP is:", otp)
            print("Booking Confirmed Successfully!")
            print("Ride cannot be cancelled after OTP sharing.")

        elif confirm == "2":
            print("\nRide cancelled successfully!")
            print("OTP has not been shared.")

        else:
            print("Invalid choice! Please run the booking again.")

    elif choice == "2":
        print("\nThank you for using our Cab Booking Chatbot!")
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please enter 1 or 2.")