from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QPushButton, QLabel
from PySide6.QtCore import QFile, QIODevice
import sys
import itertools
import random

ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
suits = ["♣", "♦", "♥", "♠"]

deck = [f"{rank}{suit}" for rank, suit in itertools.product(ranks, suits)]
HAND_SIZE = 5


class UI:
    def __init__(self):
        app = QApplication(sys.argv)

        ui_file_name = "poker_hand.ui"
        ui_file = QFile(ui_file_name)
        if not ui_file.open(QIODevice.OpenModeFlag.ReadOnly):
            print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
            sys.exit(-1)

        loader = QUiLoader()
        window = loader.load(ui_file)
        ui_file.close()

        if not window:
            print(loader.errorString())
            sys.exit(-1)
        window.show()

        self.deal_btn: QPushButton | None = window.findChild(QPushButton, "dealButton")
        self.hand_label = window.findChild(QLabel, "handLabel")

        if self.deal_btn is None:
            print("Push button could not be found!")
            sys.exit(-1)
        self.deal_btn.clicked.connect(self.deal_hand)

        sys.exit(app.exec())

    def deal_hand(self):
        random.shuffle(deck)
        hand = deck[:HAND_SIZE]

        if self.hand_label is None:
            print("Hand label could not be found!")
            sys.exit(-1)
        self.hand_label.setText(", ".join(hand))


if __name__ == "__main__":
    my_ui = UI()
