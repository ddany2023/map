import requests
from bs4 import BeautifulSoup
from money_parser import price_str
################
from email.mime.text import MIMEText
import smtplib
################

#myaccount.google.com/apppasswords
with open(r"C:\Users\Student1\Desktop\BucsaLucian\lab1\lab2\parola_google.txt") as fisier:
    parola_google = fisier.read().strip()
email="bucsa.lucian.dumitru@gmail.com"
email_destinatar = "lucimandeas2@gmail.com"
def send_email():
    msg = MIMEText(f"Pretul produsului a scazut\n{pret_produs()}\n{nume_produs()}\n{rating_produs()}")
    msg['Subject'] = "Modificare de pret!"
    msg['From'] = email
    msg['To'] = email_destinatar
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as server_smtp:
        server_smtp.login(email,parola_google)
        server_smtp.sendmail(email,email_destinatar,msg.as_string())
    print ("Email-ul a fost trimis cu succes!")    

url = "https://www.emag.ro/telefon-mobil-samsung-galaxy-s24-ultra-dual-sim-12gb-ram-512gb-5g-titanium-black-sm-s928bzkheue/pd/DF6L7KYBM/"
raspuns = requests.get(url)
raspuns2 = BeautifulSoup(raspuns.text, 'html.parser')
def afisare_continut_pagina():
    print (raspuns)                       #returneaza codul de eroare
    print (raspuns2.prettify())           #returneaza tot codul nostru

def pret_produs():
    pret = raspuns2.find('p',attrs={'class':'product-new-price'}).text
    pret = pret[0:8]
    pret = pret.replace(".","")
    pret = pret.replace(",",".")
    return pret

def pret_produs_v2():
    pret = raspuns2.find('p',attrs={'class':'product-new-price'}).text
    pret = price_str(pret)
    pret = float(pret)
    return pret

def nume_produs():
    nume = raspuns2.find('h1',attrs={'class':'page-title'}).text.strip()
    return nume

def rating_produs():
    rating = raspuns2.find('p',attrs={'class':'review-rating-data'}).text.strip()
    return rating

def verificare():
    pret_referinta = 5300
    pret = pret_produs_v2()
    nume = nume_produs()
    rating = rating_produs()
    if pret < pret_referinta:
        print("Pretul a scazut!")
        send_email()
    else:
        print("Pretul nu a scazut!")
        
verificare()

#v1
#print(pret_produs_v2())

#print(nume_produs())
#print(f"{pret_produs()}\n{nume_produs()}"rating_produs())
#print(rating_produs)
#print(parola_google)


#v2
#pret = pret_produs()
#print(pret)

#afisare_continut_pagina()