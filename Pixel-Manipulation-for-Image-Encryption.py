from pyfiglet import figlet_format
from termcolor import colored
from PIL import Image 
import numpy

# Print the title of the program
title = "Pixel Manipulation"
title_ascii = figlet_format(title, font="shadow", width=1000)
title_colored = colored(title_ascii, color="cyan")
print(title_colored)

# Display the creator of the program with their social handles
creator_info = """
Created by: Dem0saic
GitHub: https://github.com/dem0saic
LinkedIn: https://www.linkedin.com/in/owusuvincent/
"""
creator_colored = colored(creator_info, color="yellow")
print(creator_colored)

# Display welcome message
welcome = "Welcome to this program!"
welcome_colored = colored(welcome, color="green")
print(welcome_colored)

# Display the purpose of the program
purpose = """
Purpose: This program demonstrates how to encrypt and decrypt an image using pixel manipulation.
"""
purpose_colored = colored(purpose, color="green")
print(purpose_colored)

# Display the steps of the program
steps = """
Steps:
1. Load an image.
2. Convert the image to a numpy array.
3. Encrypt the image by adding 10 to each pixel value.
4. Decrypt the image by subtracting 10 from each pixel value.
5. Save the encrypted and decrypted images.
"""
steps_colored = colored(steps, color="green")
print(steps_colored)


# Load the image
image_path = "images/FuckSociety.jpg"
image = Image.open(image_path)
image.show()

# Convert the image to a numpy array
image_array = numpy.array(image)

# Display the shape of the image array
print("Shape of the image array: ", image_array.shape)

# Display the image array
print("Image array: ", image_array)

# Display the first pixel of the image
first_pixel = image_array[0, 0]
print("First pixel: ", first_pixel)

# Display the red, green, and blue values of the first pixel
red_value = first_pixel[0]
green_value = first_pixel[1]
blue_value = first_pixel[2]
print("Red value: ", red_value)
print("Green value: ", green_value)
print("Blue value: ", blue_value)


# Encrypt the image
def encrypt_image(image_array):
    # Get the shape of the image array
    rows, cols, channels = image_array.shape

    # Create an empty image array to store the encrypted image
    encrypted_image_array = numpy.zeros((rows, cols, channels), dtype=numpy.uint8)

    # Loop through each pixel in the image array
    for i in range(rows):
        for j in range(cols):
            for k in range(channels):
                # Get the pixel value
                pixel_value = image_array[i, j, k]

                # Encrypt the pixel value
                encrypted_pixel_value = pixel_value + 10

                # Store the encrypted pixel value in the encrypted image array
                encrypted_image_array[i, j, k] = encrypted_pixel_value

    return encrypted_image_array

# Encrypt the image
encrypted_image_array = encrypt_image(image_array)

# Display the shape of the encrypted image array
print("Shape of the encrypted image array: ", encrypted_image_array.shape)

# Display the encrypted image array
print("Encrypted image array: ", encrypted_image_array)

# Display the first pixel of the encrypted image
first_pixel_encrypted = encrypted_image_array[0, 0]
print("First pixel (encrypted): ", first_pixel_encrypted)

# Display the red, green, and blue values of the first pixel of the encrypted image
red_value_encrypted = first_pixel_encrypted[0]
green_value_encrypted = first_pixel_encrypted[1]
blue_value_encrypted = first_pixel_encrypted[2]
print("Red value (encrypted): ", red_value_encrypted)
print("Green value (encrypted): ", green_value_encrypted)
print("Blue value (encrypted): ", blue_value_encrypted)

# Convert the encrypted image array to an image
encrypted_image = Image.fromarray(encrypted_image_array)
encrypted_image.show()

# Decrypt the image
def decrypt_image(encrypted_image_array):
    # Get the shape of the encrypted image array
    rows, cols, channels = encrypted_image_array.shape

    # Create an empty image array to store the decrypted image
    decrypted_image_array = numpy.zeros((rows, cols, channels), dtype=numpy.uint8)

    # Loop through each pixel in the encrypted image array
    for i in range(rows):
        for j in range(cols):
            for k in range(channels):
                # Get the encrypted pixel value
                encrypted_pixel_value = encrypted_image_array[i, j, k]

                # Decrypt the pixel value
                decrypted_pixel_value = encrypted_pixel_value - 10

                # Store the decrypted pixel value in the decrypted image array
                decrypted_image_array[i, j, k] = decrypted_pixel_value

    return decrypted_image_array

# Decrypt the image
decrypted_image_array = decrypt_image(encrypted_image_array)

# Display the shape of the decrypted image array
print("Shape of the decrypted image array: ", decrypted_image_array.shape)

# Display the decrypted image array
print("Decrypted image array: ", decrypted_image_array)

# Display the first pixel of the decrypted image
first_pixel_decrypted = decrypted_image_array[0, 0]
print("First pixel (decrypted): ", first_pixel_decrypted)

# Display the red, green, and blue values of the first pixel of the decrypted image
red_value_decrypted = first_pixel_decrypted[0]
green_value_decrypted = first_pixel_decrypted[1]
blue_value_decrypted = first_pixel_decrypted[2]
print("Red value (decrypted): ", red_value_decrypted)
print("Green value (decrypted): ", green_value_decrypted)
print("Blue value (decrypted): ", blue_value_decrypted)

# Convert the decrypted image array to an image
decrypted_image = Image.fromarray(decrypted_image_array)
decrypted_image.show()

# Save the encrypted image
encrypted_image_path = "images/FuckSociety.jpg"
encrypted_image.save(encrypted_image_path)

# Save the decrypted image
decrypted_image_path = "images/FuckSociety.jpg"
decrypted_image.save(decrypted_image_path)

# Display the paths of the encrypted and decrypted images
print("Encrypted image saved at: ", encrypted_image_path)
print("Decrypted image saved at: ", decrypted_image_path)

# Display completion message
completion = "The image encryption and decryption process is complete."
completion_colored = colored(completion, color="green")
print(completion_colored)

# End of the program
end = "End of the program."
end_colored = colored(end, color="green")
print(end_colored)

# End of the program
end = "Thank you for using this program!"
end_colored = colored(end, color="green")
print(end_colored)

# End of the program
end = "Goodbye!, See you later!"
end_colored = colored(end, color="green")
print(end_colored)