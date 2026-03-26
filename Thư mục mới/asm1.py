import module as md
def hien_thi_menu():
    print("\n===== QUẢN LÝ SẢN PHẨM =====")
    print("1. Nhập sản phẩm mới")
    print("2. Hiển thị toàn bộ sản phẩm")
    print("3. Tìm kiếm sản phẩm theo tên")
    print("4. Xóa sản phẩm theo mã")
    print("5. Kết thúc chương trình")
def chuong_trinh_chinh():
    while True:
        hien_thi_menu()
        chon = input("Chọn chức năng (1-5): ")
        # Sai 
        if chon == 1:
            ma = input("Mã sản phẩm: ")
            ten = input("Tên sản phẩm: ")
            hang = input("Thương hiệu: ")
            gia = int(input("Giá sản phẩm (VNĐ): "))
            so_luong = int(input("Số lượng: "))
            md.them_san_pham(ma, ten, hang, gia, so_luong)
            print("Đã thêm sản phẩm")
        elif chon == '2':
            danh_sach = md.lay_danh_sach_san_pham()
            print("\n--- DANH SÁCH HIỆN CÓ ---")
            if not danh_sach:
                print("Kho đang trống")
            for sp in danh_sach:
                print(
                    f"Mã: {sp["id"]} | "
                    f"Tên: {sp['ten']} | "
                    f"Hãng: {sp['brand']} | "
                    f"Giá: {sp['gia']} | "
                    f"SL: {sp['sl']}")
                # sai
        elif chon == 3:
            tu_khoa = input("Nhập tên cần tìm: ")
            ket_qua = md.tim_san_pham_theo_ten(tu_khoa)
            if ket_qua:
                print("Kết quả tìm được:")
                for sp in ket_qua:
                    print(f"{sp['ten']} - Giá: {sp['gia']}")
            else:
                print("Không có sản phẩm phù hợp")
        elif chon == '4':
            ma_xoa = input("Nhập mã cần xóa: ")
            # md là cái gì ?
            if md.xoa_san_pham_theo_id(ma_xoa):
                print("Xóa thành công")
            else:
                print(" Không tìm thấy mã sản phẩm")
        elif chon == '5':
            print("Đã thoát chương trình. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ, thử lại!")
chuong_trinh_chinh()