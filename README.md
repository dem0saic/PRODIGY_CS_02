## PRODIGY_CS_02
This is a simple image encryption and decryption tool using Python that manipulates pixel values. We'll use the PIL (Pillow) library for image processing and numpy for handling pixel data.

# Explanation
Import Libraries: We import PIL for image handling and numpy for numerical operations.
Encrypt Function:
Load the image and convert it to a numpy array.
Use XOR operation with a key to encrypt the pixel values.
Convert the encrypted array back to an image and save it.
Decrypt Function:
Similar to the encrypt function, but it decrypts by applying XOR again with the same key.

# Main Function:
Defines input and output paths.
Generates a random key that matches the size of the image.
Calls the encrypt and decrypt functions and prints success messages.

# Notes
The key must be the same size as the image for the XOR operation to work correctly.
This is a basic example of image encryption. For more robust encryption, consider using established cryptographic libraries.