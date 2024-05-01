# Sermon Repurposing Script
## Overview

The Sermon_Repurposing.py script is designed to automate the process of transcribing and repurposing sermons. It uses the AssemblyAI API for transcription and the OpenAI API to generate summaries, discussion guides, and other related content based on the sermon's text. The script supports a test mode using a predefined transcript, making it suitable for both production use and development/testing purposes.
Features

- **Audio Transcription:** Converts sermon audio files to text using AssemblyAI.
- **Content Generation:** Uses OpenAI's GPT model to generate useful content from the transcribed text.
- **Modular Prompt Configuration:** Utilizes external JSON files for prompt settings, allowing easy customization without modifying the core script.
- **Test Mode:** Includes a test mode that bypasses audio transcription and uses a predefined transcript for quick testing.
- **Environment Variables:** Leverages environment variables for API key management, enhancing security and flexibility.

## Prerequisites

- Python 3.6 or higher
- assemblyai Python package
- openai Python package
- Valid API keys for AssemblyAI and OpenAI

## Setup

- **Clone the Repository:**
    git clone https://github.com/yourgithubusername/sermon-repurposing.git  
    cd sermon-repurposing

- **Install Dependencies:**
    pip install -r requirements.txt

- **Set Environment Variables:**
    Add the following lines to your .zshrc file:  
    export ASSEMBLYAI_API_KEY='your_assemblyai_api_key_here'  
    export OPENAI_API_KEY='your_openai_api_key_here'  
    Replace your_assemblyai_api_key_here and your_openai_api_key_here with your actual API keys.
    After updating your .zshrc, run:
    source ~/.zshrc

- **Configuration Files:**
    Ensure that prompt_sets.json and test_transcript.txt are configured according to your needs.

## Usage

To run the script, use the following command:  
python Sermon_Repurposing.py <path_to_mp3_file_or_url>  
To run the script in test mode, use:  
python Sermon_Repurposing.py test  

## Output

The script outputs a text file containing the processed results, formatted for clarity and ease of reading. Each prompt's response is clearly separated in the text file.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
