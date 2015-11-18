with open('input.txt') as f:
    h, m, s = [int(i) for i in f.readline().strip().split(':')]
    k = int(f.readline())

h_new = k // 3600
m_new = (k - h_new * 3600) // 60
s_new = k - h_new * 3600 - m_new * 60

s += s_new
if s > 59:
    m_new += 1
    s %= 60

m += m_new
if m > 59:
    h_new += 1
    m %= 60

h += h_new
if h > 23:
    h %= 24

with open('output.txt', 'w') as fout:
    print("%02d:%02d:%02d" % (h,m,s), file = fout)