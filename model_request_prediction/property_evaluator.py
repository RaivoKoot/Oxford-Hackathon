# very low = 0 point
# low = 1 points
# average = 3 points
# high = 4 points
# very high = 6 points
def getLabelPoints(label):
    if(label == 'very low'):
        return 0
    elif(label == 'low'):
        return 1
    elif(label == 'average'):
        return 3
    elif(label == 'high'):
        return 4
    elif(label == 'very high'):
        return 6
    else:
        print("Error in giving label points: "+str(label))
        return -9999

# gets the rating for a single image
def rateImage(img_url):
    from get_prediction import get_prediction
    result = get_prediction(img_url)
    label = result[0]
    confidence = result[1]

    if(float(confidence) < 0.15):
        return 0

    pred_label = label

    rating = getLabelPoints(pred_label)
    return rating

# iterates through list of images and returns average rating
def getPropertyRating(image_urls):
    property_rating = 0

    # give property bad rating if less than two images
    if(len(image_urls) < 4):
        print("Less than two images")
        return property_rating

    for url in image_urls:
        property_rating += rateImage(url)

    property_rating /= len(image_urls) #average image rating

    return property_rating

# iterates through list of properties and rates them
def rate_properties(property_batch):
    counter = 1
    listings = len(property_batch)
    # iterate through every property to rate it
    for property in property_batch:
        # get properties images
        property_images = property['image_urls']

        # get rating based off of the images
        rating = getPropertyRating(property_images)
        property['rating'] = rating # add attribute rating

        if(counter % 3 == 0):
            percentage = (counter / listings) * 100
            ctypes.windll.user32.MessageBoxW(0, "completed modelling "+str(percentage)+"% of properties", "Running Machine Learning Model", 0)
        counter += 1

# iterates through properties that have been rated
# and returns the n properties with the best rating
def getTopProperties(amount_num, rated_properties):
    top_ratings = [0] * amount_num
    top_properties = [None] * amount_num

    for property in rated_properties:
        rating = property['rating']

        if(rating > min(top_ratings)):
            minposition = top_ratings.index(min(top_ratings))

            # throw out the minimum rated property and put new one in
            top_ratings[minposition] = rating
            top_properties[minposition] = property


    return [top_ratings, top_properties]





import sys
sys.path.append('../webscraping_houselistings')
from rentingpage_navigator import requestBatchOfPropertydata

property_batch = requestBatchOfPropertydata()
import ctypes
ctypes.windll.user32.MessageBoxW(0, "batch of property-data collected", "3/4", 0)
ctypes.windll.user32.MessageBoxW(0, "Model will now analyse, predict and rate properties.\nThis may take a few minutes", "3/4", 0)

rate_properties(property_batch)
top_properties = getTopProperties(10, property_batch)

ctypes.windll.user32.MessageBoxW(0, "Finished! Top Ten Houses found!", "Model Run Complete", 0)
ctypes.windll.user32.MessageBoxW(0, "Go back to the java application and click \'display results\'", "Model Run Complete", 0)

import json
with open('top_houses.json', 'a') as the_file:
    for property in top_properties[1]:
        if(property is None):
            break
        the_file.write(json.dumps(property)+"\n\n")
