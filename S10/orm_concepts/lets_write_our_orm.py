import sqlite3


conn = sqlite3.connect('my_database.sqlite')



class DB:
    def __init__(self, **kwargs):
        class_dict = self.__class__.__dict__
        class_keys = class_dict.keys()
        cols = [k + ' ' + class_dict[k]  for k in class_keys if not k.startswith('_')]
        other = ','.join(cols)

        tbl = self.__class__.__name__

        conn.execute("""
            create table if not exists {table_name}(
              id integer primary key autoincrement ,
              {other}
              );""".format(table_name=tbl, other=other))

        columns = ','.join(tuple(kwargs.keys()))
        vals = str(tuple(kwargs.values()))
        insert = """INSERT INTO {table_name} ({columns}) VALUES {vals}""".format(
            table_name=tbl, columns=columns, vals=vals)
        print(insert)
        conn.execute(insert)
        conn.commit()


class Person(DB):
    firstname = 'char(20)'
    lastname = 'char(20)'
    adress = 'TEXT'
    age = 'integer'


class Track(DB):
    name = 'char(30)'
    milliseconds = 'INTEGER'




p = Person(firstname='John', lastname='Smith', age=30)
p.firstname
Track(name='Stairway To Heaven', milliseconds=1000)