import ecdsa
import os

# 1. ĐÃ SỬA ĐƯỜNG DẪN TẠO THƯ MỤC
if not os.path.exists('ecc/keys'):
    os.makedirs('ecc/keys')

class ECCCipher:
    def __init__(self):
        pass

    def generate_keys(self):
        sk = ecdsa.SigningKey.generate()        # Tạo khóa riêng tư
        vk = sk.get_verifying_key()             # Lấy khóa công khai từ khóa riêng tư

        # ĐÃ SỬA ĐƯỜNG DẪN LƯU FILE
        with open('ecc/keys/privateKey.pem', 'wb') as p:
            p.write(sk.to_pem())

        with open('ecc/keys/publicKey.pem', 'wb') as p:
            p.write(vk.to_pem())

    def load_keys(self):
        # ĐÃ SỬA ĐƯỜNG DẪN ĐỌC FILE
        with open('ecc/keys/privateKey.pem', 'rb') as p:
            sk = ecdsa.SigningKey.from_pem(p.read())

        with open('ecc/keys/publicKey.pem', 'rb') as p:
            vk = ecdsa.VerifyingKey.from_pem(p.read())
            
        return sk, vk

    def sign(self, message, key):
        # Ký dữ liệu bằng khóa riêng tư (Trả về định dạng bytes)
        return key.sign(message.encode('ascii'))

    def verify(self, message, signature, key):
        _, vk = self.load_keys()
        try:
            # Nhận signature định dạng bytes từ API và xác thực
            return vk.verify(signature, message.encode('ascii'))
        except ecdsa.BadSignatureError:
            return False