class View:

    def show_menu(self):
        self.show_message("\nМеню:")
        self.show_message("1. Додати рядок")
        self.show_message("2. Показати таблицю")
        self.show_message("3. Редагувати рядок")
        self.show_message("4. Видалити рядок")
        self.show_message("5. Вихід")
        choice = input("Виберіть пункт: ")
        return choice

    def show_tables(self):
        self.show_message("\nТаблиці:")
        self.show_message("1. Drugs")
        self.show_message("2. Producers")
        self.show_message("3. Forms")
        self.show_message("4. Groups")
        self.show_message("5. Drugs Groups")
        self.show_message("6. Повернутися до меню")
        table = input("Оберіть потрібну таблицю: ")
        return table

    def show_search(self):
        self.show_message("\nПошук:")
        self.show_message("1. Відповідність преперату групі")
        self.show_message("2. ТОП найдешевших преператів")
        self.show_message("3. Кількість препаратів у кожній групі")
        self.show_message("4. Повернутися до меню")
        choice = input("Обреріть щось: ")
        return choice

    @staticmethod
    def show_forms(forms):
        print("\nForms:")
        for form in forms:
            print(f"ID: {form[0]}, Name: {form[1]}")

    @staticmethod
    def show_groups(groups):
        print("\nGroups:")
        for group in groups:
            print(f"ID: {group[0]}, Name: {group[1]}")

    @staticmethod
    def show_drugs_groups(drugs_groups):
        print("\nDrugs Groups:")
        for dg in drugs_groups:
            print(f"drug_ID: {dg[0]}, group_ID: {dg[1]}")

    @staticmethod
    def show_producers(producers):
        print("\nProducers:")
        for producer in producers:
            print(f"ID: {producer[0]}, Name: {producer[1]}, Address: {producer[2]}, Link: {producer[3]} , Phone number: {producer[4]}")

    @staticmethod
    def show_drugs(drugs):
        print("\nDrugs:")
        for drug in drugs:
            print(f"ID: {drug[0]}, Name: {drug[1]}, Price: {drug[2]}, Quantity: {drug[3]}, Form_id: {drug[4]}, Producer_id: {drug[5]}")

    @staticmethod
    def get_drug_input():
        while True:
            try:
                name = input("Enter drug name: ")
                if name.strip():
                    break
                else:
                    print("Name cannot be empty.")
            except ValueError:
                print("It must be a string.")
        while True:
            try:
                price = input("Enter drug price: ")
                if price.strip():
                    price = float(price)
                    break
                else:
                    print("Price cannot be empty.")
            except ValueError:
                print("It must be a number.")
        while True:
            try:
                quantity = input("Enter drug quantity: ")
                if quantity.strip():
                    break
                else:
                    print("Quantity cannot be empty.")
            except ValueError:
                print("It must be a string.")
        while True:
            try:
                form_id = int(input("Enter drug form_id: "))
                break
            except ValueError:
                print("Form_id must be a number.")
        while True:
            try:
                producer_id = int(input("Enter drug producer_id: "))
                break
            except ValueError:
                print("Producer_id must be a number.")
        return name, price, quantity, form_id, producer_id

    @staticmethod
    def get_producer_input():
        while True:
            try:
                name = input("Enter producer name: ")
                if name.strip():
                    break
                else:
                    print("Name cannot be empty.")
            except ValueError:
                print("It must be a string.")
        while True:
            try:
                address = input("Enter producer address: ").strip()
                if address == "":
                    address = None
                    break
                else:
                    break
            except ValueError:
                print("It must be a string.")
        while True:
            try:
                link = input("Enter producer link: ").strip()
                if link == "":
                    link = None
                    break
                else:
                    break
            except ValueError:
                print("It must be a string.")
        while True:
            try:
                phone_number = input("Enter producer phone number: ").strip()
                if phone_number == "":
                    phone_number = None
                    break
                else:
                    break
            except ValueError:
                print("It must be a string.")
        return name, address, link, phone_number

    @staticmethod
    def get_form_input():
        while True:
            try:
                name = input("Enter form name: ")
                if name.strip():
                    break
                else:
                    print("Name cannot be empty.")
            except ValueError:
                print("It must be a string.")
        return name

    @staticmethod
    def get_group_input():
        while True:
            try:
                name = input("Enter group name: ")
                if name.strip():
                    break
                else:
                    print("Name cannot be empty.")
            except ValueError:
                print("It must be a string.")
        return name

    @staticmethod
    def get_drug_group_input():
        while True:
            try:
                drug_id = int(input("Enter drug_id: "))
                break
            except ValueError:
                print("Drug_id must be a number.")
        while True:
            try:
                group_id = int(input("Enter group_id: "))
                break
            except ValueError:
                print("Group_id must be a number.")
        return drug_id, group_id

    @staticmethod
    def get_drug_id():
        while True:
            try:
                id = int(input("Enter drug ID: "))
                break
            except ValueError:
                print("It must be a number.")
        return id

    @staticmethod
    def get_producer_id():
        while True:
            try:
                id = int(input("Enter producer ID: "))
                break
            except ValueError:
                print("It must be a number.")
        return id

    @staticmethod
    def get_form_id():
        while True:
            try:
                id = int(input("Enter form ID: "))
                break
            except ValueError:
                print("It must be a number.")
        return id

    @staticmethod
    def get_group_id():
        while True:
            try:
                id = int(input("Enter group ID: "))
                break
            except ValueError:
                print("It must be a number.")
        return id

    @staticmethod
    def get_task_id():
        while True:
            try:
                id = int(input("Enter task ID: "))
                break
            except ValueError:
                print("It must be a number.")
        return id

    @staticmethod
    def show_message(message):
        print(message)

    @staticmethod
    def get_number():
        while True:
            try:
                number = int(input("Enter the number: "))
                break
            except ValueError:
                print("It must be a number.")
        return number