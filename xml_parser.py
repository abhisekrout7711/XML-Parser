import pandas as pd
import xml.etree.ElementTree as et

def parse_xml(xml_path: str, csv_path: str) -> bool:
    """Parse XML and generate a CSV file"""
    
    # Get the root tag
    try:
        tree = et.parse(xml_path)
        root = tree.getroot()
    except Exception as err:
        print(err)
        return False

    # Populate list[dict] with data from CSV
    # Works for xml schema with hierarchy as follows: root>child>grandchild
    rows : list = []
    for child in root:
        row : dict = {}
        for ele in child:
            row[ele.tag] = ele.text
        rows.append(row)

    # Generate csv file
    df = pd.DataFrame(rows)
    df.to_csv(csv_path)
    
    return True

if __name__ == '__main__':
    xml_path: str = "books_xml.xml"
    csv_path: str = 'csv_output.csv'

    if parse_xml(xml_path, csv_path):
        print("CSV file generated")
