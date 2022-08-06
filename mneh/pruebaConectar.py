import gspread
from oauth2client import service_account
from gspread_formatting import *
from usuario import Usuario

def leerCredenciales():
    scp = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    creds = service_account.ServiceAccountCredentials.from_json_keyfile_name('C:/Users/herna/Documents/mneh/Hernan/mneh/credentials.json', scp)
    client = gspread.authorize(creds)

    hoja_c = client.open('prueba').sheet1

    return(hoja_c)

def validarCeldas(hoja_c):
    #Gestion de Coordenadas
    coord = 'B11:H11'
    nums = coord.split(':')
    fila_P = nums[0]
    fila_P = fila_P.split('B')
    num_F = int(fila_P[1])
    
    #Sector de Mierda/Pruebas
    '''
    if(get_effective_format(hoja_c,'A'+num_F).backgroundColor == Color(0.5764706,0.76862746,0.49019608)): #Funciona
        print('nachi')
    '''

    #print(get_effective_format(hoja_c, 'A11'))
    '''
    if(hoja_c.acell('A53').value == None):
        print('nachi')
    '''
    band = False
    cds = 'B' + str(num_F + 1)
    while(get_effective_format(hoja_c,cds)).backgroundColor != Color(0.5764706,0.76862746,0.49019608) and not band:
        
        if(hoja_c.acell(cds).value != None):
            print(len(hoja_c.acell(cds).value))
            #Se concatenan las coordenadas
            new_cds = 'B'+str(num_F)+':'+'H'+str(num_F)
            print(new_cds)
            #print(hoja_c.get(new_cds))
            num_F += 1
            list = hoja_c.get(new_cds)
            print(list)
            #Usuario(list[0],list[1],list[2],list[3],list[4],list[6])
            list.clear()

        else:
            print('deberia haber salido')
            band = True


if __name__ == '__main__':
    hoja_c = leerCredenciales()
    validarCeldas(hoja_c)
    
