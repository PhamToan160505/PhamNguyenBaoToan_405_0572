# ==========================================
# Developer: Phạm Nguyễn Bảo Toàn
# Student ID: 2380610572
# Project: Transposition Cipher UI via API
# ==========================================

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

# Import file UI
from transposition.transposition_ui import Ui_MainWindow 
# CHỈ import API, KHÔNG import file logic trực tiếp
from api import CryptoAPI 

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnEncrypt.clicked.connect(self.handle_encrypt)
        self.ui.btnDecrypt.clicked.connect(self.handle_decrypt)

    def handle_encrypt(self):
        text = self.ui.txtInput.toPlainText().strip() 
        key_str = self.ui.txtKey.toPlainText().strip() 

        if not text or not key_str:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đủ văn bản và khóa!")
            return

        try:
            key = int(key_str)
            # Gọi hàm từ api.py
            result = CryptoAPI.process_trans_encryption(text, key)
            
            # Xử lý kết quả trả về từ API
            if result["status"] == "success":
                self.ui.txtOutput.setPlainText(result["data"])
            else:
                QMessageBox.critical(self, "Lỗi thuật toán", result["message"])

        except ValueError:
            QMessageBox.warning(self, "Lỗi", "Khóa (Key) phải là một số nguyên!")

    def handle_decrypt(self):
        text = self.ui.txtInput.toPlainText().strip() 
        key_str = self.ui.txtKey.toPlainText().strip() 

        if not text or not key_str:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đủ văn bản và khóa!")
            return

        try:
            key = int(key_str)
            # Gọi hàm từ api.py
            result = CryptoAPI.process_trans_decryption(text, key)
            
            # Xử lý kết quả trả về từ API
            if result["status"] == "success":
                self.ui.txtOutput.setPlainText(result["data"])
            else:
                QMessageBox.critical(self, "Lỗi thuật toán", result["message"])

        except ValueError:
            QMessageBox.warning(self, "Lỗi", "Khóa (Key) phải là một số nguyên!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())