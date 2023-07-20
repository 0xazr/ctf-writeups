from PIL import Image

def decode_lsb(image_path, encoded_image_path):
    image = Image.open(image_path)
    pixels = image.load()
    encoded_image = Image.open(encoded_image_path)
    encoded_pixels = encoded_image.load()

    binary_message = ''

    i = 0
    for y in range(image.height):
        for x in range(image.width):
            r, g, b, a = pixels[x, y]
            r2, g2, b2, a2 = encoded_pixels[x, y]

            if r > g and r > b and i < 54*8:
                binary_message += str(bin(r2))[-2]
                i += 1

    # Convert the binary message back to ASCII
    message = ''
    for i in range(0, len(binary_message), 8):
        char_binary = binary_message[i:i+8]
        char = chr(int(char_binary, 2))
        message += char

    return message


# Example usage
image_path = "rules-iceberg.png"
encoded_image_path = "new-rules-iceberg.png"
decoded_message = decode_lsb(image_path, encoded_image_path)
print("Decoded message:", decoded_message)