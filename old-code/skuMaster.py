import pysftp
import cx_Oracle
import csv
import datetime
import mailJet
import sys
import shutil

now = datetime.datetime.now()


def logData(msg):
    date_time = now.strftime("%d%m%Y")
    path = "./logs/" + date_time + ".log"
    myfile = open(path, "a")
    myfile.write(msg)
    myfile.close()


def genSKU(
    pYear,
    pMonth,
    orionID,
    orionPass,
    connDetail,
    companyCode,
    sftpHost,
    sftpUser,
    sftpPass,
    sftpPath,
):

    try:
        con = cx_Oracle.connect(orionID, orionPass, connDetail)
        cursor = con.cursor()
        company = companyCode
        dataType = "SKU"
        # year = now.year
        # period = now.month
        year = pYear
        period = pMonth
        filename = company + "_" + dataType + "_P" + str(period) + str(year) + ".csv"
        filename1 = (
            company + "_" + dataType + "_" + now.strftime("%d%m%Y-%H_%M_%S") + ".csv"
        )
        filePath = "C:/kFiles/" + filename
        filePath1 = "C:/kFiles_bkup/" + filename1
        # print ( filename)
        csv_file = open(filePath, "w")
        writer = csv.writer(
            csv_file, delimiter=",", lineterminator="\n", quoting=csv.QUOTE_NONNUMERIC
        )

        sql = (
            """SELECT DISTINCT ITEM_CODE,PLI_COMP_CODE COMPANY,ITEM_NAME,ITEM_IG_CODE ITEM_GROUP ,ITEM_ANLY_CODE_03 CATEGORY , AD_NAME BRAND,ITEM_UOM_CODE,ITEM_FLEX_01 GM,ITEM_FLEX_02 PKT 
                FROM OM_ITEM,OM_ANALYSIS_DETAIL,OM_PRICE_LIST_ITEM
                WHERE ITEM_IG_CODE IN ('K NOODLES','RX','RTEC','PRINGLE')
                AND ITEM_ANLY_CODE_02=AD_CODE
                AND AD_ANLY_TYPE='ITEM' AND AD_ANLY_NO=2
                --AND PLI_ITEM_CODE=ITEM_CODE 
                AND PLI_COMP_CODE='"""
            + company
            + """'"""
        )

        r = cursor.execute(sql)

        header = []
        count = 0
        for desc in cursor.description:
            header.append(desc[0])

        writer.writerow(header)

        numberOfrow = 0
        for row in cursor:
            writer.writerow(row)
            numberOfrow += 1

        cursor.close()
        con.close()
        csv_file.close()

        if numberOfrow > 0:
            try:
                shutil.copy(filePath, filePath1)
                logData("Pushing " + filename + " to SFTP server.\n")
                cnopts = pysftp.CnOpts()
                cnopts.hostkeys = None
                srv = pysftp.Connection(
                    host=sftpHost, username=sftpUser, password=sftpPass, cnopts=cnopts
                )

                with srv.cd(sftpPath):  # chdir to public
                    srv.put(filePath)  # upload file to nodejs/

                # Closes the connection
                srv.close()
            except:
                mailJet.sendEmail(
                    "Error pushing SKU master file to SFTP server",
                    "dev.team@tolaram.com",
                    "Hi Team, Please check. FTP can not connect "
                    + connDetail
                    + companyCode,
                )
                mailJet.sendEmail(
                    "Error pushing SKU master file to SFTP server",
                    "moni.john@tolaram.com",
                    "Hi Team, Please check. FTP can not connect "
                    + connDetail
                    + companyCode,
                )
                mailJet.sendEmail(
                    "Error pushing SKU master file to SFTP server",
                    "rao.topuri@tolaram.com",
                    "Hi Team, Please check. FTP can not connect "
                    + connDetail
                    + companyCode,
                )
                logData("Error pushing file to SFTP server.\n")
    except:
        mailJet.sendEmail(
            "Error connecting database " + companyCode,
            "dev.team@tolaram.com",
            "Hi Team, Please check. Error connecting database "
            + connDetail
            + companyCode,
        )
        mailJet.sendEmail(
            "Error connecting database " + companyCode,
            "moni.john@tolaram.com",
            "Hi Team, Please check. Error connecting database  "
            + connDetail
            + companyCode,
        )
        mailJet.sendEmail(
            "Error connecting database " + companyCode,
            "rao.topuri@tolaram.com",
            "Hi Team, Please check. Error connecting database "
            + connDetail
            + companyCode,
        )
        logData(
            "Error connecting database while running -skuMaster.py- for company - "
            + companyCode
            + " .\n"
        )
