"""Task: A microcontroller writes data to flash memory in "pages" of exactly 4096 bytes.

    Ask the user for the total number of bytes they need to write (integer).
    Using only // and %, print how many full pages will be written.
    Print how many bytes will be written to the final, incomplete page.
    Format exactly as: Pages: X, Leftover bytes: Y. """

capacity = 4096
pages = int(input("Total number of bytes to be written: "))

full_pages = pages // 4096
left_over = (pages % 4096)

print(f"Pages: {full_pages}, Leftover bytes: {left_over}")
