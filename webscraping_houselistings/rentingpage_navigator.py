def assembleUrl(bedrooms, city, min_price, max_price, radius):
    BASE_URL = 'https://www.zoopla.co.uk/to-rent/property/#-bedrooms/city/?page_size=100&price_frequency=per_month&q=Sheffield%2C%20South%20Yorkshire&results_sort=newest_listings&search_source=refine'

    #***** parameter url codes *****#
    price_max_code = "&price_max=#"
    price_min_code = "&price_min=#"
    radius_code = "&radius=#"
    page_number_code = "&pn=0"

    url = BASE_URL.replace('#', bedrooms).replace('city', city)

    url += price_min_code.replace('#', min_price)
    url += price_max_code.replace('#', max_price)
    url += radius_code.replace('#', radius)
    url += page_number_code

    return url

def getNextPageUrl(url):
    url = list(url) # convert to list to change a single character
    url[-1] = str(int(url[-1]) + 1) # add one to last character of url (page number)

    nextPageUrl = ''.join(url) # convert back to string

    return nextPageUrl

def getAdLinks(bedrooms, city, min_price, max_price, radius):
    from rentingpage_listing_link_scraper import scrape_ad_links
    # iterations collect links from a rental seach on zoopla from
    # page one to the last that has no listing on it

    ad_links = []
    url = assembleUrl(bedrooms, city, min_price, max_price, radius)
    # limit to web scraping 10 pages since each has 100 listings
    for page_number in range(10):
        url = getNextPageUrl(url)

        new_links = scrape_ad_links(url)

        # once no more links ar found we have finished our search
        if(len(new_links) == 0):
            break

        ad_links += new_links

    return ad_links

def request_ad_links():
    import sys
    bedrooms = sys.argv[1]
    city = sys.argv[2]
    min_price = sys.argv[3]
    max_price = sys.argv[4]
    radius = sys.argv[5]

    print(sys.argv)

    links = getAdLinks(bedrooms, city, min_price, max_price, radius)
    #links = getAdLinks('4', 'sheffield', '300', '400', '1')
    return links

if __name__ == "__main__":
    links = request_ad_links()

    from listing_info_scraper import getListingInformationAsJson

    json_string = getListingInformationAsJson(links[0])
    file = open('listing_data.json', 'w')
    file.write(json_string)
