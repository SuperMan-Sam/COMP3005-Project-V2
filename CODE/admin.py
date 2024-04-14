from main import *
from function import *

def room_management_ui():
    while True:
        print("\nRoom Booking Management")
        print("1. Update Booking")
        print("2. Delete Booking")
        print("3. Booking Details")
        print("4. Book Room")

        choice = input("Enter your choice: ")

        if choice == "1":
            update_room_ui()
        elif choice == "2":
            delete_room_ui()
        elif choice == "3":
            check_room_ui()
        elif choice == "4":
            book_room_ui()
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
            
def administrative_ui():
    while True:
        print("\nAdministrative System")
        print("1. Room Booking Management")
        print("2. Update Session")
        print("3. Equipment")

        choice = input("Enter your choice: ")

        if choice == "1":
            room_management_ui()
        elif choice == "2":
            update_session_ui()
        elif choice == "3":
            equipment_ui()
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")
            
def update_room_ui():
    booking_id = input("Enter booking ID: ")
    date = input("Enter booking date (YYYY-MM-DD): ")
    start_time = input("Enter start time (HH:MM): ")
    end_time = input("Enter end time (HH:MM): ")
    update_room(booking_id, date, start_time, end_time)

def update_room(booking_id, date, start_time, end_time):
    room_id = does_booking_exist(booking_id)
    if not room_id:
        print("Booking ID does not exist in room booking table.")
        return
    
    if not is_room_available(room_id, date, start_time, end_time):
        print("Room is not available for the specified time.")
        return
    
    
    conn = connect_db()
    cur = conn.cursor()
    print(start_time, end_time, room_id, date)
    cur.execute("UPDATE roombookings SET starttime = %s, endtime = %s, bookingdate = %s WHERE bookingid = %s",
                (start_time, end_time, date, booking_id))
    conn.commit()
    cur.close()
    conn.close()
    print("Room booking updated successfully.")
    
def does_booking_exist(booking_id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT roomid FROM roombookings WHERE bookingid = %s", (booking_id,))
    result = cur.fetchone()
    cur.close()
    conn.close()
    return result[0] if result else False
    
def delete_room_ui():
    room_id = input("Enter room ID: ")
    date = input("Enter booking date (YYYY-MM-DD): ")
    delete_room(room_id, date)
    print("Room booking deleted successfully.")

def delete_room(room_id, date):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM RoomBookings WHERE RoomID = %s AND BookingDate = %s", (room_id, date))
    conn.commit()
    cur.close()
    conn.close()
    
def check_room_ui():
    room_id = input("Enter room ID: ")
    date = input("Enter booking date (YYYY-MM-DD): ")
    rooms = check_room(room_id, date)
    if rooms:
        print("========Room:"+room_id+"==========")
        for room in rooms:
            print("-----Booking ID:", room[0], "-----")
            print("Booking Date:", room[1])
            print("Start Time:", room[2])
            print("End Time:", room[3])
    else:
        print("No bookings found for room {} on date {}.".format(room_id, date))
    
def check_room(room_id, date):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM RoomBookings WHERE RoomID = %s AND BookingDate = %s", (room_id, date))
    rooms = cur.fetchall()
    cur.close()
    conn.close()
    return rooms

def book_room_ui():
    """User interface for booking a room."""
    room_id = input("Enter room ID: ")
    date = input("Enter booking date (YYYY-MM-DD): ")
    start_time = input("Enter start time (HH:MM): ")
    end_time = input("Enter end time (HH:MM): ")
    book_room(room_id, date, start_time, end_time)

def book_room(room_id, date, start_time, end_time):
    if not is_room_available(room_id, date, start_time, end_time):
        print("Room is not available for booking.")
        return
    
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO RoomBookings (RoomID, BookingDate, StartTime, EndTime) VALUES (%s, %s, %s, %s)",
                (room_id, date, start_time, end_time))
    conn.commit()
    cur.close()
    conn.close()
    print("Room booked successfully.")
    
def update_session_ui():
    session_id = input("Enter session ID: ")
    date = input("Enter booking date (YYYY-MM-DD): ")
    start_time = input("Enter start time (HH:MM): ")
    end_time = input("Enter end time (HH:MM): ")
    update_session(session_id, date, start_time, end_time)
    
def update_session(session_id, date, start_time, end_time):
    if not is_session_exists(session_id):
        print("Session is not exists.")
        return
    
    if not is_class_available(get_trainer_id(session_id), date, start_time, end_time):
        print("Session is not available for the specified time.")
        return
    
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("UPDATE SessionBooking SET start_time = %s, end_time = %s, booking_date = %s WHERE session_id = %s",
                (start_time, end_time, date, session_id))
    conn.commit()
    cur.close()
    conn.close()
    print("Session updated successfully.")
    
def equipment_ui():
    while True:
        print("\nEquipment Management")
        print("1. Update Equipment")
        print("2. Equipment Details")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            update_equipment_ui()
        elif choice == "2":
            check_equipment_ui()
        elif choice == "3":
            administrative_ui()
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

def update_equipment_ui():
    equipment_id = input("Enter equipment ID: ")
    equipment_status = input("Enter equipment status(1=available, 2=unavailable): ")
    if equipment_status != "1" and equipment_status != "2":
        print("Invalid equipment status. Please enter '1' or '2'.")
        return
    update_equipment(equipment_id, equipment_status)
    
def update_equipment(equipment_id, equipment_status):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("UPDATE Equipment SET status = %s WHERE equipment_id = %s",
                (equipment_status, equipment_id))
    conn.commit()
    cur.close()
    conn.close()
    print("Equipment updated successfully.")
    
def check_equipment_ui():
    equipment_id = input("Enter equipment ID: ")
    equipment = check_equipment(equipment_id)
    if equipment:
        print("Equipment ID:", equipment[0])
        print("Equipment Status:", equipment[1])
    else:
        print("Equipment not found.")
        
def check_equipment(equipment_id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Equipment WHERE equipment_id = %s", (equipment_id,))
    equipment = cur.fetchone()
    cur.close()
    conn.close()
    return equipment