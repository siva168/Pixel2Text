from PIL import Image
def pixelConverter(image, type, keep, size):
    size = int(size)  # Convert string to integer
    # Open to obtain the size of the image
    IMG = Image.open(image)
    width, height = IMG.size
    # Shrink image
    IMG.resize((width//size, height//size)).save("Cropped.%s" % type)
    # Display new image
    IMG = Image.open("Cropped.%s" % type)
    width, height = IMG.size
    grid = []
    for i in range(height):
        grid.append(["!"]*width)
    pixel = IMG.load()
    for a in range(height):
        row = []
        for b in range(width):
            pixel_sum = sum(pixel[b, a])
            print(f"Pixel sum at ({b}, {a}): {pixel_sum}")
            if pixel_sum == 0:
                grid[a][b] = "#"
            elif 1 <= pixel_sum < 100:
                grid[a][b] = "X"
            elif 100 <= pixel_sum < 200:
                grid[a][b] = "%"
            elif 200 <= pixel_sum < 300:
                grid[a][b] = "&"
            elif 300 <= pixel_sum < 400:
                grid[a][b] = "ø"
            elif 400 <= pixel_sum < 500:
                grid[a][b] = "₭"
            elif 500 <= pixel_sum < 600:
                grid[a][b] = "?"
            elif 600 <= pixel_sum < 700:
                grid[a][b] = "*"
            elif 700 <= pixel_sum < 800:
                grid[a][b] = "+"
            elif 800 <= pixel_sum < 900:
                grid[a][b] = "/"
            elif 900 <= pixel_sum < 1000:
                grid[a][b] = "'"
            else:
                grid[a][b] = ""
    with open(keep, "w",encoding="utf-8") as pic:  # Open the file in write mode
        for row in grid:
            line = "".join(row) + "\n"
            pic.write(line)  # Write each row to the file
if __name__ == '__main__':
    pixelConverter("mozart.jpeg", "jpeg", "mozart.txt", "3")