from scipy.misc import imread, imresize


def predict_to_image(photo, emoji_images, prediction, bb):
    if prediction == "Angry":
        img = imresize(imread(emoji_images[0]), bb)
    elif prediction == "Disgust":
        img = imresize(imread(emoji_images[1]), bb)
    elif prediction == "Fear":
        img = imresize(imread(emoji_images[2]), bb)
    elif prediction == "Happy":
        img = imresize(imread(emoji_images[3]), bb)
    elif prediction == "Sad":
        img = imresize(imread(emoji_images[4]), bb)
    elif prediction == "Surprise":
        img = imresize(imread(emoji_images[5]), bb)
    elif prediction == "Neutral":
        img = imresize(imread(emoji_images[6]), bb)

    photo[bb[0]:bb[2], bb[1]:bb[3], :] = img
    return photo