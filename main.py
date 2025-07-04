from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit ,QFileDialog, QMenuBar
from PyQt5.QtGui import QFont, QTextOption
from PyQt5.uic import loadUi
import sys

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        # Load the UI file
        loadUi("interface.ui", self)

        # Set the initial title of window
        self.setWindowTitle("Untitled - WritePad")

        # Define our widgets or Variables
        self.editText = self.findChild(QTextEdit, "textEdit")
        self.menu = self.findChild(QMenuBar, "menubar")
        self.fileName = None
        self.wordwrap = True
        self.defaultfont = QFont("Arial", 12)
        self.smallfont = QFont("Arial", 8)
        self.bigfont = QFont("Arial", 16)
        self.largefont = QFont("Arial", 24)

        # Set the font size of edit area
        self.editText.setFont(self.defaultfont)

        # Add functions to all actions
        self.actionNew.triggered.connect(self.newFile)
        self.actionSave.triggered.connect(self.saveFile)
        self.actionSave_as.triggered.connect(self.saveAs)
        self.actionOpen.triggered.connect(self.openFile)
        self.actionExit.triggered.connect(self.windowClose)
        self.actionUndo.triggered.connect(self.undoText)
        self.actionCut.triggered.connect(self.cutText)
        self.actionCopy.triggered.connect(self.copyText)
        self.actionPaste.triggered.connect(self.pasteText)
        self.actionSelect_All.triggered.connect(self.selectallText)
        self.actionWord_Rap.triggered.connect(self.wordwrapText)
        self.actionLight.triggered.connect(self.lightTheme)
        self.actionDark.triggered.connect(self.darkTheme)
        self.actionSmall.triggered.connect(self.setSmallFont)
        self.actionBig.triggered.connect(self.setBigFont)
        self.actionLarge.triggered.connect(self.setLargeFont)
        self.actionDefault.triggered.connect(self.setDefaultFont)

        # Show the Ui file
        self.show()

    def newFile(self):
        # Set the window title
        self.setWindowTitle("Untitled - WritePad")
        # Clear the text edit's text
        self.editText.clear()

    def openFile(self):
        # Open the file dialog to ask the file which y9ou want to open 
        self.fileName = QFileDialog.getOpenFileName(self, "Open File", "C:\\Users\\Firasat ali jhuih\\Documents", "Text Files (*.txt) ;; Python Files (*.py) ;; Ui Files (*.ui)")[0]
        # Get the text from file
        with open(self.fileName, "r") as f:
            # Get the text from the file
            text = f.read()
            # Put the text into the textEdit
            self.editText.setPlainText(text)
        
        # Set the window tilte
        self.setWindowTitle(self.fileName + " - " + "WritePad")

    def saveFile(self):
        # Check the path is present
        if self.fileName is not None:
            # Grab the text from fileEdit
            text = self.editText.toPlainText()
            # Save file
            with open(self.fileName, "w") as f:
                f.write(text)
            # Set the window tilte
            self.setWindowTitle(self.fileName + " - " + "WritePad")
        else:
            self.saveAs()

    def saveAs(self):
        # Open the file dialog to save file
        self.fileName = QFileDialog.getSaveFileName(self, "Save As", "C:\\Users\\Firasat ali jhuih\\Documents", "Text Files (*.txt) ;; Python Files (*.py) ;; Ui Files (*.ui)")[0]
        
        # Grab the text from fileEdit
        text = self.editText.toPlainText()
        # Save file
        with open(self.fileName, "w") as f:
            f.write(text)
        # Set the window tilte
        self.setWindowTitle(self.fileName + " - " + "WritePad")
        
    def windowClose(self):
        # Destroy the main window and exit
        sys.exit(self.destroy())

    def undoText(self):
        self.editText.undo()

    def cutText(self):
        self.editText.cut()

    def copyText(self):
        self.editText.copy()

    def pasteText(self):
        self.editText.paste()

    def selectallText(self):
        self.editText.selectAll()

    def wordwrapText(self):
        if self.wordwrap:
            self.editText.setWordWrapMode(QTextOption.NoWrap)
            self.wordwrap = False
        else:
            self.editText.setWordWrapMode(QTextOption.WordWrap)
            self.wordwrap = True

    def lightTheme(self):
        # Reset the style of text edit
        self.setStyleSheet("")
        # Reset the style of Qmenubar
        self.menu.setStyleSheet("")
    
    def darkTheme(self):
        # Set the style of text edit
        self.setStyleSheet("background-color:rgb(39, 39, 39);color:white;")
        # Set the style of Qmenubar
        self.menu.setStyleSheet(
        """
        QMenuBar {background-color:rgb(39, 39, 39);color:white;}
        QMenuBar::item:selected {color: black;}
        """
        )

    def setSmallFont(self):
        self.editText.setFont(self.smallfont)
    
    def setBigFont(self):
        self.editText.setFont(self.bigfont)
        
    def setLargeFont(self):
        self.editText.setFont(self.largefont)
        
    def setDefaultFont(self):
        self.editText.setFont(self.defaultfont)
        
if __name__ == "__main__":
    # Create the Application 
    app = QApplication(sys.argv)
    # Create the Ui
    ui = Ui_MainWindow()
    # Execute the application
    app.exec_()