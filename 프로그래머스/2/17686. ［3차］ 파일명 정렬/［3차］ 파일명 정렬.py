def solution(files):
    parsed_files = []

    for file in files:
        head = ''
        number = ''
        i = 0

        while i < len(file) and not file[i].isdigit():
            head += file[i]
            i += 1

        while i < len(file) and file[i].isdigit():
            number += file[i]
            i += 1

        parsed_files.append([head, number, file])

    parsed_files.sort(key=lambda x: (x[0].lower(), int(x[1])))

    return [file[2] for file in parsed_files]