import csv

CARS_FILE = "cars.csv"
USERS_FILE = "users.csv"

def demo_read_csv():
    with open(CARS_FILE) as file:
        reader = csv.reader(file)
        for row in reader:
            #print(row)
            print(row[0], row[1], "прайс:", row[4])
            #print(row[3])
            print()

def demo_read_csv_dict():
    with open(CARS_FILE) as file:
        reader = csv.DictReader(file)
        print("field names:", reader.fieldnames)
        for row in reader:
            print(row)
            print(row["Year"], row["Make"], "прайс:", row["Price"])
            print(row["Description"])
            print()

class FieldNames:
    USERNAME = "username"
    EMAIL = "email"
    PHONE = "phone"

def demo_write_csv():
    field_names = [
        FieldNames.USERNAME,
        FieldNames.EMAIL,
        FieldNames.PHONE,
    ]
    with open(USERS_FILE, "w") as file:
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()

        writer.writerow({
            FieldNames.USERNAME: "John",
            FieldNames.EMAIL: "john@example.com",
            FieldNames.PHONE: "99-11-12"
        })

        user_sam = {
            FieldNames.EMAIL: "sam@example.com",
            FieldNames.USERNAME: "Sam",
            FieldNames.PHONE: "11-55-12"
        }
        user_nick = {
            FieldNames.EMAIL: "nick@example.com",
            FieldNames.USERNAME: "Nick",
            FieldNames.PHONE: "33-11-56"
        }
        users = [user_sam, user_nick]
        writer.writerows(users)

def main():
    #demo_read_csv()
    #demo_read_csv_dict()
    demo_write_csv()

if __name__ == '__main__':
    main()