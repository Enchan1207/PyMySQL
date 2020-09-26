#
# 接続用環境変数設定
#

import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

DB_QUERY = os.environ.get("DB_QUERY")