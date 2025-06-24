# 🧠 Face Recognition using PCA + LDA + MLP

A machine learning pipeline for facial recognition using a custom dataset of Indian celebrities. The model combines dimensionality reduction (PCA + LDA) with a Multi-Layer Perceptron (MLP) classifier.

---

## 📂 Dataset

- The dataset is in the `faces/` folder (zipped as `Faces.zip`).
- Structure:
  ```
  faces/
  ├── Aamir/
  ├── Alia/
  ├── Amitabh/
  ├── Deepika/
  └── ...
  ```
- Each subfolder contains grayscale face images of that person.

---

## 📊 Pipeline Overview

| Step | Method |
|------|--------|
| 📥 Data Preprocessing | Grayscale conversion, resizing (300x300) |
| 📉 Dimensionality Reduction | PCA → LDA |
| 🤖 Classifier | MLP (3 layers: 10-10-9) |
| 📈 Evaluation | Accuracy + Sample Predictions |

---

## 🧪 Results

- Achieved **~54% accuracy** on unseen test data.
- Sample visualization of eigenfaces and predictions using `matplotlib`.

---

## 🛠️ How to Run

1. Install dependencies:
    ```bash
    pip install opencv-python scikit-learn matplotlib
    ```

2. Unzip the dataset:
    ```bash
    unzip Faces.zip
    ```

3. Run the Python file:
    ```bash
    python face_recognition.py
    ```
---

## 🤝 Credits

- Created by [Sanskriti Jha](https://github.com/sanskkriti)
- Dataset: Curated manually from celebrity images

---

## 📌 Note

- Accuracy depends heavily on image quality, lighting, and dataset size.
- You can extend the model with CNNs or use transfer learning (e.g., with VGGFace) for better performance.

---
