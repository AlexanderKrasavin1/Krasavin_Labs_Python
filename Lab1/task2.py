
capacity_bits = 1.44 * 1024 * 1024
count_of_pages = 100
count_of_strings = 50
count_of_symbols = 25
bite_for_symbol = 4
count_of_books = int(capacity_bits//((count_of_pages * count_of_strings * count_of_symbols)*4))
print("Количество книг, помещающихся на дискету:", count_of_books)
