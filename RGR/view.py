class View:

    def show_menu(self):
        self.show_message("\nМеню:")
        self.show_message("1. Додати рядок")
        self.show_message('2. Генерування «рандомізованих» даних (тільки для таблиці "Drugs")')
        self.show_message("3. Показати таблицю")
        self.show_message("4. Редагувати рядок")
        self.show_message("5. Видалити рядок")
        self.show_message("6. Пошук")
        self.show_message("7. Вихід")
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

    def show_forms(self, forms):
        print("\nForms:")
        for form in forms:
            print(f"ID: {form[0]}, Name: {form[1]}")

    def show_groups(self, groups):
        print("\nGroups:")
        for group in groups:
            print(f"ID: {group[0]}, Name: {group[1]}")

    def show_drugs_groups(self, drugs_groups):
        print("\nDrugs Groups:")
        for dg in drugs_groups:
            print(f"drug_ID: {dg[0]}, group_ID: {dg[1]}")

    def show_producers(self, producers):
        print("\nProducers:")
        for producer in producers:
            print(f"ID: {producer[0]}, Name: {producer[1]}, Address: {producer[2]}, Link: {producer[3]} , Phone number: {producer[4]}")

    def show_drugs(self, drugs):
        print("\nDrugs:")
        for drug in drugs:
            print(f"ID: {drug[0]}, Name: {drug[1]}, Price: {drug[2]}, Quantity: {drug[3]}, Form_id: {drug[4]}, Producer_id: {drug[5]}")

    def show_drugs_with_groups(self, rows):
        print("\nDrugs-Groups:")
        for row in rows:
            print(f"Drug ID: {row[0]}, Drug name: {row[1]}, Group name: {row[2]}")

    def show_sorting_by_price(self, rows):
        print("\nSorting by price:")
        for row in rows:
            print(f"Drug: {row[0]}, Form: {row[1]}, Price: {row[2]}")

    def show_number_drugs_in_groups(self, rows):
        print("\nNumber drugs in groups:")
        for row in rows:
            print(f'Кількість преператів у групі "{row[0]}": {row[1]}.')

    def get_drug_input(self):
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

    def get_producer_input(self):
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

    def get_form_input(self):
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

    def get_group_input(self):
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

    def get_drug_group_input(self):
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

    def get_drug_id(self):
        while True:
            try:
                id = int(input("Enter drug ID: "))
                break
            except ValueError:
                print("It must be a number.")
        return id

    def get_producer_id(self):
        while True:
            try:
                id = int(input("Enter producer ID: "))
                break
            except ValueError:
                print("It must be a number.")
        return id

    def get_form_id(self):
        while True:
            try:
                id = int(input("Enter form ID: "))
                break
            except ValueError:
                print("It must be a number.")
        return id

    def get_group_id(self):
        while True:
            try:
                id = int(input("Enter group ID: "))
                break
            except ValueError:
                print("It must be a number.")
        return id

    def get_task_id(self):
        while True:
            try:
                id = int(input("Enter task ID: "))
                break
            except ValueError:
                print("It must be a number.")
        return id

    def show_message(self, message):
        print(message)

    def get_number(self):
        while True:
            try:
                number = int(input("Enter the number: "))
                break
            except ValueError:
                print("It must be a number.")
        return number