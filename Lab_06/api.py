from transposition.transposition_cipher import TranspositionCipher 
from ecc.ecc_cipher import ECCCipher
class CryptoAPI:
    @staticmethod
    def process_trans_encryption(plaintext, key):
        try:
            cipher = TranspositionCipher()
            ciphertext = cipher.encrypt(plaintext, key)
            return {"status": "success", "data": ciphertext}
        except Exception as e:
            return {"status": "error", "message": f"Lỗi mã hóa: {str(e)}"}

    @staticmethod
    def process_trans_decryption(ciphertext, key):
        try:
            cipher = TranspositionCipher()
            plaintext = cipher.decrypt(ciphertext, key)
            return {"status": "success", "data": plaintext}
        except Exception as e:
            return {"status": "error", "message": f"Lỗi giải mã: {str(e)}"}
    @staticmethod
    def generate_ecc_keys():
        try:
            cipher = ECCCipher()
            cipher.generate_keys()
            return {"status": "success", "message": "Đã tạo khóa Public/Private thành công trong thư mục keys!"}
        except Exception as e:
            return {"status": "error", "message": f"Lỗi tạo khóa: {str(e)}"}

    @staticmethod
    def process_ecc_sign(message):
        try:
            cipher = ECCCipher()
            sk, _ = cipher.load_keys() # Load khóa riêng tư (sk)
            
            # Ký và chuyển kết quả (byte) sang chuỗi Hex để hiển thị lên UI
            signature_bytes = cipher.sign(message, sk)
            signature_hex = signature_bytes.hex() 
            
            return {"status": "success", "data": signature_hex}
        except FileNotFoundError:
            return {"status": "error", "message": "Không tìm thấy file khóa. Vui lòng bấm 'Tạo khóa' trước!"}
        except Exception as e:
            return {"status": "error", "message": f"Lỗi tạo chữ ký: {str(e)}"}

    @staticmethod
    def process_ecc_verify(message, signature_hex):
        try:
            cipher = ECCCipher()
            # Chuyển chữ ký từ UI (dạng Hex) ngược lại thành byte
            signature_bytes = bytes.fromhex(signature_hex) 
            
            # Hàm verify của bạn không dùng tham số key (nó tự load bên trong), nên truyền None
            is_valid = cipher.verify(message, signature_bytes, None)
            return {"status": "success", "data": is_valid}
        except ValueError:
            return {"status": "error", "message": "Lỗi định dạng: Chữ ký phải là chuỗi Hex hợp lệ!"}
        except Exception as e:
            return {"status": "error", "message": f"Lỗi xác thực: {str(e)}"}