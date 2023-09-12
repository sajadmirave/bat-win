# Sample data as a list of items
data = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hank", "Ivy"]

# Define the maximum number of rows per column
max_rows_per_column = 2

# Calculate the number of columns required
num_columns = (len(data) + max_rows_per_column - 1) // max_rows_per_column

# Calculate the maximum item length for proper alignment
max_item_length = max(len(item) for item in data)

# Calculate the width of each column
column_width = max_item_length + 2  # Add padding

# Loop through columns
for column in range(num_columns):
    # Initialize a list for the current column's data
    column_data = []

    # Iterate through the data, collecting items for the current column
    for i in range(column * max_rows_per_column, (column + 1) * max_rows_per_column):
        if i < len(data):
            column_data.append(data[i])

    # Print the current column
    for row in column_data:
        print(row.ljust(column_width), end='  ')
    print()  # Move to the next line for the next column
