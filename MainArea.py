from LogicArea import *

def main() -> None:
    '''
    This function sets up the Gui
    :return: None
    '''
    application = QApplication([])
    window = Logic()
    window.show()
    application.exec()

if __name__ == "__main__":
    main()