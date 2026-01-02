# WhisperWave-Speech-to-Text-with-OpenAI-Whisper-Streamlit
WhisperWave is a simple and interactive Speech-to-Text web application built using Streamlit and OpenAI Whisper. Users can record audio directly from their browser, transcribe it into text using OpenAI’s Whisper model, and optionally save the transcript to a file.

---

## 🚀 Features

- 🎤 Record audio directly from the browser
- 🤖 Transcribe speech using OpenAI Whisper
- 📄 Display transcribed text instantly
- 💾 Save transcription as a `.txt` file
- 🐳 Docker support for easy deployment

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **OpenAI Whisper API**
- **Docker**
- **python-dotenv**

---

## 📂 Project Structure
├── app.py

├── requirements.txt

├── Dockerfile

├── README.md

└── .env


---

## 🔐 Environment Variables

Create a `.env` file in the project root:

env

- OPENAI_API_KEY=your_openai_api_key_here

▶️ Running the App Locally

1️⃣ Clone the repository

git clone https://github.com/your-username/whisperwave.git

cd whisperwave

2️⃣ Install dependencies

pip install -r requirements.txt

3️⃣ Run the app

streamlit run app.py


The app will be available at:

http://localhost:8501

🐳 Run with Docker

Build the image

docker build -t whisperwave .

Run the container

docker run -p 8501:8501 --env-file .env whisperwave

📸 How It Works

1.Record audio using the microphone

2.Click Transcribe Audio

3.Whisper converts speech → text

4.View or save the transcription

🧠 OpenAI Model Used

Model: whisper-1

Purpose: Automatic Speech Recognition (ASR)

⚠️ Notes

Requires an active OpenAI API key

Audio is temporarily stored during transcription

Best performance with clear audio input

📌 Future Improvements

Support for multiple languages

Audio file upload option

Timestamped transcription

UI enhancements

🤝 Contributing

Contributions are welcome!

Feel free to open issues or submit pull requests.

📜 License

This project is licensed under the MIT License.

⭐ Acknowledgements

OpenAI Whisper

Streamlit Community

<------------------------------------------------------------------------------------->
<------------------------------------------------------------------------------------->

Authors:

- **Name : MD Karaamathullah sheriff| Email : mdkaraamathullahsheriff@gmail.com** 
