import os
import cv2 as cv
import numpy as np

people = ['Audrey', 'Dani', 'Eimi', 'Johny', 'Maria']
DIR = r'/home/wray/opencv/images/tes'

haar_cascade = cv.CascadeClassifier('haar_face.xml')

features = []
labels = []

def create_train():
    for label, person in enumerate(people):
        path = os.path.join(DIR, person)
        
        if not os.path.exists(path):
            print(f"Directory {path} does not exist. Skipping...")
            continue

        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            
            try:
                img_array = cv.imread(img_path)
                if img_array is None:
                    print(f"Image {img_path} could not be read. Skipping...")
                    continue

                gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
                faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

                for (x, y, w, h) in faces_rect:
                    faces_roi = gray[y:y+h, x:x+w]
                    features.append(faces_roi)
                    labels.append(label)

            except Exception as e:
                print(f"Error processing {img_path}: {e}")

create_train()

# Convert lists to numpy arrays
features = np.array(features, dtype='object')
labels = np.array(labels)

print(f'Length of the features = {len(features)}')
print(f'Length of the labels = {len(labels)}')

# Optional: Save features and labels for later use
np.save('features.npy', features)
np.save('labels.npy', labels)
