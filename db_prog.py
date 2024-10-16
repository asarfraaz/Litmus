import sqlite3
import os.path

def display_rows(cur):
    for row in cur:
        print(row)
        #print(f'{row(1):10} {row[2]:3} {row[-1]}')

def get_db_info():
    dbfile = 'students_info_db.sqlite'
    dbpath = os.path.join("data", dbfile)

    if not os.path.exists(dbpath):
        raise SystemExit(f'{dbpath} not found')

    return dbpath

def main():
    db_filepath = get_db_info()

    conn = sqlite3.connect(db_filepath)
    cur = conn.cursor()

    cur.execute( """
        SELECT * FROM 'Students' """ )

    display_rows(cur)

if __name__ == "__main__":
    main()
