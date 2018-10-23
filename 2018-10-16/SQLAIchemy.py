from sqlalchemy import Column,String,create_engine,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base

Base =declarative_base()

class User(Base):

    __tablename__ ='user'

    id = Column(String(20),primary_key=True)
    name = Column(String(20))

    sorce = relationship('Book')


class Book(Base):
    __table__ ='book'

    id =Column(String(20),primary_key=True)
    name = Column(String(20))

    user_id = Column(String(20),ForeignKey('user.id'))

engine = create_engine('mysql+mysqlconnector://root:root123@localhost:3306/test')
DBSession = sessionmaker(bind=engine)

session = DBSession()
new_user = User(id='5',name='Bob')
session.add(new_user)
session.commit()
session.close()

session =DBSession()
user = session.query(User).filter(User.id=='5').one()
print('type:',type(user))
print('name:',user.name)
session.close()





