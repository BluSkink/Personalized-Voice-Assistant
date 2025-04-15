A Python-based voice assistant that listens for commands, understands natural language, and performs tasks like checking the time, weather, telling jokes, and more.

##Features

- Wake-word activation: “Hey Assistant”
- Voice-to-text command recognition
- Natural language command processing
- Perform the following tasks:
  -  Tell the current time
  -  Search the web
  -  Get current weather info
  -  Tell a joke
  -  Set a timer

## Requirements

Install dependencies with:

bash
pip install -r requirements.txt


Additional setup for microphone support (if needed):

bash
pip install pipwin
pipwin install pyaudio


## Weather API Setup

1. Sign up at [OpenWeatherMap](https://openweathermap.org/api)
2. Get your API key
3. Add it to config.py:
python
OPENWEATHER_API_KEY = "your_api_key_here"


## How to Run

bash
python main.py


Say “Hey Assistant” followed by a command, such as:
- “Hey Assistant, what time is it?”
- “Hey Assistant, search for Python tutorials”
- “Hey Assistant, tell me a joke”
- “Hey Assistant, what’s the weather like?”
- “Hey Assistant, set a timer for 10 seconds”


## Future Ideas

- Add GUI with text feedback
- Continuous background listening with threading or VAD
- More natural language understanding (e.g., using spaCy or transformers)
- Add new commands (e.g., control media, send emails)
