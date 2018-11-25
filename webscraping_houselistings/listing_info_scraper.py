def parseCleanData(images_container, price_container, title_container, address_container):
    image_urls = []
    for container in images_container:
        image_url = container["src"]
        image_urls.append(image_url)

    # parse out just the number
    price = price_container.text.replace('pcm','')
    price = price.replace('£','').replace(',','').strip()

    title = title_container.text.strip()
    address = address_container.text

    data = {"image_urls":image_urls, "price":price, "title":title, "address":address}

    return data

def getContainers(page_soup):
    # get information about property listing
    images_container = page_soup.findAll("img",{"class": "dp-gallery__image"})
    price_container = page_soup.find("p",{"class": "ui-pricing__main-price"})
    title_container = page_soup.find("h1",{"class": "ui-prop-summary__title ui-title-subgroup"})
    address_container = page_soup.find("h2",{"class": "ui-prop-summary__address"})

    return [images_container, price_container, title_container, address_container]

# returns information about one property listings as a JSON
# attributes are title, address, price, image_urls
def getListingInformationAsJson(url_extension):
    BASE_URL = 'https://www.zoopla.co.uk'
    url = BASE_URL + url_extension

    from urllib.request import urlopen as uReq
    from bs4 import BeautifulSoup as soup

    #open connection an grab page
    uClient = uReq(url)

    # load html content
    page_html = uClient.read()
    uClient.close()

    page_soup = soup(page_html, "html.parser")

    # containers holding the information we want
    containers = getContainers(page_soup)

    # the information from the containers
    data = parseCleanData(containers[0],containers[1],containers[2],containers[3],)
    data['listing_link'] = url # add listing url

    import json
    json_string = json.dumps(data)

    return json_string
