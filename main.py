# Importarea si definirea claselor folosite

from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "CLJ"

# Daca in baza de date importata de clasa DataManager nu sunt inregistrate destinatii, se apeleaza functia de cautare a clasei FlightSearch

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])

# Codurile iata preluate de functia Get_destination_code sunt inregistrate in baza de date Google Sheet

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

# Daca baza de date nu este goala, sau dupa ce acesteia i-au fost atribuite noi coduri iata, pentru fiecare destinatie inregistrata
#se va cauta un zbor folosind functia clasei FlightSearch cu parametrii indicati.

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

# Daca pretul ofertei este mai mic decat cel din baza de date, este formulat un mesaj care va fi trimis pe numarul de telefon inregistrat de utilizator.
#Pentru trimiterea mesajului, se foloseste platforma Twilio apelata de functia clasei NotificationManager

    if flight.price < destination["lowestPrice"]:
        notification_manager.send_sms(
            message=f"Pret scauzt: {flight.price}$ pentru zborul {flight.origin_city}-{flight.origin_airport} catre {flight.destination_city}-{flight.destination_airport}, din {flight.out_date} pana {flight.return_date}."
        )
