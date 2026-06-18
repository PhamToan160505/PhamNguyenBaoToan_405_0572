import math

class TranspositionCipher:
    def __init__(self):
        pass

    def encrypt(self, text, key):
        encrypted_text = ""
        for col in range(key):
            pointer = col
            while pointer < len(text):
                encrypted_text += text[pointer]
                pointer += key
        return encrypted_text

    def decrypt(self, text, key):
        # Tính toán chính xác lưới giải mã
        num_cols = math.ceil(len(text) / key) # Số cột giải mã
        num_rows = key                        # Số hàng giải mã (chính là key)
        num_shaded_boxes = (num_cols * num_rows) - len(text) # Tính số ô trống ở góc dưới cùng bên phải

        # Khởi tạo mảng dựa trên số cột, KHÔNG phải dựa trên key
        decrypted_text = [""] * num_cols
        row, col = 0, 0
        
        for symbol in text:
            decrypted_text[col] += symbol
            col += 1
            
            # Chuyển cột nếu:
            # 1. Chạm đáy cột (col == num_cols)
            # 2. Hoặc rơi vào ô bị khuyết ở cột cuối cùng
            if (col == num_cols) or (col == num_cols - 1 and row >= num_rows - num_shaded_boxes):
                col = 0
                row += 1
                
        return "".join(decrypted_text)