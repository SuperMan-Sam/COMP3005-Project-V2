from main import *
from function import *

def register_member_ui():
    """User interface for registering a new member."""
    name = input("Enter member's name: ")
    email = input("Enter member's email: ")
    password = input("Enter member's password: ")
    fitness_goals = input("Enter member's fitness goals: ")
    health_metrics = input("Enter member's health metrics: ")
    register_member(name, email, password, fitness_goals, health_metrics)
    
def register_member(name, email, password, fitness_goals, health_metrics):
    conn = connect_db()
    cur = conn.cursor()
    
    cur.execute("SELECT COUNT(*) FROM Members WHERE Email = %s", (email,))
    email_exists = cur.fetchone()[0]
    if email_exists > 0:
        cur.close()
        conn.close()
        print("The email address is already registered.")
        return False
    
    cur.execute("INSERT INTO Members (Name, Email, Password, FitnessGoals, HealthMetrics) VALUES (%s, %s, %s, %s, %s) RETURNING memberid",
                (name, email, password, fitness_goals, health_metrics))
    member_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    insert_payment(member_id)
    print("Member registered successfully.")
    
    
def insert_payment(member_id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO Payment (member_id, amount, paid) VALUES (%s, %s, %s)", (member_id, 0, 0))
    conn.commit()
    cur.close()
    conn.close()
    
def update_member_ui():
    """User interface for updating a member's details."""
    member_id = input("Enter member's ID: ")
    name = input("Enter member's name: ")
    email = input("Enter member's email: ")
    password = input("Enter member's password: ")
    fitness_goals = input("Enter member's fitness goals: ")
    health_metrics = input("Enter member's health metrics: ")
    update_member(member_id, name, email, password, fitness_goals, health_metrics)
    print("Member details updated successfully.")
    
def update_member(member_id, name, email, password, fitness_goals, health_metrics):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("UPDATE Members SET Name = %s, Email = %s, Password = %s, FitnessGoals = %s, HealthMetrics = %s WHERE memberid = %s",
                (name, email, password, fitness_goals, health_metrics, member_id))
    conn.commit()
    cur.close()
    conn.close()

def delete_member_ui():
    """User interface for deleting a member."""
    member_id = input("Enter member's ID: ")
    delete_member(member_id)
    print("Member deleted successfully.")
    
def delete_member(member_id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM Members WHERE memberid = %s", (member_id,))
    conn.commit()
    cur.close()
    conn.close()
    
def check_member_ui():
    """User interface for checking a member's details."""
    member_id = input("Enter member's ID: ")
    member = check_member(member_id)
    if not member:
        print("Member not found.")
        return
    print("Member ID:", member[0])
    print("Name:", member[1])
    print("Email:", member[2])
    print("Fitness Goals:", member[3])
    print("Health Metrics:", member[4])

def check_member(member_id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Members WHERE memberid = %s", (member_id,))
    member = cur.fetchone()
    cur.close()
    conn.close()
    return member if member else False
    
def book_class_ui():
    """User interface for booking a class."""
    class_type = input("Enter class type(Group or Personal)(G or P): ")
    if class_type == "Group" or class_type == "G":
        member_id = input("Enter member ID: ")
        trainer = input("Enter trainer ID: ")
        date = input("Enter booking date (YYYY-MM-DD): ")
        start_time = input("Enter start time (HH:MM): ")
        end_time = input("Enter end time (HH:MM): ")
        book_class(trainer, date, start_time, end_time, member_id, 1)
    elif class_type == "Personal" or class_type == "P":
        member_id = input("Enter member ID: ")
        trainer = input("Enter trainer ID: ")
        date = input("Enter booking date (YYYY-MM-DD): ")
        start_time = input("Enter start time (HH:MM): ")
        end_time = input("Enter end time (HH:MM): ")
        book_class(trainer, date, start_time, end_time, member_id, 0)
    else:
        print("Invalid class type. Please enter 'Group' or 'Personal'.")
        
def book_class(trainer, date, start_time, end_time, member_id, group):
    if not is_class_available(trainer, date, start_time, end_time):
        print("Class is not available for booking.")
        return
    
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO sessionbooking (trainer_id, booking_date, start_time, end_time, member_id, \"group\") VALUES (%s, %s, %s, %s, %s, %s)",
            (trainer, date, start_time, end_time, member_id, group))

    conn.commit()
    cur.close()
    conn.close()
    add_payment(member_id, 100)
    print("Class booked successfully, the payment $100 has been added to the member's account.")
    
def add_payment(member_id, amount):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("UPDATE Payment SET amount = amount + %s WHERE member_id = %s", (amount, member_id))
    conn.commit()
    cur.close()
    conn.close()
    
def payment_ui():
    """User interface for making a payment."""
    member_id = input("Enter member ID: ")
    amount = input("Enter amount to pay: ")
    payment(member_id, amount)
    
def payment(member_id, amount):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("UPDATE Payment SET amount = amount - %s WHERE member_id = %s", (amount, member_id))
    conn.commit()

    cur.execute("SELECT amount FROM Payment WHERE member_id = %s", (member_id,))
    remaining_amount = cur.fetchone()[0]

    cur.close()
    conn.close()
    print("Payment $" + str(amount) + " made successfully.")
    print("Remaining amount: $" + str(remaining_amount))