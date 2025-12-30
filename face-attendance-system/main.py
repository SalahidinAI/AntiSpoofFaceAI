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

import cv2
import numpy as np
from test import test


def main():
    # 0 is the camera index we confirmed works
    cap = cv2.VideoCapture(0)

    # Your specific model path
    model_dir = '/Users/salahidin/PycharmProjects/Customs/AntiSpoofFace/face-attendance-system/Silent-Face-Anti-Spoofing/resources/anti_spoof_models'
    device_id = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Run the anti-spoofing test
        # label: 1=Real, 0=Spoof
        # prediction: Array of raw scores (e.g., [SpoofScore, LiveScore, OtherSpoofScore])
        label, prediction = test(
            image=frame,
            model_dir=model_dir,
            device_id=device_id
        )

        # --- Calculate Scores ---
        # prediction shape is usually (1, 3). Index 1 is Real.
        # We assume the sum of all classes is the total "weight"
        total_score = np.sum(prediction[0])

        # Calculate 'Live' score (Index 1)
        live_score = prediction[0][1] / total_score

        # 'Spoof' is everything else (1.0 - Live)
        spoof_score = 1.0 - live_score

        # Format the string: "[0.10, 0.90]"
        score_text = f"[{live_score:.2f}, {spoof_score:.2f}]"

        # --- Draw on Frame ---
        if label == 1:
            # Green for Live
            color = (0, 255, 0)
            result_text = "Live"
        else:
            # Red for Spoof
            color = (0, 0, 255)
            result_text = "Spoof"

        # 1. Draw "Live" or "Spoof"
        cv2.putText(frame, result_text, (30, 50), cv2.FONT_HERSHEY_SIMPLEX,
                    1.5, color, 3)

        # 2. Draw the scores "Live, Spoof" title
        cv2.putText(frame, "Live, Spoof", (30, 100), cv2.FONT_HERSHEY_SIMPLEX,
                    0.8, (255, 255, 255), 2)

        # 3. Draw the actual numbers [0.x, 0.y]
        cv2.putText(frame, score_text, (30, 140), cv2.FONT_HERSHEY_SIMPLEX,
                    0.8, (255, 255, 255), 2)

        cv2.imshow('Anti-Spoofing Detection', frame)

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

