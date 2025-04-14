#!/usr/bin/env python3
import argparse
import random
import string
import pyperclip
import secrets
import re
from typing import List

class PasswordGenerator:
    def __init__(self):
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.digits = string.digits
        self.special_chars = string.punctuation
        self.similar_chars = 'iIl1Lo0O'
        self.ambiguous_chars = '{}[]()/\'"`~,;:.<>'

    def generate_password(self,
                         length: int = 12,
                         use_uppercase: bool = False,
                         use_numbers: bool = False,
                         use_specials: bool = False,
                         exclude_similar: bool = False,
                         exclude_ambiguous: bool = False,
                         min_uppercase: int = 0,
                         min_numbers: int = 0,
                         min_specials: int = 0) -> str:
        """
        Generate a password based on specified criteria
        """
        if length < 1:
            raise ValueError("Password length must be at least 1")

        # Initialize character pool
        chars = list(self.lowercase)
        if use_uppercase:
            chars.extend(self.uppercase)
        if use_numbers:
            chars.extend(self.digits)
        if use_specials:
            chars.extend(self.special_chars)

        # Remove excluded characters
        if exclude_similar:
            chars = [c for c in chars if c not in self.similar_chars]
        if exclude_ambiguous:
            chars = [c for c in chars if c not in self.ambiguous_chars]

        if not chars:
            raise ValueError("No characters available with current restrictions")

        # Generate initial password
        password = []

        # Ensure minimum requirements
        if use_uppercase and min_uppercase > 0:
            password.extend(secrets.choice(self.uppercase) for _ in range(min_uppercase))
        if use_numbers and min_numbers > 0:
            password.extend(secrets.choice(self.digits) for _ in range(min_numbers))
        if use_specials and min_specials > 0:
            password.extend(secrets.choice(self.special_chars) for _ in range(min_specials))

        # Fill remaining length with random characters
        remaining_length = length - len(password)
        if remaining_length < 0:
            raise ValueError("Minimum requirements exceed password length")

        password.extend(secrets.choice(chars) for _ in range(remaining_length))

        # Shuffle the password
        random.shuffle(password)
        return ''.join(password)

    def check_password_strength(self, password: str) -> dict:
        """
        Evaluate password strength and return a detailed analysis
        """
        analysis = {
            'length': len(password),
            'has_uppercase': bool(re.search(r'[A-Z]', password)),
            'has_lowercase': bool(re.search(r'[a-z]', password)),
            'has_numbers': bool(re.search(r'\d', password)),
            'has_special': bool(re.search(r'[^A-Za-z0-9]', password)),
            'strength': 'Weak'
        }

        score = 0
        score += len(password) * 4
        score += 10 if analysis['has_uppercase'] else 0
        score += 10 if analysis['has_lowercase'] else 0
        score += 10 if analysis['has_numbers'] else 0
        score += 15 if analysis['has_special'] else 0

        if score >= 80:
            analysis['strength'] = 'Very Strong'
        elif score >= 60:
            analysis['strength'] = 'Strong'
        elif score >= 40:
            analysis['strength'] = 'Moderate'

        analysis['score'] = score
        return analysis

    def generate_multiple_passwords(self, count: int, **kwargs) -> List[str]:
        """
        Generate multiple passwords with the same criteria
        """
        return [self.generate_password(**kwargs) for _ in range(count)]

def main():
    parser = argparse.ArgumentParser(
        description="""
Password Generator Tool
----------------------
A secure password generator with multiple options for customization.
Generated passwords can be analyzed for strength and copied to clipboard.
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument("-l", "--length", type=int, default=12,
                       help="Length of the password (default: 12)")
    parser.add_argument("-u", "--uppercase", action="store_true",
                       help="Include uppercase letters")
    parser.add_argument("-n", "--numbers", action="store_true",
                       help="Include numbers")
    parser.add_argument("-s", "--specials", action="store_true",
                       help="Include special characters")
    parser.add_argument("--min-uppercase", type=int, default=0,
                       help="Minimum number of uppercase letters")
    parser.add_argument("--min-numbers", type=int, default=0,
                       help="Minimum number of numbers")
    parser.add_argument("--min-specials", type=int, default=0,
                       help="Minimum number of special characters")
    parser.add_argument("--no-similar", action="store_true",
                       help="Exclude similar characters (iIl1Lo0O)")
    parser.add_argument("--no-ambiguous", action="store_true",
                       help="Exclude ambiguous characters {}[]()/\'\"~,;:.<>")
    parser.add_argument("-c", "--count", type=int, default=1,
                       help="Number of passwords to generate (default: 1)")
    parser.add_argument("--clipboard", action="store_true",
                       help="Copy the generated password to clipboard")
    parser.add_argument("--analyze", action="store_true",
                       help="Analyze password strength")

    args = parser.parse_args()

    try:
        generator = PasswordGenerator()

        if args.count > 1:
            passwords = generator.generate_multiple_passwords(
                args.count,
                length=args.length,
                use_uppercase=args.uppercase,
                use_numbers=args.numbers,
                use_specials=args.specials,
                exclude_similar=args.no_similar,
                exclude_ambiguous=args.no_ambiguous,
                min_uppercase=args.min_uppercase,
                min_numbers=args.min_numbers,
                min_specials=args.min_specials
            )
            print("\nGenerated Passwords:")
            for i, password in enumerate(passwords, 1):
                print(f"{i}. {password}")
        else:
            password = generator.generate_password(
                length=args.length,
                use_uppercase=args.uppercase,
                use_numbers=args.numbers,
                use_specials=args.specials,
                exclude_similar=args.no_similar,
                exclude_ambiguous=args.no_ambiguous,
                min_uppercase=args.min_uppercase,
                min_numbers=args.min_numbers,
                min_specials=args.min_specials
            )
            print(f"\nGenerated Password: {password}")

            if args.clipboard:
                pyperclip.copy(password)
                print("Password copied to clipboard!")

            if args.analyze:
                analysis = generator.check_password_strength(password)
                print("\nPassword Analysis:")
                print(f"Length: {analysis['length']}")
                print(f"Contains Uppercase: {'Yes' if analysis['has_uppercase'] else 'No'}")
                print(f"Contains Lowercase: {'Yes' if analysis['has_lowercase'] else 'No'}")
                print(f"Contains Numbers: {'Yes' if analysis['has_numbers'] else 'No'}")
                print(f"Contains Special Characters: {'Yes' if analysis['has_special'] else 'No'}")
                print(f"Strength Score: {analysis['score']}/100")
                print(f"Overall Strength: {analysis['strength']}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()