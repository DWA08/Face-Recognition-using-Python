import cv2
import os

# Create a directory to store student data
if not os.path.exists("student_data"):
    os.makedirs("student_data")

# Initialize the webcam
video_capture = cv2.VideoCapture(0)

# Specify the number of students to capture
num_students_to_capture = 5  # Change this to the desired number

# Counter for captured students
captured_count = 0

# Create a dictionary to store student data
student_data = {}

while captured_count < num_students_to_capture:
    ret, frame = video_capture.read()

    # Display the student's face on the screen
    cv2.imshow('Student Face', frame)

    # Wait for a moment to capture the face
    key = cv2.waitKey(100)

    if key == ord('c'):
        # Prompt the user to enter the student's name
        student_name = input("Enter student's name: ")

        # Save the captured picture with the student's name
        cv2.imwrite(f"student_data/{student_name}.jpg", frame)

        # Store the student's data in the dictionary
        student_data[student_name] = {
            "present": False,
            "photo_path": f"student_data/{student_name}.jpg"
        }

        # Update the captured count
        captured_count += 1

    if captured_count == num_students_to_capture:
        print("Data capture completed.")
        break

video_capture.release()
cv2.destroyAllWindows()

# Save the student data to a file (students_details.txt)
with open("students_details.txt", "w") as file:
    for student_name, data in student_data.items():
        file.write(f"{student_name}: {data['photo_path']}\n")

# At this point, you have captured and saved student data and photos to a file.
