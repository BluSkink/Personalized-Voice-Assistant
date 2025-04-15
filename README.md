Voice Assistant
A Python-based voice assistant that listens for commands, understands natural language, and performs tasks like checking the time, weather, telling jokes, and more.

Features
Wake-word activation: “Hey Assistant”

Voice-to-text command recognition

Natural language command processing

Perform the following tasks:

Tell the current time

Search the web

Get current weather info

Tell a joke

Set a timer

Requirements
Before running the project, ensure you have the following Python packages installed:

Install the necessary Python dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Install additional libraries for microphone support:

bash
Copy
Edit
pip install pipwin
pipwin install pyaudio
Install pyttsx3 dependencies for text-to-speech (TTS) functionality (this will help with the assistant’s spoken responses):

bash
Copy
Edit
pip install pyttsx3
Install pywin32 to resolve any Windows-specific issues (if needed):

bash
Copy
Edit
pip install pywin32
Weather API Setup
Sign up at OpenWeatherMap and get your API key.

Add the API key to config.py:

python
Copy
Edit
OPENWEATHER_API_KEY = "your_api_key_here"
How to Run
Ensure you have all dependencies installed as mentioned above.

Run the main script:

bash
Copy
Edit
python main.py
Say “Hey Assistant” followed by a command, such as:

“Hey Assistant, what time is it?”

“Hey Assistant, search for Python tutorials”

“Hey Assistant, tell me a joke”

“Hey Assistant, what’s the weather like?”

“Hey Assistant, set a timer for 10 seconds”

Future Ideas
Add GUI with text feedback

Continuous background listening with threading or VAD (Voice Activity Detection)

More natural language understanding (e.g., using spaCy or transformers)

Add new commands (e.g., control media, send emails)
