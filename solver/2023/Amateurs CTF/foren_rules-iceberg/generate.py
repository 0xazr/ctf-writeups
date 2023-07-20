from PIL import Image

def encode_lsb(image_path, message):
    # Open the image
    image = Image.open(image_path)
    pixels = image.load()

    # Check if the message can fit within the image
    if len(message) * 8 > image.width * image.height:
        raise ValueError("Message is too long to fit within the image.")

    # Convert the message to binary
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    print("Binary Message:", binary_message)
    # Embed the message into the image
    char_index = 0
    for y in range(image.height):
        for x in range(image.width):
            r, g, b, a = pixels[x, y]

            if char_index < len(binary_message):
                # Modify the second least significant bit of the red channel
                # only if red is greater than green and blue
                if r > g and r > b:
                    # least significant bit of the red channel
                    r2 = str(bin(r))[-2] 
                    print(f"{str(bin(r))}[{r2}]", end=" -> ")
                    temp = r
                    r = (r & 0xFD) | (int(binary_message[char_index]) << 1)
                    r3 = str(bin(r))[-2]
                    modified = temp == r
                    same = r2 == r3
                    yes = 'yes' if r3 == binary_message[char_index] else 'no'
                    print(f"{str(bin(r))}[{r3}]\t{'unchanged' if modified else 'modified'}\t{binary_message[char_index]}\t{'same' if same else 'diff'}\t{yes}")
                    char_index += 1

            pixels[x, y] = (r, g, b, a)

    # Save the modified image
    encoded_image_path = f"test-{image_path}"
    image.save(encoded_image_path)
    print("Message encoded successfully in the image:", encoded_image_path)


# Example usage
image_path = "rules-iceberg.png"

# extract flag from flag.txt
# with open("flag.txt", "r") as f:
#     flag = f.read().strip()
flag = "flag{this_is_a_flag}"

# assert len(flag) == 54

encode_lsb(image_path, flag)