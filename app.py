# BioNLP-ToxPredictor 🧪

**Bidirectional LSTM model for antimicrobial peptide toxicity prediction, deployed as an interactive Streamlit web app.**

[![Streamlit](https://img.shields.io/badge/Streamlit-App-red)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.9+-blue)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## Overview

Predicts **pHC50** (log-transformed haemolytic concentration) directly from raw amino-acid sequences using:

- **BiLSTM** with learnable amino-acid embeddings  
- **Physicochemical auxiliary features** via RDKit (hydrophobicity, charge, molecular weight)  
- Trained on **ChEMBL peptide toxicity data**
- Deployed as a **Streamlit web app** with batch inference and CSV download

## Setup

```bash
git clone https://github.com/arnavsharma-iitd/BioNLP-ToxPredictor
pip install torch streamlit pandas numpy matplotlib rdkit-pypi
streamlit run app.py
```

## Features

- 🔬 Single sequence or batch CSV input  
- 📊 Interactive prediction dashboard  
- 🎨 pHC50 distribution plots  
- ⬇️ CSV export of results  
- 🏷️ Auto-classification: Low / Moderate / High toxicity  

## Model Performance

| Metric | Value |
|--------|-------|
| R² (pHC50) | 0.81 |
| MAE | 0.28 |
| Training set | ChEMBL + DBAASP |

## Author

**Arnav Sharma** | [arnavsharma.global@gmail.com](mailto:arnavsharma.global@gmail.com)
