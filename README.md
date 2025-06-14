
# ✈️ Simple Flight Reservation Desktop App

A simple and user-friendly desktop application for managing flight reservations. Built using **Python**, **Tkinter** for the graphical interface, and **SQLite** for the database.
---

## 📁 Project Structure

```
/flight_reservation_app
├── main.py               # Main app entry point
├── database.py           # SQLite database connection and  setup
├── home.py               # Home page UI
├── booking.py            # Flight booking form UI
├── reservations.py       # View reservations UI
├── edit_reservation.py   # Edit reservations UI
├── assets/               # Contains App icon/images
├── flights.sqlite        # SQLite database file
├── requirements.txt      # Python dependencies
├── README.md             
```

---

## ⚙️ Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/ahmedg3x1/Simple-Flight-Reservation-Desktop-App.git
cd Simple-Flight-Reservation-Desktop-App
```

### Step 2: Install Required Packages

#### ➞ For **Windows**:
```bash
pip install -r requirements.txt
```


#### ➞ For **Linux**:
```bash
sudo apt install python3-tk
pip install -r requirements.txt
```
---

## ▶️ Running the App

```bash
python main.py
```

---

## 🛠️ (Optional) Build Executable with PyInstaller

### Step 1: Install PyInstaller

```bash
pip install pyinstaller
```

### Step 2: Build the Executable

#### ➞ For **Windows**:

```bash
pyinstaller --noconsole --icon assets\App.png --onefile --add-data "assets;assets" main.py
```
> 🗂️ The executable will be located in the `dist/` folder as `main.exe`.

#### ➞ For **Linux**:
```bash
sudo apt install binutils

pyinstaller --noconsole --icon assets/App.png --onefile --add-data "assets:assets" --hidden-import PIL._tkinter_finder main.py
```

> 🗂️ The executable will be located in the `dist/` folder as `main`.
----

