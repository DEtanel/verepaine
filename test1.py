from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QTableWidgetItem, QMainWindow , QFileDialog
from Ui_mainwindow import Ui_MainWindow
import sys
# import csv
import matplotlib.pyplot as plt



class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.push_Save_clicked)
        self.pushButton_2.clicked.connect(self.push_Graph_clicked)
        self.tableWidget.setHorizontalHeaderLabels(['Data','Sys','Dia','Pulse'])
        

# Дебаггер жалуется, что не находит местоположение txt-файлов, несмотря на работу программы
        with open('date.txt', 'r') as f1, open('sys.txt', 'r') as f2, open('dia.txt', 'r') as f3, open('pulse.txt','r') as f4 :
            data1 = f1.readlines()
            data2 = f2.readlines()
            data3 = f3.readlines()
            data4 = f4.readlines()

        # Set the number of rows and columns in the table
        rows = max(len(data1), len(data2), len(data3), len(data4))
        self.tableWidget.setRowCount(rows)
        self.tableWidget.setColumnCount(4)

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

        # Resize the columns to fit the contents
        # self.tableWidget.resizeColumnsToContents()


####  REVERSE ORDER of Data view doesnt work! Why??? #####
# # read lines from each file into a separate list and reverse the order of each list
#         with open('date.txt', 'r') as f1, open('sys.txt', 'r') as f2, open('dia.txt', 'r') as f3:
#             lines1 = f1.readlines()[::-1]
#             lines2 = f2.readlines()[::-1]
#             lines3 = f3.readlines()[::-1]

# # interleave the lines from the three lists to create a new list in reverse order
#             combined_lines = []
#             for line1, line2, line3 in zip(lines1, lines2, lines3):
#                 combined_lines.append(line1.strip() + '\t' + line2.strip() + '\t' + line3.strip() + '\n')

#             # populate the table using the reversed list
#             for i, line in enumerate(reversed(combined_lines)):
#                 # create a new row in the table
#                 row_position = self.tableWidget.rowCount()
#                 self.tableWidget.insertRow(row_position)

#                 # split the line into columns
#                 columns = line.strip().split('\t')

#                 # populate the cells in the new row
#                 for j, column in enumerate(columns):
#                     cell = QTableWidgetItem(column)
#                     self.tableWidget.setItem(row_position, j, cell)




    def push_Save_clicked(self):
        sys_value=self.textEdit.text()
        dia_value=self.textEdit_2.text()
        pulse_value=self.textEdit_3.text()
        data_value=self.textEdit_4.text()

        rowCount = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowCount)
        self.tableWidget.setItem(rowCount, 0, QTableWidgetItem(data_value))
        self.tableWidget.setItem(rowCount, 1, QTableWidgetItem(sys_value))
        self.tableWidget.setItem(rowCount, 2, QTableWidgetItem(dia_value))
        self.tableWidget.setItem(rowCount, 3, QTableWidgetItem(pulse_value))

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


    def push_Graph_clicked(self):
        selectedRows = set(index.row() for index in self.tableWidget.selectedIndexes())

        x = []
        y1 = []
        y2 = []
        y3 = []

 # !!!!  Здесь сделать возможность регулировки смещения по дате на 1-2 дня взятых (и сохраняемых в отдельный weaterpress.txt)
 #  с интернет-метеоресурса/сайта данных давления воздуха в регионе (тоже где-то прописать в переменную, вставляемую в API-запрос )


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


# Сделать возможность очищения сохранённых в txt-файлы данных
# For button "Clear Data"
#   def push_ClearData_clicked(self):
#       pass



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())