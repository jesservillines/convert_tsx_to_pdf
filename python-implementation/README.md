# Python PDF Generator Implementation

This directory contains the Python implementation of the Tax Credit Documentation PDF generator.

## Features

- Generates a complete tax credit documentation PDF
- Includes cover sheet, invoices, and bank statements
- Uses FPDF2 for PDF generation
- Clean, maintainable code structure

## Installation

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Simply run the main script:
```bash
python main.py
```

This will generate a file named `tax_credit_documentation.pdf` in the current directory.

## Customization

To modify the content:

1. Edit the items and amounts in the `main()` function
2. Modify the formatting in the respective creation functions
3. Adjust page layouts by modifying the PDF class methods

## Structure

- `main.py`: Contains all the PDF generation logic
- `requirements.txt`: Lists all required Python packages

## Dependencies

- fpdf2: PDF generation
- reportlab: Additional PDF functionality if needed
- Pillow: Image handling
- WeasyPrint: Alternative HTML-to-PDF conversion