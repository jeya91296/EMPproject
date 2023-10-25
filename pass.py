import sys
import mysql.connector
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from datetime import timedelta # representing time durations rather than actual date and time
from datetime import datetime  # Add this import statement at the top of your script
import pandas as pd

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("EXON AIR CONDITIONING")
        self.setGeometry(100, 100, 800, 600)    #(x,y,width,height)      

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()

        label = QLabel(central_widget)
        label.setText("EXON AIR CONDITIONING")
        label.setFont(QFont('Times New Roman',33))
        #layout.addWidget(label)
        label.move(280,100) #y axis change label comes down,change x axis sidewise move
        label.show()
        
        btn1 = QPushButton(central_widget)
        btn1.setText('EMPLOYEE\nATTENDANCE')
        btn1.setFont(QFont('Times New Roman',20,QFont.Weight.Bold))
        btn1.setStyleSheet("background-color: maroon; color: white;")
        btn1.resize(200,200)
        btn1.move(300,200) #xy position
        btn1.show()
        btn1.clicked.connect(self.empatt)
        
        btn2 = QPushButton(central_widget)
        btn2.setText('ADMIN')
        btn2.setFont(QFont('Times New Roman',20,QFont.Weight.Bold))
        btn2.setStyleSheet("background-color: maroon; color:white;")
        btn2.resize(200,200)
        btn2.move(570,200)
        btn2.show()
        btn2.clicked.connect(self.admin)

        central_widget.setLayout(layout)


        try:
            # Connect to the MySQL server
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root"
            )
            
            # Create a cursor
            cursor = connection.cursor()
            # Define the database name
            database_name = "Exon"

            # Execute the SQL command to create the database if it doesn't exist
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")

            # Close the cursor and connection
            cursor.close()
            connection.close()

            #print("Database created successfully!")
            print(f"Database '{database_name}' created successfully or already exists.")

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return
    
    def empatt(self):
        self.emp_att = WindowEmpAtt()
        self.emp_att.show()
       
    def admin(self):
        self.emp_admin = WindowAdmin()
        self.emp_admin.show()

