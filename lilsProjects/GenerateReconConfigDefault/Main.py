import os
import GenerateQryInsertReconConfigProduct as RcnConfigProduct
import GenerateQryInsertReconConfigProductAccount as RcnConfigProductAccount
import GenerateQryInsertReconConfigProductFeeTiering as RcnConfigProductThirdPartyStatement
import GenerateQryInsertReconConfigProductThirdPartyStatement as RcnConfigProductThirdPartyStatment


def main():

    try:
        print('='*40)
        print('Parameter ReconciliationConfig')
        print('='*40)

        produtcsid = input("Masukan ProductID : ")
        pathlocation = "C:\\Users\\90184762\\Documents\\Works\\Program\\LittleProjects\\lilsProjects\\ResultFiles"
        os.makedirs(pathlocation, exist_ok=True)

        all_tabs = [
            f"--------------------------------------------------\n "
            f"-- Script Insert Product  \n"
            f"--------------------------------------------------\n"
        ]

        print("Sedang Di Generate")
        rcncfgproduct = RcnConfigProduct.generatequeryinsertcfgproduct(produtcsid,all_tabs)
        rcncfgproductacc = RcnConfigProductAccount.generatequeryinsertcfgproductaccount(produtcsid,all_tabs)
        rcncfgproductfeetiering = RcnConfigProductThirdPartyStatement.generatequeryinsertcfgproductfeetiering(produtcsid,all_tabs)
        rcncfgproductthirdpartystatment = RcnConfigProductThirdPartyStatement.generatequeryinsertcfgproductfeetiering(produtcsid,all_tabs)

        if rcncfgproduct or rcncfgproductacc or rcncfgproductfeetiering :
            filesnamesproduct = f"Insert_Reconciliation_Config_{produtcsid}.sql"
            pathfiles = os.path.join(pathlocation,filesnamesproduct)

            sql_contetnt = "\n".join(all_tabs)
            with open(pathfiles,"w",encoding="utf-8") as products:
                products.write(sql_contetnt)
            print(f"File Berhasil Tergenerate di dalam = {filesnamesproduct}")

        else:
            print("Gagal membuat file. Pastikan ProductID terdaftar di database.")

    except Exception as Errs:
        print(f"Terjadi Kesalah pada bagian {Errs}")

if __name__ ==  "__main__" :
    main()