# -*- coding:utf-8 -*-
__author__ = 'kafka'



import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String,BOOLEAN,Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python ins\tance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python ins\tance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

# company table....
class TBCompany(Base):
    __tablename__='tbcompany'
    id=Column(Integer,primary_key=True)
    bizName=Column(String(),nullable=False)   #상호
    bizCode=Column(String(10),nullable=False,unique=True) #사업자번호
    bizBossName=Column(String(20))
    bizType=Column(String(100)) #업태
    bizKind=Column(String(100)) #업종
    bizAddr = Column(String(200))
    bizTel = Column(String(20))
    bizPhone= Column(String(20))
    bizEmail=Column(String(50))
    bizActivity=Column(Boolean(False))

class TBUser(Base):
    __tablename__="tbuser"
    id=Column(Integer,primary_key=True)
    userEmail  =Column(String(50),nullable=False,unique=True)#이메일이 곧 아이디다.
    userName=Column(String(10)) #이름.
    userMinNumber=Column(String(20)) #주민등록번호...
    userPhone=Column(String(20)) #핸드폰.
    userPosition=Column(String(10))#직책
    userAddr=Column(String(50)) #집주소.
    userEtc = Column(String(255)) #기타사항..
    companykey = Column(Integer,ForeignKey('tbcompany.id'))


DB_PATH=os.path.abspath(os.path.dirname(sys.argv[0]))+'/database_company.sqlite'

# Create an engine that stores data in the local director
class DataBaseCompany:

    def onCreate(self):

        engine = create_engine('sqlite:///'+DB_PATH)
        # engine = create_engine('sqlite:///'+DB_PATH)
        print "---engine to ", engine

        Base.metadata.create_all(engine)

        return engine

    def get_DBPATH(self):
        return os.path.abspath(os.path.dirname(sys.argv[0]))+'/database_company.sqlite'

##....
# sqlalchemy_example.db file.

