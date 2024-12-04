# TSX and Python PDF Generator

This repository contains examples of generating PDFs from both React/TypeScript components and Python. It includes a tax credit documentation template implemented in both technologies.

## Repository Structure

```
├── react-implementation/     # TypeScript/React implementation
│   ├── src/
│   ├── package.json
│   └── README.md
└── python-implementation/    # Python implementation
    ├── requirements.txt
    ├── templates/
    └── main.py
```

## React/TypeScript Implementation

### Prerequisites

- Node.js (v14 or higher)
- npm or yarn

### Setup

1. Navigate to the react-implementation directory:
   ```bash
   cd react-implementation
   ```

2. Install dependencies:
   ```bash
   npm install
   # or
   yarn install
   ```

3. Start the development server:
   ```bash
   npm run dev
   # or
   yarn dev
   ```

4. Open your browser and navigate to `http://localhost:3000`

## Python Implementation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Setup

1. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
   ```

2. Navigate to the python-implementation directory:
   ```bash
   cd python-implementation
   ```

3. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the script:
   ```bash
   python main.py
   ```

## Python vs React: Which to Choose?

### Choose Python if:
- You need to generate PDFs automatically without user interaction
- You're more comfortable with Python
- You need to integrate with other Python services
- You want to generate PDFs server-side

### Choose React if:
- You need an interactive UI for PDF generation
- You're building a web application
- You need real-time preview
- You want to maintain exact styling from web to PDF

## Contributing

Feel free to submit issues and enhancement requests!

## License

MIT