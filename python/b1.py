từ matplotlib nhập khẩu pyplot as plt
từ phong cách nhập khẩu matplotlib
 
phong cách. sử dụng('ggplot')
x = [5,8,10]
y = [12,16,6]
x2 = [6,9,11]
y2 = [6,15,7]
plt. cốt truyện(x,y,'g',nhãn='dòng một', linewidth=5)
plt. cốt truyện(x2,y2,'c',nhãn='dòng hai',linewidth=5)
plt. Tiêu đề('Thông tin sử thi')
plt. ylabel('trục Y')
plt. xlabel('Trục X')
plt. truyền thuyết()
plt. lưới(Đúng,màu sắc='k')
plt. hiển thị()