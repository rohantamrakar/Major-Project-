import integrationMethods
from PyQt5 import QtGui
from PyQt5.QtWidgets import QFileDialog

class Selector:
    def pick_new(self):
        dialog = QFileDialog()
        folder_path = dialog.getExistingDirectory(None, "Select Folder")
        return folder_path