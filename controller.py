import time
from model import Model
from view import View

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def run(self):
        while True:
            choice = self.view.show_menu()

            if choice == '7':
                break
            if choice == '6':
                self.process_search_option()
            elif choice in ['1', '2', '3', '4', '5']:
                self.process_menu_choice(choice)
            else:
                self.view.show_message("Wrong choice. Try again.")

    def process_menu_choice(self, choice):
        while True:
            table = self.view.show_tables()

            if table == '6':
                break

            if choice == '1':
                self.process_add_option(table)
            elif choice == '2':
                self.process_add_random_option(table)
            elif choice == '3':
                self.process_view_option(table)
            elif choice == '4':
                self.process_update_option(table)
            elif choice == '5':
                self.process_delete_option(table)

    def process_add_option(self, table):
        if table == '1':
            self.view.show_message("\nAdding drug:")
            self.add_drug()
        elif table == '2':
            self.view.show_message("\nAdding producer:")
            self.add_producer()
        elif table == '3':
            self.view.show_message("\nAdding form:")
            self.add_form()
        elif table == '4':
            self.view.show_message("\nAdding group:")
            self.add_group()
        elif table == '5':
            self.view.show_message("\nAdding drug to group:")
            self.add_drug_group()
        else:
            self.view.show_message("Wrong choice. Try again.")

    def process_add_random_option(self, table):
        if table == '1':
            self.view.show_message("\nAdding random drugs:")
            self.add_random_fields()
        else:
            self.view.show_message("Wrong choice. Try again.")

    def process_view_option(self, table):
        if table == '1':
            self.view_drugs()
        elif table == '2':
            self.view_producers()
        elif table == '3':
            self.view_forms()
        elif table == '4':
            self.view_groups()
        elif table == '5':
            self.view_drugs_groups()
        elif table == '6':
            self.view.show_menu()
        else:
            self.view.show_message("Wrong choice. Try again.")

    def process_update_option(self, table):
        if table == '1':
            self.view.show_message("\nUpdating drug:")
            self.update_drug()
        elif table == '2':
            self.view.show_message("\nUpdating producer:")
            self.update_producer()
        elif table == '3':
            self.view.show_message("\nUpdating form:")
            self.update_form()
        elif table == '4':
            self.view.show_message("\nUpdating group:")
            self.update_group()
        elif table == '5':
            self.view.show_message("\nUpdating drug to group:")
            self.update_drug_group()
        else:
            self.view.show_message("Wrong choice. Try again.")

    def process_delete_option(self, table):
        if table == '1':
            self.view.show_message("\nDeleting drug:")
            self.delete_drug()
        elif table == '2':
            self.view.show_message("\nDeleting producer:")
            self.delete_producer()
        elif table == '3':
            self.view.show_message("\nDeleting form:")
            self.delete_form()
        elif table == '4':
            self.view.show_message("\nDeleting group:")
            self.delete_group()
        elif table == '5':
            self.view.show_message("\nDeleting drug to group:")
            self.delete_drug_group()
        else:
            self.view.show_message("Wrong choice. Try again.")

    def process_search_option(self):
        option = self.view.show_search()

        if option == '1':
            start_time = time.time()
            self.show_drugs_with_groups()
            end_time = time.time()
            elapsed_time = (end_time - start_time) * 1000
            print(f"Час виконання: {elapsed_time:.2f} мс")
        elif option == '2':
            start_time = time.time()
            self.show_sorting_by_price()
            end_time = time.time()
            elapsed_time = (end_time - start_time) * 1000
            print(f"Час виконання: {elapsed_time:.2f} мс")
        elif option == '3':
            start_time = time.time()
            self.show_number_drugs_in_groups()
            end_time = time.time()
            elapsed_time = (end_time - start_time) * 1000
            print(f"Час виконання: {elapsed_time:.2f} мс")
        else:
            self.view.show_menu()

    def add_drug(self):
        try:
            name, price, quantity, form_id, producer_id = self.view.get_drug_input()
            self.model.add_drug(name, price, quantity, form_id, producer_id)
            self.view.show_message("Drug added successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def add_producer(self):
        try:
            name, address, link, phone_number = self.view.get_producer_input()
            self.model.add_producer(name, address, link, phone_number)
            self.view.show_message("Producer added successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def add_form(self):
        try:
            name = self.view.get_form_input()
            self.model.add_form(name)
            self.view.show_message("Form added successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def add_group(self):
        try:
            name = self.view.get_group_input()
            self.model.add_group(name)
            self.view.show_message("Group added successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def add_drug_group(self):
        try:
            drug_id, group_id = self.view.get_drug_group_input()
            self.model.add_drug_group(drug_id, group_id)
            self.view.show_message("Drug-Group added successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def view_drugs(self):
        try:
            drugs = self.model.get_all_drugs()
            self.view.show_drugs(drugs)
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def view_producers(self):
        try:
            producers = self.model.get_all_producers()
            self.view.show_producers(producers)
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def view_forms(self):
        try:
            forms = self.model.get_all_forms()
            self.view.show_forms(forms)
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def view_groups(self):
        try:
            groups = self.model.get_all_groups()
            self.view.show_groups(groups)
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def view_drugs_groups(self):
        try:
            drugs_groups = self.model.get_all_drugs_groups()
            self.view.show_drugs_groups(drugs_groups)
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def show_drugs_with_groups(self):
        try:
            rows = self.model.get_all_drugs_with_groups()
            self.view.show_drugs_with_groups(rows)
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def show_sorting_by_price(self):
        try:
            self.view.show_message("\nYou need to enter the maximum price for filtering.")
            number = self.view.get_number()
            rows = self.model.show_sorting_by_price(number)
            self.view.show_sorting_by_price(rows)
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def show_number_drugs_in_groups(self):
        try:
            rows = self.model.show_number_drugs_in_groups()
            self.view.show_number_drugs_in_groups(rows)
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def update_drug(self):
        try:
            drug_id = self.view.get_drug_id()
            name, price, quantity, form_id, producer_id = self.view.get_drug_input()
            self.model.update_drug(drug_id, name, price, quantity, form_id, producer_id)
            self.view.show_message("Drug updated successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def update_producer(self):
        try:
            producer_id = self.view.get_producer_id()
            name, address, link, phone_number = self.view.get_producer_input()
            self.model.update_producer(producer_id, name, address, link, phone_number)
            self.view.show_message("Producer updated successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def update_form(self):
        try:
            form_id = self.view.get_form_id()
            name = self.view.get_form_input()
            self.model.update_form(form_id, name)
            self.view.show_message("Form updated successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def update_group(self):
        try:
            group_id = self.view.get_group_id()
            name = self.view.get_group_input()
            self.model.update_group(group_id, name)
            self.view.show_message("Group updated successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def update_drug_group(self):
        try:
            drug_id = self.view.get_drug_id()
            group_id = self.view.get_group_id()
            self.model.update_drug_group(drug_id, group_id)
            self.view.show_message("Drug-group updated successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def delete_drug(self):
        try:
            drug_id = self.view.get_drug_id()
            self.model.delete_drug(drug_id)
            self.view.show_message("Drug deleted successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def delete_producer(self):
        try:
            producer_id = self.view.get_producer_id()
            self.model.delete_producer(producer_id)
            self.view.show_message("Producer deleted successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def delete_form(self):
        try:
            form_id = self.view.get_form_id()
            self.model.delete_form(form_id)
            self.view.show_message("Form deleted successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def delete_group(self):
        try:
            group_id = self.view.get_group_id()
            self.model.delete_group(group_id)
            self.view.show_message("Group deleted successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def delete_drug_group(self):
        try:
            group_id = self.view.get_drug_id()
            self.model.delete_drug_group(group_id)
            self.view.show_message("Drug-group deleted successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def add_random_fields(self):
        try:
            number = self.view.get_number()
            self.model.add_random_fields(number)
            self.view.show_message("Random fields added successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

