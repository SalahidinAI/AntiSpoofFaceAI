# # ✅ Working code No1
#
# import os.path
# import datetime
# import pickle
#
# import tkinter as tk
# import cv2
# from PIL import Image, ImageTk
# import face_recognition
#
# import util
# from test import test
#
#
# class App:
#     def __init__(self):
#         self.main_window = tk.Tk()
#         self.main_window.geometry("1200x520+350+100")
#
#         self.login_button_main_window = util.get_button(self.main_window, 'login', 'green', self.login)
#         self.login_button_main_window.place(x=750, y=200)
#
#         self.logout_button_main_window = util.get_button(self.main_window, 'logout', 'red', self.logout)
#         self.logout_button_main_window.place(x=750, y=300)
#
#         self.register_new_user_button_main_window = util.get_button(self.main_window, 'register new user', 'gray',
#                                                                     self.register_new_user, fg='black')
#         self.register_new_user_button_main_window.place(x=750, y=400)
#
#         self.webcam_label = util.get_img_label(self.main_window)
#         self.webcam_label.place(x=10, y=0, width=700, height=500)
#
#         self.add_webcam(self.webcam_label)
#
#         self.db_dir = './db'
#         if not os.path.exists(self.db_dir):
#             os.mkdir(self.db_dir)
#
#         self.log_path = './log.txt'
#
#     def add_webcam(self, label):
#         if 'cap' not in self.__dict__:
#             self.cap = cv2.VideoCapture(0)
#
#         self._label = label
#         self.process_webcam()
#
#     def process_webcam(self):
#         ret, frame = self.cap.read()
#
#         # Add this safety check!
#         # if not ret or frame is None:
#         #     # If camera fails, try again in 1 second instead of crashing
#         #     self._label.after(1000, self.process_webcam)
#         #     return
#         #
#         # self.most_recent_capture_arr = frame
#         # img_ = cv2.cvtColor(self.most_recent_capture_arr, cv2.COLOR_BGR2RGB)
#         # ... rest of your code ...
#
#         self.most_recent_capture_arr = frame
#         img_ = cv2.cvtColor(self.most_recent_capture_arr, cv2.COLOR_BGR2RGB)
#         self.most_recent_capture_pil = Image.fromarray(img_)
#         imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)
#         self._label.imgtk = imgtk
#         self._label.configure(image=imgtk)
#
#         self._label.after(20, self.process_webcam)
#
#     def login(self):
#
#         label = test(
#                 image=self.most_recent_capture_arr,
#                 model_dir='/Users/salahidin/PycharmProjects/Customs/AntiSpoofFace/face-attendance-system/Silent-Face-Anti-Spoofing/resources/anti_spoof_models',
#                 device_id=0
#                 )
#
#         if label == 1:
#
#             name = util.recognize(self.most_recent_capture_arr, self.db_dir)
#
#             if name in ['unknown_person', 'no_persons_found']:
#                 util.msg_box('Ups...', 'Unknown user. Please register new user or try again.')
#             else:
#                 util.msg_box('Welcome back !', 'Welcome, {}.'.format(name))
#                 with open(self.log_path, 'a') as f:
#                     f.write('{},{},in\n'.format(name, datetime.datetime.now()))
#                     f.close()
#
#         else:
#             util.msg_box('Hey, you are a spoofer!', 'You are fake!')
#
#     def logout(self):
#
#         label = test(
#                 image=self.most_recent_capture_arr,
#                 model_dir='/Users/salahidin/PycharmProjects/Customs/AntiSpoofFace/face-attendance-system/Silent-Face-Anti-Spoofing/resources/anti_spoof_models',
#                 device_id=0
#                 )
#
#         if label == 1:
#
#             name = util.recognize(self.most_recent_capture_arr, self.db_dir)
#
#             if name in ['unknown_person', 'no_persons_found']:
#                 util.msg_box('Ups...', 'Unknown user. Please register new user or try again.')
#             else:
#                 util.msg_box('Hasta la vista !', 'Goodbye, {}.'.format(name))
#                 with open(self.log_path, 'a') as f:
#                     f.write('{},{},out\n'.format(name, datetime.datetime.now()))
#                     f.close()
#
#         else:
#             util.msg_box('Hey, you are a spoofer!', 'You are fake!')
#
#
#     def register_new_user(self):
#         self.register_new_user_window = tk.Toplevel(self.main_window)
#         self.register_new_user_window.geometry("1200x520+370+120")
#
#         self.accept_button_register_new_user_window = util.get_button(self.register_new_user_window, 'Accept', 'green', self.accept_register_new_user)
#         self.accept_button_register_new_user_window.place(x=750, y=300)
#
#         self.try_again_button_register_new_user_window = util.get_button(self.register_new_user_window, 'Try again', 'red', self.try_again_register_new_user)
#         self.try_again_button_register_new_user_window.place(x=750, y=400)
#
#         self.capture_label = util.get_img_label(self.register_new_user_window)
#         self.capture_label.place(x=10, y=0, width=700, height=500)
#
#         self.add_img_to_label(self.capture_label)
#
#         self.entry_text_register_new_user = util.get_entry_text(self.register_new_user_window)
#         self.entry_text_register_new_user.place(x=750, y=150)
#
#         self.text_label_register_new_user = util.get_text_label(self.register_new_user_window, 'Please, \ninput username:')
#         self.text_label_register_new_user.place(x=750, y=70)
#
#     def try_again_register_new_user(self):
#         self.register_new_user_window.destroy()
#
#     def add_img_to_label(self, label):
#         imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)
#         label.imgtk = imgtk
#         label.configure(image=imgtk)
#
#         self.register_new_user_capture = self.most_recent_capture_arr.copy()
#
#     def start(self):
#         self.main_window.mainloop()
#
#     def accept_register_new_user(self):
#         name = self.entry_text_register_new_user.get(1.0, "end-1c")
#
#         embeddings = face_recognition.face_encodings(self.register_new_user_capture)[0]
#
#         file = open(os.path.join(self.db_dir, '{}.pickle'.format(name)), 'wb')
#         pickle.dump(embeddings, file)
#
#         util.msg_box('Success!', 'User was registered successfully !')
#
#         self.register_new_user_window.destroy()
#
#
# if __name__ == "__main__":
#     app = App()
#     app.start()
#
#



