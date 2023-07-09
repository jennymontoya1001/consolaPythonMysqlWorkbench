import pymysql
import os

class App:

    def __init__(self):
        self.conn = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            db='master'
            )
        self.cursor = self.conn.cursor()

    def Insertar(self):
        document = int(input("Ingrese documento de identidad: \n"))
        name = input("Ingrese sus nombres: \n")
        lastName = input("Ingrese sus apellidos: \n")
        phone = int(input("Ingrese número de teléfono: \n"))
        address = input("Ingrese dirección: \n")
        sql = "INSERT INTO STUDENT (DOCUMENT,NAME,LASTNAME,PHONE,ADDRESS) VALUES ('{}','{}','{}','{}','{}')".format(document,name,lastName,phone,address)

        self.cursor.execute(sql)
        print("Ingresado a la base de datos correctamente")
        self.conn.commit()
        os.system('pause')


application = App()
application.Insertar()
