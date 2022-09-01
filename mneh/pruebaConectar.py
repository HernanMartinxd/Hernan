import gspread
import time
from oauth2client import service_account
from gspread_formatting import *
from ClassUsuario import Usuario
from ClassListaUsuarios import ListaUsuarios

def leerCredenciales():
    scp = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    creds = service_account.ServiceAccountCredentials.from_json_keyfile_name('C:/Users/herna/Documents/mneh/Hernan/mneh/credentials.json', scp)
    client = gspread.authorize(creds)
    hoja_c = client.open('prueba').sheet1

    return(hoja_c)

def validarCeldas(hoja_c,obj):
    # >> Gestion de Coordenadas
    with open('cds.txt','r') as file:
        linea = file.readline()
        print(linea)
        coord = linea
    
    
    nums = coord.split(':')
    fila_P = nums[0]
    fila_P = fila_P.split('B')
    num_F = int(fila_P[1])
    band = False
    cds = 'B' + str(num_F + 1)
    i = 1
    while(get_effective_format(hoja_c,cds)).backgroundColor != Color(0.5764706,0.76862746,0.49019608) and not band:
        # >>Se concatenan las coordenadas

        num_F += 1
        new_cds = 'B'+str(num_F)+':'+'H'+str(num_F)
        aux = hoja_c.get(new_cds)
        if(len(aux) != 0):
            # >>Carga una lista auxiliar con los datos de los alumos

            list = []
            for dat in aux[0]:
                list.append(dat)
            
            print('Cagado {} usuarios'.format(i))
            i+=1
            time.sleep(0.6)
            usr = Usuario(list[0],list[1],list[2],list[3],list[4],list[6]) # >>Crea Instancia de clase Usuario
            obj.AgregarUser(usr)    # >>Almacena la instancia creada en una clase manejadora

            list.clear()
            aux.clear()

            cdn = new_cds.replace('B', 'A')
            fullCoordenates = cdn.replace('H', 'L')
            formatoCelda = cellFormat(backgroundColor = Color(0.5764706,0.76862746,0.49019608))
            format_cell_range(hoja_c,fullCoordenates,formatoCelda)
            cds = 'B' + str(num_F + 1)

        else:
            print('Good Bye!')
            band = True
            # >> Guarda la ultima coordenada en un archivo .txt
            cds = 'B'+str(num_F)+':'+'L'+str(num_F)
            guardarArchAux(cds)

def guardarArchAux(cds):
    with open('cds.txt','w+') as file:
        file.write(cds)
    file.close()

def ArreglarDatosUsuario(obj):
    obj.probarMetodo1()
    obj.probarMetodo2()
    obj.probarMetodo3()
    obj.probarMetodo4()
    obj.probarMetodo6()
    
if __name__ == '__main__':
    obj = ListaUsuarios()
    hoja_c = leerCredenciales()
    validarCeldas(hoja_c,obj)
    ArreglarDatosUsuario(obj)