import sqlite3

from vehicle import Vehicle


class Garage:
    def __init__(self):
        self.conn = sqlite3.connect("garage.db", check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS vehiculos (id INTEGER PRIMARY KEY AUTOINCREMENT, marca TEXT, model TEXT, year INTEGER, km REAL)"
        )
        self.conn.commit()

    def add_car(self):

        vehicle_make = input("Introduce la marca del vehiculo: ")
        vehicle_model = input("Introduce el modelo del vehiculo: ")

        year_valido = True
        while year_valido:

            try:
                vehicle_year = int(input("Introduce el año del vehiculo (ej: 2007): "))
                year_valido = False

            except ValueError:
                print("Porfavor introduce un numero valido!")

        km_valido = True
        while km_valido:

            try:
                vehicle_km = float(input("Introduce el kilometraje del vehiculo: "))
                km_valido = False

            except ValueError:
                print("Porfavor introduce un numero valido!")

        print()
        print("--------------------------------------------")
        print("Vehiculo registrado correctamente!")

        new_vehicle = Vehicle(
            make=vehicle_make, model=vehicle_model, year=vehicle_year, km=vehicle_km
        )

        vals = (vehicle_make, vehicle_model, vehicle_year, vehicle_km)
        sql = "insert into vehiculos(marca, model, year, km) values(?,?,?,?)"

        self.cursor.execute(sql, vals)
        self.conn.commit()

    def list_cars(self):

        self.cursor.execute("SELECT * FROM vehiculos")
        selected = self.cursor.fetchall()
        return selected

    def close_db(self):
        self.conn.close()

    def delete_car(self):

        try:
            print("--------------------------------------------")
            car_to_delete = int(input("Introduce el ID del vehiculo a eliminar: "))
            print("--------------------------------------------")

        except ValueError:
            print("Porfavor introduce un numero valido!")

        self.cursor.execute("SELECT id FROM vehiculos")
        selected = self.cursor.fetchall()

        ids = [row[0] for row in selected]

        if car_to_delete not in ids:
            print("El ID seleccionado no existe")
            return

        self.cursor.execute("DELETE FROM vehiculos WHERE id = ?", (car_to_delete,))
        self.conn.commit()
        print(f"Se ha eliminado el ID:{car_to_delete}, correctamente!")

    def update_vehicle_km(self):

        try:
            print("--------------------------------------------")
            id_to_update = int(
                input("Por favor introduzca el ID del vehiculo a actualizar: ")
            )
            print("--------------------------------------------")

            new_km = float(input("Introduzca el nuevo kilometraje: "))
            print("--------------------------------------------")

            self.cursor.execute("SELECT id FROM vehiculos")
            selected = self.cursor.fetchall()

            ids = [row[0] for row in selected]

            if id_to_update not in ids:
                print("El ID seleccionado no existe")
                return

            vals = (new_km, id_to_update)

            self.cursor.execute("UPDATE vehiculos SET km = ? WHERE id = ?", vals)
            self.conn.commit()

            print("Kilometraje actualizado con exito")

        except ValueError:
            print("Porfavor introduce un numero valido!")

    def add_car_web(self, marca, model, year, km):
        sql = "INSERT INTO vehiculos(marca, model, year, km) VALUES(?,?,?,?)"
        self.cursor.execute(sql, (marca, model, year, km))
        self.conn.commit()

    def delete_car_web(self, car_id):
        self.cursor.execute("DELETE FROM vehiculos WHERE id = ?", (car_id,))
        self.conn.commit()

    def update_km_web(self, car_id, new_km):
        self.cursor.execute("UPDATE vehiculos SET km=? WHERE id = ?", (new_km, car_id))
        self.conn.commit()

    def get_stats(self):
        self.cursor.execute("SELECT COUNT(*), AVG(km), MAX(km) FROM vehiculos")
        return self.cursor.fetchone()

    def get_upcoming_services(self):
        self.cursor.execute(
            "SELECT * FROM vehiculos WHERE (km % 10000) > 9500 OR (km % 10000) < 500 AND km > 500"
        )
        return self.cursor.fetchall()
