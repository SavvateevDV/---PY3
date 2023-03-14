BYTES_ONE_CHAR = 1  # размер одного символа в байтах

# никаких магических чисел
pages = 100
lines = 50
chars = 25
disket_size_MB = 1.44

total_chars = pages*lines*chars
total_bytes = total_chars

disk_size = disket_size_MB*1024*1024

print(round(float(round(disk_size/total_bytes)),1))
#пустая строка