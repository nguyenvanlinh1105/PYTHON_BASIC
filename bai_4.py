#       BAI 4:    NHÓM NHẬP DL
# Cách xuất dữ liệu bằng câu lệnh print 
# cú pháp
"""
print(object(s), sep=separator, end = end, file=file, flush=flush)

trong đó : 
object(s) đối tượng, dữ liệu được xuất
sep: ngăn cách 
end: kết thúc 
file: tên tập tin 
flush: đẩy dữ liệu 
"""
print()
print("Tôi tên là nguyễn Văn linh ")

#thực hiện nhiều câu lệnh cùng một dòng 
print("Cau lệnh đầu tiên"); print("Cau lệnh số 2") 

# truyền nhiều tham số => kết quả như nối chuỗi  ngăn cách bằng các khoảng trắng 
print("Linh", "Nguyễn", 234)

# ko muốn ngăn cách bởi các khoảng trắng mà ngăn cách bởi dấu - 
print("Linh", "Nguyen", "DepTry", sep="-")

# có sử dụng end : kết thúc ngay sau chương trình có kí tự đó
print('Xin', 'Chao', sep='-', end=':')
print('Linh Nguyen')


# in theo định dạng
print('Ten={0}, Ho={1}'.format('Linh','Nguyễn'))
