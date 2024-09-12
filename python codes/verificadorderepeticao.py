import csv

def find_repeated_lines(file_path, column_index):
    with open(file_path, 'r') as file, open(f'{file_path}_sem repetidos.csv', 'w') as file_no_repet:
        reader = csv.reader(file)
        repeated_lines = []
        seen_values = set()
        for line_number, row in enumerate(reader, start=1):
            value = row[column_index]
            if value in seen_values:
                repeated_lines.append(line_number)
            else:
                seen_values.add(value)
                file_no_repet.write(f"{','.join(row)}\n")


# Usage example
file_path = 'dados_casan/processado/juntos_ostras.csv'
column_index = 1  # Index of the column to check (0-based)

repeated_lines = find_repeated_lines(file_path, column_index)
print(f"Lines with repeated values in column {column_index}: {repeated_lines}")