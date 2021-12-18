import bs4 as bs
import requests 


def get_data(url):
    header = {
        "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}

    responce = requests.get(url , headers=header)
    soup = bs.BeautifulSoup(responce.content, 'html.parser')
    if responce.status_code == 200:
        title = soup.find('span' , id="productTitle");
        try:
            price = soup.select('.a-offscreen')[0].text
            if (len(price) == 0):
                    price = soup.find(id="price_inside_buybox");
            price = price.replace('₹' , '')
            price = price.replace(',' , '')
        except TypeError():
            pass
        except Exception() as e:
            pass
        if price and title != None:
            title = str(title)
            title = title.replace('<span class="a-size-large product-title-word-break" id="productTitle">' , '')
            title = title.replace('</span>' , '')
            title = title.replace('        ' , '')
            return title , price

            