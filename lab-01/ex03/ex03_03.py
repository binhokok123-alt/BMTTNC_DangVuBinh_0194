def tao_tuple_tu_list(lst):
    return tuple(lst)
input_list = input("Nhập ds sách các số, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))
my_tuple = tao_tuple_tu_list(numbers)
print("Danh sách ban đầu là:", numbers)
print("Tuple được tạo từ danh sách là:", my_tuple)
