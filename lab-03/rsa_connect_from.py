import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.rsa import Ui_MainWindow

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Kết nối sự kiện (Đã sửa tên button cho khớp với rsa.py)
        self.ui.btn_gen_keys.clicked.connect(self.call_api_gen_keys)
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)
        self.ui.btn_sign.clicked.connect(self.call_api_sign)
        self.ui.btn_verify.clicked.connect(self.call_api_verify)

    def show_message(self, title, text, icon=QMessageBox.Information):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setIcon(icon)
        msg.setText(text)
        msg.exec_()

    def call_api_gen_keys(self):
        url = "http://127.0.0.1:5000/api/rsa/generate_keys"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                self.show_message("Thông báo", "Đã khởi tạo cặp khóa mới trên Server!")
            else:
                self.show_message("Lỗi", f"Server phản hồi lỗi: {response.status_code}", QMessageBox.Critical)
        except Exception as e:
            self.show_message("Lỗi kết nối", "Không thể kết nối đến Server Flask!", QMessageBox.Critical)

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/rsa/encrypt"
        payload = {
            "message": self.ui.txt_plain_text.toPlainText(),
            "key_type": "public"
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_cipher_text.setPlainText(data["encrypted_message"])
            else:
                self.show_message("Lỗi", "Mã hóa thất bại!")
        except Exception as e:
            print(f"Error: {e}")

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/rsa/decrypt"
        payload = {
            "ciphertext": self.ui.txt_cipher_text.toPlainText(),
            "key_type": "private"
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_plain_text.setPlainText(data["decrypted_message"])
            else:
                self.show_message("Lỗi", "Giải mã thất bại!")
        except Exception as e:
            print(f"Error: {e}")

    def call_api_sign(self):
        url = "http://127.0.0.1:5000/api/rsa/sign"
        # Sử dụng txt_sign cho nội dung cần ký
        payload = {"message": self.ui.txt_sign.toPlainText()}
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                # Hiển thị chữ ký vào ô txt_verify hoặc chính nó
                self.ui.txt_verify.setPlainText(data["signature"])
                self.show_message("Ký số", "Đã tạo chữ ký thành công!")
        except Exception as e:
            print(f"Error: {e}")

    def call_api_verify(self):
        url = "http://127.0.0.1:5000/api/rsa/verify"
        payload = {
            "message": self.ui.txt_sign.toPlainText(),
            "signature": self.ui.txt_verify.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                if data.get("is_verified"):
                    self.show_message("Xác thực", "Chữ ký HỢP LỆ ✅")
                else:
                    self.show_message("Xác thực", "Chữ ký KHÔNG hợp lệ ❌", QMessageBox.Warning)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())