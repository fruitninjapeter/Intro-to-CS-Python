def file_read():
    try:
        a = open("file.txt")

    except FileNotFoundError:
        print("error you dolt")
        exit(1)

    for line in a:
        line_char = line.split()
        try:
            first = float(line_char[0])
            second = float(line_char[1])
            print(str(first + second))
        except ValueError:
            print("you didn't do 2 numbers >:(")
        except IndexError:
            print("Only two values fam")
    a.close()


if __name__ == '__main__':
    file_read()