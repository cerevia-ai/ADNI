# setup.py
from setuptools import setup, find_packages

setup(
    name="adni_clf",
    version="0.1.0",
    description="ADNI Cognitive Classifier with SHAP Explainability",
    packages=find_packages(),  # This will include 'interpretability'
    python_requires=">=3.8",
    install_requires=[
        "shap",
        "pandas",
        "numpy",
        "scikit-learn",
        "matplotlib",
        "pytest",
    ],
)