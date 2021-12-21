import bs4 as bs
import requests 


def get_data(url , state=False):
    try:
        print("Find App .py")
        header = {
            "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}

        responce = requests.get(url , headers=header)
        soup = bs.BeautifulSoup(responce.content, 'html.parser')
        if responce.status_code == 200:
            title = soup.find('span' , id="productTitle");
            short_desc = soup.find(id="productOverview_feature_div");
            try:
                review = soup.select('#acrPopover > span.a-declarative > a > i.a-icon.a-icon-star')[0].text;
                print(review)
            except Exception:
                review = "Unable to fetch"
                pass
            try:
                img = soup.find(id="landingImage")['src'];

            except :
                img = "unable to fetch"
                print(img)
                pass
            try:
                about = soup.find(id="feature-bullets");
            except Exception():
                about = "Unable to fetch"
                pass
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
                if (state == False):
                    about = str(about.get_text().strip())
                    short_desc = str(short_desc.get_text().strip())
                about = str(about)
                short_desc = str(short_desc)
                about = about.replace('\n' , '')
                return str(title) , str(price) , str(review) , str(img) , str(about) , str(short_desc)    
    except Exception as e:
            print("Error=>"+str(e))
            pass