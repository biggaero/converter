# Character/Digit Converter

A Python terminal application that converts letters and digits to their binary, hexadecimal, octal, and ASCII representations.

## Features

- **Interactive Terminal Interface**: Clean, user-friendly command-line interface
- **Multiple Format Support**: Converts to binary, hexadecimal, octal, and ASCII
- **Character Type Detection**: Identifies uppercase/lowercase letters, digits, special characters, and whitespace
- **Flexible Input**: Handles single characters or multiple character strings
- **Clear Functionality**: Clear screen for follow-up conversions
- **Multiple Exit Options**: Quit via commands or keyboard shortcuts

## Usage

### Running the Application

```bash
# Make executable (if not already)
chmod +x converter.py

# Run the application
python3 converter.py
# or
./converter.py
```

### Commands

| Command | Alternative | Description |
|---------|-------------|-------------|
| `quit` | `q`, `exit` | Exit the program |
| `clear` | `c`, `cls` | Clear the screen |
| `help` | `h` | Show help banner |
| **Ctrl+C** | - | Quick exit |

### Examples

#### Single Character Conversion
```
Enter a character/digit (or command): A

Conversion Results for: 'A'
----------------------------------------
Character:    A
ASCII:        65
Binary:       01000001 (1000001)
Hexadecimal:  0x41 (41)
Octal:        0o101 (101)
----------------------------------------
Type:         uppercase letter
```

#### Multiple Character Processing
```
Enter a character/digit (or command): Hi!

Processing multiple characters: 'Hi!'
==================================================

Position 1:

Conversion Results for: 'H'
----------------------------------------
Character:    H
ASCII:        72
Binary:       01001000 (1001000)
Hexadecimal:  0x48 (48)
Octal:        0o110 (110)
----------------------------------------
Type:         uppercase letter

Position 2:

Conversion Results for: 'i'
----------------------------------------
Character:    i
ASCII:        105
Binary:       01101001 (1101001)
Hexadecimal:  0x69 (69)
Octal:        0o151 (151)
----------------------------------------
Type:         lowercase letter

Position 3:

Conversion Results for: '!'
----------------------------------------
Character:    !
ASCII:        33
Binary:       00100001 (100001)
Hexadecimal:  0x21 (21)
Octal:        0o41 (41)
----------------------------------------
Type:         special character
```

## File Structure

```
converter/
├── converter.py      # Main application
├── test_converter.py # Test script
└── README.md         # This file
```

## Testing

Run the test script to verify functionality:

```bash
python3 test_converter.py
```

## Requirements

- Python 3.x
- No external dependencies required

## Key Features Explained

1. **ASCII Values**: Shows the decimal ASCII code for each character
2. **Binary**: Displays both zero-padded (8-bit) and minimal binary representations
3. **Hexadecimal**: Shows values in uppercase with and without the '0x' prefix
4. **Octal**: Displays octal values with and without the '0o' prefix
5. **Character Type**: Automatically identifies the type of character (letter, digit, special, whitespace)

## Error Handling

- Graceful handling of keyboard interrupts (Ctrl+C)
- Input validation for empty inputs
- Error messages for unexpected issues
- Continues running after errors