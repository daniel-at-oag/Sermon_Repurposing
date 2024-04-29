#!/usr/bin/env python3

import sys
import os
import time
import assemblyai as aai
from openai import OpenAI

# Replace with your actual API keys
aai.settings.api_key = '2f17b010f29849e7af8f0447a932b956'
openai_client = OpenAI(api_key='sk-proj-aRMe9sd0xZ3f89nZkMcgT3BlbkFJCUKu1KabPoJ46Nl92jHL')

prompt_sets = {
    'youth': ["Please give me a 150 word summary of the sermon for the parents of the students that heard this sermon. The summary should be in the first person point of view, from Pastor Amanda.", "Please give me five dinner table discussion guides for the parents of the teens that heard this sermon.", "Please give me an outline of the sermon, using the following as the main points: Starter, Message, Dig Deeper, Application, Conclusion.", "Please give me a one sentence summary of the sermon from the first person point of view of Pastor Amanda.", "I want to send an email to the parents of the teens who heard this sermon. Please give me an email with a friendly and brief greeting, a brief summary of the sermon, and 3 family action steps. Finally, give me a brief closing that includes some encouragement for the parents."],
    'set1': ["This is an empty set."],
    'set2': ["Extract actionable items.", "Identify dates or deadlines."]
}

def choose_prompt_set():
    print("\nAvailable prompt sets:\n")
    for key, prompts in prompt_sets.items():
        print(f"{key}:")
        for prompt in prompts:
            print(f"  - {prompt}")
        print("\n")  # Adds an extra line for better separation
    choice = input("Enter the prompt set to use (e.g., 'set1'): ")
    return prompt_sets.get(choice, prompt_sets['set1'])  # Default to 'set1' if an invalid choice is made

def notify(title, text):
    print("\n========== Notification ==========")
    print("Title:", title)
    print("Message:", text)
    print("==================================\n")

def process_file(file_path, prompts):
    notify("Process Starting", "Uploading and processing new audio file.")
    try:
        transcriber = aai.Transcriber()
        transcript = transcriber.transcribe(file_path)

        while transcript.status == aai.TranscriptStatus.processing:
            time.sleep(5)
            transcript = transcriber.get_transcript(transcript.id)

        if transcript.status == aai.TranscriptStatus.completed:
            transcript_text = transcript.text
            notify("Transcription Complete", "Processing transcript with ChatGPT.")
            
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
                    for choice in chat_completion.choices:
                        response_text = f"Response for '{prompt}':\n{choice.message.content}\n\n"
                        print(response_text)
                        f.write(response_text)

            notify("Process Complete", "Output saved to " + output_file)
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
