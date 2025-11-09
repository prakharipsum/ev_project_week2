# ev_chatbot.py
import joblib
import pandas as pd
import sys

MODEL_PATH = "xgboost_model.pkl"  # change if saved under different name

def load_model(path=MODEL_PATH):
    try:
        pipeline = joblib.load(path)
        print(f"Loaded model pipeline from {path}")
        return pipeline
    except Exception as e:
        print("Failed to load model:", e)
        sys.exit(1)

def get_user_input_for_features(X_sample):
    print("Provide feature values. Press Enter to use dataset median/default.")
    user_values = {}
    for col in X_sample.columns:
        dtype = X_sample[col].dtype
        if str(dtype).startswith('float') or str(dtype).startswith('int'):
            s = input(f"{col} (numeric): ").strip()
            if s == "":
                user_values[col] = X_sample[col].median()
            else:
                try:
                    user_values[col] = float(s)
                except:
                    print("Invalid number, using median.")
                    user_values[col] = X_sample[col].median()
        else:
            s = input(f"{col} (categorical) [press Enter to use mode]: ").strip()
            if s == "":
                user_values[col] = X_sample[col].mode()[0]
            else:
                user_values[col] = s
    return pd.DataFrame([user_values])

def main():
    pipeline = load_model()
    print("EV Assistant Chatbot (type 'exit' anytime to quit)\n")
    while True:
        q = input("You: ").strip().lower()
        if q in ("exit","quit"):
            print("Chatbot: Goodbye!")
            break
        if "predict" in q or "estimate" in q:
            try:
                # need sample X to know columns -> try to load dataset
                try:
                    df = pd.read_csv("electric_vehicles_spec_2025.csv")
                    df.columns = df.columns.str.strip().str.replace(" ", "_").str.replace("/", "_").str.lower()
                    X_sample = df.drop(columns=["range_km","source_url"], errors='ignore')
                except:
                    # fallback: try to infer from pipeline preprocessor when possible
                    X_sample = pd.DataFrame({})  # will cause issues if not available
                    print("Warning: dataset not found; prediction requires dataset column info.")
                user_df = get_user_input_for_features(X_sample)
                pred = pipeline.predict(user_df)[0]
                print(f"Chatbot: Predicted EV range ≈ {pred:.2f} km")
            except Exception as e:
                print("Chatbot: Prediction failed:", e)
            continue
        if "battery" in q:
            print("Chatbot: Battery capacity (kWh) is a major factor determining range.")
            continue
        print("Chatbot: I can predict range if you say 'predict' or explain EV terms like 'battery'.")
        
if __name__ == "__main__":
    main()
