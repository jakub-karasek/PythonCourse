import json
import argparse
from functools import reduce


# Function to read data from a JSON file
def read_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)  # Load the JSON data
    return data

def process_markdown_cells(data):
    string = map(lambda s: "# " + s if s != "\n" else "", data)
    string = list(filter(None, string))
    return string

# Function to extract cell type and source from cells
def process_cells(cells, file_path):
    with open(file_path, 'w', encoding='utf-8') as file_output:
        cw_amount = 0

        for cell in cells:
            cell_type = cell.get('cell_type')
            source = cell.get('source')
            if isinstance(source, list):
                if cell_type == 'markdown':
                    print("\n\n#%%\n", file=file_output, end="")
                    print('\n'.join(process_markdown_cells(source)), file=file_output, end="", sep="")
                    cw_amount += reduce(lambda x, y: x + ("# Ćwiczenie" in y), source, 0)
                else:
                    print("\n\n", file=file_output, end="")
                    for line in source:
                        print(line, file=file_output, end="")

    print("Liczba ćwiczeń: ", cw_amount)

# Main function to handle argument parsing and processing
def main():
    parser = argparse.ArgumentParser(description='Read a JSON file and extract cell information.')
    parser.add_argument('file_path', type=str, help='Path to the JSON file')
    args = parser.parse_args()

    json_data = read_json_file(args.file_path)
    cells = json_data.get('cells', [])
    process_cells(cells, args.file_path.replace('.ipynb', '.py'))

if __name__ == '__main__':
    main()  # Run the main function
