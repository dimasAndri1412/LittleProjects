import  pyodbc as db
import Config
from sqlalchemy import create_engine
from urllib.parse import quote_plus

def connectreconciliationconfig() :

    try:
        cfg = Config.ConnectToDBReconciliationConfig
        passsource = quote_plus(cfg["password"])

        enginessource = create_engine(
            f"mssql+pyodbc://{cfg['user']}:{passsource}"
            f"@{cfg['host']}:{cfg['port']}/{cfg['database']}"
            "?driver=ODBC+Driver+18+for+SQL+Server"
            "&Encrypt=yes"
            "&TrustServerCertificate=yes"
            "&Connection+Timeout=30"
        )

        print("Connected to ReconciliationConfig Successfully")
        return enginessource

    except db.Error as Errors:
        print(f"Terjadi Kesalahan : {Errors}")


def connectparamengine() :

    try:
        cfg = Config.ConnectToDBParamEngine
        passsource = quote_plus(cfg["password"])

        enginessource = create_engine(
            f"mssql+pyodbc://{cfg['user']}:{passsource}"
            f"@{cfg['host']}:{cfg['port']}/{cfg['database']}"
            "?driver=ODBC+Driver+18+for+SQL+Server"
            "&Encrypt=yes"
            "&TrustServerCertificate=yes"
            "&Connection+Timeout=30"
        )

        print("Connected to ParamEngine Successfully")
        return enginessource

    except db.Error as Errors:
        print(f"Terjadi Kesalahan : {Errors}")

