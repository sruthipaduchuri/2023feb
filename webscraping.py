import requests
import pandas as p
from bs4 import BeautifulSoup

responce=requests.get("https://www.flipkart.com/cameras/dslr-mirrorless/pr?sid=jek%2Cp31%2Ctrv&p%5B%5D=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&p%5B%5D=facets.type%255B%255D%3DMirrorless&param=179&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InZhbHVlQ2FsbG91dCI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ2YWx1ZUNhbGxvdXQiLCJpbmZlcmVuY2VUeXBlIjoiVkFMVUVfQ0FMTE9VVCIsInZhbHVlcyI6WyJTaG9wIE5vdyEiXSwidmFsdWVUeXBlIjoiTVVMVElfVkFMVUVEIn19LCJ0aXRsZSI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ0aXRsZSIsImluZmVyZW5jZVR5cGUiOiJUSVRMRSIsInZhbHVlcyI6WyJUb3AgTWlycm9ybGVzcyBDYW1lcmFzIl0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fSwiaGVyb1BpZCI6eyJzaW5nbGVWYWx1ZUF0dHJpYnV0ZSI6eyJrZXkiOiJoZXJvUGlkIiwiaW5mZXJlbmNlVHlwZSI6IlBJRCIsInZhbHVlIjoiRExMRzJYRENGQlhWVVpUSCIsInZhbHVlVHlwZSI6IlNJTkdMRV9WQUxVRUQifX19fX0%3D&fm=neo%2Fmerchandising&iid=M_54242ffc-eac4-47bc-9983-405155c8e28d_3.Q5LU1U8PHMK6&ssid=5rmtwe674g0000001676424114735&otracker=hp_omu_Best%2Bof%2BElectronics_1_3.dealCard.OMU_Q5LU1U8PHMK6_3&otracker1=hp_omu_PINNED_neo%2Fmerchandising_Best%2Bof%2BElectronics_NA_dealCard_cc_1_NA_view-all_3&cid=Q5LU1U8PHMK6")
soup=BeautifulSoup(responce.content,"html.parser")
names=soup.find_all('div',class_="_4rR01T")
name=[]
for i in names[0:10]:
    d=i.get_text()
    name.append(d)
  
prices=soup.find_all('div',class_="_30jeq3 _1_WHN1")
price=[]
for i in prices[0:10]:
    d=i.get_text()
    price.append(d)

rates=soup.find_all('div',class_="_3LWZlK")
rate=[]
for i in rates[0:10]:
    d=i.get_text()
    rate.append(d)
  
images=soup.find_all('img', class_="_396cs4")
image=[]
for i in images[0:10]:
    d=i['src']
    image.append(d)
   
df=p.DataFrame()
df['camera_Names']=name
df['camera-Prices']=price
df['camera_Rates']=rate
df['camera_Images']=image
df.to_csv("cameras_data.csv")