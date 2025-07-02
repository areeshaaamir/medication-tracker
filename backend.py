import sqlite3

db_name = "meds.db"

def connectDBS():
    return sqlite3.connect(db_name)

def sign_up(username, email, password, age, weight, gender):
    conn = connectDBS()
    cursor = conn.cursor()

    try:
        cursor.execute("""
                       INSERT INTO users(username, email, password, age, weight, gender)
                       VALUES(?,?,?,?,?,?)
                       """, (username, email, password, age, weight, gender))
        
        conn.commit()
        
        cursor.execute('SELECT userID FROM users WHERE email = ? ', (email, ))
        user = cursor.fetchone()

        if user:
            print("user successfully registered")
            return {"userID": user[0], "username": username}
        
        else:
            return None

    except sqlite3.IntegrityError:
        print("Email already in use :( ")
        return None
    
    finally:
        conn.close()

def login(email, password):
    conn = connectDBS()
    cursor = conn.cursor()

    cursor.execute("""
                   SELECT userID, username FROM users
                   WHERE email = ? AND password = ?
                   """, (email, password))
    
    user = cursor.fetchone()
    conn.close()

    if user:
        print(f"Logged in as {user[1]}")
        return {"userID" : user[0], "username" : user[1]}
    else:
        print("Invalid email or password")
        return None
    
def addMedicine(medName, dosage_mg, quantity, start_date, end_date, reminder_enabled, userID):
    conn = connectDBS()
    cursor = conn.cursor()
    try: 
        cursor.execute('''
                    INSERT INTO medicines
                    (medName, dosage_mg, quantity, start_date, end_date, reminder_enabled, userID)
                    VALUES(?,?,?,?,?,?,?)
                    ''', (medName, dosage_mg, quantity, start_date, end_date, reminder_enabled, userID))
    
        conn.commit()
        return True
    
    except Exception as e:
        print("Error adding medicine", e)
        return False
    
    finally:
        conn.close()

def getUsername(userID):
    conn = connectDBS()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE userID = ?', (userID, ))
    results = cursor.fetchone()
    conn.close()
    return results[1] if results else "User"

def updateMedicine(userID, medName, dosage_mg, quantity, start_date, end_date, reminder_enabled):
    conn = connectDBS()
    cursor = conn.cursor()
    
    cursor.execute('SELECT medID FROM medicines WHERE medName = ? AND userID = ?', (medName, userID))
    result = cursor.fetchone()

    if not result:
        conn.close()
        return False 

    medID = result[0]

    cursor.execute('''
        UPDATE medicines SET
        medName = ?, dosage_mg = ?, quantity = ?, start_date = ?, end_date = ?, reminder_enabled = ?
        WHERE medID = ?
    ''', (medName, dosage_mg, quantity, start_date, end_date, reminder_enabled, medID))

    conn.commit()
    conn.close()
    return True


def deleteMedicine(userID, medName):
    conn = connectDBS()
    cursor = conn.cursor()
    cursor.execute('''
                   DELETE FROM medicines
                   WHERE medName = ? and userID = ?
                   ''', (medName, userID))
    conn.commit()
    conn.close()
    return True

def searchMedicine(userID, medName):
    conn = connectDBS()
    cursor = conn.cursor()
    cursor.execute('''
                   SELECT * FROM medicines
                   WHERE medName LIKE ? COLLATE NOCASE AND userID = ?
                   ''', (f"%{medName}%", userID))  # Correct order
    results = cursor.fetchall()
    conn.close()
    return results


def viewAllMedicines(userID):
    conn = connectDBS()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM medicines WHERE userID = ?', (userID, ))

    meds = cursor.fetchall()
    conn.close()
    return meds

def debug_view_medicines():
    conn = connectDBS()
    cursor = conn.cursor()
    cursor.execute("SELECT medName, userID FROM medicines")
    rows = cursor.fetchall()
    conn.close()
    for row in rows:
        print("DB Entry:", row)

def manual_test_search():
    conn = connectDBS()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM medicines 
        WHERE medName LIKE ? COLLATE NOCASE AND userID = ?
    """, ("%Disprin%", 4))
    results = cursor.fetchall()
    conn.close()
    print("Manual search results:", results)

def addReminderTimes(medID, times):
    conn = connectDBS()
    cursor = conn.cursor()

    try: 
        for t in times:
            cursor.execute('INSERT INTO reminders(medID, time) VALUES (?,?)', (medID, t))
        conn.commit()
        return True
    except Exception as e:
        print("Error adding reminder", e)
        return False
    finally:
        conn.close()

def getReminder(medID):
    conn = connectDBS()
    cursor = conn.cursor()
    cursor.execute('SELECT time FROM reminders WHERE medID = ?', (medID, ))

    times = [row[0] for row in cursor.fetchall()]
    conn.close()
    return times

def getMedicineID(medName, userID):
    conn = connectDBS()
    cursor = conn.cursor()
    cursor.execute("SELECT medID FROM medicines WHERE medName = ? AND userID = ?", (medName, userID))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

def getAllReminders():
    conn = connectDBS()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT medicines.medName, reminders.time, users.username
        FROM medicines
        JOIN reminders ON medicines.medID = reminders.medID
        JOIN users ON medicines.userID = users.userID
        WHERE medicines.reminder_enabled = 1
    ''')
    rows = cursor.fetchall()
    conn.close()
    return rows
