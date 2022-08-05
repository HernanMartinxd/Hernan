import gspread
from oauth2client import service_account


def leerCredenciales():
    scp = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    creds = service_account.ServiceAccountCredentials.from_json_keyfile_name("basic-zenith-358319-8d2f66396871.json", scp)
    client = gspread.authorize(creds)

    hoja_c = client.open('prueba').sheet1

    return(hoja_c)


def formatData(hoja_c):

    pass

if __name__ == '__main__':
    
    hoja_c = leerCredenciales()
    formatData(hoja_c)
