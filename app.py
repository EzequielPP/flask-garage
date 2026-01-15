from flask import Flask, redirect, render_template, request

from garage import Garage

app = Flask(__name__)
car_manager = Garage()


@app.route("/")
def index():
    coches = car_manager.list_cars()
    stats = car_manager.get_stats()
    alertas = car_manager.get_upcoming_services()

    return render_template(
        "index.html", lista_vehiculos=coches, stats=stats, alertas=alertas
    )


@app.route("/add", methods=["POST"])
def add_vehicle():
    marca = request.form.get("marca")
    modelo = request.form.get("model")
    year = request.form.get("year")
    km = request.form.get("km")

    car_manager.add_car_web(marca, modelo, year, km)

    return redirect("/")


@app.route("/delete/<int:car_id>", methods=["POST"])
def delete_vehicle(car_id):
    car_manager.delete_car_web(car_id)
    return redirect("/")


@app.route("/update_km/<int:car_id>", methods=["POST"])
def update_km(car_id):
    nuevo_km = request.form.get("nuevo_km")
    car_manager.update_km_web(car_id, nuevo_km)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
