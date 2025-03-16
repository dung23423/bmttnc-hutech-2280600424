import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.caesar import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Kết nối sự kiện cho các nút bấm
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)  # Mã hóa
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)  # Giải mã

    def get_key(self):
        """ Lấy và kiểm tra khóa có hợp lệ không """
        key_text = self.ui.txt_key.toPlainText().strip()
        if not key_text.isdigit():
            QMessageBox.warning(self, "Invalid Key", "Key must be an integer!")
            return None
        return int(key_text)

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/encrypt"
        key = self.get_key()
        if key is None: return  # Nếu key không hợp lệ, thoát luôn
        
        payload = {
            "plain_text": self.ui.txt_plain_text.toPlainText().strip(),
            "key": key
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_cipher_text.setPlainText(data.get("encrypted_message", "Error: No response data"))

                QMessageBox.information(self, "Success", "Encrypted Successfully")
            else:
                QMessageBox.critical(self, "Error", f"Encryption failed!\n{response.text}")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Request Error: {str(e)}")

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/decrypt"
        key = self.get_key()
        if key is None: return  # Nếu key không hợp lệ, thoát luôn

        payload = {
            "cipher_text": self.ui.txt_cipher_text.toPlainText().strip(),
            "key": key
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_plain_text.setPlainText(data.get("decrypted_message", "Error: No response data"))

                QMessageBox.information(self, "Success", "Decrypted Successfully")
            else:
                QMessageBox.critical(self, "Error", f"Decryption failed!\n{response.text}")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Request Error: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
