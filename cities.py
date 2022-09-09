import mysql.connector

class Cities: 
    def __init__(self) -> None:
        self.cnn = mysql.connector.connect(host="localhost", user="root", passwd="RootDaniel13", database="bdejemplopy")

    def __str__(self) -> str:
        datos = self.consulta_países()
        aux = ""
        for row in datos:
            aux = aux + str(row) + "\n"
        return aux

    def consulta_países(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM countries")
        datos = cur.fetchall()
        cur.close()
        return datos

    def buscar_pais(self, id):
        cur = self.cnn.cursor()
        sql = "SELECT * FROM countries WHERE id = {}".format(id)
        cur.execute(sql)
        datos = cur.fetchone()
        cur.close()
        return datos


    def inserta_países(self, ISO3, CountryName, Capital, CurrencyCode):
        cur = self.cnn.cursor()
        sql = '''INSERT INTO countries (ISO3, CountryName, Capital, CurrencyCode)
        VALUES('{}', '{}', '{}', '{}') '''.format(ISO3, CountryName, Capital, CurrencyCode)
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()
        cur.close() 
        
        return n

    def elimina_países(self, id):
        cur = self.cnn.cursor()
        sql = '''DELETE FROM countries WHERE id = {}'''.format(id)  
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n

    def Modificaa_países(self, id, ISO3, CountryName, Capital, CurrencyCode):
        cur = self.cnn.cursor()
        sql = '''UPDATE countries
        SET ISO3 = '{}', CountryName= '{}',Capital= '{}', CurrencyCode= '{}' WHERE id = {}'''.format( ISO3, CountryName, Capital, CurrencyCode,id)  
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n
