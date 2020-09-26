#
# DBアクセサ
#
from urllib.parse import urlparse
import mysql.connector as MySQL

class Accessor():
    def __init__(self, databaseURL):
        self.connection = None
        self.cursor = None

        # 接続
        url = urlparse(databaseURL)
        self.connection = MySQL.connect(
            host = url.hostname or 'localhost',
            port = url.port or 3306,
            user = url.username or 'root',
            password = url.password or 'password',
            database = url.path[1:] or 'test_database',
        )
        self.connection.ping(reconnect = True)
        self.isConnected = self.connection.is_connected()

        # 接続できたらcursorを作成
        if self.isConnected:
            self.cursor = self.connection.cursor()

    # SQL実行
    def exec(self, sql, param):
        if not self.isConnected:
            return -1

        print(type(param))
        self.cursor.execute(sql, param)

