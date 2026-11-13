import ConnectToDB as Conns
import pandas as pd

def generatequeryinsertcfg() :
    try :

        produtcsid = input("Masukan ProductID :")
        conn = Conns.connectreconciliationconfig()

        qrysql = (
            f"Select * from Product where ProductID = '{produtcsid}' "
        )

        dfqry = pd.read_sql(qrysql, conn)
        print(dfqry)


    except Exception as errs:
        print(f"Terjadi Kesalahan pada {errs}")

generatequeryinsertcfg()