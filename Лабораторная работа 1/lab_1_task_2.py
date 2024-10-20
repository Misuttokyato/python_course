# TODO Найдите количество книг, которое можно разместить на дискете

diskette = 1.44 * 1024 * 1024   # Размер в байтах

pages = 100
lines_per_page = 50
chars_per_line = 25
bytes_one_char = 4
book = bytes_one_char * chars_per_line * lines_per_page * pages

num_book_on_diskette = int(diskette // book)

print("Количество книг, помещающихся на дискету:", num_book_on_diskette)
