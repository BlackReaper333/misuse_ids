import pandas as pd

label_path = 'final_processed_labels.csv'

# List of file paths
data_paths = [
    'Data/Active_Wiretap_data.csv',  #5
    'Data/Fuzzing_data.csv', #2
    'Data/mitm_data.csv', #1
    'Data/SSDP_Flood_data.csv', #4
    'Data/SSL_Renegotiation_data.csv' #3
]

nRecords = 5000

start_row = 0

chunk_size = nRecords*2

output = 'final_training_data.csv'

final_dataframe = pd.DataFrame()

for index, path in enumerate(data_paths):
    selected_rows = pd.DataFrame()

    # Define column names for the first CSV file
    csv1_columns = ['index', 'attack']

    # Read the first CSV file with the specified column names
    csv1 = pd.read_csv(label_path, skiprows=range(1, start_row), nrows=chunk_size, header=None, names=csv1_columns)

        # Define column names for the second CSV file
        #csv2_columns = ['index']

    # Read the second CSV file with the specified column names
    csv2 = pd.read_csv(path,  header=None)

    # Select rows from the second CSV file based on the index values from the first CSV file
    selected_rows = csv2.loc[csv1.index]

    # Add the second column from the first CSV file to the selected rows
    selected_rows['attack'] = csv1['attack']

    final_dataframe = pd.concat([final_dataframe, selected_rows])

    start_row += chunk_size

# Store the entire combined dataset in a new CSV file
final_dataframe.to_csv(output, index=False)
