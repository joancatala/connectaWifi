#inici
import os

def confirma():
  confirmacio = raw_input ('Vols encendre el Wifi ara? [Si/No]: ')
  if confirmacio == 'Si':
      os.system('cp /etc/hostname.iwm0-' + str(opcio) + ' /etc/hostname.iwm0')
      os.system('sh /etc/netstart iwm0')
      print(chr(27)+"[1;32m"+"Ja tens xarxa")
      print(chr(27)+"[1;37m"+"\n")

os.system('clear')
print(chr(27)+"[1;33m"+"=================================================================")
os.system('figlet connectaWifi')
print(chr(27)+"[1;33m"+"=================================================================")

print(chr(27)+"[1;37m"+"[1] Casa Benicassim")
print ('[2] Casa Paiporta')
print ('[3] Wifi SEPAM')
print ('[4] Casa pares de Gemma')
print ('[5] Smartphone Xiaomi Max 2')

opcio = raw_input ('Seleciona la teua opcio: ')

if opcio == '1':
    confirma()

elif opcio == '2':
    confirma()    

elif opcio == '3':
    confirma()    

elif opcio == '4':
    confirma()        

elif opcio == '5':
    confirma()
        
else:
    print(chr(27)+"[1;31m"+"No has triat cap opcio del menu.\n")
    print(chr(27)+"[1;37m"+"\n ")

