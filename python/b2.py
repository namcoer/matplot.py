nhập matplotlib. pyplot như plt
nhập numpy dưới dạng np
def f(t):
    trả lại np. exp(-t) * np. cos(2*np. pi*t)
t1 = np. arange(0.0, 5.0, 0.1)
t2 = np. arange(0.0, 5.0, 0.02)
plt. phụ(221)
plt. plot(t1, f(t1), 'bo', t2, f(t2))
plt. phụ(222)
plt. cốt truyện(t2, np. cos(2*np. pi*t2))
plt. hiển thị()