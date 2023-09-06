#THISISZERONELABS

from PyQt5 import QtCore, QtGui, QtWidgets
import GPUtil
import subprocess
import psutil
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1153, 593)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1040, 460, 121, 151))
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setPixmap(QtGui.QPixmap("/home/zerone/ztos_stuff/zrn_logo_no_back.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-10, 10, 401, 231))
        self.label_2.setStyleSheet("font: 75 20pt \"Share Tech Mono\";\n"
"color: rgb(154, 153, 150);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(790, 50, 121, 31))
        self.label_3.setStyleSheet("font: 57 15pt \"Space Grotesk Light\";\n"
"color: rgb(154, 153, 150);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(790, 100, 121, 31))
        self.label_4.setStyleSheet("font: 57 10pt \"Space Grotesk Light\";\n"
"color: rgb(154, 153, 150);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(530, 10, 141, 31))
        self.label_5.setStyleSheet("font: 57 15pt \"Space Grotesk Light\";\n"
"color: rgb(154, 153, 150);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(670, 60, 121, 31))
        self.label_6.setStyleSheet("font: 57 10pt \"Space Grotesk Light\";\n"
"color: rgb(154, 153, 150);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(530, 150, 141, 31))
        self.label_7.setStyleSheet("font: 57 15pt \"Space Grotesk Light\";\n"
"color: rgb(154, 153, 150);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(530, 60, 121, 31))
        self.label_8.setStyleSheet("font: 57 10pt \"Space Grotesk Light\";\n"
"color: rgb(154, 153, 150);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(980, 10, 31, 31))
        self.label_9.setStyleSheet("font: 57 10pt \"Space Grotesk Light\";\n"
"color: rgb(154, 153, 150);")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(530, 100, 121, 31))
        self.label_10.setStyleSheet("font: 57 10pt \"Space Grotesk Light\";\n"
"color: rgb(154, 153, 150);")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(670, 100, 121, 31))
        self.label_11.setStyleSheet("font: 57 10pt \"Space Grotesk Light\";\n"
"color: rgb(154, 153, 150);")
        self.label_11.setObjectName("label_11")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(670, 190, 121, 31))
        self.label_13.setStyleSheet("font: 57 10pt \"Space Grotesk Light\";\n"
"color: rgb(154, 153, 150);")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(530, 230, 121, 31))
        self.label_14.setStyleSheet("font: 57 10pt \"Space Grotesk Light\";\n"
"color: rgb(154, 153, 150);")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(670, 230, 121, 31))
        self.label_15.setStyleSheet("font: 57 10pt \"Space Grotesk Light\";\n"
"color: rgb(154, 153, 150);")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(530, 340, 611, 31))
        self.label_16.setStyleSheet("font: 57 15pt \"Space Grotesk Light\";\n"
"color: rgb(154, 153, 150);")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(530, 390, 121, 31))
        self.label_17.setStyleSheet("font: 57 10pt \"Space Grotesk Light\";\n"
"color: rgb(154, 153, 150);")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(810, 200, 151, 21))
        self.label_18.setStyleSheet("font: 57 10pt \"Space Grotesk Light\";\n"
"color: rgb(154, 153, 150);")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(980, 200, 71, 21))
        self.label_19.setStyleSheet("font: 57 10pt \"Space Grotesk Light\";\n"
"color: rgb(154, 153, 150);")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(670, 390, 121, 31))
        self.label_20.setStyleSheet("font: 57 10pt \"Space Grotesk Light\";\n"
"color: rgb(154, 153, 150);")
        self.label_20.setObjectName("label_20")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 390, 171, 51))
        self.pushButton.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-color: rgb(192, 191, 188);\n"
"font: 11pt \"Space Grotesk Light\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 330, 171, 51))
        self.pushButton_2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-color: rgb(192, 191, 188);\n"
"font: 11pt \"Space Grotesk Light\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 330, 171, 51))
        self.pushButton_3.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-color: rgb(192, 191, 188);\n"
