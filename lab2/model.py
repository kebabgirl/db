from db import Base, Session, engine
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Numeric, TIMESTAMP, ForeignKey, Table

s = Session()

tables = {
    1: 'grugs',
    2: 'producers',
    3: 'forms',
    4: 'groups',
    5: 'drugs_groups',
}


class Drug_Group(Base):
    __tablename__ = 'drugs_groups'
    drug_id = Column(Integer, ForeignKey('drugs.drug_id'), primary_key=True)
    group_id = Column(Integer, ForeignKey('groups.group_id'), primary_key=True)

    def __init__(self, drug_id, group_id):
        self.drug_id = drug_id
        self.group_id = group_id

    def __repr__(self):
        return f"<Drugs_Groups(drug_id={self.drug_id}, group_id={self.group_id})>"


class Drug(Base):
    __tablename__ = 'drugs'
    drug_id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Numeric)
    quantity = Column(String)

    form_id = Column(Integer, ForeignKey('forms.form_id'))
    producer_id= Column(Integer, ForeignKey('producers.producer_id'))

    drug_group = relationship("Drug_Group")

    def __init__(self, name, price, quantity, form_id, producer_id):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.form_id = form_id
        self.producer_id = producer_id

    def __repr__(self):
        return f"<Drugs(drug_id={self.drug_id}, name={self.name}, price={self.price}, quantity={self.quantity}, form_id={self.form_id}, producer_id={self.producer_id})>"


class Producer(Base):
    __tablename__ = 'producers'
    producer_id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    link = Column(String)
    phone_number = Column(String)

    drug = relationship("Drug")

    def __init__(self, name, address, link, phone_number):
        self.name = name
        self.address = address
        self.link = link
        self.phone_number = phone_number

    def __repr__(self):
        return f"<Producers(producer_id={self.producer_id}, name={self.name}, address={self.address}, link={self.link}, phone_number={self.phone_number})>"


class Form(Base):
    __tablename__ = 'forms'
    form_id = Column(Integer, primary_key=True)
    name = Column(String)

    drug = relationship("Drug")

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Forms(form_id={self.form_id}, name={self.name})>"


class Group(Base):
    __tablename__ = 'groups'
    group_id = Column(Integer, primary_key=True)
    name = Column(String)

    drug_group = relationship("Drug_Group")

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Groups(group_id={self.group_id}, name={self.name})>"


class Model:
    def __init__(self):
        self.session = Session()
        self.connection = engine.connect()

    @staticmethod
    def insert_drug(name: str, price: float, quantity: str, form_id: int, producer_id: int) -> None:
        drug = Drug(name=name, price=price, quantity=quantity, form_id=form_id, producer_id=producer_id)
        s.add(drug)
        s.commit()

    @staticmethod
    def insert_producer(name: str, address: str, link: str, phone_number: str) -> None:
        producer = Producer(name=name, address=address, link=link, phone_number=phone_number)
        s.add(producer)
        s.commit()

    @staticmethod
    def insert_form(name: str) -> None:
        form = Form(name=name)
        s.add(form)
        s.commit()

    @staticmethod
    def insert_group(name: str) -> None:
        group = Group(name=name)
        s.add(group)
        s.commit()

    @staticmethod
    def insert_drug_group(drug_id: int, group_id: int) -> None:
        drug_group = Drug_Group(drug_id=drug_id, group_id=group_id)
        s.add(drug_group)
        s.commit()

    @staticmethod
    def show_drugs():
        return s.query(Drug.drug_id, Drug.name, Drug.price, Drug.quantity, Drug.form_id, Drug.producer_id).all()

    @staticmethod
    def show_producers():
        return s.query(Producer.producer_id, Producer.name, Producer.address, Producer.link, Producer.phone_number).all()

    @staticmethod
    def show_forms():
        return s.query(Form.form_id, Form.name).all()

    @staticmethod
    def show_groups():
        return s.query(Group.group_id, Group.name).all()

    @staticmethod
    def show_drugs_groups():
        return s.query(Drug_Group.drug_id, Drug_Group.group_id).all()

    @staticmethod
    def update_drug(drug_id: int, name: str, price: float, quantity: str, form_id: int, producer_id: int) -> None:
        s.query(Drug).filter_by(drug_id=drug_id).update({Drug.name: name, Drug.price: price, Drug.quantity: quantity, Drug.form_id: form_id, Drug.producer_id: producer_id})
        s.commit()

    @staticmethod
    def update_producer(producer_id: int, name: str, address: str, link: str, phone_number: str) -> None:
        s.query(Producer).filter_by(producer_id=producer_id).update({Producer.name: name, Producer.address: address, Producer.link: link, Producer.phone_number: phone_number})
        s.commit()

    @staticmethod
    def update_form(form_id: int, name: str) -> None:
        s.query(Form).filter_by(form_id=form_id).update({Form.name: name})
        s.commit()

    @staticmethod
    def update_group(group_id: int, name: str) -> None:
        s.query(Group).filter_by(group_id=group_id).update({Group.name: name})
        s.commit()

    @staticmethod
    def update_drug_group(drug_id: int, group_id: int) -> None:
        s.query(Drug_Group).filter_by(drug_id=drug_id).update({Drug_Group.group_id: group_id})
        s.commit()

    @staticmethod
    def delete_drug(drug_id) -> None:
        drug = s.query(Drug).filter_by(drug_id=drug_id).one()
        s.delete(drug)
        s.commit()

    @staticmethod
    def delete_producer(producer_id) -> None:
        producer = s.query(Producer).filter_by(producer_id=producer_id).one()
        s.delete(producer)
        s.commit()

    @staticmethod
    def delete_form(form_id) -> None:
        form = s.query(Form).filter_by(form_id=form_id).one()
        s.delete(form)
        s.commit()

    @staticmethod
    def delete_group(group_id) -> None:
        group = s.query(Group).filter_by(group_id=group_id).one()
        s.delete(group)
        s.commit()

    @staticmethod
    def delete_drug_group(group_id) -> None:
        drugs_groups = s.query(Drug_Group).filter_by(group_id=group_id).all()
        for drug_group in drugs_groups:
            s.delete(drug_group)
        s.commit()
