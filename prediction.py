from keras.models import model_from_json
import numpy as np
from keras.preprocessing import image



def prediction(classifier, test_image):
	test_image = image.img_to_array(test_image)
	test_image = test_image.astype('float32')/255
	test_image = np.expand_dims(test_image, axis = 0)
	result = classifier.predict(test_image)
	if result[0][0] >= 0.5:
	    prediction = 'healthy'
	else:
	    prediction = 'cancerous'
	return (prediction)




# load json and create model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")
test_image = image.load_img('Brain/test_set/cancer/cancer89.jpg', target_size = (64, 64))
print (prediction(loaded_model, test_image))