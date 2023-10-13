import pandas as pd

# List of file paths
file_paths = [
    'Labels/Active_wiretap_labels.csv',  #5
    'Labels/Fuzzing_labels.csv', #2
    'Labels/mitm_labels.csv', #1
    'Labels/SSDP_Flood_labels.csv', #4
    'Labels/SSL_Renegotiation_labels.csv' #3
]

nRecords = 5000

# Create an empty DataFrame to store the selected data
final_dataframe = pd.DataFrame()

for index, path in enumerate(file_paths):
    selected_data = pd.DataFrame()
    # Read each CSV file without column names
    df = pd.read_csv(path, header=None)
    # Select 5000 rows where the value of the second column (index 1) is 0
    df_where_0 = df[df[1] == 0].head(nRecords)

    # Select 5000 rows where the value of the second column (index 1) is 1
    df_where_1 = df[df[1] == 1].head(nRecords)
    print("Index")
    print(index)
    print(df_where_1.head)

    # Combine the two DataFrames
    selected_data = pd.concat([selected_data, df_where_0, df_where_1])

    if index == 0:
        selected_data[1] = selected_data[1].replace(1, 5)
    if index == 1:
        selected_data[1] = selected_data[1].replace(1, 2)
    if index == 2:
        selected_data[1] = selected_data[1].replace(1, 1)
    if index == 3:
        selected_data[1] = selected_data[1].replace(1, 4)
    if index == 4:
        selected_data[1] = selected_data[1].replace(1, 3)

    final_dataframe = pd.concat([final_dataframe, selected_data])

# Export the selected data to a new CSV file
final_dataframe.to_csv('final_processed_labels.csv', index=False, header=False)
