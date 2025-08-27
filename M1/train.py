import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier
import joblib
import os

# -----------------------------
# 1. Load dataset
# -----------------------------
INPUT_FILE = "data/M1_data_to_train.csv"

if not os.path.exists(INPUT_FILE):
    raise FileNotFoundError(f"{INPUT_FILE} not found!")

print(f"📄 Loading {INPUT_FILE}...")
df = pd.read_csv(INPUT_FILE)

# Features (already numeric & one-hot encoded) and target
X = df.drop(columns=["DIAGNOSIS"])
y = df["DIAGNOSIS"]

# -----------------------------
# 2. Train/test split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"✅ Training set: {X_train.shape}, Test set: {X_test.shape}")

# -----------------------------
# 3. Train classifiers
# -----------------------------
models = {
    "RandomForest": RandomForestClassifier(
        n_estimators=200, random_state=42, class_weight="balanced"
    ),
    "LogisticRegression": LogisticRegression(
        max_iter=1000, class_weight="balanced", random_state=42
    ),
    "XGBoost": XGBClassifier(
        eval_metric="mlogloss", random_state=42, use_label_encoder=False
    )
}

best_model = None
best_acc = 0
best_model_name = None

for name, model in models.items():
    print(f"\n🔹 Training {name}...")
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"{name} Accuracy: {acc:.4f}")
    print(f"{name} Classification Report:\n", classification_report(y_test, y_pred))

    # Track best model
    if acc > best_acc:
        best_acc = acc
        best_model = model
        best_model_name = name

# -----------------------------
# 4. Save the best model
# -----------------------------
if best_model is not None:
    model_filename = f"{best_model_name}.joblib"
    joblib.dump(best_model, model_filename)
    print(f"\n✅ Best model ({best_model_name}) saved to {model_filename}")
else:
    raise RuntimeError("❌ No model was trained successfully")

# -----------------------------
# 5. Load the model and predict (example)
# -----------------------------
loaded_model = joblib.load(model_filename)
y_new_pred = loaded_model.predict(X_test)

print("\n🔮 Predictions on test set with loaded model:")
print(y_new_pred[:10])
