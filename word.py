s = input()
upp = s.upper()
upcont = 0
low = s.lower()
lowcont = 0

for i in s:
    if i in upp:
        upcont += 1
    elif i in low:
        lowcont += 1

if upcont > lowcont:
    print(upp)
else:
    print(low)