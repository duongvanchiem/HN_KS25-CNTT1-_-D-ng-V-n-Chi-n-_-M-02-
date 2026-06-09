row =[
    {
        "id":"SP001",
        "name": "chuot khong day logitech",
        "price": "250000",
        "quantity": "15",
        "safety_lock": "20",
        "value": "3750000",
        "status": "canh bao"
    }
        def row():
    if len(row) == 0:
        print("Danh sách rỗng!")
        return
    print("\n{id:<15} {name:<10} {price:<10} {uantity:<10} {safety_lock:<15} {value:<15} {status:<10}".format())
    print("-" * 100)
    
    def row():
    if len(row) == 0:
        print("Danh sách rỗng!")
        return

    keyword = input("Nhập mã sản phẩm: ").lower()

    found = False

    for p in rows:
        if keyword == p["id"].lower() or keyword in p["name"].lower():
            print("\ntìm thấy:")
            print(p)
            found = True

    if not found:
        print("Không tìm thấy sản phẩm!")
    
def update_row():
    row_id = input("nhập mã sản phẩm: ")

    for p in row:
        if p["id"] == row_id:

            try:
                product_quantity = int(input("số lượng sản phẩm: "))
                product_price= int(input("số tiền của sản phẩm: "))
               
                if product_quantity < 0 or product_quantity > 50:
                    print("số lượng sản phẩm không hợp lệ!")
                    return

                if product_price< 0 or product_price < 0:
                    print("số tiền sản phẩm không hợp lệ!")
                    return
            except ValueError:
                print("nhập sai định dạng!")
                return
    print("Không tìm thấy sản phẩm!")
    
    def statistics_row():
    if len(row) == 0:
        print("danh sách rỗng!")
        return
    for p in row:
        if p["quntity"] == "số lượng sản phẩm":
            row += 1
        elif p["price"] == "số tiền sản phẩm":
            row_price += 1
        else:
            remove += 1
  
]
def main():
    while True:
        print("MENU LỰA CHỌN")
        print("1. Hiển thị danh sách kho hàng")
        print("2. Khai báo sản phẩm")
        print("3. Cập nhật số lượng và giá vốn")
        print("4. Xóa sản phẩm khỏ danh mục")
        print("5. Tìm kiếm sản phẩm")
        print("6. Thống kê trạng thái kho hàng")
        print("7. Phân loại trạng thái tự động")
        print("8. Thoát chương trình")
              
        choice = input("nhập lựa chọn của bạn:")
      
        if choice == "1":
            row_list()

        elif choice == "2":
            display_row()

        elif choice == "3":
            update_row()

        elif choice == "4":
             delete_row()

        elif choice == "5":
            search_row()

        elif choice == "6":
            statistics_row()

        elif choice == "7":
            classification_status

        elif choice == "8":
            print("thoát chương trình!")
            break

        else:
            print("lựa chọn không hợp lệ!")



