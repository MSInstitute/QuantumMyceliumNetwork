# Installation Guide

## Requirements
- Python 3.9+
- pip package manager
- Virtual environment (recommended)

## Quick Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/quantum-mycelium-network.git
cd quantum-mycelium-network

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install package in development mode
pip install -e .
```

## Dependencies Overview
- Core Dependencies:
  - numpy>=1.21.0
  - networkx>=2.6.0
  - quantum-circuit>=0.3.0
  - torch>=1.9.0
  - pandas>=1.3.0

- Visualization Dependencies:
  - gephi-toolkit>=0.9.2
  - graphviz>=0.16
  - matplotlib>=3.4.0

## Verification
Test your installation:
```bash
python examples/basic_network.py
```

## Troubleshooting

### Common Issues

1. Quantum Dependencies
```bash
pip install quantum-circuit>=0.3.0
```

2. Visualization Tools
```bash
pip install gephi-toolkit>=0.9.2 graphviz>=0.16
```

3. CUDA Support (Optional)
```bash
pip install torch==1.9.0+cu111 -f https://download.pytorch.org/whl/torch_stable.html
```

### Support
For issues, please create a ticket in our GitHub repository.