"font: 11pt \"Space Grotesk Light\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(380, 10, 121, 121))
        self.label_22.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_22.setText("")
        self.label_22.setTextFormat(QtCore.Qt.RichText)
        self.label_22.setPixmap(QtGui.QPixmap("/home/zerone/ZeroneApps/cpu.png"))
        self.label_22.setScaledContents(True)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(380, 150, 121, 121))
        self.label_23.setText("")
        self.label_23.setPixmap(QtGui.QPixmap("/home/zerone/ZeroneApps/gpu.png"))
        self.label_23.setScaledContents(True)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(380, 330, 121, 121))
        self.label_24.setText("")
        self.label_24.setPixmap(QtGui.QPixmap("/home/zerone/ZeroneApss/ram.png"))
        self.label_24.setScaledContents(True)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(810, 230, 151, 31))
        self.label_25.setStyleSheet("font: 57 10pt \"Space Grotesk Light\";\n"
"color: rgb(154, 153, 150);")
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(980, 230, 71, 31))
        self.label_26.setStyleSheet("font: 57 10pt \"Space Grotesk Light\";\n"
"color: rgb(154, 153, 150);")
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(650, 150, 521, 31))
        self.label_27.setStyleSheet("font: 20 15pt \"Space Grotesk Light\";\n"
"color: rgb(154, 153, 150);")
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setGeometry(QtCore.QRect(650, 10, 311, 31))
        self.label_28.setStyleSheet("font: 57 15pt \"Space Grotesk Light\";\n"
"color: rgb(154, 153, 150);")
        self.label_28.setObjectName("label_28")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(530, 190, 121, 31))
        self.label_12.setStyleSheet("font: 57 10pt \"Space Grotesk Light\";\n"
"color: rgb(154, 153, 150);")
        self.label_12.setObjectName("label_12")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(1040, 190, 111, 31))
        self.progressBar.setStyleSheet("")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.progressBar_2 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_2.setGeometry(QtCore.QRect(1040, 232, 111, 31))
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName("progressBar_2")
        self.progressBar_3 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_3.setGeometry(QtCore.QRect(810, 390, 331, 31))
        self.progressBar_3.setProperty("value", 24)
        self.progressBar_3.setObjectName("progressBar_3")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(390, 130, 761, 21))
        self.line.setStyleSheet("color: rgb(255, 255, 255);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(400, 310, 761, 21))
        self.line_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(530, 270, 121, 31))
        self.label_21.setStyleSheet("font: 57 10pt \"Space Grotesk Light\";\n"
"color: rgb(154, 153, 150);")
        self.label_21.setObjectName("label_21")
        self.progressBar_4 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_4.setGeometry(QtCore.QRect(610, 270, 541, 31))
        self.progressBar_4.setProperty("value", 24)
        self.progressBar_4.setObjectName("progressBar_4")
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.label_16.raise_()
        self.label_17.raise_()
        self.label_18.raise_()
        self.label_19.raise_()
        self.label_20.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.label_22.raise_()
        self.label_23.raise_()
        self.label_24.raise_()
        self.label_25.raise_()
        self.label_27.raise_()
        self.label_28.raise_()
        self.label_26.raise_()
        self.label_12.raise_()
        self.progressBar.raise_()
        self.progressBar_2.raise_()
        self.progressBar_3.raise_()
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setGeometry(QtCore.QRect(910, 50, 81, 81))
        self.label_29.setText("")
        self.label_29.setTextFormat(QtCore.Qt.RichText)
        self.label_29.setPixmap(QtGui.QPixmap("/home/zerone/ZeroneApps/test.png"))
        self.label_29.setScaledContents(True)
        self.label_29.setObjectName("label_29")

        self.line.raise_()
        self.line_2.raise_()
        self.label_21.raise_()
        self.progressBar_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self._update_timer = QtCore.QTimer()
        self._update_timer.timeout.connect(self.gpu_stat)
        self._update_timer.timeout.connect(self.get_gpu_core_clock_speed)
        self._update_timer.timeout.connect(self.get_gpu_memory_clock_speed)
        self._update_timer.timeout.connect(self.get_cpu_clock_speed)
        self._update_timer.timeout.connect(self.get_cpu_temperature)
        self._update_timer.timeout.connect(self.get_ram_info)
        self._update_timer.timeout.connect(self.get_gpu_utilization)
        self._update_timer.timeout.connect(self.read_file_content)
        self._update_timer.start(0)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def gpu_stat(self):
        gpus = GPUtil.getGPUs()
        if len(gpus) > 0:
                gpu  = gpus[0]
                gputemp = str(gpu.temperature)
                gpumem = str(gpu.memoryUsed)+" MB"
                self.label_26.setText(gputemp)
                pass_progress = int(round(float(gputemp)))
                self.progressBar_2.setValue(pass_progress)
                self.label_19.setText(gpumem)
                self.progressBar.setValue(int(round(gpu.memoryUtil*100)))

        else:
                self.label_27.setText("ONBOARD CARD / ! \\")
    def get_gpu_core_clock_speed(self):
        try:
                output = subprocess.check_output(["nvidia-smi", "--query-gpu=clocks.current.sm", "--format=csv,noheader"])
                output = output.decode("utf-8").strip()
                send_data = str(output.split()[0])+" MHZ"
                self.label_13.setText(send_data)
        except (subprocess.CalledProcessError, FileNotFoundError):
                print("An error occured !")
    def get_gpu_memory_clock_speed(self):
        try:
                output = subprocess.check_output(["nvidia-smi", "--query-gpu=clocks.mem", "--format=csv,noheader"])
                output = output.decode("utf-8").strip()
                send_data = str(output.split()[0])+" MHZ"
                self.label_15.setText(send_data)
        except (subprocess.CalledProcessError, FileNotFoundError):
                return None
    def get_cpu_clock_speed(self):
        cpu_info = psutil.cpu_freq()
        send_data = str(round(cpu_info.current)) + 'MHZ'
        self.label_6.setText(send_data)
    def get_cpu_temperature(self):
        temperature_info = psutil.sensors_temperatures()
        if "coretemp" in temperature_info:
                cpu_temperatures = temperature_info["coretemp"]
                for entry in cpu_temperatures:
                        if "Package" in entry.label:
                                self.label_11.setText(str(entry.current))
        return None
    def get_ram_info(self):
        ram_info = psutil.virtual_memory()
        get_mem = str(round(float(ram_info.available))) + 'KB'
        self.label_20.setText(get_mem)
        self.progressBar_3.setValue(int(round(ram_info.percent)))
    def get_gpu_utilization(self):
        try:
                output = subprocess.check_output(['nvidia-smi'])
                output_lines = output.decode('utf-8').strip().split('\n')
                gpu_utilization = None
                for line in output_lines:
                        if 'P0' in line:
                                gpu_utilization = int(line.split()[11].strip('%'))
                                break
                self.progressBar_4.setValue(gpu_utilization)
        except :
                self.progressBar_4.setValue(0)
    def read_file_content(self):
        try:
            with open("/home/zerone/ZeroneApps/fan_dump.txt", "r") as file:
                content = file.read()
                self.label_4.setText(content)
        except FileNotFoundError:
            self.textLabel_4.setText("File not found")
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HARDWARE MONITORING SYSTEM INTERFACE"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">z t O S</span></p><p align=\"center\"><span style=\" font-weight:600;\">H M S</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "FAN RPM :"))
        self.label_4.setText(_translate("MainWindow", "0 RPM"))
        self.label_5.setText(_translate("MainWindow", "CPU :"))
        self.label_6.setText(_translate("MainWindow", "0 GHZ"))
        self.label_7.setText(_translate("MainWindow", "GPU :"))
        self.label_8.setText(_translate("MainWindow", "Clock Speed"))
        self.label_9.setText(_translate("MainWindow", "x8"))
        self.label_10.setText(_translate("MainWindow", "Temperature"))
        self.label_11.setText(_translate("MainWindow", "0 C"))
        self.label_13.setText(_translate("MainWindow", "0 GHZ"))
        self.label_14.setText(_translate("MainWindow", "Memory Clock"))
        self.label_15.setText(_translate("MainWindow", "0 GHZ"))
        self.label_16.setText(_translate("MainWindow", "RANDOM ACCESS : 8GB"))
        self.label_17.setText(_translate("MainWindow", "Load"))
        self.label_18.setText(_translate("MainWindow", "Memory Usage"))
        self.label_19.setText(_translate("MainWindow", "0 MB"))
        self.label_20.setText(_translate("MainWindow", "0MB"))
        self.pushButton.setText(_translate("MainWindow", "SYSTEM REBOOT"))
        self.pushButton_2.setText(_translate("MainWindow", "POWER MANAGEMENT"))
        self.pushButton_3.setText(_translate("MainWindow", "GPU STATUS"))
        self.label_25.setText(_translate("MainWindow", "Temperature"))
        self.label_26.setText(_translate("MainWindow", "0 C"))
        self.label_27.setText(_translate("MainWindow", "NVIDIA HIGH PERFORMANCE PROCESSOR [CURRENT]"))
        self.label_28.setText(_translate("MainWindow", "INTEL i5 tigerLake PROCESSOR"))
        self.label_12.setText(_translate("MainWindow", "Core Clock"))
        self.label_21.setText(_translate("MainWindow", "Utilization :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
