# data_loading.py
import pandas as pd

def load_data(file_path):
    """
    Loads data from a CSV file into a pandas DataFrame.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        pandas.DataFrame: The loaded DataFrame, or None if there's an error.
    """
    try:
      df = pd.read_csv(file_path)
      return df
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None

def convert_timestamp(df, timestamp_column='Timestamp'):
    """
    Converts the 'Timestamp' column to pandas datetime objects.

    Args:
        df (pandas.DataFrame): The input DataFrame.
        timestamp_column (str, optional): The name of the timestamp column.
            Defaults to 'Timestamp'.

    Returns:
        pandas.DataFrame: The DataFrame with the converted Timestamp column.
    """
    try:
        df[timestamp_column] = pd.to_datetime(df[timestamp_column])
        return df
    except KeyError:
      print(f"Error: Column '{timestamp_column}' not found")
      return None
    except Exception as e:
      print(f"An error occured while converting the timestamps: {e}")
      return None


def set_dataframe_index(df, index_column='Timestamp'):
    """
    Sets the DataFrame index to a specified column.

    Args:
        df (pandas.DataFrame): The input DataFrame.
        index_column (str, optional): The column to use as the index.
            Defaults to 'Timestamp'.

    Returns:
        pandas.DataFrame: The DataFrame with the new index, or None if error.
    """
    try:
      df = df.set_index(index_column)
      return df
    except KeyError:
        print(f"Error: Column '{index_column}' not found")
        return None
    except Exception as e:
        print(f"An error occurred while setting index: {e}")
        return None

if __name__ == '__main__':
    # Example usage:
    test_file = 'test_data.csv'
    #Create some test data, and save it into a CSV file.
    data = {'Timestamp': ['2023-01-01 00:00:00', '2023-01-01 00:00:01', '2023-01-01 00:00:02'],
            'ID': [1, 1, 2],
            'Sensor Reading': [1.1, 2.2, 3.3]
           }
    test_df = pd.DataFrame(data)
    test_df.to_csv(test_file, index=False)

    loaded_df = load_data(test_file)
    if loaded_df is not None:
        print("Data loaded successfully:\n", loaded_df)
        converted_df = convert_timestamp(loaded_df)
        if converted_df is not None:
             print("Timestamp converted successfully:\n", converted_df)
             indexed_df = set_dataframe_index(converted_df)
             if indexed_df is not None:
                 print("Index set successfully:\n", indexed_df)
             else:
               print("There was a problem setting the index")
        else:
           print("There was a problem converting timestamps")
    else:
        print("There was a problem loading the data")
