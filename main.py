from garage import Garage
from menu import Menu

car_manager = Garage()

app_running = True

while app_running:

    Menu.show_menu()

    entry = input("Que desea hacer? :")

    try:
        user_choice = int(entry)

        if user_choice == 5:
            app_running = False
            print("Gracias por usar nuestros servicios!")
        elif (
            user_choice == 1 or user_choice == 2 or user_choice == 3 or user_choice == 4
        ):
            print("Procesando su eleccion!")
            print("--------------------------------------------")
        else:
            print("Porfavor ingrese 1, 2, 3, 4 or 5!")

    except ValueError:
        print("Porfavor ingrese un numero valido!")
        print("--------------------------------------------")

    if user_choice == 1:
        coches = car_manager.list_cars()
        if not coches:
            print("garaje vacio!")
        else:
            for id, make, model, year, km in coches:
                print(f"{id}. {make} {model}")

    elif user_choice == 2:
        car_manager.add_car()

    elif user_choice == 3:
        car_manager.list_cars()
        car_manager.delete_car()

    elif user_choice == 4:
        car_manager.list_cars()
        car_manager.update_vehicle_km()


car_manager.close_db()
