#!/usr/bin/env python3

import sys
import os
import time
import assemblyai as aai
from openai import OpenAI

# API keys
aai.settings.api_key = '2f17b010f29849e7af8f0447a932b956'
openai_client = OpenAI(api_key='sk-proj-aRMe9sd0xZ3f89nZkMcgT3BlbkFJCUKu1KabPoJ46Nl92jHL')

# Predefined test transcript
test_transcript = "Alright, guys, so tonight we are finishing. We're not actually, I'm sorry, we're not finishing. We're continuing because we just tackled three of the fruit of the spirit so far. And tonight we're gonna tackle the next one. Can anybody take it? Okay, put it up there. All right. Faithfulness. All right. You just got so excited, Pastor Daniel. So tonight we are tackling faithfulness, okay? And that is the fourth fruit of the spirit that we're talking about so far. We talked about what self control, peace. Peace was last. Enjoy. So, self control, peace and joy are the three we talked about so far. Now we're on faithfulness. And of course, how many more do we have to go? Like two? Five. We have five more after tonight because there's nine total, right? Isn't there nine total? Right? There's nine total. This is number five. I'm sorry, this is number four. It means we got five more. So obviously next week we'll continue to the next one. Then, of course, we have club 612. We'll break it up a little bit and then we'll try to finish it in May before all the craziness in summer happens. How many of you, by the way, are ready for the summer? And ready. How many of you are ready for the summer contest? Is anybody ready for the summer contest? I don't know what I'm doing. I don't know. All right, so tonight we're gonna talk about faithfulness. Can anybody tell me what they think faithfulness means? All right, Kat, what does it mean to you? Being loyal? I like that. It's a good definition, Anna. Or is that the same thing you were gonna say? Okay. Having the faith of somebody. Okay. All right. Those are both great. Those are both great. So what we're gonna do is we're gonna talk about a couple things. And this is the first part is to get you guys kind of moving around a minute. So I'm going to ask a question, and if it applies to you, the question I have, then I want you to follow the instructions. Does that make sense? It's called if this, then that. Okay, so we're going to talk about faithfulness tonight. And this leads us into it. So it has a purpose, I promise. But the questions are going to be like, if this happens, if this applies to you, then do this. Does that make sense? All right, good job. So here we go. Let me help you. For instance, if you know someone who has a close friend, that's the if. Then I want you to stand up. If you know somebody who has a close friend? You know, somebody. I mean, so, Kayla, you don't know anybody but a close friend. I mean, you're in a room full of people. You don't know any of these people. All right, raise your hand real quick. Raise your hand and answer my question. This is the question I have. How do you think that person feels? Talk about the friend and mine, that they have a close friend. How do you think they feel? Amory? Amazing. They feel amazing. Loved. Amazing. Loved. Cat. Happy. Joyful. All right, you got the idea. All right, so stay standing. Here's the next thing. If you know somebody with a close knit family means they're really connected, really close. Like, they have a good group, good bond that I want you to say hello to the person next to you. If you know somebody who has a close knit family. Again, there's a lot of people in this room that probably. I mean, stags have a close knit family. Amory and them have a close knit family. I mean, anyhow, all right, real quick. Who wants to raise their hand? Maybe somebody who has an answer already. What are some ways that families show that they are close? What are some things? Seth? Yes, vacation is a great, great answer. Daniel, you haven't said anything yet. Family dinners. Absolutely. Caitlin? Family gatherings. Groups. Kat? They get along in public. That's great. Yes. Camilla? I'm sorry. They look out for each other. Absolutely. Anna? More happy around. They like being around their family. Right. All right, all right, here's the next if then that. Here we go. You ready? Listen up. If you know somebody who has a difficult family situation, then shout the name of your favorite dessert. So a few of you okay, so a few of you know people who have some difficult family situations. Right? Let me ask you this. How do you think that person feels with that situation? Just give me generic. Don't give me any details. Like, you know, poo. Poo. Yeah. Sad. Disappointed. Weary, probably. Oh. Oh, okay, that was really attacking. All right. All right, we have two more. Two more. Here we go. If you have ever. If you. Now, if you have ever felt connected to a so group, then I want you to share the name of your least favorite food with the person next to you. So if you have ever felt connected to a certain group, share your least favorite food to the person next to you. Yes. What? Kale. Oh, God. All right, here we go. Shh. So raise your hand. How does it feel to be connected to a group? How does it feel? Kaylin? Okay. Support. Right. Cat. Okay. Daniel. But if it's like a vineyard, then I'm like, okay. Anna. Ecstatic. Ecstatic. All right, anybody else? To feel connected to a group, how would you feel? Happy. Happy. Daniel, you had a serious answer. Fulfilling. That's a great answer. That's a great answer. All right, last one, huh? One more time. Comforting. Comforting. I thought she said about 40. I'm like, what about 40? Are you calling me? I'm old. I'm not even 40 yet. All right, last question. If you talk about you again, ever felt like you didn't belong somewhere, then I want you to whisper to the person next to you the name of your favorite place to go. Well, tell them that. So if you ever felt like you didn't belong, Wendy's okay. All right, true answers only. Here you go. Raise your hand. What was that like? To not feel like you didn't belong. And what have you learned from that experience, cat? That you can't fit. That you can't fit in everywhere. It's a great thing. Daniel. Okay. Absolutely. Seth, angry? A little bit hurt sometimes. Yeah. You want to fight, make. Oh, whatever. So you feel awkward. You feel, you know, disappointed. You feel embarrassed. All sorts of things, right? All right, y'all gonna have a seat. Y'all gonna have a seat. All right, here's the key about this whole illustration, all right? Belonging to a group, whether that group is, you know, like a church group or a group at school. Like, if you're in, like, the light, for instance, maybe you're all in band together or in drama together on a certain sport or something like that. When you belong to a group or you're in a relationship, like, it could be just a friendship. I'm not talking romantic, but being in a relationship, it's important. We are created to be relational beings. It really is."

prompt_sets = {
    'youth': ["Please give me a 150 word summary of the sermon for the parents of the students that heard this sermon. The summary should be in the first person point of view, from Pastor Amanda.", "Please give me five dinner table discussion guides for the parents of the teens that heard this sermon.", "Please give me an outline of the sermon, using the following as the main points: Starter, Message, Dig Deeper, Application, Conclusion.", "Please give me a one sentence summary of the sermon from the first person point of view of Pastor Amanda.", "I want to send an email to the parents of the teens who heard this sermon. Please give me an email with a friendly and brief greeting, a brief summary of the sermon, and 3 family action steps. Finally, give me a brief closing that includes some encouragement for the parents."],
    'set1': ["Please summarize this sermon."],
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
            for choice in chat_completion.choices:
                response_text = f"Response for '{prompt}':\n{choice.message.content}\n\n"
                print(response_text)
                f.write(response_text)
    notify("Process Complete", "Output saved to " + output_file)

def process_file(file_path, prompts):
    if file_path == "test":
        notify("Test Mode", "Using predetermined test transcript.")
        transcript_text = test_transcript
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
