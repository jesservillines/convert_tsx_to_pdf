from fpdf import FPDF
from datetime import datetime

class TaxCreditPDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Tax Credit Documentation', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def create_cover_sheet(pdf):
    # Header Information
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, 'DELIVERY FEE TAX CREDIT - COVER SHEET', 0, 1, 'C')
    pdf.ln(10)

    # Business Information
    pdf.set_font('Arial', '', 12)
    pdf.cell(0, 10, f"Business Name: Tom's Grocery Store", 0, 1)
    pdf.cell(0, 10, f'Consortium Member Number: 12345', 0, 1)
    pdf.cell(0, 10, f'Date Range: 01/01/2024 - 01/31/2024', 0, 1)
    pdf.ln(10)

    # Create Table
    col_widths = [50, 30, 30, 25, 30, 30]
    headers = ['Invoice # and Supplier', 'Total Value', 'Eligible Products', '% Eligible', 'Delivery Fees', 'Eligible Fees']
    
    # Headers
    pdf.set_font('Arial', 'B', 10)
    for i, header in enumerate(headers):
        pdf.cell(col_widths[i], 10, header, 1)
    pdf.ln()

    # Data
    pdf.set_font('Arial', '', 10)
    rows = [
        ['INV-2024-001\nFresh Foods', '$12,100.00', '$12,000.00', '99.2%', '$500.00', '$495.83'],
        ['NC-245813\nNatural Choice', '$8,200.00', '$8,000.00', '97.6%', '$400.00', '$390.24']
    ]

    for row in rows:
        for i, item in enumerate(row):
            pdf.cell(col_widths[i], 10, item, 1)
        pdf.ln()

    pdf.ln(10)
    pdf.cell(0, 10, f'Total Eligible Delivery Fees Requested: $886.07', 0, 1, 'R')

def create_invoice(pdf, invoice_num, date, company_name, items, delivery_fee):
    pdf.add_page()
    
    # Invoice Header
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, company_name, 0, 1, 'L')
    pdf.set_font('Arial', '', 12)
    pdf.cell(0, 10, f'Invoice #: {invoice_num}', 0, 1, 'R')
    pdf.cell(0, 10, f'Date: {date}', 0, 1, 'R')
    
    # Bill To Section
    pdf.ln(10)
    pdf.cell(0, 10, 'Bill To:', 0, 1)
    pdf.cell(0, 10, "Tom's Grocery Store", 0, 1)
    pdf.cell(0, 10, '456 Main Street', 0, 1)
    pdf.cell(0, 10, 'Anytown, ST 12345', 0, 1)
    
    # Items Table
    pdf.ln(10)
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(100, 10, 'Description', 1)
    pdf.cell(90, 10, 'Amount', 1)
    pdf.ln()
    
    # Items
    pdf.set_font('Arial', '', 12)
    total = 0
    for item, amount in items:
        pdf.cell(100, 10, item, 1)
        pdf.cell(90, 10, f'${amount:,.2f}', 1)
        pdf.ln()
        total += amount

    # Totals
    pdf.cell(100, 10, 'Subtotal', 1)
    pdf.cell(90, 10, f'${total:,.2f}', 1)
    pdf.ln()
    pdf.cell(100, 10, 'Delivery Fee', 1)
    pdf.cell(90, 10, f'${delivery_fee:,.2f}', 1)
    pdf.ln()
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(100, 10, 'Total', 1)
    pdf.cell(90, 10, f'${total + delivery_fee:,.2f}', 1)

def create_bank_statement(pdf, date, transaction_date, amount, description):
    pdf.add_page()
    
    # Bank Statement Header
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, 'First National Bank', 0, 1, 'L')
    pdf.set_font('Arial', '', 12)
    pdf.cell(0, 10, f'Statement Date: {date}', 0, 1, 'R')
    pdf.cell(0, 10, "Account: Tom's Grocery Store", 0, 1, 'R')
    pdf.cell(0, 10, 'Account #: ****1234', 0, 1, 'R')
    
    # Transactions Table
    pdf.ln(10)
    pdf.set_font('Arial', 'B', 12)
    headers = ['Date', 'Description', 'Amount']
    col_widths = [50, 90, 50]
    
    for i, header in enumerate(headers):
        pdf.cell(col_widths[i], 10, header, 1)
    pdf.ln()
    
    # Transaction
    pdf.set_font('Arial', '', 12)
    pdf.cell(col_widths[0], 10, transaction_date, 1)
    pdf.cell(col_widths[1], 10, description, 1)
    pdf.cell(col_widths[2], 10, f'${amount:,.2f}', 1)

def main():
    # Initialize PDF
    pdf = TaxCreditPDF()
    
    # Create Cover Sheet
    create_cover_sheet(pdf)
    
    # Create First Invoice
    items1 = [
        ('Fresh Apples (40 lbs)', 2000.00),
        ('Whole Grain Bread (200 loaves)', 3000.00),
        ('Fresh Eggs (100 dozen)', 5000.00),
        ('1% Milk (200 gallons)', 2000.00),
        ('Tobacco Products', 100.00)
    ]
    create_invoice(pdf, 'INV-2024-001', '01/15/2024', 'Fresh Foods Distributors', items1, 500.00)
    
    # Create First Bank Statement
    create_bank_statement(pdf, '01/31/2024', '01/15/2024', 12600.00, 'Fresh Foods Distributors')
    
    # Create Second Invoice
    items2 = [
        ('Organic Bananas (30 cases)', 1500.00),
        ('Fresh Vegetables Assortment', 3500.00),
        ('Organic Yogurt (150 units)', 1800.00),
        ('Whole Grain Cereal (100 boxes)', 1200.00),
        ('Energy Drinks (10 cases)', 200.00)
    ]
    create_invoice(pdf, 'NC-245813', '01/22/2024', 'Natural Choice Foods', items2, 400.00)
    
    # Create Second Bank Statement
    create_bank_statement(pdf, '01/31/2024', '01/22/2024', 8600.00, 'Natural Choice Foods')
    
    # Save PDF
    pdf.output('tax_credit_documentation.pdf')

if __name__ == '__main__':
    main()