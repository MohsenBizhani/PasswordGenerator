# Secure Password Generator - Help Documentation

## OVERVIEW

The Secure Password Generator is a command-line tool that generates strong, customizable passwords. It provides various options to create passwords that meet specific requirements and security standards.

## BASIC SYNTAX

```bash
password-generator [options]
```

## COMMAND LINE OPTIONS

### Basic Options:
- `-h, --help`: Show this help message and exit
- `-l LENGTH, --length LENGTH`: Length of the password (default: 12)
- `-u, --uppercase`: Include uppercase letters
- `-n, --numbers`: Include numbers
- `-s, --specials`: Include special characters
- `-c COUNT, --count COUNT`: Number of passwords to generate (default: 1)

### Advanced Options:
- `--min-uppercase MIN`: Minimum number of uppercase letters
- `--min-numbers MIN`: Minimum number of numbers
- `--min-specials MIN`: Minimum number of special characters
- `--no-similar`: Exclude similar characters (iIl1Lo0O)
- `--no-ambiguous`: Exclude ambiguous characters {}[]()/'"~,;:.<>
- `--clipboard`: Copy the generated password to clipboard
- `--analyze`: Analyze password strength

## EXAMPLES WITH EXPLANATIONS

1. Generate a basic password:
   ```bash
   password-generator
   ```
   → Creates a 12-character password with lowercase letters only

2. Generate a strong password:
   ```bash
   password-generator -l 16 -u -n -s
   ```
   → Creates a 16-character password with all character types

3. Generate multiple passwords:
   ```bash
   password-generator -c 5 -u -n -s
   ```
   → Creates 5 different passwords with all character types

4. Generate password with minimum requirements:
   ```bash
   password-generator --min-uppercase 2 --min-numbers 2 --min-specials 1
   ```
   → Creates a password with at least 2 uppercase, 2 numbers, and 1 special character

5. Generate and analyze password:
   ```bash
   password-generator -u -n -s --analyze
   ```
   → Creates a password and shows its strength analysis

## PASSWORD STRENGTH ANALYSIS

The password strength analyzer evaluates:
- Password length (4 points per character)
- Uppercase letters (10 points)
- Lowercase letters (10 points)
- Numbers (10 points)
- Special characters (15 points)

Strength Levels:
- 0-39: Weak
- 40-59: Moderate
- 60-79: Strong
- 80+: Very Strong

## SECURITY CONSIDERATIONS

1. The tool uses the 'secrets' module for secure random generation
2. Passwords are generated in memory and not stored
3. When using --clipboard, clear your clipboard after using the password
4. Longer passwords with mixed characters are more secure

## INSTALLATION

### From GitHub:

```bash
git clone https://github.com/MohsenBizhani/PasswordGenerator.git
cd PasswordGenerator
pip install -r requirements.txt
pip install .
```

### From PyPI:

```bash
pip install passkey-generator-cli
```

## PROJECT STRUCTURE

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

## TROUBLESHOOTING

Common Issues:
1. "No characters available": Check if your restrictions are too strict
2. "Minimum requirements exceed length": Reduce minimum requirements or increase length
3. Clipboard not working: Ensure pyperclip is installed (`pip install pyperclip`)

For more information or bug reports, please visit the GitHub repository:
[https://github.com/MohsenBizhani/PasswordGenerator](https://github.com/MohsenBizhani/PasswordGenerator)
