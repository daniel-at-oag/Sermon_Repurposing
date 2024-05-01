#!/usr/bin/env python3

import sys
import os
import time
import json
import assemblyai as aai
from openai import OpenAI

# API keys
aai.settings.api_key = '2f17b010f29849e7af8f0447a932b956'
openai_client = OpenAI(api_key='sk-proj-aRMe9sd0xZ3f89nZkMcgT3BlbkFJCUKu1KabPoJ46Nl92jHL')

def load_test_transcript():
    with open('test_transcript.txt', 'r') as file:
        return file.read()

def load_prompt_sets():
    with open('prompt_sets.json', 'r') as file:
        return json.load(file)

prompt_sets = load_prompt_sets()

def choose_prompt_set():
    print("\nAvailable prompt sets:\n")
    for key, prompts in prompt_sets.items():
        print(f"{key}:")
        for prompt in prompts:
            print(f"  - {prompt}")
        print("\n")  # Adds an extra line for better separation
    choice = input("Enter the prompt set to use (e.g., 'youth'): ")
    return prompt_sets.get(choice, prompt_sets['test'])  # Default to 'test' if an invalid choice is made

def notify(title, text):
    print("\n========== Notification ==========")
    print("Title:", title)
    print("Message:", text)
    print("==================================\n")

def process_transcript(transcript_text, file_path, prompts):
    output_file = os.path.splitext(file_path)[0] + "_output.txt"
    with open(output_file, 'w') as f:
        for prompt in prompts:
            chat_completion = openai_client.chat.completions.create(
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": transcript_text + "\n\n" + prompt}
                ],
                model="gpt-3.5-turbo"
            )
            f.write(f"Prompt: {prompt}\n")
            f.write("Response:\n")
            for choice in chat_completion.choices:
                response_text = choice.message.content + "\n\n"
                f.write(response_text)
            f.write("\n" + "="*40 + "\n\n")
    notify("Process Complete", "Output saved to " + output_file)

def process_file(file_path, prompts):
    if file_path == "test":
        notify("Test Mode", "Using predetermined test transcript.")
        transcript_text = load_test_transcript()
        process_transcript(transcript_text, "test_transcript", prompts)
    else:
        notify("Process Starting", "Uploading and processing new audio file.")
        try:
            transcriber = aai.Transcriber()
            transcript = transcriber.transcribe(file_path)

            while transcript.status == aai.TranscriptStatus.processing:
                time.sleep(5)
                transcript = transcriber.get_transcript(transcript.id)

            if transcript.status == aai.TranscriptStatus.completed:
                transcript_text = transcript.text
                transcript_file = os.path.splitext(file_path)[0] + "_transcript.txt"
                with open(transcript_file, 'w') as tf:
                    tf.write(transcript_text)
                notify("Transcription Complete", "Transcript saved to " + transcript_file + " and processing with ChatGPT.")
                process_transcript(transcript_text, file_path, prompts)
            else:
                notify("Error", "Failed to complete transcription.")
        except Exception as e:
            print(f"An error occurred: {e}")
            notify("Error", str(e))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python Sermon_Repurposing.py <path_to_mp3_file_or_url>")
    else:
        chosen_prompts = choose_prompt_set()
        process_file(sys.argv[1], chosen_prompts)
