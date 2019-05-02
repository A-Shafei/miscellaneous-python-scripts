#Warning! Experimental code! Not documented! Not production quality!

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from unidecode import unidecode

for page_number in range(1, 36):
	
	my_url = 'http://www.med4d.com/getsearch?clinicName=&docName=&spec1=&level=&state1=%20573%20&city1=&gender1=&phone1=&cert1=&insurance=&page=' + str(page_number)

	uClint = uReq(my_url)
	page_html = uClint.read()
	uClint.close()

	filename = "MeD4D_Clinics.csv"
	#f = open(filename, "w")

	headers = "Name, Services, Phone, Address\n"
	#f.write(headers)

	page_soup = soup(page_html, "html.parser")

	containers = page_soup.findAll("div", {"class":"clinic-entity text-center "})

	for container in containers:
		
		doctor_name = container.h2.text.replace("\n", " ")
		doctor_name = doctor_name.replace(",", " ")
		
		if container.ol == None:
			Services = "مكتبوش خدمات"
		else:
			Services = container.ol.text
		Services = Services.replace(",", " ")
		
		messy_phone = unidecode(container.p.get_text().replace("\n", "@"))
		phone = ""
		for item in messy_phone:
			if item != "@":
				phone = phone + item
			else:
				break
		if phone == "":
			phone = "مكتبوش تليفون"
		phone = phone.replace(",", " ")
		
		address = container.findAll("p")[-2].text.replace("\u0664\u0666 ", "") + " " + container.findAll("p")[-1].text
		address = address.replace("\n", " ").replace(",", " ")

		print(doctor_name)
		#print(Services)
		#print(phone)
		#print(address)

		#f.write(doctor_name + "," + Services + "," + phone + "," + address + "\n")

#f.close()
		
