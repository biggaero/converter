#!/usr/bin/env python3
"""
Character/Digit Converter Terminal Application

Converts letters and digits to binary, hexadecimal, octal, and ASCII values.
Features:
- Interactive terminal interface
- Clear function for follow-up conversions
- Ctrl+C or 'quit' to exit
"""

import sys
import os


def clear_screen():
    """Clear the terminal screen."""
    os.system('clear' if os.name == 'posix' else 'cls')


def display_banner():
    """Display the application banner."""
    print("=" * 60)
    print("        CHARACTER/DIGIT CONVERTER")
    print("=" * 60)
    print("Convert any letter or digit to:")
    print("• Binary   • Hexadecimal   • Octal   • ASCII")
    print("-" * 60)
    print("Commands:")
    print("• Type any character or digit to convert")
    print("• 'clear' or 'c' - Clear screen")
    print("• 'quit' or 'q' - Exit program")
    print("• Ctrl+C - Quick exit")
    print("=" * 60)
    print()


def convert_character(char):
    """
    Convert a character to different number systems.
    
    Args:
        char (str): Single character to convert
        
    Returns:
        dict: Dictionary containing conversions
    """
    if len(char) != 1:
        return None
    
    ascii_val = ord(char)
    
    return {
        'character': char,
        'ascii': ascii_val,
        'binary': bin(ascii_val)[2:],  # Remove '0b' prefix
        'hexadecimal': hex(ascii_val)[2:].upper(),  # Remove '0x' prefix, uppercase
        'octal': oct(ascii_val)[2:]  # Remove '0o' prefix
    }


def display_conversion(conversion):
    """
    Display the conversion results in a formatted table.
    
    Args:
        conversion (dict): Conversion results
    """
    char = conversion['character']
    ascii_val = conversion['ascii']
    binary = conversion['binary']
    hex_val = conversion['hexadecimal']
    octal = conversion['octal']
    
    print(f"\nConversion Results for: '{char}'")
    print("-" * 40)
    print(f"Character:    {char}")
    print(f"ASCII:        {ascii_val}")
    print(f"Binary:       {binary.zfill(8)} ({binary})")  # Show both padded and unpadded
    print(f"Hexadecimal:  0x{hex_val} ({hex_val})")
    print(f"Octal:        0o{octal} ({octal})")
    print("-" * 40)
    
    # Additional info for common characters
    if char.isalpha():
        case_info = "uppercase" if char.isupper() else "lowercase"
        print(f"Type:         {case_info} letter")
    elif char.isdigit():
        print(f"Type:         digit")
    elif char.isspace():
        print(f"Type:         whitespace character")
    else:
        print(f"Type:         special character")
    
    print()


def get_user_input():
    """
    Get user input with prompt.
    
    Returns:
        str: User input string
    """
    try:
        return input("Enter a character/digit (or command): ").strip()
    except (EOFError, KeyboardInterrupt):
        return "quit"


def main():
    """Main application loop."""
    clear_screen()
    display_banner()
    
    while True:
        try:
            user_input = get_user_input()
            
            # Handle empty input
            if not user_input:
                print("Please enter a character, digit, or command.\n")
                continue
            
            # Handle commands
            if user_input.lower() in ['quit', 'q', 'exit']:
                print("\nThank you for using Character/Digit Converter!")
                break
            elif user_input.lower() in ['clear', 'c', 'cls']:
                clear_screen()
                display_banner()
                continue
            elif user_input.lower() in ['help', 'h']:
                display_banner()
                continue
            
            # Handle multi-character input
            if len(user_input) > 1:
                print(f"\nProcessing multiple characters: '{user_input}'")
                print("=" * 50)
                for i, char in enumerate(user_input):
                    conversion = convert_character(char)
                    if conversion:
                        print(f"\nPosition {i+1}:")
                        display_conversion(conversion)
                continue
            
            # Convert single character
            conversion = convert_character(user_input)
            if conversion:
                display_conversion(conversion)
            else:
                print("Error: Unable to process input.\n")
        
        except KeyboardInterrupt:
            print("\n\nExiting... Goodbye!")
            break
        except Exception as e:
            print(f"\nError: {e}")
            print("Please try again.\n")


if __name__ == "__main__":
    main()