import requests
from bs4 import BeautifulSoup

baseUrl = 'https://www.darmawisataindonesia.co.id'

page = int(input("Masukan Jumlah Halaman yang ingin di scrape : "))

if page < 1:
    print("Jumlah Halaman tidak boleh kurang dari 1")
    exit()
    
for indexPage in range(1, page + 1):
    # Define the URL of the webpage to scrape
    url = 'https://www.darmawisataindonesia.co.id/Tour/International?keyword=&price=&minimumpax=&duration=&province=&category=&page='+indexPage.__str__()

    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content of the webpage
    soup = BeautifulSoup(response.text, 'html.parser')

    # # Find elements by their HTML tags
    # title = soup.title
    # print("Title of the webpage:", title.text)
    # print("------------------------------------------------------------------------------------------------------------------------\n")

    # Find elements by selecting all class
    crawledDataByClass = soup.find_all(class_='z-panel-list')
    for part in crawledDataByClass:
        # Title
        titlePart = part
        title = titlePart.find(class_='hotel-detail-button')
        print('\nTitle : ', title.text)
        
        # Image URL
        imagePart = part
        image = imagePart.find(class_='img-tour')
        imageLink = image.find('a')
        print('URL Image : ', baseUrl + imageLink.img['src'])
        
        # Tour Promo Data (Place, Date, Price)
        tourPromoDataPart = part
        tourPromoData = tourPromoDataPart.find(class_='z-tour-info')
        detailTitle = ['Place : ', 'Date : ', 'Price : ']
        for index, promoData in enumerate(tourPromoData.find_all('li')):
            print(detailTitle[index], promoData.text)
            
        # Tour Price
        pricePromoPart = part
        pricePromoData = pricePromoPart.find(class_='z-content-price')
        print('Starting Price : ', pricePromoData.text.replace('mulai dari', '').strip())