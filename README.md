# ADNI Research Repository

This repository serves as the central hub for Cerevia AI's research on Alzheimer's Disease (AD) using data from the [Alzheimer's Disease Neuroimaging Initiative (ADNI)](https://adni.loni.usc.edu/). It contains a series of modular machine learning models focused on **cognitive classification**, **risk assessment**, and **progression prediction**.

Our goal is to develop transparent, clinically relevant AI tools to support early detection and longitudinal monitoring of cognitive decline.

---

## 📁 Project Structure

This repository organizes three core research modules:

| Module | Purpose | Repository |
|-------|--------|-----------|
| **M1: AD Classification** | Classifies cognitive status (Cognitively Normal, Mild Cognitive Impairment, Alzheimer's Disease) using clinical, cognitive, and biomarker data. | [github.com/cerevia-ai/ADNI-M1](https://github.com/cerevia-ai/ADNI-M1) |
| **M2: Cognitive Prediction** | Predicts future cognitive scores (e.g., MMSE, ADAS13) based on baseline and longitudinal data. | [github.com/cerevia-ai/ADNI-M2](https://github.com/cerevia-ai/ADNI-M2) |
| **M3: Progression Prediction** | Models the likelihood and trajectory of progression from CN → MCI → AD using time-series analysis and survival modeling. | [github.com/cerevia-ai/ADNI-M3](https://github.com/cerevia-ai/ADNI-M3) |

> 🔍 Each module is a standalone repository with its own code, models, and documentation.

---

## 🧪 Key Features
- **Evidence-Based**: Built using ADNI data and aligned with clinical research standards.
- **Interpretable AI**: Uses SHAP and other methods to explain model predictions (e.g., "Why was this patient classified as MCI?").
- **Longitudinal Modeling**: M2 and M3 leverage repeated measures to forecast cognitive trajectories.
- **Research-Grade**: For **Research Use Only (RUO)** — not for clinical diagnosis.

---

## 🚀 Getting Started

Each module has its own `README` and setup instructions. Start by exploring the individual repositories:

1. Clone a module:
   ```bash
   git clone https://github.com/cerevia-ai/ADNI-M1.git
   ```
