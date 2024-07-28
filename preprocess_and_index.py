import pandas as pd
from database_setup import main as fetch_data

def preprocess_data(documents):
    df = pd.DataFrame(documents)
    # Example: Remove unwanted columns or perform other preprocessing tasks
    return df

def save_preprocessed_data(df, output_file='preprocessed_data.csv'):
    df.to_csv(output_file, index=False)

def main():
    documents = fetch_data()
    preprocessed_df = preprocess_data(documents)
    save_preprocessed_data(preprocessed_df)

if __name__ == "__main__":
    main()  
