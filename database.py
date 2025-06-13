import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('flights.sqlite')
        self.curs = self.conn.cursor()
        self.create_table()

    def create_table(self):
        if not self.check_table_exist():
            self.curs.execute("""CREATE TABLE reservation (
                                id integer,
                                name text,
                                flight_number integer,
                                departure text,
                                destination text,
                                date text,
                                seat_number integer,
                                PRIMARY KEY (id))""")

    def check_table_exist(self):
        self.curs.execute("SELECT EXISTS(SELECT name FROM sqlite_master WHERE type='table' AND name='reservation')");
        return self.curs.fetchone()[0]
    
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