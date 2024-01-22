import csv


def write_csv(data):
    with open('5.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([data['name'],
                         data['surname'],
                         data['age']])


def write_csv2(data):
    """чтобы каждый раз не прописывать поля и указывать свою последовательность"""
    with open('5.csv', 'a') as file:
        order = ['name', 'surname', 'age']
        writer = csv.DictWriter(file, fieldnames=order)

        writer.writerow(data)


def main():
    d = {'name': 'Petr', 'surname': 'Ivanov', 'age': 21}
    d1 = {'name': 'Kirill', 'surname': 'Ganichev', 'age': 16}
    d2 = {'name': 'Kirill', 'surname': 'Marilov', 'age': 15}

    l = [d, d1, d2]

    with open('4.csv', 'r') as file:
        fieldnames = ['name', 'url', 'desc']
        reader = csv.DictReader(file, fieldnames=fieldnames)

        for row in reader:
            print(row)


if __name__ == '__main__':
    main()
