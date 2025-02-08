import requests
from email.mime.text import MIMEText
import smtplib
from apscheduler.schedulers.blocking import BlockingScheduler
with open(r"C:\Users\Student1\Desktop\BucsaLucian\lab1\lab2\cheie_api.txt") as fisier:
    API_KEY = fisier.read().strip()

URL_API = "https://api.openweathermap.org/data/2.5/weather"
oras = "Bacau"
units = "metric"
request_url = f"{URL_API}?q={oras}&appid={API_KEY}&units={units}"
units = "metric"
def verificare_vreme():
    raspuns = requests.get(request_url)
    data = raspuns.json()
    if raspuns.status_code==200:
        vreme = data['main']['temp']
        starea_vremii = data['weather'][0]['description']
        umiditate = data['main']['humidity']
        return vreme,starea_vremii,umiditate
    else:
        print("EROARE pt request-ul tau!")
        return None

def afisare_vreme():
    vreme,starea_vremii,umiditate = verificare_vreme()
    print(f"Temperatura {vreme}\nUmiditate: {umiditate}\nStare vreme: {starea_vremii}")

vreme,starea_vremii,umiditate = verificare_vreme()
#print(f"Temperatura {vreme}\nUmiditate: {umiditate}\nStare vreme: {starea_vremii}")
continut_fisier = verificare_vreme()
with open("C:\\Users\\Student1\\Desktop\\BucsaLucian\\lab1\\lab2\\raport_vreme.txt","w") as fisier_scriere:
    fisier_scriere.write(f"Temperatura: {vreme}\nUmiditate: {umiditate}\nStare vreme: {starea_vremii}")


with open(r"C:\Users\Student1\Desktop\BucsaLucian\lab1\lab2\parola_google.txt") as fisier:
    parola_google = fisier.read().strip()
email="bucsa.lucian.dumitru@gmail.com"
email_destinatar = "lucimandeas2@gmail.com"
def send_email():
    msg = MIMEText(f"Starea vremii este:\n{vreme}\n{umiditate}\n{starea_vremii}")
    msg['Subject'] = "Starea vremii"
    msg['From'] = email
    msg['To'] = email_destinatar
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as server_smtp:
        server_smtp.login(email,parola_google)
        server_smtp.sendmail(email,email_destinatar,msg.as_string())
    print ("Email-ul a fost trimis cu succes!")      
#send_email()


apelare_interval_de_timp = BlockingScheduler()
#apelare_interval_de_timp.add_job(afisare_vreme,'interval',seconds=10)
apelare_interval_de_timp.add_job(afisare_vreme,'cron',hour=13,minute=38)
apelare_interval_de_timp.start()