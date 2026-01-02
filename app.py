#Code snippet
import os 
import tempfile
from pathlib import Path
import streamlit as st
from dotenv import load_dotenv
import openai

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

st.set_page_config(page_title="Speech to Text App - Whisper", page_icon=":microphone:", layout="centered")


st.title("Speech to Text App using OpenAI Whisper")
st.write("Record your voice -- Transribe using Open AI API")

st.markdown("_____")
st.header("Record Audio")


audio_file = st.audio_input("click to record")

if audio_file:
    st.audio(audio_file,format="audio/wav")

    audio_bytes = audio_file.read()

    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    tmp.write(audio_bytes)
    tmp.flush()
    audio_path = Path(tmp.name)

    st.write(f"Temp audio file created : {audio_path.name}")

    if st.button("Transcribe Audio"):

        with st.spinner("Transcribing..."):
            try:
            with open(audio_path, "rb") as f:
                response = openai.Audio.transcribe(model = "whisper-1", file = f)
                transcript = None

                if isinstance(response, dict):
                    transcript = response.get("text") or response.get("transcript")
                else:
                    transcript = getattr(response,'text',None)
                if not transcript:
                    st.error("Transcription failed. No text found in the response.")
                    st.write(response)
                else:
                    st.success("Transcription completed!")

                    st.subheader("Transcribed Text")
                    st.write(transcript)
                    st.caption(f"Word Count: {len(transcript.split())}")

                    if st.button("Save Transcript"):
                        Path("transcript.txt").write_text(transcript,encoding="utf-8")
                        st.success("Saved transcript.txt")
            except Exception as e:
                st.error("Error during transcription")
                st.exception(e)
                            

