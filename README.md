# Sermon Repurposing Script

## Overview
The `Sermon_Repurposing.py` script is designed to help repurpose sermons by transcribing audio files, processing the transcripts with AI-powered models to generate summaries, discussion guides, and other relevant content. It supports a test mode for development and debugging without the need for actual audio processing.

## Features
- **Audio Transcription**: Utilizes AssemblyAI to transcribe sermon audio files into text.
- **AI-Powered Text Generation**: Leverages OpenAI's ChatGPT model to generate various forms of content based on the transcribed text.
- **Multiple Prompt Sets**: Supports different sets of prompts for generating specific content types, which are stored in an external JSON file for easy modification.
- **Test Mode**: Includes a test mode that uses a predefined transcript instead of uploading a file, facilitating rapid testing and development.
- **Readable Output**: Formats the AI-generated content into an easy-to-read text file, clearly separating responses to different prompts.

## Usage
To use the script, simply run it with a path to an audio file, or the word 'test' to engage test mode:

```bash
python Sermon_Repurposing.py <path_to_mp3_file_or_url>
python Sermon_Repurposing.py test

## Configuration
Before running the script, ensure that you have updated the prompt_sets.json with your desired prompts. Also, verify that your API keys for AssemblyAI and OpenAI are set correctly within the script.
