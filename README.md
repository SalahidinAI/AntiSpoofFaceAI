Anti-Spoof Face Attendance System
A real-time face recognition and attendance system with built-in Liveness Detection to prevent spoofing attacks (e.g., photos or video replays). This project is based on the tutorials by Computer Vision Engineer and the Silent-Face-Anti-Spoofing library.

🌟 Features
Real-time Anti-Spoofing: Continuous classification of "Live" vs "Spoof" faces directly in the video feed.

Probability Scores: Displays live/spoof confidence scores (e.g., [0.95, 0.05]) for transparency.

Face Recognition: Identifies registered users using 128-d face embeddings.

Keyboard-Driven Commands:

1: Login - Verifies liveness and logs "In" time for recognized users.

2: Logout - Verifies liveness and logs "Out" time.

3: Register - Captures a face and registers a new user via console input.

4: Delete - Removes a user from the database after liveness verification.

q: Quit - Safely closes the application.

🛠 Tech Stack
Python 3.8: Required for compatibility with older dlib and numpy versions.

OpenCV: For video processing and GUI overlays.

Face_recognition: Dlib-based library for facial feature extraction.

Silent-Face-Anti-Spoofing: A lightweight anti-spoofing model based on MiniVision.

🚀 Installation & Setup
1. Environment Requirements
It is highly recommended to use Python 3.8.x. If you are on a newer version, use pyenv to manage your versions.

Bash

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate

# Install core dependencies
pip install "numpy<2" 
pip install -r requirements.txt
pip install git+https://github.com/ageitgey/face_recognition_models
2. Silent-Face-Anti-Spoofing Setup
Clone the engine into the face-attendance-system directory:

Bash

git clone https://github.com/computervisioneng/Silent-Face-Anti-Spoofing.git
pip install -r face-attendance-system/requirements.txt
pip install -r face-attendance-system/Silent-Face-Anti-Spoofing/requirements.txt

if you use windows os then also 

Bash

pip install -r face-attendance-system/requirements.txt

3. Critical Fixes Applied
Model Path Fix: Corrected the typo in anti_spoof_predict.py from Widerface-RatinaFace to Widerface-RetinaFace.

NumPy Compatibility: Downgraded to numpy<2 to avoid _ARRAY_API import errors.

Path Calibration: Updated model_dir in main.py to match the local macOS directory structure.

📂 Project Structure
main.py: The entry point with the OpenCV loop and keyboard logic.

util.py: Helper functions for face recognition and GUI elements.

db/: Directory containing .pickle files of registered users.

log.txt: Attendance logs (Name, Timestamp, In/Out status).

📖 Usage
Run the application from your terminal:

Bash

python main.py
Wait for the camera window to open. The system will immediately begin scoring your face for liveness. Use keys 1, 2, 3, or 4 to interact with the database.

⚖️ License
This project is licensed under the MIT License.

🙏 Acknowledgments
Computer Vision Engineer for the base attendance system.

MiniVision for the Silent-Face-Anti-Spoofing models.