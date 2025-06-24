# 🤖 MLP Face Recognition System

A face recognition system using **Multi-Layer Perceptron (MLP)** neural networks, integrated with **PCA** and **LDA** for dimensionality reduction. The model is trained to identify Bollywood celebrities with competitive accuracy and visualizes important training insights.

---

## 📌 Project Overview

This project demonstrates a full pipeline of a **face recognition system**:
- Face detection using OpenCV
- Dimensionality reduction using **Principal Component Analysis (PCA)** and **Linear Discriminant Analysis (LDA)**
- Classification using an **MLP Neural Network**
- Visualization of eigenfaces and prediction confidence

---

## 🚀 Key Features

✅ Face recognition via MLP classifier  
✅ Dimensionality reduction with PCA + LDA  
✅ Works on real celebrity images  
✅ Accuracy evaluation + loss visualization  
✅ Probability scores for predictions  
✅ Eigenface visualizations  

---

## 🛠️ Tech Stack

- **Python**  
- **Jupyter Notebook**
- **Libraries:**
  - `scikit-learn` (MLPClassifier, PCA, LDA)
  - `OpenCV` (cv2)
  - `NumPy`
  - `Matplotlib`

---

## 🧠 Model Architecture

- **Input:** 150 PCA components  
- **MLP Structure:**
  - Hidden Layers: (10, 10)
  - Output: Number of classes (based on celebrities)
- **Training:**
  - Max Iterations: 1000
  - Early Stopping when loss change < 0.0001

---

## 📂 Dataset Structure

faces/
├── Aamir/
├── Ajay/
├── Akshay/
├── Alia/
├── Amitabh/
├── Deepika/
├── Disha/
├── Farhan/
└── Ileana/

Each folder contains face images of the respective celebrity.

---

## 📈 Results

- **Accuracy:** ~77.88%  
- **Loss:** Converged smoothly  
- **Confidence Scores:** Displayed alongside predictions  
- **Visuals:** Eigenfaces and training loss curves


Author
Sanskriti Jha


