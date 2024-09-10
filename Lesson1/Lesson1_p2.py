from Lesson1_p1 import Car, Student, Food

# Tạo danh sách đối tượng
cars = [
    Car('Toyota', 'Camry', 2015, 50000),
    Car('Honda', 'Civic', 2018, 30000),
    Car('Mercerdes', 'S600', 2020, 240000),
    Car('BMW', 'Q7', 2022, 200000),
    Car('Audi', 'A4', 2019, 180000)
]

# # In ra thông tin của các xe
# # for car in cars:
# #     print(car)

# # Sắp xếp danh sách theo giá
# sorted_car = sorted(cars, key=lambda car: car.price)
#     # In ra thông tin của các xe sau sắp xếp
# for car in sorted_car:
#     print(car)

# # Tìm xe có giá cao nhất
# max_car = max(cars, key=lambda car: car.price)
# print('Xe giá cao nhất:', max_car)

students = []

# Thêm học sinh
def add_student(name, age, score):
    students.append(Student(name, age, score))

# Xóa sinh viên theo tên
def delete_student(name):
    for student in students:
        if student.name == name:
            students.remove(student)

# Chỉnh sửa thông tin theo tên
def update_student(name, new_age=None, new_score=None):
    for student in students:
        if student.name == name:
            if new_age:
                student.age = new_age
            if new_score:
                student.score = new_score
            print('Updated !!!')
            return
    print(f'Student {name} not found')

# # Thêm học sinh vào danh sách
# add_student('Duc Trung', 25, 8.5)
# add_student('Quoc Khanh', 25, 9)
# add_student('Duy Long', 13, 8)
# add_student('Phuong Thuy', 13, 8)
# # Sửa thông tin
# update_student('Duc Trung', 26, 10)
# # Xóa học sinh theo tên
# delete_student('Quoc Khanh')

# # In danh sách
# for student in students:
#     print(student)

# Danh sách menu
menu = []

# Thêm đồ ăn vào danh sách
def add_food():
    name = input("Mời bạn nhập vào tên đồ ăn: ")
    price = int(input("Mời bạn nhập giá đồ ăn: "))
    menu.append(Food(name, price))
    print(f"Đã thêm món {name} vào menu")

def remove_food():
    name = input("Mời bạn nhập vào tên đồ ăn cần xoá: ")
    for food in menu:
        if food.name == name:
            menu.remove(food)
            print("Xoá đồ ăn thành công khỏi menu")
            return
    print("Không có đồ ăn cần tìm trong menu")

def update_food():
    name = input("Mời bạn nhập vào tên đồ ăn cần chỉnh sửa: ")
    for food in menu:
        if food.name == name:
            price = int(input("Mời bạn sửa giá đồ ăn: "))
            food.price = price
            print("Sửa giá món ăn thành công")
            return
    print("Không có đồ ăn cần tìm trong menu")

def display_menu():
    if menu:
        print("Danh sách đồ ăn:")
        for index, food in enumerate(menu):
            print(f"{index + 1}. {food.name} - {food.price}")
    else:
        print("Menu rỗng")

def tang_dan():
    menu.sort(key=lambda x: x.price)
    print("Sắp xếp tăng dần thành công")

def giam_dan():
    menu.sort(key=lambda x: x.price, reverse=True)
    print("Sắp xếp giảm dần thành công")

def max_price():
    if menu:
        print(max(menu, key=lambda food: food.price))
    else:
        print("Không có đồ ăn cần tìm trong menu")
        
# Giao diện menu
while True:
    print("\nMenu")
    print("1. Thêm đồ ăn vào danh sách")
    print("2. Xoá đồ ăn ra khỏi danh sách")
    print("3. Chỉnh sửa đồ ăn có trong danh sách")
    print("4. Sắp xếp món ăn theo chiều tăng dần")
    print("5. Sắp xếp món ăn theo chiều giảm dần")
    print("6. Hiển thị món ăn đắt tiền nhất")
    print("7. Hiển thị menu")
    print("8. Thoát chương trình")

    choice = int(input("Mời bạn nhập lựa chọn: "))

    if choice == 1:
        add_food()
    elif choice == 2:
        remove_food()
    elif choice == 3:
        update_food()
    elif choice == 4:
        tang_dan()
    elif choice == 5:
        giam_dan()
    elif choice == 6:
        max_price()
    elif choice == 7:
        display_menu()
    else:
        print("Cảm ơn bạn đã sử dụng chương trình!")
        break