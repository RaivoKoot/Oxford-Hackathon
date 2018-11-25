from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient

ENDPOINT = "https://southcentralus.api.cognitive.microsoft.com"
project_id = '40412ce6-fe45-4fc2-b949-9bb6fe28abf2'
predictor = CustomVisionPredictionClient('57c2350f261b4cf0aec943bcf893e2d8', endpoint=ENDPOINT)

import sys
#img_url = sys.argv[1]
img_url = 'https://images.pexels.com/photos/259962/pexels-photo-259962.jpeg?auto=compress&cs=tinysrgb&h=350'

results =  predictor.predict_image_url(project_id, url=img_url)

output_file_probabilities = open('prediction_result_probabilites.txt', 'w')
output_file_labels = open('prediction_result_labels.txt', 'w')

for prediction in results.predictions:
    probability = "{0:.2f} ".format(prediction.probability)
    label = prediction.tag_name

    output_file_probabilities.write(probability+'\n')
    output_file_labels.write(label+"\n")
