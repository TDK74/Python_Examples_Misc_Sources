status = 0b00101111
status_int = int(status)

mask_status = bin(status % (1 << 4)) # Give the bits from 0 to 3
mask_status_int = int(mask_status, 2)
#https://stackoverflow.com/questions/8928240/convert-base-2-binary-number-string-to-int

print(f"{status:b}")
print(status_int)
print(mask_status)
print(mask_status_int)
