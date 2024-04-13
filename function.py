from main import *
from datetime import datetime

def is_room_available(room_id, date, start_time, end_time):
    if start_time >= end_time:
        print("Invalid start and end times.")
        return False
    
    conn = connect_db()
    cur = conn.cursor()

    # Check if the room exists
    cur.execute("SELECT * FROM rooms WHERE RoomID = %s", (room_id,))
    room_exists = cur.fetchone() is not None

    if not room_exists:
        # Room does not exist
        cur.close()
        conn.close()
        return False

    # Check if there are conflicting bookings
    cur.execute("""
        SELECT * FROM RoomBookings 
        WHERE RoomID = %s 
        AND BookingDate = %s 
        AND (StartTime < %s AND EndTime > %s)
    """, (room_id, date, end_time, start_time))
    conflicting_bookings = cur.fetchone() is not None
    cur.close()
    conn.close()

    return not conflicting_bookings

def is_class_available(trainer, date, start_time, end_time):
    start_time = datetime.strptime(start_time, "%H:%M").time()
    end_time = datetime.strptime(end_time, "%H:%M").time()
    if start_time >= end_time:
        print("Invalid start and end times.")
        return False
    
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("SELECT starttime, endtime FROM traineravailability WHERE trainerid = %s AND availabledate = %s", (trainer, date))
    availabilities = cur.fetchall()
    if not availabilities:
        print("Trainer is not available on the specified date.")
        return False

    for availability in availabilities:
        trainer_start_time, trainer_end_time = availability
        if not start_time < trainer_end_time and not end_time > trainer_start_time:
            print(end_time, trainer_start_time, start_time, trainer_end_time)
            print("Requested time slot overlaps with the trainer's availability.")
            return False
    
    # Check if the class exists
    cur.execute("SELECT * FROM SessionBooking WHERE trainer_id = %s AND booking_date = %s", (trainer,date))
    date_exists = cur.fetchone() is not None
    
    if date_exists:
        cur.execute("SELECT * FROM SessionBooking WHERE trainer_id = %s AND booking_date = %s AND start_time < %s AND end_time > %s", 
                (trainer, date, end_time, start_time))
        conflicting_sessions = cur.fetchall()
        if conflicting_sessions:
            print("Requested time slot overlaps with another session.")
            return False
        
    cur.close()
    conn.close()

    return True

def is_session_exists(session_id):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM SessionBooking WHERE session_id = %s", (session_id,))
    session_exists = cur.fetchone() is not None

    cur.close()
    conn.close()

    return session_exists

def get_trainer_id(session_id):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("SELECT trainer_id FROM SessionBooking WHERE session_id = %s", (session_id,))
    trainer_id = cur.fetchone()[0]
    
    cur.close()
    conn.close()

    return trainer_id