class WindowEmpAtt(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("EMPLOYEE ATTENDANCE")
        self.setGeometry(100, 100, 800, 600)
        
        layout=QFormLayout()

        label = QLabel("EMPLOYEE ATTENDANCE LOG-IN LOG-OUT")
        label.setFont(QFont('Times New Roman',20))
        label.setStyleSheet("background-color: maroon; color:white;")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter) 
        layout.addWidget(label)
        label.show()

        label1 = QLabel("Employee Id:")
        label1.setFont(QFont('Times New Roman',13))
        layout.addWidget(label1)
        label1.show()

        self.entry1 = QLineEdit()
        self.entry1.setFont(QFont('Times New Roman',13))
        self.entry1.setPlaceholderText('Enter your Employee ID')
        self.entry1.setValidator(QIntValidator())
        layout.addWidget(self.entry1)
        self.entry1.show()

        label2 = QLabel("Employee Name:")
        label2.setFont(QFont('Times New Roman',13))
        layout.addWidget(label2)
        label2.show()
        
        self.entry2 = QLineEdit()
        self.entry2.setFont(QFont('Times New Roman',13))
        self.entry2.setPlaceholderText('Enter your Employee Name')
        alphabet_pattern = QRegularExpression("[A-Za-z ]+")
        self.entry2.setValidator(QRegularExpressionValidator(alphabet_pattern))
        layout.addWidget(self.entry2)
        self.entry2.show()

        label3 = QLabel("Date:")
        label3.setFont(QFont('Times New Roman',13))
        layout.addWidget(label3)
        label3.show()

        self.entry3 = QDateEdit()
        self.entry3.setFont(QFont('Times New Roman',13))
        layout.addWidget(self.entry3)
        self.entry3.show()
        self.entry3.setDate(QDate.currentDate())
        #self.entry3.setDate(Qt.QDate.currentDate())
        
        label4 = QLabel("Log-In")
        label4.setFont(QFont('Times New Roman',13))
        layout.addWidget(label4)
        label4.show()

        self.entry4 = QTimeEdit()
        self.entry4.setFont(QFont('Times New Roman',13))
        layout.addWidget(self.entry4)
        self.entry4.setTime(QTime.currentTime())    
        self.entry4.show()
       
        label5 = QLabel("Log-Out")
        label5.setFont(QFont('Times New Roman',13))
        layout.addWidget(label5)
        label5.show()

        self.entry5 = QTimeEdit()
        self.entry5.setFont(QFont('Times New Roman',13))
        layout.addWidget(self.entry5)
        self.entry5.setTime(QTime.currentTime())        
        self.entry5.show()
      
        self.Subbtn1 = QPushButton()
        self.Subbtn1.setText('Submit')
        self.Subbtn1.setFont(QFont('Times New Roman',18))
        self.Subbtn1.setStyleSheet("background-color: maroon; color:white;")
        layout.addWidget(self.Subbtn1)
        self.Subbtn1.setEnabled(True)
        self.Subbtn1.show()
        self.Subbtn1.clicked.connect(self.empattsubmit)

        Closebtn = QPushButton()
        Closebtn.setText('Close')
        Closebtn.setFont(QFont('Times New Roman',18))
        Closebtn.setStyleSheet("background-color: maroon; color:white;")        
        layout.addWidget(Closebtn)
        Closebtn.show()
        Closebtn.clicked.connect(self.main1)
       
        self.status_bar = QStatusBar() 
        self.status_bar.setFont(QFont('Times New Roman',20,QFont.Weight.Bold))         
        layout.addWidget(self.status_bar)
        # Clear the input fields
        self.status_bar.showMessage("")

        self.setLayout(layout)    
                   
    def empattsubmit(self):            
            ID=self.entry1.text()
            print(ID)            
            if not ID:
                self.status_bar.showMessage("Please Enter Employee ID.........")
                return
            else:
                self.status_bar.showMessage("")
    
            Name=self.entry2.text()
            if not Name:
                self.status_bar.showMessage("Please Enter Employee Name........")
                return
            else:
                self.status_bar.showMessage("")

            Name1=Name.capitalize()
            print(Name1)
         
            date1=self.entry3.date()
            date2=self.entry3.text()
            print(date1,date2)
            date = self.entry3.date().toString(Qt.DateFormat.ISODate)

            mydb = mysql.connector.connect(host="localhost",  user="root",  password="root",  database="Exon")
            try:
                mycursor9 = mydb.cursor()
                mycursor9.execute("select Date from Employee_Attendance where Date=%s and Employee_Id=%s",(date,ID))
                print(mycursor9)
                results=mycursor9.fetchone()
                print(results)
                mycursor9.close()
                if results is not None:
                    self.status_bar.showMessage("Entered date already exist so Please Enter Valid date.......")
                    return
                else:
                    self.status_bar.showMessage(" ")
                        
            except Exception as e:
                print("Error:", str(e))
                return
            
            mydb.close()
            
            logindate = self.entry4.time().toString(Qt.DateFormat.ISODate)            
            logoutdate=self.entry5.time().toString(Qt.DateFormat.ISODate)
            logindate1=self.entry4.time()
            logoutdate1=self.entry5.time()
            print(logindate1,logoutdate1)
            print(ID,Name1,date,logindate,logoutdate)
            
            if logindate1.hour() == logoutdate1.hour() and logindate1.minute() == logoutdate1.minute():
                print("inside")
                self.status_bar.showMessage("Please Enter Valid Login time.........")
                return
            else:
                self.status_bar.showMessage("")
                print("else")
                        
            # MySQL database connection
            mydb = mysql.connector.connect(host="localhost",  user="root",  password="root",  database="Exon")
            try:
                mycursor8 = mydb.cursor()
                mycursor8.execute("CREATE TABLE IF NOT EXISTS Employee_Attendance (Employee_Id int NOT NULL , Employee_Name VARCHAR(255) NOT NULL,Date date NOT NULL,Log_In time NOT NULL,Log_Out time NOT NULL)")
                print(mycursor8)
                mydb.commit()
            except Exception as e:
                print("Error:", str(e))
                return
            
            print("table created successfully")

            try:    
                mycursor8.execute("INSERT INTO Employee_Attendance VALUES (%s, %s,%s, %s,%s)", (ID,Name1,date,logindate,logoutdate))
                print(mycursor8)
                mydb.commit()
                mycursor8.close()
            except Exception as e:
                print("Error:", str(e))
                return
            
            mydb.close()  # Always close the database connection
            print("Data inserted successfully")
            
            # Clear the input fields
            self.entry1.clear()
            self.entry2.clear()
            self.entry3.setDate(QDate.currentDate())
            self.entry4.setTime(QTime.currentTime())
            self.entry5.setTime(QTime.currentTime())

            self.Subbtn1.setEnabled(False)
            if self.Subbtn1.isEnabled():
                print("Button is enabled")
            else:
                print("Button is disabled")
            self.status_bar.showMessage("Details has been successfully updated")

    def main1(self):
        self.close()

