"""Task: A microcontroller writes data to flash memory in "pages" of exactly 4096 bytes.

    Ask the user for the total number of bytes they need to write (integer).
    Using only // and %, print how many full pages will be written.
    Print how many bytes will be written to the final, incomplete page.
    Format exactly as: Pages: X, Leftover bytes: Y. """


capacity = 4096 #Initializing Microcontroller write capacity
total_byte = int(input("Total number of bytes to be written: ")) #Collect user info on how many byte need to be written

# Arithemetic operation to determine number of Full pages and left over bytes by the microcontroller
full_pages = total_byte // 4096
left_over = (total_byte % 4096)

# Displays the Output
print(f"Pages: {full_pages}, Leftover bytes: {left_over}")
