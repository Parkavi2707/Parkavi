import cv2
import pygame

# Set up Pygame for audio playback
pygame.mixer.init()
songs = ["Add your path"]  # Add your song paths here
song_index = 0

# Set up the camera
camera = cv2.VideoCapture(1)

# Check if the camera is opened
if not camera.isOpened():
    print("Cannot open camera")
    exit()

# Main loop for capturing hand gestures
while True:
    # Read a frame from the camera
    ret, frame = camera.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Add your hand gesture recognition code here using OpenCV

    # Example: detecting navy blue color
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_green = (40, 40, 40)
    upper_green = (80, 255, 255)
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # Process the gesture
    if cv2.countNonZero(mask) > 200000:  # Adjust the threshold value as needed
        print(f"Playing {songs[song_index]}")
        pygame.mixer.music.load(songs[song_index])
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
        song_index = (song_index + 1) % len(songs)  # Cycle through the songs

    # Display the frame
    cv2.imshow("Frame", frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up
camera.release()
cv2.destroyAllWindows()
