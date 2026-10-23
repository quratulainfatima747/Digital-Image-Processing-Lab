# Exercise 1: Variables and Data Types
width = 640
height = 480
image_name = "sample.png"
is_color = True

print("Width:", width, type(width))
print("Height:", height, type(height))
print("Image name:", image_name, type(image_name))
print("Is color:", is_color, type(is_color))
print("Total pixels:", width * height)


# Exercise 2: Conditions
intensities = [-1, 0, 127, 128, 255, 256]

for intensity in intensities:
    if intensity < 0 or intensity > 255:
        label = "Invalid"
    elif intensity >= 128:
        label = "Bright pixel"
    else:
        label = "Dark pixel"
    print(intensity, ":", label)


# Exercise 3: Loops
pixels = [20, 130, 255]

for pixel in pixels:
    if pixel >= 128:
        print(pixel, "Bright")
    else:
        print(pixel, "Dark")

counter = 0
while counter < 3:
    print(counter)
    counter += 1


# Exercise 4: Function
def is_bright(pixel, threshold=128):
    return pixel >= threshold

print(is_bright(127))
print(is_bright(128))
print(is_bright(200, 210))


# Exercise 5: Lists and Tuples
pixels = [0, 128, 255]
print("First pixel:", pixels[0])

pixels[1] = 150
pixels.append(64)

print("Updated list:", pixels)
print("List length:", len(pixels))

size = (640, 480)
width, height = size
print("Width:", width)
print("Height:", height)

# Lists are mutable; tuples are immutable.


# Exercise 6: Dictionaries and Sets
image = {"width": 640, "height": 480}
image["mode"] = "RGB"

print("Image width:", image["width"])
print("Image mode:", image["mode"])

animals = ["cat", "dog", "cat", "bird"]
unique_animals = set(animals)

print("Unique animals:", unique_animals)
print("Number of unique animals:", len(unique_animals))