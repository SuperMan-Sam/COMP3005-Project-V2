from main import *

def set_trainer_availability_ui():
    """User interface for setting a trainer's availability."""
    trainer_id = input("Enter trainer's ID: ")
    date = input("Enter available date (YYYY-MM-DD): ")
    start_time = input("Enter start time (HH:MM): ")
    end_time = input("Enter end time (HH:MM): ")
    set_trainer_availability(trainer_id, date, start_time, end_time)
    print("Trainer availability set successfully.")
    
def set_trainer_availability(trainer_id, date, start_time, end_time):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO TrainerAvailability (TrainerID, AvailableDate, StartTime, EndTime) VALUES (%s, %s, %s, %s)",
                (trainer_id, date, start_time, end_time))
    conn.commit()
    cur.close()
    conn.close()
    
def search_member_ui():
    """User interface for searching a member."""
    member_name = input("Enter member's Name: ")
    member = search_member(member_name)
    print("Member ID:", member[0])
    print("Member Name:", member[1])
    print("Member Email:", member[2])
    print("Member Fitness Goals:", member[3])
    print("Member Health Metrics:", member[4])

def search_member(member_name):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Members WHERE Name = %s", (member_name,))
    member = cur.fetchone()
    cur.close()
    conn.close()
    return member