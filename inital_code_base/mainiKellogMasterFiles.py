import customerMaster
import skuMaster
import mailJet
import datetime
#from dateutil.relativedelta import relativedelta
now = datetime.datetime.now()


def logData(msg):
    date_time = now.strftime("%d%m%Y")
    path = './logs/' + date_time + '.log'
    myfile = open(path, 'a')
    myfile.write(msg)
    myfile.close()


year = now.year
period = now.month
sftpHost = 'aloc3kru2lzdi.westeurope.azurecontainer.io'
sftpUser = 'orion'
sftpPass = "M3LC0rp234!@0011"
sftpPath = "/upload/TEST-ENV"
logData('Script: mainiKellogMasterFiles.py\n')
logData('Date: '+now.strftime("%b %d %Y %H:%M:%S")+'\n')

#year = 2020
#period = 12

conndict = {
    "KTLFTZ": ["orktnl", "orktnl", "10.1.28.8:1521/orcl"],
    "KTNL": ["orktnl", "orktnl", "10.1.28.8:1521/orcl"],
    "KTEG": ["orkteg", "orkteg", "192.168.1.37:1521/orcl"],
    "KTEPL": ["orktsa", "orktsa", "192.168.1.37:1521/orcl"],
    "KTSA": ["orktsa", "orktsa", "192.168.1.37:1521/orcl"],
    "KTGL": ["orktgl", "orktgl", "10.1.8.5:1521/orcl"],
    "KTPL": ["orsing", "orsing", "10.1.4.16:1521/orsing"],
    "KTNSPL": ["orsing", "orsing", "10.1.4.16:1521/orsing"]
}

for comp in conndict:
    compDetail = conndict[comp]
    # print(comp)
    vComp = comp
    vUser = compDetail[0]
    vPass = compDetail[1]
    vConnDesc = compDetail[2]
    logData('Company: '+vComp+'\n')

    if vComp != 'KTPL' and vComp != 'KTNSPL':

        customerMaster.genCustomer(
            year, period, vUser, vPass, vConnDesc, vComp, sftpHost, sftpUser, sftpPass, sftpPath)

        skuMaster.genSKU(year, period, vUser, vPass, vConnDesc,
                         vComp, sftpHost, sftpUser, sftpPass, sftpPath)

logData('Script completed at '+now.strftime("%b %d %Y %H:%M:%S")+'\n\n')
