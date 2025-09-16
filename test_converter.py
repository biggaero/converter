#!/usr/bin/env python3
"""
Test script for the converter application
"""

# Import the functions from our main script
from converter import convert_character, display_conversion

def test_conversions():
    """Test the conversion functions with various inputs."""
    test_chars = ['A', 'z', '5', '@', ' ', '!']
    
    print("Testing Character/Digit Converter Functions")
    print("=" * 50)
    
    for char in test_chars:
        conversion = convert_character(char)
        if conversion:
            display_conversion(conversion)
        else:
            print(f"Failed to convert: {char}")
    
    print("All tests completed!")

if __name__ == "__main__":
    test_conversions()