# ✅ Working code No2

# import cv2
# import numpy as np
# from test import test
#
#
# def main():
#     # 0 is the camera index we confirmed works
#     cap = cv2.VideoCapture(0)
#
#     # Your specific model path
#     model_dir = '/Users/salahidin/PycharmProjects/Customs/AntiSpoofFace/face-attendance-system/Silent-Face-Anti-Spoofing/resources/anti_spoof_models'
#     device_id = 0
#
#     while cap.isOpened():
#         ret, frame = cap.read()
#         if not ret:
#             break
#
#         # Run the anti-spoofing test
#         # label: 1=Real, 0=Spoof
#         # prediction: Array of raw scores (e.g., [SpoofScore, LiveScore, OtherSpoofScore])
#         label, prediction = test(
#             image=frame,
#             model_dir=model_dir,
#             device_id=device_id
#         )
#
#         # --- Calculate Scores ---
#         # prediction shape is usually (1, 3). Index 1 is Real.
#         # We assume the sum of all classes is the total "weight"
#         total_score = np.sum(prediction[0])
#
#         # Calculate 'Live' score (Index 1)
#         live_score = prediction[0][1] / total_score
#
#         # 'Spoof' is everything else (1.0 - Live)
#         spoof_score = 1.0 - live_score
#
#         # Format the string: "[0.10, 0.90]"
#         score_text = f"[{live_score:.2f}, {spoof_score:.2f}]"
#
#         # --- Draw on Frame ---
#         if label == 1:
#             # Green for Live
#             color = (0, 255, 0)
#             result_text = "Live"
#         else:
#             # Red for Spoof
#             color = (0, 0, 255)
#             result_text = "Spoof"
#
#         # 1. Draw "Live" or "Spoof"
#         cv2.putText(frame, result_text, (30, 50), cv2.FONT_HERSHEY_SIMPLEX,
#                     1.5, color, 3)
#
#         # 2. Draw the scores "Live, Spoof" title
#         cv2.putText(frame, "Live, Spoof", (30, 100), cv2.FONT_HERSHEY_SIMPLEX,
#                     0.8, (255, 255, 255), 2)
#
#         # 3. Draw the actual numbers [0.x, 0.y]
#         cv2.putText(frame, score_text, (30, 140), cv2.FONT_HERSHEY_SIMPLEX,
#                     0.8, (255, 255, 255), 2)
#
#         cv2.imshow('Anti-Spoofing Detection', frame)
#
#         # Press 'q' to quit
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#
#     cap.release()
#     cv2.destroyAllWindows()
#
#
# if __name__ == "__main__":
#     main()



# ✅ Working code No3

import cv2
import numpy as np
import os
import datetime
import pickle
import face_recognition
from test import test
import util  # We use the util.py you already have for existing logic


def register_user(frame, db_dir):
    """
    Captures the current frame, asks for a name via console,
    and saves the face embedding to the database.
    """
    # Check if face exists in frame before asking for name
    face_locations = face_recognition.face_locations(frame)
    if len(face_locations) == 0:
        return "No face detected! Cannot register."

    # Ask for name in the console (Video will pause briefly)
    print("\n[INFO] Please enter the new user's name in the console:")
    name = input(">>> User Name: ").strip()

    if name == "":
        return "Registration cancelled."

    # Generate embeddings
    embeddings = face_recognition.face_encodings(frame)[0]

    # Save to pickle file
    filename = os.path.join(db_dir, '{}.pickle'.format(name))
    with open(filename, 'wb') as file:
        pickle.dump(embeddings, file)

    return f"User '{name}' registered successfully!"


def delete_user(name, db_dir):
    """Deletes the user's pickle file."""
    file_path = os.path.join(db_dir, '{}.pickle'.format(name))
    if os.path.exists(file_path):
        os.remove(file_path)
        return f"User '{name}' deleted."
    else:
        return f"File for '{name}' not found."


def sharpen_frame(frame):
    # Create a sharpening kernel
    kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    sharpened = cv2.filter2D(frame, -1, kernel)
    return sharpened


def main():
    # Setup
    # cap = cv2.VideoCapture('test1.mp4') # uncomment 339, 341
    cap = cv2.VideoCapture(0)
    model_dir = '/Users/salahidin/PycharmProjects/Customs/AntiSpoofFace/face-attendance-system/Silent-Face-Anti-Spoofing/resources/anti_spoof_models'
    device_id = 0

    # Database setup
    db_dir = './db'
    if not os.path.exists(db_dir):
        os.mkdir(db_dir)
    log_path = './log.txt'

    # UI Variables
    message = ""
    message_color = (255, 255, 255)
    message_timer = 0  # To keep text on screen for a few seconds

    print("System Started. Press 1:Login, 2:Logout, 3:Register, 4:Delete, q:Quit")

    history = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Use 0 for vertical flip, or -1 for both axes
        # frame = cv2.flip(frame, 0) # change it, depends on video or camera

        # --- 1. Anti-Spoofing Check ---
        # frame = sharpen_frame(frame) # if blurred then u need this row
        label, prediction = test(
            image=frame,
            model_dir=model_dir,
            device_id=device_id
        )

        # Calculate Scores
        total_score = np.sum(prediction[0])
        live_score = prediction[0][1] / total_score
        spoof_score = 1.0 - live_score
        score_text = f"[{live_score:.2f}, {spoof_score:.2f}]"

        history.append(live_score)
        if len(history) > 20: history.pop(0)
        avg_live_score = sum(history) / len(history)

        # --- 2. Draw Anti-Spoof UI ---
        # if label == 1:
        if avg_live_score > 0.4:
            color = (0, 255, 0)  # Green
            result_text = "Live"
        else:
            color = (0, 0, 255)  # Red
            result_text = "Spoof"

        cv2.putText(frame, result_text, (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, color, 3)
        cv2.putText(frame, "Live, Spoof", (30, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
        cv2.putText(frame, score_text, (30, 140), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

        # --- 3. Handle Keyboard Commands ---
        key = cv2.waitKey(1) & 0xFF

        if key == ord('1'):  # LOGIN
            if label == 1:  # Only if Real
                name = util.recognize(frame, db_dir)
                if name in ['unknown_person', 'no_persons_found']:
                    message = "Unknown user. Please register."
                    message_color = (0, 0, 255)
                else:
                    message = f"Welcome, {name}!"
                    message_color = (0, 255, 0)
                    with open(log_path, 'a') as f:
                        f.write(f'{name},{datetime.datetime.now()},in\n')
            else:
                message = "Spoof detected! Login denied."
                message_color = (0, 0, 255)
            message_timer = 60  # Show for ~2 seconds

        elif key == ord('2'):  # LOGOUT
            if label == 1:  # Only if Real
                name = util.recognize(frame, db_dir)
                if name in ['unknown_person', 'no_persons_found']:
                    message = "Unknown user."
                    message_color = (0, 0, 255)
                else:
                    message = f"Goodbye, {name}!"
                    message_color = (0, 255, 0)
                    with open(log_path, 'a') as f:
                        f.write(f'{name},{datetime.datetime.now()},out\n')
            else:
                message = "Spoof detected! Logout denied."
                message_color = (0, 0, 255)
            message_timer = 60

        elif key == ord('3'):  # REGISTER
            # Note: This will pause the video to ask for input
            message = "Check console to enter name..."
            cv2.imshow('Anti-Spoofing Detection', frame)
            cv2.waitKey(1)  # Force UI update before blocking

            result = register_user(frame, db_dir)
            message = result
            message_color = (255, 255, 0)  # Cyan
            message_timer = 100

        elif key == ord('4'):  # DELETE
            if label == 1:
                name = util.recognize(frame, db_dir)
                if name in ['unknown_person', 'no_persons_found']:
                    message = "Cannot delete: User not found."
                    message_color = (0, 0, 255)
                else:
                    result = delete_user(name, db_dir)
                    message = result
                    message_color = (0, 0, 255)
            else:
                message = "Spoof detected! Action denied."
                message_color = (0, 0, 255)
            message_timer = 60

        elif key == ord('q'):  # QUIT
            break

        # --- 4. Display System Messages ---
        if message_timer > 0:
            # Draw a background rectangle for better visibility
            cv2.rectangle(frame, (25, 450), (700, 500), (0, 0, 0), -1)
            cv2.putText(frame, message, (30, 490), cv2.FONT_HERSHEY_SIMPLEX, 1, message_color, 2)
            message_timer -= 1

        cv2.imshow('Anti-Spoofing Detection', frame)

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

