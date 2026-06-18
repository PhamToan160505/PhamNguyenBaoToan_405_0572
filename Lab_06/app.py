# ==========================================
# Developer: Phạm Nguyễn Bảo Toàn
# Student ID: 2380610572
# Project: Crypto GUI (Transposition & ECC)
# ==========================================

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

# Import file UI
from transposition.transposition_ui import Ui_MainWindow as Ui_TransMainWindow
from ecc.ecc_ui import Ui_MainWindow as Ui_ECCMainWindow 

# Import API
from api import CryptoAPI 

# ==========================================
# FORM TRANSPOSITION
# ==========================================
class TranspositionApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TransMainWindow()
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
            result = CryptoAPI.process_trans_encryption(text, key)
            
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
            result = CryptoAPI.process_trans_decryption(text, key)
            
            if result["status"] == "success":
                self.ui.txtOutput.setPlainText(result["data"])
            else:
                QMessageBox.critical(self, "Lỗi thuật toán", result["message"])

        except ValueError:
            QMessageBox.warning(self, "Lỗi", "Khóa (Key) phải là một số nguyên!")


# ==========================================
# FORM ECC (Chữ ký điện tử)
# ==========================================
class ECCApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ECCMainWindow()
        self.ui.setupUi(self)

        # Đã cập nhật đúng tên object từ ecc.ui của bạn
        self.ui.btn_gen_keys.clicked.connect(self.handle_genkey)
        self.ui.btn_sign.clicked.connect(self.handle_sign)
        self.ui.btn_verify.clicked.connect(self.handle_verify)

    def handle_genkey(self):
        result = CryptoAPI.generate_ecc_keys()
        if result["status"] == "success":
            QMessageBox.information(self, "Thành công", result["message"])
        else:
            QMessageBox.critical(self, "Lỗi", result["message"])

    def handle_sign(self):
        message = self.ui.txt_info.toPlainText().strip()
        
        if not message:
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng nhập văn bản cần ký vào ô Information!")
            return

        result = CryptoAPI.process_ecc_sign(message)
        
        if result["status"] == "success":
            self.ui.txt_sign.setPlainText(result["data"])
        else:
            QMessageBox.critical(self, "Lỗi", result["message"])

    def handle_verify(self):
        message = self.ui.txt_info.toPlainText().strip()
        signature = self.ui.txt_sign.toPlainText().strip()

        if not message or not signature:
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng nhập đủ Information và Signature!")
            return

        result = CryptoAPI.process_ecc_verify(message, signature)
        
        if result["status"] == "success":
            if result["data"] is True:
                QMessageBox.information(self, "Kết quả", "✅ Xác thực THÀNH CÔNG! Chữ ký hợp lệ.")
            else:
                QMessageBox.warning(self, "Kết quả", "❌ Xác thực THẤT BẠI! Chữ ký sai hoặc văn bản đã bị sửa.")
        else:
            QMessageBox.critical(self, "Lỗi", result["message"])


# ==========================================
# KHỞI CHẠY CHƯƠNG TRÌNH
# ==========================================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # window = TranspositionApp()  # Tạm ẩn Transposition
    window = ECCApp()              # Mở form ECC
    
    window.show()
    sys.exit(app.exec_())