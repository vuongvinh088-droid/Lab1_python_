danh_sach_sp = []
def them_san_pham(ma, ten, hang, gia, so_luong):
    for item in danh_sach_sp:
        if item["id"] == ma:
            print("Mã sản phẩm đã tồn tại")
            return False
    sp_moi = {
        "id": ma,
        "ten": ten,
        "brand": hang,
        "gia": int(gia),
        "sl": int(so_luong)}
    danh_sach_sp.append(sp_moi)
    return True
def lay_danh_sach_san_pham():
    return danh_sach_sp
def tim_san_pham_theo_ten(ten_can_tim):
    ket_qua = []
    for item in danh_sach_sp:
        if ten_can_tim.lower() in item["ten"].lower():
            ket_qua.append(item)
    return ket_qua
def xoa_san_pham_theo_id(ma_can_xoa):
    vi_tri = -1
    for i in range(len(danh_sach_sp)):
        if danh_sach_sp[i]["id"] == ma_can_xoa:
            vi_tri = i
            break
    if vi_tri != -1:
        danh_sach_sp.pop(vi_tri)
        #pop đe xác định vị trí - sai
        return True
    return False