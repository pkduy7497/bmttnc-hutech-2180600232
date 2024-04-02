print("Nhập các dòng văn bản (nhập 'done' để kết thúc): ")
lines = []
while True:
    line = input()
    if line.lower() == 'done':
        break
    line.append(line)
    print("\nCác dòng đã nhập chuyển thành chữ in hoa là: ")
    for line in lines:
        print(line.upper())