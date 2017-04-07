try: open("division.out", "w").write((lambda a, b: str(a // b))(*[int(i) for i in open("division.in").read().split()]))
except: open("division.out", "w").write("Na nol' delit' nel'zya!!!")