from datetime import date, datetime
import sqlite3
import shutil

source = "./database/hotel_reservtion_db.db"
db_file = "database/working_db.db"
shutil.copyfile(source, db_file) #Copy original DB first to always start fresh.

def date_to_db(d: date) -> str:
    return d.isoformat()

def db_to_date(s: str) -> date:
    return datetime.strptime(s.decode(), "%Y-%m-%d").date()

## Adapter: Wandelt `date`-Objekt in `TEXT` um
sqlite3.register_adapter(date, date_to_db)

## Konverter: Wandelt gespeicherte `TEXT`-Werte wieder in `date`
sqlite3.register_converter("DATE", db_to_date)

# Kontextmanager, damit das Objekt am Ende des Blocks geschlossen wird
def connect(connection_str: str):
    with sqlite3.connect(connection_str, detect_types=sqlite3.PARSE_DECLTYPES) as conn:
