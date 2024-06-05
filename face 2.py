# Load student data from the file
student_data = {}

with open("students_details.txt", "r") as file:
    for line in file:
        parts = line.strip().split(": ")
        student_name = parts[0]
        photo_path = parts[1]
        student_data[student_name] = {
            "present": False,
            "photo_path": photo_path
        }

# Initialize the webcam for attendance marking
video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()

    # Detect faces in the frame using face_recognition or Haar Cascade

    # Perform face recognition or other methods to identify students in the frame

    # If a student is recognized, mark them as present in the student_data dictionary
    if student_name in student_data:
        student_data[student_name]["present"] = True

    cv2.imshow('Video', frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()

# Save the attendance records to a file or database
with open("attendance_records.txt", "w") as file:
    for student_name, data in student_data.items():
        attendance_status = "Present" if data["present"] else "Absent"
        file.write(f"{student_name}: {attendance_status}\n")

# At this point, you have marked attendance based on student data and captured photos.
