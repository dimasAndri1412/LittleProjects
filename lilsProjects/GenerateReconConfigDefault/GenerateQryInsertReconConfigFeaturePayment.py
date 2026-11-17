import ConnectToDB as Conns
import pandas as pd

def format_sql_values(df):
    val_rows = []
    for _, row in df.iterrows():
        formatted_values = []
        for v in row:
            if pd.isna(v):
                formatted_values.append("NULL")
            elif isinstance(v, (int, float)):
                formatted_values.append(f"'{int(v)}'" if v == int(v) else f"'{v}'")
            else:
                clean_val = str(v).replace("'", "''")
                formatted_values.append(f"'{clean_val}'")
        val_rows.append(f"({','.join(formatted_values)})")
    return ",\n  ".join(val_rows)

def generatequeryinsertcfgfeaturepayment(produtcsid,all_tabs) :
    try :

        conn = Conns.connectreconciliationconfig()
        qrysql = (
            f"Select FeatureId, ProductId, PaymentType, BRIActingAs, DebitAccountDefinition, DebitDescription, CreditAccountDefinition, CreditDescription, Fee1AccountDefinition, Fee1Description, Fee1Definition, Fee1Calculation, Fee1Value, Fee2AccountDefinition, Fee2Description, Fee2Definition, Fee2Calculation, Fee2Value, Fee3AccountDefinition, Fee3Description, Fee3Definition, Fee3Calculation, Fee3Value " # <-- Pastikan ada spasi di sini
            f"from ReconciliationConfig..FeaturePayment where ProductID = '{produtcsid}' "
        )
        dfqry = pd.read_sql(qrysql, conn)

        if not dfqry.empty :
            listprdid = dfqry['ProductId'].iloc(0)
            jmldata = len(dfqry)
            print(f"Ditemukan {jmldata} ProductId pada FeaturePayment untuk ProductId Berikut '{produtcsid}'.")

            dfinsert = dfqry.drop(columns=['ProductId'])
            colsfitur = ",".join(dfinsert.columns)
            valuesfitur = format_sql_values(dfinsert)
            insertfitur = f"INSERT INTO ReconciliationConfig..FeaturePayment ({colsfitur}) VALUES\n  {valuesfitur};"

            productsids = dfqry['ProductId'].iloc[0]
            writefiles = all_tabs

            bodyscriptrcncfgproduct = (
                f"--- ReconciliationConfig - FeaturePayment \n"
                f"IF NOT EXISTS ( \n"
                f"  SELECT * FROM ReconciliationConfig..FeaturePayment\n"
                f"  WHERE ProductId = '{productsids}'\n"
                f") BEGIN \n"
                f"  {insertfitur}\n"
                f"  END \n"
                f"  ELSE \n"
                f"    BEGIN \n"
                f"      PRINT('Values sudah ada untuk table FeaturePayment') \n"
                f"    END\n"
                f"\nGO\n\n"
            )

            writefiles.append(bodyscriptrcncfgproduct +'\n')
            return listprdid

        else:
            print('Data Table ProductFeeTiering tidak tersedia ')
            return []

    except Exception as errs:
        print(f"Terjadi Kesalahan pada {errs}")

