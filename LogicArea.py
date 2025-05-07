from PyQt6.QtWidgets import *
from GuiArea import *
from FunctionsArea import *

#TODO: Add type hinting, test new FunctionsArea functions, maybe add hiding if time allows

class Logic (QMainWindow, Ui_MainWindow):
    value = 0
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.label_number1.setText("")
        self.label_number2.setText("")
        self.label_number3.setText("")
        self.label_compute.setText("")

    def clear_inputs(self):
        self.input_number1.clear()
        self.input_number2.clear()
        self.input_number3.clear()

    def select(self):
        if self.radio_circle.isChecked():
            Logic.value = 1
            self.clear_inputs()
            self.label_number1.setText("Radius")
            self.label_number2.setText("")
            self.label_number3.setText("")

        elif self.radio_square.isChecked():
            Logic.value = 2
            self.clear_inputs()
            self.label_number1.setText("Side")
            self.label_number2.setText("")
            self.label_number3.setText("")

        elif self.radio_rectangle.isChecked():
            Logic.value = 3
            self.clear_inputs()
            self.label_number1.setText("Length")
            self.label_number2.setText("Width")
            self.label_number3.setText("")

        elif self.radio_triangle.isChecked():
            Logic.value = 4
            self.clear_inputs()
            self.label_number1.setText("Base")
            self.label_number2.setText("Height")
            self.label_number3.setText("")

        elif self.radio_rectangular_prism.isChecked():
            Logic.value = 5
            self.clear_inputs()
            self.label_number1.setText("Length")
            self.label_number2.setText("Width")
            self.label_number3.setText("Height")

        elif self.radio_cone.isChecked():
            Logic.value = 6
            self.clear_inputs()
            self.label_number1.setText("Radius")
            self.label_number2.setText("Height")
            self.label_number3.setText("Slant")

        elif self.radio_pyramid.isChecked():
            Logic.value = 7
            self.clear_inputs()
            self.label_number1.setText("Base Width")
            self.label_number2.setText("Height")
            self.label_number3.setText("Slant")

    def shape_calc(self):
        if Logic.value == 1:
            return circle(self.input_number1.text())
        elif Logic.value == 2:
            return square(self.input_number1.text())
        elif Logic.value == 3:
            return rectangle(self.input_number1.text(), self.input_number2.text())
        elif Logic.value == 4:
            return triangle(self.input_number1.text(), self.input_number2.text())

        if self.radio_area.isChecked():
            if Logic.value == 5:
                return rectangular_prism(self.input_number1.text(), self.input_number2.text(), self.input_number3.text())
            elif Logic.value == 6:
                return cone(self.input_number1.text(), self.input_number2.text(), self.input_number3.text())
            elif Logic.value == 7:
                return pyramid(self.input_number1.text(), self.input_number2.text(), self.input_number3.text())
        elif self.radio_surface_area.isChecked():
            if Logic.value == 5:
                return rectangular_prism_surface_area(self.input_number1.text(), self.input_number2.text(), self.input_number3.text())
            elif Logic.value == 6:
                return cone_surface_area(self.input_number1.text(), self.input_number2.text(), self.input_number3.text())
            elif Logic.value == 7:
                return pyramid_surface_area(self.input_number1.text(), self.input_number2.text(), self.input_number3.text())

    def submit(self):
        area_type = ''
        if self.radio_surface_area.isChecked():
            area_type = "Surface Area"
        elif self.radio_area.isChecked():
            area_type = "Area"
        try:
            if Logic.value == 1:
                self.label_compute.setText(f"Circle {area_type} = {self.shape_calc()}")
            elif Logic.value == 2:
                self.label_compute.setText(f"Square {area_type} = {self.shape_calc()}")
            elif Logic.value == 3:
                self.label_compute.setText(f"Rectangle {area_type} = {self.shape_calc()}")
            elif Logic.value == 4:
                self.label_compute.setText(f"Triangle {area_type} = {self.shape_calc()}")
            elif Logic.value == 5:
                self.label_compute.setText(f"Rect. Prism {area_type} = {self.shape_calc()}")
            elif Logic.value == 6:
                self.label_compute.setText(f"Cone {area_type} = {self.shape_calc()}")
            elif Logic.value == 7:
                self.label_compute.setText(f"Pyramid {area_type} = {self.shape_calc()}")
        except:
            self.label_output_2.setText("Please enter numeric, positive values.")

        self.clear_inputs()