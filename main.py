from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QTableWidgetItem, QWidget, QVBoxLayout, QMainWindow , QFileDialog
from PyQt5.QtCore import QCoreApplication
from mainwindow5 import Ui_MainWindow
from datetime import datetime
import sys
import pyowm                                 # needs for import data from OpenWeather.com -websevices
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.push_Save_clicked)                 # Call push_Save_clicked procedure for action by pressing the button "Save"
        self.pushButton_2.clicked.connect(self.push_Graph_clicked)
        self.pushButton_3.clicked.connect(self.push_Bloodpressure_clicked)  
        self.pushButton_4.clicked.connect(QCoreApplication.instance().quit)
        self.read_files()                                                       # Read values and show in table
      
    def read_files(self):
        # Open files for visual showing in QTableWidget
        with open('date_1.txt', 'r') as f1, open('sys_1.txt', 'r') as f2, open('dia_1.txt', 'r') as f3, open('pulse_1.txt','r') as f4, open('weather_pressure_1.txt','r') as f5:
            data1 = f1.readlines()
            data2 = f2.readlines()          # read values from files
            data3 = f3.readlines()
            data4 = f4.readlines()
            data5 = f5.readlines()

        # Set the numbers and names of columns in the table
        rows = max(len(data1), len(data2), len(data3), len(data4), len(data5))
        self.tableWidget.setRowCount(rows)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(['Data','Sys','Dia','Pulse','Weather pressure'])   # Tabel labels


        # Add the data to the table
        for row in range(rows):
            # Add the data from date.txt
            if row < len(data1):
                item1 = QTableWidgetItem(data1[row].strip())
            else:
                item1 = QTableWidgetItem('')
            self.tableWidget.setItem(row, 0, item1)

            # Add the data from sys.txt
            if row < len(data2):
                item2 = QTableWidgetItem(data2[row].strip())
            else:
                item2 = QTableWidgetItem('')
            self.tableWidget.setItem(row, 1, item2)

            # Add the data from dia.txt
            if row < len(data3):
                item3 = QTableWidgetItem(data3[row].strip())
            else:
                item3 = QTableWidgetItem('')
            self.tableWidget.setItem(row, 2, item3)

            # Add the data from pulse.txt
            if row < len(data4):
                item4 = QTableWidgetItem(data4[row].strip())
            else:
                item4 = QTableWidgetItem('')
            self.tableWidget.setItem(row, 3, item4)

            # Add the data from weather_pressure.txt
            if row <  len(data5):
                item5 = QTableWidgetItem(data5[row].strip())
            self.tableWidget.setItem(row, 4, item5)


    def push_Save_clicked(self):
        owm =pyowm.OWM('f8c43bbd601d39c177afabec2d050d04')                      # included API-key: f8c43bbd601d39c177afabec2d050d04
        mgr = owm.weather_manager()
        weather_pressure = mgr.weather_at_place('Helsinki').weather.pressure
        pressure_value=str(weather_pressure['press'])
        
        sys_value = self.lineEdit.text()
        dia_value = self.lineEdit_2.text()
        pulse_value = self.lineEdit_3.text()
        data_value = self.dateEdit.text() 
    

        with open('sys.txt', 'a') as sysfile:
            sysfile.write(str(sys_value) + '\n')
            sysfile.close()

        with open('dia.txt', 'a') as diafile:
            diafile.write(str(dia_value) + '\n')
            diafile.close()

        with open('pulse.txt', 'a') as pulsefile:
            pulsefile.write(str(pulse_value) + '\n')
            pulsefile.close()
        
        with open('date.txt', 'a') as datefile:
            datefile.write(str(data_value) + '\n')
            datefile.close()
        
        with open('weather_pressure.txt', 'a') as pressdatafile:
            pressdatafile.write(str(pressure_value) + '\n')
            pressdatafile.close()
        
        self.save_to_reversed_files()                                # call function for reversing values. It´s needed for show it in QTable
        self.read_files()                                            # call function for reading and showing values in table


    def save_to_reversed_files(self):
        # Array converter for reverse data showing in QTableWidget
        array = list()
        with open("date.txt", 'r') as date:
            for line in date:
                array.insert(0,line.strip())
        date.close
        date_1 = open('date_1.txt','w')
        for i in range (0, len(array)):
            date_1.write(array[i]+'\n')
        date_1.close
        array.clear()


        with open("sys.txt", 'r') as sys:
            for line in sys:
                array.insert(0,line.strip())
        sys.close
        sys_1 = open('sys_1.txt','w')
        for i in range (0, len(array)):
            sys_1.write(array[i]+'\n')
        sys_1.close
        array.clear()


        with open("dia.txt", 'r') as dia:
            for line in dia:
                array.insert(0,line.strip())
        dia.close
        dia_1 = open('dia_1.txt','w')
        for i in range (0, len(array)):
            dia_1.write(array[i]+'\n')
        dia_1.close
        array.clear()


        with open("pulse.txt", 'r') as pulse:
            for line in pulse:
                array.insert(0,line.strip())
        pulse.close
        pulse_1 = open('pulse_1.txt','w')
        for i in range (0, len(array)):
            pulse_1.write(array[i]+'\n')
        pulse_1.close
        array.clear()

        with open("weather_pressure.txt", 'r') as wpr:
            for line in wpr:
                array.insert(0,line.strip())
        wpr.close
        wpr_1 = open('weather_pressure_1.txt','w')
        for i in range (0, len(array)):
            wpr_1.write(array[i]+'\n')
        wpr_1.close
        array.clear()


    def push_Bloodpressure_clicked(self):
        with open('date.txt', 'r') as file:     # Read the dates from a txt-file
            date_strs = file.readlines()        # Parse the date strings into datetime objects
        dates = []
        for date_str in date_strs:
            date_str = date_str.strip()         # remove any whitespace or newline characters
            date = datetime.strptime(date_str, '%d.%m.%Y')      # replace with your format
            dates.append(date)

        # Read the integer values from three txt-files
        with open('sys.txt', 'r') as sysfile1:
            values_sys1 = []
            for valsys1 in sysfile1.readlines():
                values_sys1.append(int(valsys1.strip()))
            
        with open('dia.txt', 'r') as diafile2:
            values_dia2 = []
            for valdia2 in diafile2.readlines():
                values_dia2.append(int(valdia2.strip()))
        
        with open('pulse.txt', 'r') as pulsefile3:
            values_pulse3 = []
            for valpulse3 in pulsefile3.readlines():
                values_pulse3.append(int(valpulse3.strip()))

        # PLOT data and values
        fig = Figure()
        ax = fig.add_subplot(211)
        ax.set_ylabel('SYS & DIA')
        ax.set_title('SYS and DIA & Pulse graph')
        ax.grid(linewidth=1)
        ax.plot(dates, values_sys1, color='r', label='Sys', marker='*')    # x-axis =Date  y-axis = SYS
        ax.plot(dates, values_dia2, color='g', label='Dia')    # x-axis =Date  y-axis = Dia
 
        ax = fig.add_subplot(212)
        ax.tick_params(axis='x', rotation=45)
        ax.set_xlabel('Date')
        ax.set_ylabel('Pulse')
        ax.grid(linewidth=1)
        ax.plot(dates, values_pulse3, color='b', label='Pulse', linestyle='--')    # x-axis =Date  y-axis = Dia

        canvas = FigureCanvas(fig)
        self.plot_window = QWidget()
        layout = QVBoxLayout(self.plot_window)
        layout.addWidget(canvas)
        
        self.plot_window.show()


    def push_Graph_clicked(self):         
        # Read the dates from a txt-file
        with open('date.txt', 'r') as file:
            date_strs = file.readlines()
        # Parse the date strings into datetime objects
        dates = []
        for date_str in date_strs:
            date_str = date_str.strip()                     # remove any whitespace or newline characters
            date = datetime.strptime(date_str, '%d.%m.%Y')  # replace with your format
            dates.append(date)

        # Read the integer values from two txt-files
        with open('sys.txt', 'r') as file1:
            values1 = []
            for val1 in file1.readlines():
                values1.append(int(val1.strip()))
            
        with open('weather_pressure.txt', 'r') as file2:
            values2 = []
            for val2 in file2.readlines():
                values2.append(int(val2.strip()))
            

        # PLOT data and values
        fig = Figure()
        ax = fig.add_subplot(111)
        ax.tick_params(axis='x', rotation=45)
        ax.set_xlabel('Date')
        ax.set_ylabel('Sys')
        ax.set_title('SYS & Weather pressure')
        ax.plot(dates, values1, color='r', label='Sys')         # x-axis =Date  y-axis = SYS
        ax.legend(loc='upper left',labelcolor='red')
        ax2 = ax.twinx()                                        #define second y-axis that shares x-axis with current plot                 
        ax2.plot(dates, values2, color='g', label='weather')    # x-axis =Date  y-axis = Weather pressure data
        ax2.legend(loc='upper right',labelcolor='green')
        ax2.set_ylabel('Weather pressure')
        canvas = FigureCanvas(fig)
        self.plot_window = QWidget()
        layout = QVBoxLayout(self.plot_window)
        layout.addWidget(canvas)
        self.plot_window.show()


if __name__ == "__main__":                      
    app = QtWidgets.QApplication(sys.argv)      # creating a PyQT5 application
    w = MainWindow()                            # creating a window object
    w.show()                                    # showing the window
    sys.exit(app.exec_())                       # loop