import pandas as pd

def convert_floats_to_ints(filename, column_name):
    # Read the CSV file
    df = pd.read_csv(filename)

    # Check if the column exists in the DataFrame
    if column_name in df.columns:
        # Convert the float numbers to integers
        df[column_name] = df[column_name].apply(lambda x: int(x) if x == x else x)

    # Write the DataFrame back to the CSV file
    df.to_csv(filename, index=False)

# Usage
convert_floats_to_ints('../data/final_data_publish.csv', 'dlr_soft_class')