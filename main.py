with open('input.png', 'rb') as file:
    byte_count = 0
    while True:
        byte = file.read(1)
        if not byte:
            break
        print(f'{byte.hex().upper()}', end=' ')
        byte_count += 1

        if byte_count % 16 == 0:
            print()