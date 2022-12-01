def decipher(lattice, password, lattice_size):
    error_text = '\n\tРешетка и/или пароль заданы неправильно!'
    if not (len(lattice) == lattice_size
            and len(password) == lattice_size):
        print(error_text)
        return
    for i in range(lattice_size):
        if not (len(lattice[i]) == lattice_size
                and len(password[i]) == lattice_size):
            print(error_text)
            return

    copy_lattice = lattice[:]
    decrypted_message = ''
    for turn_number in range(4):
        decrypted_message_list = [
                                    password[i][j]
                                    for i in range(lattice_size)
                                    for j in range(lattice_size)
                                    if copy_lattice[i][j] == 'X'
                                ]
        decrypted_message += ''.join(decrypted_message_list)

        reversed_lattice = list(reversed(copy_lattice))
        copy_lattice.clear()
        for i in range(lattice_size):
            list_lattice = [
                                reversed_lattice[j][i]
                                for j in range(lattice_size)
                           ]
            string_lattice = ''.join(list_lattice)
            copy_lattice.append(string_lattice)

    return decrypted_message

assert decipher(['X...', '..X.', 'X..X', '....'],
                ['itdf', 'gdce', 'aton', 'qrdi'], 4) == 'icantforgetiddqd'
assert decipher(['....', 'X..X', '.X..', '...X'],
                ['xhwc', 'rsqx', 'xqzz', 'fyzr'], 4) == 'rxqrwsfzxqxzhczy'