thickness = int(input()) # Must be odd
c = 'H'

# Top Cone
for i in range(thickness):
    print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

# Top Pillars
for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

# Middle Belt
for i in range((thickness + 1) // 2):
    print((c * thickness * 5).center(thickness * 6))    

# Bottom Pillars
for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))    
# Bottom Cone (FIXED)
for i in range(thickness):
    # 1. Build the inverted triangle row
    # 2. Center it in (thickness * 2)
    # 3. Right-align the entire block to (thickness * 6)
    row = (c * (thickness - i - 1)).rjust(thickness - 1) + c + (c * (thickness - i - 1)).ljust(thickness - 1)
    print(row.center(thickness * 2).rjust(thickness * 6))