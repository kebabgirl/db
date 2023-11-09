import psycopg2

class Model:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname='directory',
            user='postgres',
            password='1111',
            host='localhost',
            port=3000
        )

    def add_drug(self, name, price, quantity, form_id, producer_id):
        c = self.conn.cursor()
        c.execute('INSERT INTO drugs (name, price, quantity, form_id, producer_id) VALUES (%s, %s, %s, %s, %s)', (name, price, quantity, form_id, producer_id))
        self.conn.commit()

    def add_producer(self, name, address, link, phone_number):
        c = self.conn.cursor()
        c.execute('INSERT INTO producers (name, address, link , phone_number) VALUES (%s, %s, %s, %s)', (name, address, link, phone_number))
        self.conn.commit()

    def add_form(self, name):
        c = self.conn.cursor()
        c.execute('INSERT INTO forms (name) VALUES (%s)', (name,))
        self.conn.commit()

    def add_group(self, name):
        c = self.conn.cursor()
        c.execute('INSERT INTO groups (name) VALUES (%s)', (name,))
        self.conn.commit()

    def add_drug_group(self, drug_id, group_id):
        c = self.conn.cursor()
        c.execute('INSERT INTO drugs_groups (drug_id, group_id) VALUES (%s, %s)', (drug_id, group_id))
        self.conn.commit()

    def get_all_drugs(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM drugs')
        return c.fetchall()

    def get_all_producers(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM producers')
        return c.fetchall()

    def get_all_forms(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM forms')
        return c.fetchall()

    def get_all_groups(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM groups')
        return c.fetchall()

    def get_all_drugs_groups(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM drugs_groups')
        return c.fetchall()

    def get_all_drugs_with_groups(self):
        c = self.conn.cursor()
        c.execute('SELECT drugs.drug_id, drugs.name AS drug_name, groups.name AS group_name FROM drugs LEFT JOIN drugs_groups ON drugs_groups.drug_id = drugs.drug_id LEFT JOIN groups ON drugs_groups.group_id = groups.group_id;')
        return c.fetchall()

    def show_sorting_by_price(self, number):
        c = self.conn.cursor()
        c.execute('SELECT drugs.name AS drug_name, forms.name AS form_name, drugs.price FROM drugs JOIN forms ON drugs.form_id = forms.form_id WHERE drugs.price < %s ORDER BY drugs.price ASC;', (number,))
        return c.fetchall()

    def show_number_drugs_in_groups(self):
        c = self.conn.cursor()
        c.execute('SELECT groups.name AS group_name, COALESCE(COUNT(drugs.drug_id), 0) AS drug_count FROM groups LEFT JOIN drugs_groups ON groups.group_id = drugs_groups.group_id LEFT JOIN drugs ON drugs_groups.drug_id = drugs.drug_id GROUP BY groups.group_id, groups.name ORDER BY group_name;')
        return c.fetchall()

    def update_drug(self, drug_id, name, price, quantity, form_id, producer_id):
        c = self.conn.cursor()
        c.execute('UPDATE drugs SET name=%s, price=%s, quantity=%s, form_id=%s, producer_id=%s WHERE drug_id=%s', (name, price, quantity, form_id, producer_id, drug_id))
        self.conn.commit()

    def update_producer(self, producer_id, name, address, link, phone_number):
        c = self.conn.cursor()
        c.execute('UPDATE producers SET name=%s, address=%s, link=%s, phone_number=%s WHERE producer_id=%s', (name, address, link, phone_number, producer_id))
        self.conn.commit()

    def update_form(self, form_id, name):
        c = self.conn.cursor()
        c.execute('UPDATE forms SET name=%s WHERE form_id=%s', (name, form_id))
        self.conn.commit()

    def update_group(self, group_id, name):
        c = self.conn.cursor()
        c.execute('UPDATE groups SET name=%s WHERE group_id=%s', (name, group_id))
        self.conn.commit()

    def update_drug_group(self, drug_id, group_id):
        c = self.conn.cursor()
        c.execute('UPDATE drugs_groups SET group_id = %s WHERE drug_id = %s', (group_id, drug_id))
        self.conn.commit()

    def delete_drug(self, drug_id):
        c = self.conn.cursor()
        c.execute('DELETE FROM drugs WHERE drug_id=%s', (drug_id,))
        self.conn.commit()

    def delete_producer(self, producer_id):
        c = self.conn.cursor()
        c.execute('DELETE FROM producers WHERE producer_id=%s', (producer_id,))
        self.conn.commit()

    def delete_form(self, form_id):
        c = self.conn.cursor()
        c.execute('DELETE FROM forms WHERE form_id=%s', (form_id,))
        self.conn.commit()

    def delete_group(self, group_id):
        c = self.conn.cursor()
        c.execute('DELETE FROM groups WHERE group_id=%s', (group_id,))
        self.conn.commit()

    def delete_drug_group(self, drug_id):
        c = self.conn.cursor()
        c.execute('DELETE FROM drugs_groups WHERE drug_id = %s', (drug_id,))
        self.conn.commit()

    def add_random_fields(self, number):
        c = self.conn.cursor()
        c.execute(
            'INSERT INTO drugs (name, price, quantity, form_id, producer_id) SELECT chr(trunc(65 + random() * 25)::int) || chr(trunc(65 + random() * 25)::int), random() * 100, trunc(random() * 100), trunc(random() * 7) + 1, trunc(random() * 5) + 1 FROM generate_series(1, %s)',
            (number,)
        )
        self.conn.commit()


