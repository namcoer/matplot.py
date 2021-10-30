nhập numpy dưới dạng np
nhập panda làm pd
my_column_names = ['Môt', 'hai', 'ba', 'bon']

my_data = np. ngẫu nhiên. randint(thấp=0, cao=101, kích thước=(3, 4))

df = pd. DataFrame(dữ liệu=my_data, cột=my_column_names)

in(df)

print("\nCột thứ 2 : %d\n" % df['Môt'][1])

df['Hulk'] = df['ba'] + df['bon']

in(df)