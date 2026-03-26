import pandas as pd
import matplotlib.pyplot as plt

# TẠO DỮ LIỆU GIẢ ĐỂ CHẠY THỬ (Thay thế cho việc đọc file CSV)
data = {
    'Price': [100, 150, None, 200, -50, 300],
    'StockQuantity': [10, None, 5, 20, 15, -2],
    'Category': ['ELECTRONICS', 'home', 'Electronics', 'HOME', 'food', 'FOOD'],
    'Rating': [4.5, 3.8, 6.0, 4.0, 2.0, 4.2],
    'Description': ['  Good item  ', 'Nice!', '  Value  ', 'Old ', 'New', 'Check ']
}
df = pd.DataFrame(data)

print("--- ĐÃ NẠP DỮ LIỆU THÀNH CÔNG ---")
print(df.head())

# BÀI 1 & 2: Xử lý thiếu
df['Price'] = df['Price'].fillna(df['Price'].median())
df['StockQuantity'] = df['StockQuantity'].fillna(0)

# BÀI 3: Xử lý lỗi (Lọc giá > 0 và Rating <= 5)
df = df[(df['Price'] > 0) & (df['Rating'] <= 5) & (df['StockQuantity'] >= 0)]

# BÀI 5: Chuẩn hóa
df['Category'] = df['Category'].str.lower()
df['Description'] = df['Description'].str.strip()

print("\n--- DỮ LIỆU SAU KHI LÀM SẠCH ---")
print(df)