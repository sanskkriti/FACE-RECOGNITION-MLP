
from google.colab import files
uploaded = files.upload()

# Step 1: Unzip and prepare the dataset
import zipfile
import os
import shutil

zip_path = "Faces.zip"
extract_path = "faces"

# Remove previous extraction if exists
if os.path.exists(extract_path):
    shutil.rmtree(extract_path)

with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)
print("Faces dataset extracted.")

# Handle nested folder case (e.g., faces/Faces)
if os.path.exists("faces/Faces"):
    for item in os.listdir("faces/Faces"):
        shutil.move(os.path.join("faces/Faces", item), "faces")
    shutil.rmtree("faces/Faces")
    print("Fixed nested 'Faces/Faces' directory.")

# Step 2: Import required libraries
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neural_network import MLPClassifier
import numpy as np
import cv2

# Step 3: Define gallery plot function
def plot_gallery(images, titles, h, w, n_row=3, n_col=4):
    plt.figure(figsize=(1.8 * n_col, 2.4 * n_row))
    plt.subplots_adjust(bottom=0, left=.01, right=.99, top=.90, hspace=.35)
    for i in range(min(n_row * n_col, len(images))):
        plt.subplot(n_row, n_col, i + 1)
        plt.imshow(images[i].reshape((h, w)), cmap=plt.cm.gray)
        plt.title(titles[i], size=12)
        plt.xticks(())
        plt.yticks(())

# Step 4: Load images and labels
dir_name = "faces/"
x, y, target_names = [], [], []
person_id = 0
h = w = 300
class_names = []
n_samples = 0

for person_name in os.listdir(dir_name):
    dir_path = os.path.join(dir_name, person_name)
    if not os.path.isdir(dir_path):
        continue
    class_names.append(person_name)
    for image_name in os.listdir(dir_path):
        image_path = os.path.join(dir_path, image_name)
        img = cv2.imread(image_path)
        if img is None:
            continue
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        resized_image = cv2.resize(gray, (h, w))
        v = resized_image.flatten()
        x.append(v)
        y.append(person_id)
        target_names.append(person_name)
        n_samples += 1
    person_id += 1

x = np.array(x)
y = np.array(y)
target_names = np.array(target_names)
n_features = x.shape[1]
n_classes = len(class_names)

print("Loaded data")
print("x shape:", x.shape)
print("y shape:", y.shape)
print("Samples:", n_samples)
print("Classes:", n_classes)

# Step 5: Split the dataset
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)

# Step 6: PCA
n_components = 150
print(f"🔍 Extracting top {n_components} eigenfaces")
pca = PCA(n_components=n_components, svd_solver='randomized', whiten=True).fit(x_train)
eigenfaces = pca.components_.reshape((n_components, h, w))

eigenfaces_titles = [f"eigenface {i}" for i in range(eigenfaces.shape[0])]
plot_gallery(eigenfaces, eigenfaces_titles, h, w)
plt.show()

print("📐 Projecting data into PCA space")
x_train_pca = pca.transform(x_train)
x_test_pca = pca.transform(x_test)

# Step 7: LDA
lda = LinearDiscriminantAnalysis()
lda.fit(x_train_pca, y_train)
x_train_lda = lda.transform(x_train_pca)
x_test_lda = lda.transform(x_test_pca)
print("PCA → LDA completed")

# Step 8: Train MLP Classifier
clf = MLPClassifier(random_state=1, hidden_layer_sizes=(10, 10), max_iter=1000, verbose=True)
clf.fit(x_train_lda, y_train)

print("Model trained. Layer shapes:")
for i, shape in enumerate(clf.coefs_):
    print(f" Layer {i + 1}: {shape.shape}")

# Step 9: Predict
y_pred = []
y_prob = []

for test_face in x_test_lda:
    prob = clf.predict_proba([test_face])[0]
    class_id = np.argmax(prob)
    y_pred.append(class_id)
    y_prob.append(np.max(prob))

y_pred = np.array(y_pred)

# Step 10: Evaluate and visualize results
prediction_titles = []
true_positive = 0

for i in range(y_pred.shape[0]):
    true_name = class_names[y_test[i]]
    pred_name = class_names[y_pred[i]]
    result = f'pred: {pred_name}, pr: {str(y_prob[i])[:4]} \ntrue: {true_name}'
    prediction_titles.append(result)
    if true_name == pred_name:
        true_positive += 1

accuracy = true_positive * 100 / y_pred.shape[0]
print(f"Accuracy: {accuracy:.2f}%")

plot_gallery(x_test, prediction_titles, h, w)
plt.show()
