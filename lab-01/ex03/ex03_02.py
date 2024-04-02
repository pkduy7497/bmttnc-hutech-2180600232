#Chương trình đảo ngược thứ tự phần từ trong list.
def dao_nguoc_list(lst):
    return lst[::-1]
# Nhập danh sách
input_list = input("Nhập danh sách cách số, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, input_list.split(",")))
# Sử dụng hàm và in ra
list_dao_nguoc = dao_nguoc_list
print("List sao khi đảo ngược là: ", list_dao_nguoc)