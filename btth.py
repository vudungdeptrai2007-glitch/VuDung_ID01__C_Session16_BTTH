blood_inventory = [
    "BL001-Nguyen Van A-O+-250-31/12/2026",
    "BL002-Tran Thi B-A--350-15/11/2026",
    "BL003-Le Van C-AB+-250-20/10/2026"
]

def display_inventory(inventory):
    if len(inventory) == 0:
        print("Kho máu hiện chưa có túi máu nào.")
        return
    total = 0
    print("--- DANH SÁCH KHO MÁU ---")
    print(
        f"{'Mã Túi':<10} | {'Người Hiến':<20} | {'Nhóm Máu':<10} | {'Thể Tích':<10} | {'Ngày Hết Hạn':<15}"
    )
    print("-" * 80)
    for blood in inventory:
        data = blood.split("-")
        blood_id = data[0]
        donor = data[1]
        blood_group = data[2]
        volume = data[3]
        expiry = data[4]
        total += int(volume)
        print(
            f"{blood_id:<10} | {donor:<20} | {blood_group:<10} | {volume} ml{' ':<4} | {expiry:<15}"
        )
    print("----------------------------------------------------------")
    print("Tổng thể tích máu trong kho:", total, "ml")


def add_blood_bag(inventory):
    print("--- NHẬP TÚI MÁU MỚI ---")
    blood_id = input("Nhập mã túi máu mới: ").strip().upper()
    if blood_id == "":
        print("Lỗi: Mã túi máu không được để trống!")
        return

    for blood in inventory:
        data = blood.split("-")
        if data[0] == blood_id:
            print(f"\nLỗi: Mã túi máu {blood_id} đã tồn tại!")
            return
    donor = input("Nhập tên người hiến: ").strip().title()
    if donor == "":
        print("\nLỗi: Tên người hiến không được để trống!")
        return
    blood_group = input("Nhập nhóm máu: ").strip().upper()
    volume = input("Nhập thể tích (ml): ").strip()
    if volume.isdigit() == False or int(volume) <= 0:
        print("\nLỗi: Thể tích phải là số nguyên lớn hơn 0!")
        return
    expiry = input("Nhập ngày hết hạn (DD/MM/YYYY): ").strip()
    new_blood = "-".join([
        blood_id,
        donor,
        blood_group,
        volume,
        expiry
    ])
    inventory.append(new_blood)
    print(f"\nThành công: Đã nhập túi máu {blood_id} vào kho!")


def update_expiry(inventory):
    print("--- GIA HẠN / SỬA NGÀY HẾT HẠN ---")
    blood_id = input(
        "Nhập mã túi máu cần cập nhật: "
    ).strip().upper()
    if blood_id == "":
        print("\nLỗi: Mã túi máu không được để trống!")
        return

    for i in range(len(inventory)):
        data = inventory[i].split("-")
        if data[0] == blood_id:
            new_expiry = input("Nhập ngày hết hạn mới: ").strip()
            if len(data) == 5:
                data[4] = new_expiry
            else:
                data[5] = new_expiry
            inventory[i] = "-".join(data)
            print(
                f"\nThành công: Đã cập nhật ngày hết hạn cho túi máu {blood_id}!"
            )
            return
    print(f"\nLỗi: Không tìm thấy túi máu {blood_id} trong kho!")


def remove_blood_bag(inventory):
    print("--- XUẤT / HỦY TÚI MÁU ---")
    blood_id = input(
        "Nhập mã túi máu cần xuất/hủy: "
    ).strip().upper()
    if blood_id == "":
        print("\nLỗi: Mã túi máu không được để trống!")
        return

    for blood in inventory:
        data = blood.split("-")
        if data[0] == blood_id:
            inventory.remove(blood)
            print(
                f"\nThành công: Đã xuất túi máu {blood_id} khỏi kho!"
            )
            return
    print(f"\nLỗi: Không tìm thấy túi máu {blood_id} trong kho!")


def main():
    while True:
        print("""
=== HỆ THỐNG QUẢN LÝ KHO MÁU RIKKEI ===
1. Xem danh sách túi máu trong kho
2. Nhập túi máu mới
3. Gia hạn / Sửa ngày hết hạn
4. Xuất / Hủy túi máu
5. Thoát chương trình
========================================
""")
        choice = input("Chọn chức năng (1-5): ").strip()
        match choice:

            case "1":
                display_inventory(blood_inventory)

            case "2":
                add_blood_bag(blood_inventory)

            case "3":
                update_expiry(blood_inventory)

            case "4":
                remove_blood_bag(blood_inventory)

            case "5":
                print(
                    "Cảm ơn bác sĩ đã sử dụng hệ thống. Hẹn gặp lại!"
                )
                break

            case _:
                print(
                    "Lựa chọn không hợp lệ, vui lòng nhập số từ 1-5!"
                )

    main()