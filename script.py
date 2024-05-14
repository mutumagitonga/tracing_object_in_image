from PIL import Image
import numpy as np
import cv2
import turtle

# Load the image with Pillow
original_image = Image.open('./lamborghini.png')

# Convert the PIL image to OpenCV format for further processing
opencv_image = np.array(original_image)

# Convert the image to HSV (Hue, Saturation, Value)
hsv = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2HSV)

# Define the range of neon orange color in HSV
lower_orange = np.array([10, 100, 100])  # Lower boundary of the HSV range
upper_orange = np.array([25, 255, 255])  # Upper boundary of the HSV range

# Threshold the HSV image to get only orange colors
mask = cv2.inRange(hsv, lower_orange, upper_orange)

# Find contours
contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Get the largest contour (assuming the car is the largest object)
cnt = max(contours, key=cv2.contourArea)

# Scaling factor
scale = 4  # Adjust scale factor as needed to increase the size of the drawing

# Create a turtle object
screen = turtle.Screen()
scaled_width = opencv_image.shape[1] * scale
scaled_height = opencv_image.shape[0] * scale
screen.setup(width=scaled_width, height=scaled_height)
screen.bgcolor("black")
t = turtle.Turtle()
t.pencolor("white")
t.speed(0)  # Fastest drawing speed

# Adjust the turtle starting position
t.penup()
t.goto(-scaled_width // 2, scaled_height // 2)
t.pendown()

# Extract the x and y coordinates of the contour points and draw them using the scaling factor
for point in cnt:
    x, y = point[0]
    t.penup()
    t.goto(x * scale - scaled_width // 2, scaled_height // 2 - y * scale)  # Apply scaling here
    t.pendown()
    t.forward(1 * scale)  # Adjust the step size as needed, scaled accordingly

# Keep the window open until closed manually
turtle.done()
