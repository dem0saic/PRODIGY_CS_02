## PRODIGY_CS_02
This is a simple image encryption and decryption tool using Python that manipulates pixel values. We'll use the PIL (Pillow) library for image processing and numpy for handling pixel data.

## Pixel Manipulation

# Overview
The **Pixel Manipulation** program demonstrates how to encrypt and decrypt images using pixel manipulation techniques. By modifying the pixel values of an image, this program showcases a simple method of image encryption.

# Features
- Loads an image and converts it into a numpy array for manipulation.
- Encrypts the image by adding a fixed value to each pixel.
- Decrypts the image by subtracting the same value from each pixel.
- Displays the shape and pixel values of the original, encrypted, and decrypted images.
- Saves the encrypted and decrypted images to specified paths.

# Requirements
- `Python 3.x`
- `Pillow (PIL)`
- `NumPy`
- `PyFiglet`
- `Termcolor`

# Installation
1. **Install Python**: Ensure Python 3.x is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
2. **Install Required Libraries**: Use pip to install the necessary libraries:
   ```bash
   pip install pillow numpy pyfiglet termcolor
   ```
# Usage
To run the Pixel Manipulation program, execute the following command in your terminal or command prompt:

```python pixel_manipulation.py```

# Steps to Use the Program
Load an image by specifying the path in the code (currently set to images/FuckSociety.jpg).
The program will display the original image and its pixel values.
The encryption process will add 10 to each pixel's RGB values.
The decrypted image will be obtained by subtracting 10 from the encrypted pixel values.
Both the encrypted and decrypted images will be saved in the specified paths.
Example Command
You can modify the image path in the code
image_path = "images/FuckSociety.jpg"

# Code Explanation
The program consists of the following key components:

Title Display: The title "Pixel Manipulation" is printed in a stylized ASCII format using the pyfiglet library.
Creator Information: Displays the creator's name and social media handles.
Welcome Message: A brief introduction to the program's functionality.
Purpose Statement: Describes the program's goal of demonstrating image encryption and decryption.
Encryption and Decryption Functions:
encrypt_image(image_array): Encrypts the image by adding 10 to each pixel's RGB values.
decrypt_image(encrypted_image_array): Decrypts the image by subtracting 10 from each pixel's RGB values.
Image Display: Displays the original, encrypted, and decrypted images using the PIL library.

# Creator
Created by: Dem0saic
GitHub: dem0saic
LinkedIn: owusuvincent

License
This project is licensed under the MIT License - see the LICENSE file for details.
