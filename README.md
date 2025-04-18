# 🔍 Fingerprint Matching with OpenCV

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green?logo=opencv)](https://opencv.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project uses **SIFT (Scale-Invariant Feature Transform)** and **FLANN (Fast Library for Approximate Nearest Neighbors)** from OpenCV to detect and match fingerprints. Given an altered fingerprint, the script compares it against a dataset of real fingerprints and identifies the best match based on keypoint similarity.

---

## 📁 Dataset Structure

Place the fingerprint images in the following directory structure:

```
SOCOFing/
├── Altered/
│   └── Altered-Hard/
│       └── [sample fingerprint].BMP
├── Real/
│   └── [real fingerprint dataset].BMP
```

You can download the [SOCOFing dataset](https://www.kaggle.com/datasets/ruizgara/socofing?resource=download) from Kaggle.

---

## 🚀 How It Works

1. Reads a fingerprint from the `Altered-Hard` folder.
2. Loops through all real fingerprints in the `Real` folder.
3. Detects and computes SIFT keypoints and descriptors.
4. Matches them using FLANN and applies Lowe’s ratio test.
5. Scores each match and selects the best one.
6. Displays a visual comparison of matched features.

---

## 🧪 Requirements

- Python 3.8+
- OpenCV 4.x

Install dependencies:

```bash
pip install opencv-python
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🤝 Acknowledgements

- [OpenCV](https://opencv.org/)
- [SOCOFing Dataset - Kaggle](https://www.kaggle.com/datasets/ruizgara/socofing?resource=download)

