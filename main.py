
def Persons_emotion():
    from EmoPy.src.fermodel import FERModel
    #way_photo = 'image_data/sample_happy_image.png'
    way_photo = '/home/mariya/Загрузки/1.jpg'
    target_emotions = ['anger', 'calm', 'happiness']
    model = FERModel(target_emotions, verbose=False)
    print('Predicting on image...')
    model.predict(way_photo)
    return model.emotion
