import sqlite3

# curs.execute("""CREATE TABLE reservation (
#                 id integer AUTO_INCREMENT,
#                 name text,
#                 flight_number integer,
#                 departure text,
#                 destination text,
#                 date text,
#                 seat_number integer,
#                 PRIMARY KEY (id))""")



class Database:
    def __init__(self):
        self.conn = sqlite3.connect('flights.sqlite')
        self.curs = self.conn.cursor()

    def create_reservation(self, name, flight_number, departure, destination, date, seat_number):
        with self.conn:
            self.curs.execute("INSERT INTO reservation(name, flight_number, departure, destination, date, seat_number) VALUES(?, ?, ?, ?, ?, ?)", 
                              (name, flight_number, departure, destination, date, seat_number))
   
    def read_reservations(self):
        self.curs.execute("SELECT * FROM reservation")
        return self.curs.fetchall()


    def Update_reservation(self, id, name, flight_number, departure, destination, date, seat_number):
        with self.conn:
            self.curs.execute("""UPDATE reservation 
                              SET name = ?, 
                              flight_number = ?, 
                              departure = ?, 
                              destination = ?, 
                              date = ?, 
                              seat_number = ? 
                              WHERE id = ?""", (name, flight_number, departure, destination, date, seat_number, id))
   
    def delete_reservations(self, id):
        with self.conn:
            self.curs.execute("DELETE FROM reservation WHERE id = ?", (id,))

    def close(self):
        self.conn.close()