import pytest

from PyQt5 import QtCore # QtTest

import mainApp


@pytest.fixture
def app(qtbot):
    test_app = mainApp.HomeWindow()
    qtbot.add_widget(test_app)

    return test_app


def test_HomeWindow(app):
    assert app.pushButton1.text() == "View"
    assert app.pushButton2.text() == "Count"

def test_HomeWindow_AfterClick(qtbot, app):
    qtbot.mouseClick(app.pushButton2, QtCore.Qt.LeftButton)
    assert app.w.selectButton.text() == "Select"
    assert app.w.pushButton2.text() == "Run"
    assert app.w.pushButton3.text() == "Back"

def test_CountWindow_AfterClick(qtbot, app):
    qtbot.mouseClick(app.pushButton2, QtCore.Qt.LeftButton)
    qtbot.mouseClick(app.w.pushButton2, QtCore.Qt.LeftButton)
    assert app.w.w.pushButton1.text() == "Update"
    assert app.w.w.pushButton2.text() == "Back"