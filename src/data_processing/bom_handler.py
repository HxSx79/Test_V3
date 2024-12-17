import pandas as pd

class BOMHandler:
    def __init__(self, bom_file_path):
        """Initialize BOM handler with Excel file path"""
        self.bom_data = pd.read_excel(bom_file_path)
        
    def get_part_info(self, class_name):
        """Get part information from BOM based on detected class name"""
        try:
            part_info = self.bom_data[self.bom_data['Class_Name'] == class_name].iloc[0]
            return {
                'Program': part_info['Program'],
                'Part_Number': part_info['Part_Number'],
                'Part_Description': part_info['Part_Description']
            }
        except (IndexError, KeyError):
            return {
                'Program': 'Unknown',
                'Part_Number': 'Unknown',
                'Part_Description': 'Unknown'
            }