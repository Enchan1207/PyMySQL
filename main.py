#
# MySQLアクセスユーティリティ
#
from DBAccess import Accessor

def main():
    pdo = Accessor("")
    pdo.exec("SELECT * FROM StatusesTable", ())

    print("MySQL access util start...")

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Interrupt")


if __name__ == "__main__":
    main()
