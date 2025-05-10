from PyQt6.QtWidgets import *
from GuiArea import *
from FunctionsArea import *

class Logic (QMainWindow, Ui_MainWindow):
    value = 0
    def __init__(self) -> None:
        """
        This function sets up the Gui and sets the Gui's
        labels to their defaults
        :return: None
        """
        super().__init__()
        self.setupUi(self)

        self.label_number1.setText("")
        self.label_number2.setText("")
        self.label_number3.setText("")
        self.label_compute.setText("")
        self.label_output_2.setText("Output:")

    def clear_inputs(self) -> None:
        """
        This function clears the number input boxes
        :return: None
        """
        self.input_number1.clear()
        self.input_number2.clear()
        self.input_number3.clear()

    def select(self) -> None:
        """
        This function handles the logic for selecting the different
        radio buttons and setting the text for the
        number input boxes accordingly
        :return: None
        """
        if self.radio_circle.isChecked():
            Logic.value = 1
            self.clear_inputs()
            self.label_number1.setText("Radius")
            self.label_number2.setText("")
            self.label_number3.setText("")
            self.input_number2.hide()
            self.input_number3.hide()
            self.radio_surface_area.hide()
            self.radio_area.hide()
            self.label_area_or_surface_area.hide()
            self.button_compute.setText("3. COMPUTE")

        elif self.radio_square.isChecked():
            Logic.value = 2
            self.clear_inputs()
            self.label_number1.setText("Side")
            self.label_number2.setText("")
            self.label_number3.setText("")
            self.input_number2.hide()
            self.input_number3.hide()
            self.radio_surface_area.hide()
            self.radio_area.hide()
            self.label_area_or_surface_area.hide()
            self.button_compute.setText("3. COMPUTE")

        elif self.radio_rectangle.isChecked():
            Logic.value = 3
            self.clear_inputs()
            self.label_number1.setText("Length")
            self.label_number2.setText("Width")
            self.label_number3.setText("")
            self.input_number2.show()
            self.input_number3.hide()
            self.radio_surface_area.hide()
            self.radio_area.hide()
            self.label_area_or_surface_area.hide()
            self.button_compute.setText("3. COMPUTE")

        elif self.radio_triangle.isChecked():
            Logic.value = 4
            self.clear_inputs()
            self.label_number1.setText("Base")
            self.label_number2.setText("Height")
            self.label_number3.setText("")
            self.input_number2.show()
            self.input_number3.hide()
            self.radio_surface_area.hide()
            self.radio_area.hide()
            self.label_area_or_surface_area.hide()
            self.button_compute.setText("3. COMPUTE")

        elif self.radio_rectangular_prism.isChecked():
            Logic.value = 5
            self.clear_inputs()
            self.label_number1.setText("Length")
            self.label_number2.setText("Width")
            self.label_number3.setText("Height")
            self.input_number2.show()
            self.input_number3.show()
            self.radio_surface_area.show()
            self.radio_area.show()
            self.radio_area.setText("Volume")
            self.label_area_or_surface_area.show()
            self.label_area_or_surface_area.setText("3. Would you like volume or surface area?")
            self.button_compute.setText("4. COMPUTE")

        elif self.radio_cone.isChecked():
            Logic.value = 6
            self.clear_inputs()
            self.label_number1.setText("Radius")
            self.label_number2.setText("Height")
            self.label_number3.setText("Slant")
            self.input_number2.show()
            self.input_number3.show()
            self.radio_surface_area.show()
            self.radio_area.show()
            self.radio_area.setText("Volume")
            self.label_area_or_surface_area.show()
            self.label_area_or_surface_area.setText("3. Would you like volume or surface area?")
            self.button_compute.setText("4. COMPUTE")


        elif self.radio_pyramid.isChecked():
            Logic.value = 7
            self.clear_inputs()
            self.label_number1.setText("Base")
            self.label_number2.setText("Height")
            self.label_number3.setText("Slant")
            self.input_number2.show()
            self.input_number3.show()
            self.radio_surface_area.show()
            self.radio_area.show()
            self.radio_area.setText("Volume")
            self.label_area_or_surface_area.show()
            self.label_area_or_surface_area.setText("3. Would you like volume or surface area?")
            self.button_compute.setText("4. COMPUTE")


    def shape_calc(self) -> float:
        """
        This function deals with computing the end result of the
        user's input by using functions in the FunctionsArea file
        :return: The area or surface area of the user's shape
        """
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

    def submit(self) -> None:
        """
        This function calls the shape_calc() function and contains
        the logic needed to output the correct phrases according to
        the user's shape.  It also clears all the inputs and is
        attached to the calculate button.
        :return: None
        """
        area_type = ''
        if self.radio_surface_area.isChecked():
            area_type = "Surface Area"
        elif self.radio_area.isChecked():
            area_type = "Area"
        try:
            if Logic.value == 1:
                self.label_compute.setText(f"Circle {area_type} = {self.shape_calc():.3f}")
            elif Logic.value == 2:
                self.label_compute.setText(f"Square {area_type} = {self.shape_calc():.3f}")
            elif Logic.value == 3:
                self.label_compute.setText(f"Rectangle {area_type} = {self.shape_calc():.3f}")
            elif Logic.value == 4:
                self.label_compute.setText(f"Triangle {area_type} = {self.shape_calc():.3f}")
            elif Logic.value == 5:
                self.label_compute.setText(f"Rect. Prism {area_type} = {self.shape_calc():.3f}")
            elif Logic.value == 6:
                self.label_compute.setText(f"Cone {area_type} = {self.shape_calc():.3f}")
            elif Logic.value == 7:
                self.label_compute.setText(f"Pyramid {area_type} = {self.shape_calc():.3f}")
            self.label_output_2.setText("Output:")
        except:
            self.label_output_2.setText("Numeric, positive values ONLY.")
            self.label_compute.setText("")

        self.clear_inputs()