from transposition.transposition_cipher import TranspositionCipher 

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