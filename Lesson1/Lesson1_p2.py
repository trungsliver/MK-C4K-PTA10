from Lesson1_p1 import Car, Student

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

# Thêm học sinh vào danh sách
add_student('Duc Trung', 25, 8.5)
add_student('Quoc Khanh', 25, 9)
add_student('Duy Long', 13, 8)
add_student('Phuong Thuy', 13, 8)
# Sửa thông tin
update_student('Duc Trung', 26, 10)
# Xóa học sinh theo tên
delete_student('Quoc Khanh')

# In danh sách
for student in students:
    print(student)