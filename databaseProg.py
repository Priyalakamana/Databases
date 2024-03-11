import pyodbc

# Database connection parameters
server = 'localhost'
database = 'ResortMgmtSystem'
username = 'sa'
password = 'Siddhu@1831'
driver = 'SQL Server'

# Connect to the database
connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'
connection = pyodbc.connect(connection_string)
cursor = connection.cursor()

try:
    # Query data from the database
    query = '''
            SELECT
                Bookings.booking_id,
                Bookings.is_canceled,
                Bookings.lead_time,
                Bookings.arrival_date_year,
                Bookings.arrival_date_month,
                Bookings.arrival_date_week_number,
                Bookings.arrival_date_day_of_month,
                Bookings.stays_in_weekend_nights,
                Bookings.stays_in_week_nights,
                Bookings.adults,
                Bookings.children,
                Bookings.babies,
                Bookings.meal,
                Countries.country_name,
                MarketSegments.market_segment,
                DepositTypes.deposit_type,
                Guests.name AS guest_name,
                RoomTypes.room_type,
                MealTypes.meal_type
            FROM
                Bookings
                INNER JOIN Countries ON Bookings.country_id = Countries.country_id
                INNER JOIN MarketSegments ON Bookings.market_segment_id = MarketSegments.segment_id
                INNER JOIN DepositTypes ON Bookings.deposit_type_id = DepositTypes.deposit_type_id
                INNER JOIN Guests ON Bookings.guest_id = Guests.guest_id
                INNER JOIN RoomTypes ON Bookings.room_type_id = RoomTypes.room_type_id
                INNER JOIN MealTypes ON Bookings.meal_type_id = MealTypes.meal_type_id;
            '''

    cursor.execute(query)

    # Fetch data and display on the screen
    print("Booking Report:")
    print("------------------------------------------------------------")
    for row in cursor.fetchall():
        print(f"Booking ID: {row.booking_id}, Canceled: {row.is_canceled}, Lead Time: {row.lead_time}, Arrival Date: {row.arrival_date_year}-{row.arrival_date_month}-{row.arrival_date_day_of_month}, Country: {row.country_name}, Guest: {row.guest_name}")

    # Save data to a text file
    with open('booking_report.txt', 'w') as file:
        file.write("Booking Report:\n")
        file.write("------------------------------------------------------------\n")
        for row in cursor.fetchall():
            file.write(f"Booking ID: {row.booking_id}, Canceled: {row.is_canceled}, Lead Time: {row.lead_time}, Arrival Date: {row.arrival_date_year}-{row.arrival_date_month}-{row.arrival_date_day_of_month}, Country: {row.country_name}, Guest: {row.guest_name}\n")

finally:
    # Close the cursor and connection
    cursor.close()
    connection.close()
