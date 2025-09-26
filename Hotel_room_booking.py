# Hotel Room Booking system

# Dictionary to stroe room status
rooms = {
    101: "Available",
    102: "Available",
    103: "Available",
    104: "Available",
    105: "Available",
    201: "Available",
    202: "Available",
    203: "Available",
    204: "Available",
    205: "Available",
    301: "Available",
    302: "Available",
    303: "Available",
    304: "Available",
    305: "Available",
}
# Function to display all rooms
def show_room():
    print("\nRoom Number : Status")
    for room,status in rooms.items():
        print(f"{room} : {status}")

# Function to book a room
def book_room():
    room_number = int(input("Enter room number to book: "))
    if room_number in rooms:
        if rooms[room_number] == "Available":
            rooms[room_number] = "Booked"
            print(f"Room {room_number} has been booked successfully!")
        else:
            print(f"Room {room_number} is already booked.")
    else:
        print("Invalid room number!")

# Function to cancle a booking
def cancle_booing ():
    room_number = int(input("Enter room number to cancle booking: "))
    if room_number in rooms:
        if rooms[room_number] == "Booked":
            rooms[room_number] = "Available"
            print(f"Booking for room {room_number} has been cancelled.")
        else:
            print(f"Room {room_number} is not booked yet.")
    else:
        print("Invalid room number!")

# Main program loop
while True:
    print("\n---Hotel Room Booking System---")
    print("1. Show Rooms")
    print("2. Book Rooms")
    print("3. Cancle Booking")
    print("4. Exit")

    print("===================================")
    
    choice = input("Enter your choice: ")
    if choice == "1":
        show_room()
    elif choice == "2":
        book_room()
    elif choice == "3":
        cancle_booing()
    elif choice == "4":
        print("Thank you for using our system!")
        break
    else:
        print("Invalid choice! Please try again.")