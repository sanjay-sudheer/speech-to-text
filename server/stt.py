# `pip3 install assemblyai` (macOS)
# `pip install assemblyai` (Windows)

import assemblyai as aai
from flask import jsonify

def data():
    aai.settings.api_key = "97ad5eac2a1a4f6a8bcd363bd712808e"
    transcriber = aai.Transcriber()

    transcript = transcriber.transcribe("https://storage.googleapis.com/aai-web-samples/espn-bears.m4a")
    # transcript = transcriber.transcribe("./my-local-audio-file.wav")

    print(transcript.text)
    return jsonify({
        'message': transcript.text
    })
