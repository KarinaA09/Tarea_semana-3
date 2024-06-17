from datetime import datetime, timedelta


class DailyWeatherData:
    def __init__(self):
        self.data = []  # Lista para almacenar los datos diarios (tuplas de fecha y temperatura)

    def set_data(self, date_str, temperature):
        """
        Método para ingresar datos diarios de temperatura.

        Args:
        - date_str (str): String en formato 'YYYY-MM-DD' representando la fecha.
        - temperature (float): Temperatura registrada para ese día.
        """
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            print(f"Error: La fecha '{date_str}' no tiene el formato esperado 'YYYY-MM-DD'.")
            return

        self.data.append((date, temperature))
        print(f"Dato agregado: Fecha={date_str}, Temperatura={temperature}")

    def calculate_weekly_average(self):
        """
        Método para calcular el promedio semanal de las temperaturas registradas.

        Returns:
        - float: Promedio semanal de las temperaturas.
        """
        if not self.data:
            print("No hay datos para calcular el promedio semanal.")
            return 0.0

        # Obtener la fecha del día actual
        current_date = datetime.now().date()

        # Calcular la fecha de inicio de la semana (7 días atrás)
        start_date = current_date - timedelta(days=current_date.weekday())

        # Filtrar los datos para obtener las temperaturas de la semana actual
        weekly_temperatures = [temp for date, temp in self.data if start_date <= date <= current_date]

        if not weekly_temperatures:
            print(f"No hay datos registrados para la semana del {start_date} al {current_date}.")
            return 0.0

        # Calcular el promedio semanal
        weekly_average = sum(weekly_temperatures) / len(weekly_temperatures)

        return weekly_average


# Ejemplo de uso:
if __name__ == "__main__":
    weather_data = DailyWeatherData()

    # Ingresar datos diarios
    weather_data.set_data('2024-06-10', 25.5)
    weather_data.set_data('2024-06-11', 27.0)
    weather_data.set_data('2024-06-12', 26.8)
    weather_data.set_data('2024-06-13', 28.2)
    weather_data.set_data('2024-06-14', 26.5)
    weather_data.set_data('2024-06-15', 24.9)
    weather_data.set_data('2024-06-16', 25.7)

    # Calcular el promedio semanal
    average_temp = weather_data.calculate_weekly_average()
    print(f"El promedio semanal de temperatura es: {average_temp:.2f}")
