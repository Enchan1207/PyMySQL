#
# MySQLアクセスユーティリティ
#
from DBAccess import Accessor
import settings

def main():
    pdo = Accessor(settings.DB_QUERY)

    if not pdo.isConnected:
        print("ERROR: Database connection failed.")
        return
    print("MySQL access util start...")

    records = [
        (0, 3000),
        (1, 114514),
    ]
    pdo.exec("INSERT INTO StatusesTable VALUES (%s, %s)", records)

    pdo.exec("SELECT * FROM StatusesTable ORDER BY id LIMIT 5;")
    print(pdo.fetch())

    pdo.exec("DELETE FROM StatusesTable ORDER BY id LIMIT 2;")

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Interrupt")
        pdo.disConnection()

if __name__ == "__main__":
    main()
