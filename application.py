import streamlit as st
import pandas as pd
import psycopg2
from datetime import date

# DB Mgmt
# Initialize connection.


@st.experimental_singleton
def init_connection():
    # return psycopg2.connect(dbname=st.secrets["postgres"].name, user=st.secrets["postgres"].user, password=st.secrets["postgres"].password, host=st.secrets["postgres"].host, port=st.secrets["postgres"].port)
    # return psycopg2.connect(dbname="timetable", user="postgres", password="postgres", host="localhost", port=5432)
    return psycopg2.connect(**st.secrets["postgres"])


conn = init_connection()
cur = conn.cursor()
conn.autocommit = True


def fetch_duty_type():
    cur.execute("Select Duty_type from Duties;")
    rows = list(cur.fetchall())
    return rows


def fetch_subcode(sem):
    cur.execute("SELECT subject_code from Sub_code_name where sem=%s;", (sem,))
    rows = list(cur.fetchall())
    return rows


def fetch_initials():
    cur.execute("SELECT initials from faculty_details;")
    rows = list(cur.fetchall())
    return rows


today = date.today().strftime("%d-%m-%Y")
st.text(str(today))
month = str(today).split("-")[1]
odd_sem_menu = ["1", "3", "5", "7"]
even_sem_menu = ["2", "4", "6", "8"]
days_of_the_week = ["Monday", "Tuesday", "Wednesday",
                    "Thursday", "Friday", "Saturday", "Sunday"]
time_slots = ["8:15 - 9:15", "9:15 - 10:15", "10:45 - 11:45",
              "11:45 - 12:45", "1:30 - 2:30", "3:30 - 3:45", "3:45 - 4:45", 'Other...']
st.title('PES University')

pages_menu = ["Home", "Subjects", "Faculty Details", "Faculty Subject", "Designation Rank", "Duties",
              "Theory Faculty Timetable Entry", "Lab Faculty Timetable Entry", "Faculty Duties", "About"]

page_choice = st.sidebar.selectbox("Menu", pages_menu)
search = st.sidebar.button("Search For Individual Timetable")

if search:
    st.subheader("Individual Timetable")
    initials = st.selectbox("Initials", fetch_initials())
    if st.button("Get Timetable"):
        cur.execute(f"(SELECT sec_timetable.sem, sec_timetable.sec , day , start_time, end_time, sec_timetable.subject_code FROM sec_timetable, faculty_subject where sec_timetable.subject_code = faculty_subject.subject_code and sec_timetable.sec=faculty_subject.sec and initial = {initials}) UNION (\
        SELECT lab_timetable.sem, lab_timetable.sec , day , start_time, end_time, lab_timetable.subject_code FROM lab_timetable, faculty_subject where lab_timetable.subject_code = faculty_subject.subject_code and sec_timetable.sec=faculty_subject.sec and initial = {initials} );")
        rows = cur.fetchall()
        df = pd.DataFrame(rows, columns=('Semester', 'Section',
                                         'Day', 'Start Time', 'End Time', 'Subject Code'))
        st.table(df)


elif page_choice == pages_menu[0]:
    st.subheader("Home")
    st.subheader('Faculty Duties and Workload management')
    # for i in st.secrets["postgres"]:
    #     st.write(st.secrets["postgres"].user)

elif page_choice == pages_menu[1]:
    st.subheader("Add Subjects")
    if(int(month) > 6):
        sem = st.selectbox("Semester", odd_sem_menu)
    else:
        sem = st.selectbox("Semester", even_sem_menu)
    sub_code = st.text_input("Enter SUbject Code", "")
    sub_name = st.text_input("Enter Subject Name", "")

    if sub_name != "":
        st.write(
            f"""
            * Semester : {sem}
            * Subject Code : {sub_code}
            * Subject Name : {sub_name}
            """
        )

    if st.button("Add Data"):
        cur.execute("INSERT into Sub_code_name VALUES (%s,%s,%s);",
                    (sem, sub_code, sub_name,))
        st.text("Data added")

    if st.button("Show data"):
        cur.execute("SELECT * from sub_code_name")
        rows = cur.fetchall()
        # st.write(rows)
        #df=pd.DataFrame(rows,columns=('Sem','Subject Code','subject name',''))
        # st.write('Sem','Subject Code','subject name','')
        # st.table(df)
        for i in range(len(rows)):
            col1, col2 = st.columns([1, 1])
            with col1:
                st.write(rows[i])
            with col2:
                st.button(f'Delete row{i}')