class WindowAdmin(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("REPORT")
        self.setGeometry(100, 100, 800, 600)
       
        layout1=QFormLayout()

        label = QLabel("REPORT")
        label.setFont(QFont('Times New Roman',20))
        label.setStyleSheet("background-color: maroon; color:white;")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout1.addWidget(label)
        label.show()

        label1 = QLabel("Employee_Id")
        label1.setFont(QFont('Times New Roman',13))
        layout1.addWidget(label1)
        label1.show()

        self.entry1 = QLineEdit()
        self.entry1.setFont(QFont('Times New Roman',13))
        self.entry1.setPlaceholderText('Enter your Employee ID')
        self.entry1.setValidator(QIntValidator())
        layout1.addWidget(self.entry1)
        self.entry1.show()
       
        label2 = QLabel("From Date")
        label2.setFont(QFont('Times New Roman',13))
        layout1.addWidget(label2)
        label2.show()

        self.entry2 = QDateEdit()
        self.entry2.setFont(QFont('Times New Roman',13))
        layout1.addWidget(self.entry2)
        self.entry2.show()
        self.entry2.setDate(QDate.currentDate())
        
        
        label3 = QLabel("To Date")
        label3.setFont(QFont('Times New Roman',13))
        layout1.addWidget(label3)
        label3.move(160,310)
        label3.show()

        self.entry3 = QDateEdit()
        self.entry3.setFont(QFont('Times New Roman',13))       
        layout1.addWidget(self.entry3)        
        self.entry3.show()
        self.entry3.setDate(QDate.currentDate())
                
        Subbtn = QPushButton()
        Subbtn.setText('Submit')
        Subbtn.setFont(QFont('Times New Roman',18))
        Subbtn.setStyleSheet("background-color: maroon; color:white;")
        Subbtn.resize(100,100)
        Subbtn.move(300,200) #xy position
        layout1.addWidget(Subbtn)
        Subbtn.show()
        Subbtn.clicked.connect(self.adminsubmit)
        
        Closebtn = QPushButton()
        Closebtn.setText('Close')
        Closebtn.setFont(QFont('Times New Roman',18))
        Closebtn.setStyleSheet("background-color: maroon; color:white;")
        Closebtn.resize(100,100)
        Closebtn.move(300,200) #xy position
        layout1.addWidget(Closebtn)
        Closebtn.show()
        Closebtn.clicked.connect(self.main2)

        self.status_bar = QStatusBar() 
        self.status_bar.setFont(QFont('Times New Roman',20,QFont.Weight.Bold))       
        layout1.addWidget(self.status_bar)
        self.status_bar.showMessage("")
     
        self.setLayout(layout1)
         
    def main2(self):
        self.close()
      
    def adminsubmit(self):
        self.EmpId=self.entry1.text()
        if not self.EmpId:
            self.status_bar.showMessage("Please Enter Employee ID.........")
            return
        else:
            self.status_bar.showMessage("")

        self.fromdate = self.entry2.date().toString(Qt.DateFormat.ISODate)
        self.todate = self.entry3.date().toString(Qt.DateFormat.ISODate)
        print(self.EmpId,self.fromdate,self.todate)
        
        
        # MySQL database connection
        mydb = mysql.connector.connect(host="localhost",  user="root",  password="root",  database="Exon")
        try:
            mycursor9 = mydb.cursor()
            mycursor9.execute("""CREATE TABLE IF NOT EXISTS Salary(Regularpay_Onehr decimal(8,2) ,
                      Overtimepay_Onehr decimal(8,2) ,Regular_Hr time,Break_Hr time,
                      PRIMARY KEY (Regular_Hr, Break_Hr) -- Adding primary constraint
                      )""")
            print(mycursor9)
            mydb.commit()
                
        except Exception as e:
            print("Error:", str(e))
            return
        
        print("Table 'Salary' created successfully or already exists.")
        print("table created successfully")

        try:    
            mycursor9.execute("insert IGNORE into Salary  values(6.73,10,'08:00:00','01:00:00')")
            print(mycursor9)
            mydb.commit()
            mycursor9.close()
        except Exception as e:
            print("Error:", str(e))
            return
            
        mydb.close()  # Always close the database connection
        print("Data inserted successfully")

        self.entry1.clear()
        self.entry2.setDate(QDate.currentDate())
        self.entry3.setDate(QDate.currentDate())

        self.admin_sub = WindowReportSal(self.EmpId, self.fromdate, self.todate)
        self.admin_sub.show()   

class WindowReportSal(QWidget):
    def __init__(self,empid, fromdate, todate):
        super().__init__()

        self.setWindowTitle("REPORT EMPLOYEE SALARY")
        self.setGeometry(100, 100, 800, 600)

        self.EmpId = empid  # Store the passed data as attributes
        self.fromdate = fromdate
        self.todate = todate
      
        layout = QVBoxLayout()

        label = QLabel("Employee Salary Report")
        label.setFont(QFont('Times New Roman',23))
        label.setStyleSheet("background-color: maroon; color:white;")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)
        label.show()

        self.attendance_table = QTableWidget()
        self.attendance_table.setFont(QFont('Times New Roman',12))
        self.attendance_table.setColumnCount(12)
       
        self.attendance_table.setHorizontalHeaderLabels(["Emp Id","Employee Name","Day","Date","LogIn Time","LogOut Time","TotalHr\nexcluded breakhr","OverTimeHr","RegularTimeHr\nexcluded breakhr","RegularSalary","OverTimeSalary","Total Salary"])
        # Create a font for the header labels
        header_font = QFont("Times New Roman", 13, QFont.Weight.Bold)  # Set the font to bold and increase size
        # Set the font for the horizontal header labels
        self.attendance_table.horizontalHeader().setFont(header_font)
        
        layout.addWidget(self.attendance_table)
       
        mydb = mysql.connector.connect(host="localhost",  user="root",  password="root",  database="Exon")
        mycursor = mydb.cursor()
        
        print(self.EmpId,self.fromdate,self.todate)

        query=("""select
c.id,c.name,c.day,c.date,c.login,c.logout,c.totalhr,c.overtimehr
 from
 (select
 a.Employee_Id as id,a.Employee_Name as name,(dayname(a.date)) as day,a.Date as Date,a.Log_In as login,a.Log_Out as logout,
 (select timediff((timediff(a.Log_Out,a.Log_In)),b.Break_Hr)) as totalhr,
 (select timediff(timediff((timediff(a.Log_Out,a.Log_In)),b.Break_Hr),b.Regular_Hr)) as overtimehr
 from Employee_Attendance a, Salary b  where a.Employee_Id=%s and a.Date between %s and %s)c""")
        print(type(self.EmpId),type(self.fromdate),type(self.todate))
        print(str(self.EmpId),str(self.fromdate),str(self.todate))
        val=(self.EmpId,self.fromdate,self.todate)

        mycursor.execute(query,val)
        print(mycursor)
        results = mycursor.fetchall()
        print(results)
        mycursor.close()
        row_index=0
        totsum=0.00
        print(row_index,totsum)
        
        for row in results:
            column_0, column_1, column_2, column_3, column_4, column_5, column_6, column_7 = row            
            self.attendance_table.setRowCount(row_index + 1)
            print(self.attendance_table.setRowCount(row_index + 1))
            self.attendance_table.setItem(row_index, 0, QTableWidgetItem(str(column_0)))
            self.attendance_table.setItem(row_index, 1, QTableWidgetItem(str(column_1)))
            self.attendance_table.setItem(row_index, 2, QTableWidgetItem(str(column_2)))
            self.attendance_table.setItem(row_index, 3, QTableWidgetItem(str(column_3)))
            self.attendance_table.setItem(row_index, 4, QTableWidgetItem(str(column_4)))
            self.attendance_table.setItem(row_index, 5, QTableWidgetItem(str(column_5)))
            self.attendance_table.setItem(row_index, 6, QTableWidgetItem(str(column_6)))            
            
            time_delta = column_6
            total_seconds = time_delta.total_seconds()
            hours, remainder = divmod(total_seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            qtime = QTime(int(hours), int(minutes), int(seconds))
            time1 = QTime(8, 0, 0)
            if qtime >= time1:
                self.attendance_table.setItem(row_index, 7, QTableWidgetItem(str(column_7)))
            else:
                column_7 = "00:00:00"
                self.attendance_table.setItem(row_index, 7, QTableWidgetItem(str(column_7)))            
            
            mycursor1 = mydb.cursor()
            q = "SELECT TIMEDIFF(%s,%s)"
            print(type(column_6),type(column_7),type(q))
            mycursor1.execute(q, (column_6, column_7))
            result = mycursor1.fetchone()
            column_8 = (result[0]) if result else "No more rows to fetch"
            mycursor1.close()
            self.attendance_table.setItem(row_index, 8, QTableWidgetItem(str(column_8)))

            # Convert column_8 to a tuple with a single element (the timedelta)
            column_8_param = (column_8,)
            if column_2 != "Sunday":
                mycursor2 = mydb.cursor()
                q1 = "SELECT format((Regularpay_Onehr * %s),2) from Salary"
                print(q1)
                print(type(column_8),type(q1))
                mycursor2.execute(q1, column_8_param)
                print(mycursor2)
                result1 = mycursor2.fetchone()
                column_9 = result1[0] if result1 else "No more rows to fetch"
                mycursor2.close()
                self.attendance_table.setItem(row_index, 9, QTableWidgetItem(str(column_9)))
            else:
                mycursor2 = mydb.cursor()
                q1 = "SELECT format((Overtimepay_Onehr * %s),2) from Salary"
                mycursor2.execute(q2, column_8_param)
                result1 = mycursor2.fetchone()
                column_9 = result1[0] if result1 else "No more rows to fetch"
                mycursor2.close()
                self.attendance_table.setItem(row_index, 9, QTableWidgetItem(str(column_9)))

            column_7_param = (column_7,)
            mycursor3 = mydb.cursor()
            q2 = "SELECT Overtimepay_Onehr * %s from Salary"
            print(q2)
            print(type(column_7),type(q2))
            mycursor3.execute(q2, column_7_param)
            print(mycursor3)
            result2 = mycursor3.fetchone()
            column_10 = result2[0] if result2 else "No more rows to fetch"
            mycursor3.close()
            self.attendance_table.setItem(row_index, 10, QTableWidgetItem(str(column_10)))
            
            column_11= float(column_9) + float(column_10)
            self.attendance_table.setItem(row_index, 11, QTableWidgetItem(str(column_11)))
        
            totsum=totsum + column_11
            print(totsum)

            print(row_index)
            # Increment the row index
            row_index += 1
            print(row_index)
            self.attendance_table.setRowCount(row_index + 1)   #next line
        
        # Show the QTableWidget
        total_summary_item = QTableWidgetItem("Total Summary:")
        total_summary_item.setFont(QFont('Times New Roman',15 ,QFont.Weight.Bold))
        total_summary_item.setBackground(QColor("lightgreen"))
        total_summary_item.setForeground(QColor("black"))
        self.attendance_table.setItem(row_index, 10, total_summary_item)
        

        total_summary_value = QTableWidgetItem(str(totsum))
        total_summary_value.setFont(QFont("Times New Roman", 14, QFont.Weight.Bold))  # Set the font to bold and increase size
        total_summary_value.setBackground(QColor("lightgreen"))
        total_summary_value.setForeground(QColor("black"))
        self.attendance_table.setItem(row_index, 11, total_summary_value)        
     
        self.attendance_table.resizeColumnsToContents()
        self.attendance_table.show()            

        self.status_bar = QStatusBar() 
        self.status_bar.setFont(QFont('Times New Roman',20,QFont.Weight.Bold))        
        layout.addWidget(self.status_bar)        
        self.status_bar.showMessage("")
        
        Downloadbtn = QPushButton()
        Downloadbtn.setText('Download')
        Downloadbtn.setFont(QFont('Times New Roman',20))
        Downloadbtn.setStyleSheet("background-color: maroon; color:white;")
        layout.addWidget(Downloadbtn)
        Downloadbtn.show()
        Downloadbtn.clicked.connect(self.download)

        Closebtn = QPushButton()
        Closebtn.setText('Close')
        Closebtn.setFont(QFont('Times New Roman',20))
        Closebtn.setStyleSheet("background-color: maroon; color:white;")
        layout.addWidget(Closebtn)
        Closebtn.show()
        Closebtn.clicked.connect(self.main3)        
        
        self.setLayout(layout)

    def download(self):
        # Get the current date in the format YYYY-MM-DD
        current_date = datetime.now().strftime('%d-%m-%Y')
        print(current_date)

        # Define the file name with the 'exon' prefix and current date
        file_name = f"exon_{current_date}.xlsx"
        print(file_name)       
            
        full_file_path = "C:\\Users\\user\\Downloads\\" + file_name
        print(full_file_path)

        # Get the data from QTableWidget
        data = []
        headers = []
        for col in range(self.attendance_table.columnCount()):
            headers.append(self.attendance_table.horizontalHeaderItem(col).text())
        data.append(headers)
        for row in range(self.attendance_table.rowCount()):
            row_data = []
            for col in range(self.attendance_table.columnCount()):
                item = self.attendance_table.item(row, col)
                if item is not None:
                    row_data.append(item.text())
                else:
                    row_data.append("")
            data.append(row_data)

        # Create a Pandas DataFrame
        df = pd.DataFrame(data)

        # Save the DataFrame to an Excel file
        df.to_excel(full_file_path, index=False, header=False, engine='openpyxl')

        self.status_bar.showMessage(f"Data exported to {file_name} successfully!")
        print(f"Data exported to {file_name} successfully!")

    def main3(self):
        self.close()

    
def main():
    app = QApplication(sys.argv)

    qp = QPalette()
    qp.setColor(QPalette.ColorRole.WindowText, QColor("black"))
    qp.setColor(QPalette.ColorRole.Window, QColor("white"))
    
    app.setPalette(qp)
    
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()