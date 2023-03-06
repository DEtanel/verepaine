from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QTableWidgetItem, QMainWindow , QFileDialog, QLCDNumber
from PyQt5.QtCore import QCoreApplication
from mainwindow3 import Ui_MainWindow
import sys
import pyowm
# import matplotlib.pyplot as plt



class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.push_Save_clicked)
        self.pushButton_2.clicked.connect(self.push_Graph_clicked)
        self.pushButton_3.clicked.connect(self.push_Settings_clicked)    
        self.pushButton_4.clicked.connect(QCoreApplication.instance().quit)

        # Open files for visual showing in QTableWidget
        with open('date.txt', 'r') as f1, open('sys.txt', 'r') as f2, open('dia.txt', 'r') as f3, open('pulse.txt','r') as f4, open('weather_pressure.txt','r') as f5:
            data1 = f1.readlines()
            data2 = f2.readlines()
            data3 = f3.readlines()
            data4 = f4.readlines()
            data5 = f5.readlines()

        # Set the numbers and names of columns in the table
        rows = max(len(data1), len(data2), len(data3), len(data4), len(data5))
        self.tableWidget.setRowCount(rows)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(['Data','Sys','Dia','Pulse','Weather pressure'])

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
            else:
                item5 = QTableWidgetItem('')
            self.tableWidget.setItem(row, 4, item5)



    def push_Save_clicked(self):
        sys_value = self.textEdit.text()
        dia_value = self.textEdit_2.text()
        pulse_value = self.textEdit_3.text()
        data_value = self.textEdit_4.text() 
    
        with open('weather_pressure.txt', 'a') as weatherpress_file:
            weatherpress_file.write(str(pressure_value) + '\n')
            print(str(pressure_value)+'Weather-tiedot saved')
            weatherpress_file.close()

        with open('sys.txt', 'a') as sysfile:
            sysfile.write(str(sys_value) + '\n')
            print('Sys-tiedot saved')
            sysfile.close()

        with open('dia.txt', 'a') as diafile:
            diafile.write(str(dia_value) + '\n')
            print('Dia-tiedot saved')
            diafile.close()

        with open('pulse.txt', 'a') as pulsefile:
            pulsefile.write(str(pulse_value) + '\n')
            print('Pulse-tiedot saved')
            pulsefile.close()
        
        with open('date.txt', 'a') as datefile:
            datefile.write(str(data_value) + '\n')
            print('Sys-tiedot saved')
            datefile.close()

        rowCount = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowCount)
        self.tableWidget.setItem(rowCount, 0, QTableWidgetItem(data_value))
        self.tableWidget.setItem(rowCount, 1, QTableWidgetItem(sys_value))
        self.tableWidget.setItem(rowCount, 2, QTableWidgetItem(dia_value))
        self.tableWidget.setItem(rowCount, 3, QTableWidgetItem(pulse_value))
        self.tableWidget.setItem(rowCount, 4, QTableWidgetItem(pressure_value))
        


    def push_Graph_clicked(self):
        selectedRows = set(index.row() for index in self.tableWidget.selectedIndexes())

        x = []
        y1 = []
        y2 = []
        y3 = []


        for row in range(self.tableWidget.rowCount()):
            if row in selectedRows:
                x.append(row)
                y1.append(float(self.tableWidget.item(row, 0).text()))
                y2.append(float(self.tableWidget.item(row, 1).text()))
                y3.append(float(self.tableWidget.item(row, 2).text()))
        
        plt.plot(x, y1, label='Field1')
        plt.plot(x, y2, label='Field2')
        plt.plot(x, y3, label='Field3')

        plt.xlabel('Row')
        plt.ylabel('Value')
        plt.title('Plot blood pressure data & weather pressure')
        plt.legend
        plt.show

    def push_Settings_clicked(self):
        pass




# def weather_pressure(self):                                     # OpenWeatherMap ilmapainetietoa hakeminen
owm =pyowm.OWM('f8c43bbd601d39c177afabec2d050d04')
mgr = owm.weather_manager()
weather_pressure = mgr.weather_at_place('Helsinki').weather.pressure  # 'weather', not 'observation'
pressure_value=weather_pressure['press']
# return pressure_value


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())

#  pyuic5 -o pyfilename.py design.ui  # Convert QT Desigenrfile to .py