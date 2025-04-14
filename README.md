# Secure Password Generator

A powerful and flexible command-line password generator tool with advanced features for generating secure passwords.

## Features

- Generate single or multiple passwords
- Customizable password length
- Include/exclude character types (uppercase, numbers, special characters)
- Set minimum requirements for each character type
- Exclude similar-looking characters
- Exclude ambiguous characters
- Password strength analysis
- Clipboard integration
- Secure random generation using the `secrets` module

## Installation

### From GitHub

1. Clone the repository:
```bash
git clone https://github.com/MohsenBizhani/PasswordGenerator.git
cd PasswordGenerator
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Install the package:
```bash
pip install .
```

### From PyPI

```bash
pip install passkey-generator-cli
```

## Usage

### Basic Usage

```bash
password-generator
```

### Common Options

- `-l, --length`: Set password length (default: 12)
- `-u, --uppercase`: Include uppercase letters
- `-n, --numbers`: Include numbers
- `-s, --specials`: Include special characters
- `-c, --count`: Generate multiple passwords
- `--analyze`: Analyze password strength
- `--clipboard`: Copy password to clipboard

### Advanced Options

- `--min-uppercase`: Minimum number of uppercase letters
- `--min-numbers`: Minimum number of numbers
- `--min-specials`: Minimum number of special characters
- `--no-similar`: Exclude similar characters (iIl1Lo0O)
- `--no-ambiguous`: Exclude ambiguous characters {}[]()/'"~,;:.<>

### Examples

1. Generate a basic 12-character password:
```bash
password-generator
```

2. Generate a strong 16-character password with all character types:
```bash
password-generator -l 16 -u -n -s
```

3. Generate and analyze a password:
```bash
password-generator -u -n -s --analyze
```

4. Generate 5 passwords:
```bash
password-generator -c 5 -u -n -s
```

5. Generate password with minimum requirements:
```bash
password-generator -u -n -s --min-uppercase 2 --min-numbers 2 --min-specials 1
```

6. Generate password without similar-looking characters:
```bash
password-generator -u -n --no-similar
```

7. Generate and copy to clipboard:
```bash
password-generator -u -n -s --clipboard
```

## Password Strength Analysis

The tool analyzes passwords based on:
- Length (4 points per character)
- Presence of uppercase letters (10 points)
- Presence of lowercase letters (10 points)
- Presence of numbers (10 points)
- Presence of special characters (15 points)

Strength levels:
- Weak: Score < 40
- Moderate: Score 40-59
- Strong: Score 60-79
- Very Strong: Score ≥ 80

## Security Features

- Uses Python's `secrets` module for cryptographically strong random generation
- Implements secure password shuffling
- Provides options to exclude similar and ambiguous characters
- Enforces minimum requirements for different character types

## Project Structure

```
PasswordGenerator/
├── password_generator/       # Main package
│   ├── __init__.py           # Package initialization
│   └── cli.py                # Command-line interface implementation
├── setup.py                  # Package installation setup
├── README.md                 # Project documentation
├── HELP.md                   # Help documentation
├── LICENSE                   # License file
└── requirements.txt          # Dependencies
```

## Requirements

- Python 3.6 or higher
- pyperclip package (>=1.8.2)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Author

Mohsen Bizhani - [bizhani.2002@gmail.com](mailto:bizhani.2002@gmail.com)

## Links

- GitHub: [https://github.com/MohsenBizhani/PasswordGenerator](https://github.com/MohsenBizhani/PasswordGenerator)
- PyPI: [https://pypi.org/project/passkey-generator-cli/](https://pypi.org/project/passkey-generator-cli/)