elif page_choice == pages_menu[2]:
    st.subheader("Faculty Details")
    Initials = st.text_input("Initials", "")
    Fac_name = st.text_input("Faculty Name", "")
    Ph_no = st.number_input("Phone Number")
    email = st.text_input("E-mail", "")
    Address = st.text_input("Address", "")
    Rank = st.selectbox("Designation", [
                        "Prof", "Associate Prof", "Assistant Prof", "HOD", "Chairperson", "Lab Assistant", "Lab in-charge"])
    if Address != "":
        st.write(
            f"""
            * Initials : {Initials}
            * Faculty Name : {Fac_name}
            * Phone No. : {Ph_no}
            * Email : {email}
            * Address : {Address}
            * Rank : {Rank}
            """
        )
    if st.button("Add Data"):
        cur.execute("INSERT into Faculty_details VALUES (%s,%s,%s,%s,%s,%s);",
                    (Initials, Fac_name, int(Ph_no), email, Address, Rank,))
        st.text("Data Added")
    if st.button("Show All Data"):
        cur.execute("SELECT * from Faculty_details;")
        rows = cur.fetchall()
        # st.write(rows)
        #df=pd.DataFrame(rows,columns=('Sem','Subject Code','subject name',''))
        # st.write('Sem','Subject Code','subject name','')
        # st.table(df)
        for i in range(len(rows)):
            col1, col2 = st.columns([1, 1])
            with col1:
                st.write(rows[i])
            with col2:
                st.button(f'Delete row{i}')


elif page_choice == pages_menu[3]:
    st.subheader("Faculty Subjects")
    initials = st.selectbox("Initials", fetch_initials())
    if(int(month) > 6):
        sem = st.selectbox("Semester", odd_sem_menu)
    else:
        sem = st.selectbox("Semester", even_sem_menu)
    sub_code = st.selectbox("Enter SUbject Code", fetch_subcode(sem))
    sec = st.text_input("Section", "")
    if sec != "":
        st.write(
            f"""
            * Initials : {initials}
            * Semester : {sem}
            * Subject Code : {sub_code}
            * Section : {sec}
            """
        )

    if st.button("Add Data"):
        cur.execute("INSERT into Faculty_subject VALUES (%s,%s,%s,%s);",
                    (sub_code, sem, sec, initials,))
        st.text("Data added")
    if st.button("Show data"):
        cur.execute("SELECT * from Faculty_subject;")
        rows = cur.fetchall()
        # st.write(rows)
        #df=pd.DataFrame(rows,columns=('Sem','Subject Code','subject name',''))
        # st.write('Sem','Subject Code','subject name','')
        # st.table(df)
        for i in range(len(rows)):
            col1, col2 = st.columns([1, 1])
            with col1:
                st.write(rows[i])
            with col2:
                st.button(f'Delete row{i}')
        # Add query to insert
        pass

# REMOVE THIS!
elif page_choice == pages_menu[4]:
    st.subheader("Designation Ranks")
    Designation = st.text_input("Designation", "")
    Rank = st.text_input("Rank", "")
    if Rank != "":
        st.write(
            f"""
            * Designation : {Designation}
            * Rank : {Rank}
            """
        )
    if st.button("Submit"):
        # Query to add data
        cur.execute("INSERT into designation_rank VALUES (%s,%s);",
                    (Designation, Rank))
        st.text("Data Added")
    if st.button("Show Duties"):
        cur.execute("SELECT * FROM Designation_Rank;")
        rows = cur.fetchall()
        df = pd.DataFrame(rows, columns=('Designation', 'Rank'))
        st.table(df)
        pass

elif page_choice == pages_menu[5]:
    st.subheader("Duties")
    amount = 0
    duty_type = st.text_input("Duty type", "")
    duty_priority = st.text_input("Duty Priority", "")
    duty_paid = st.selectbox("Paid or unpaid", ['yes', 'no'])
    if(duty_paid == 'yes'):
        amount = st.text_input("Enter amount", "")

    if duty_priority != "" and duty_paid == "yes":
        st.write(
            f"""
            * Duty Type : {duty_type}
            * Duty Priority : {duty_priority}
            * Duty Paid : {duty_paid}
            * Amount : {amount}
            """
        )
    elif duty_priority != "" and duty_paid == "no":
        st.write(
            f"""
            * Duty Type : {duty_type}
            * Duty Priority : {duty_priority}
            * Duty Paid : {duty_paid}
            """
        )
    if st.button("Add Duty"):
        # Query to add data
        cur.execute("INSERT into Duties VALUES (%s,%s,%s);",
                    (duty_type, duty_priority, amount))
        st.text("Data Added")
        pass
    if st.button("Show Duty"):
        # Query to add data
        cur.execute("SELECT * FROM Duties;")
        rows = cur.fetchall()
        df = pd.DataFrame(rows, columns=('Duty Type', 'Priority', 'Paid'))
        st.table(df)
        pass


elif page_choice == pages_menu[6]:
    st.subheader("Theory Faculty Timetable")

    if(int(month) > 6):
        sem = st.selectbox("Semester", odd_sem_menu)
    else:
        sem = st.selectbox("Semester", even_sem_menu)

    section = st.text_input("Section", "")

    day = st.selectbox("Day of the week to update timetable", days_of_the_week)

    timing = st.selectbox("Time Slot", time_slots)

    if timing == 'Other...':
        start_tm = st.text_input("Starting time")
        end_tm = st.text_input("Ending time")
    else:
        start_tm, end_tm = timing.split(" - ")

    subject = st.selectbox("Subject code", fetch_subcode(sem))

    st.write(
        f"""
        * Semester : {sem}
        * Section : {section}
        * Day : {day}
        * Start Time : {start_tm}
        * End Time : {end_tm}
        * Subject Code : {subject}
        """
    )

    if st.button("Submit"):
        # Query to add data
        cur.execute("INSERT into sec_timetable VALUES (%s,%s,%s,%s,%s,%s);",
                    (sem, section, day, start_tm, end_tm, subject))
        st.text("Data Added")
        pass
    if st.button("Show Duty"):
        # Query to add data
        cur.execute("SELECT * FROM sec_timetable;")
        rows = cur.fetchall()
        df = pd.DataFrame(rows, columns=('Semester', 'Section',
                                         'Day', 'Start Time', 'End Time', 'Subject Code'))
        st.table(df)
        pass

elif page_choice == pages_menu[7]:
    st.subheader("Lab Faculty Timetable")
    if(int(month) > 6):
        sem = st.selectbox("Semester", odd_sem_menu)
    else:
        sem = st.selectbox("Semester", even_sem_menu)
    section = st.text_input("Section", "")
    day = st.selectbox("Day of the week to update timetable", days_of_the_week)
    timing = st.selectbox("Time Slot", time_slots)

    if timing == 'Other...':
        start_tm = st.text_input("Starting time")
        end_tm = st.text_input("Ending time")
    else:
        start_tm, end_tm = timing.split(" - ")
    Room = st.text_input("Room", "")
    Subject = st.text_input("Subject", "")
    if(Subject != ""):
        st.write(
            f"""
            * Semester : {sem}
            * Section : {section}
            * Day : {day}
            * Start Time : {start_tm}
            * End Time : {end_tm}
            * Room : {Room}
            * Subject Code : {Subject}
            """
        )
        if st.button("Submit"):
            # Query to add data
            cur.execute("INSERT into lab_timetable VALUES (%s,%s,%s,%s,%s,%s,%s);",
                        (sem, section, day, start_tm, end_tm, Room, Subject))
            st.text("Data Added")
        pass
        if st.button("Show Duty"):
            # Query to add data
            cur.execute("SELECT * FROM lab_timetable;")
            rows = cur.fetchall()
            df = pd.DataFrame(rows, columns=(
                'Semester', 'Section', 'Day', 'Start Time', 'End Time', 'Room', 'Subject Code'))
            st.table(df)
        pass

elif page_choice == pages_menu[8]:
    time_slots = ["8:15 - 9:15", "9:15 - 10:15", "10:45 - 11:45",
                  "11:45 - 12:45", "1:30 - 2:30", "3:30 - 3:45", "3:45 - 4:45", 'Other...']
    st.subheader("Faculty Duties")
    Initials = st.selectbox("Initials", fetch_initials())
    Duty_type = st.selectbox("Duty type", fetch_duty_type())
    Duty_date = st.text_input("Date", "")
    Duty_reporting_time = st.text_input("Reporting Time", "")
    Duty_duration = st.selectbox("Duration", time_slots)
    Duty_venue = st.text_input("Venue", "")

    if Duty_duration == 'Other...':
        start_tm = st.text_input("Starting time")
        end_tm = st.text_input("Ending time")
    else:
        start_tm, end_tm = Duty_duration.split(" - ")
    Duty_duration = " - ".join(Duty_duration)
    if Duty_venue != "":
        st.write(
            f"""
            * Initials : {Initials}
            * Duty Type : {Duty_type}
            * Date : {Duty_date}
            * Reporting Time : {Duty_reporting_time}
            * Start Time : {start_tm}
            * End Time : {end_tm}
            * Venue : {Duty_venue}
            """
        )
    if st.button("Submit"):
        # Query to add data
        cur.execute("INSERT into faculty_duties VALUES (%s,%s,%s,%s,%s,%s);", (Initials,
                                                                               Duty_type, Duty_duration, Duty_venue, Duty_date, Duty_reporting_time))
        st.text("Data Added")
        pass
    if st.button("Show Duty"):
        # Query to add data
        cur.execute("SELECT * FROM faculty_duties;")
        rows = cur.fetchall()
        df = pd.DataFrame(rows, columns=(
            'Initials', 'Duty Type', 'Duration', 'Venue', 'Date', 'Reporting Time'))
        st.table(df)
        pass

elif page_choice == pages_menu[9]:
    st.balloons()
    st.write("# Made with :heartbeat:")
    st.write("## **Abhijit Sethi**")
    st.write("## **Aditi D Anchan**")
    st.write("## **Aakanksha V Akkihal**")
