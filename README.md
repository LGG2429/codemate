# Codemate

I'm learning Python, how LLms work, and basic web development - by building a coding assistant from scratch, in public, starting from zero coding experience. ( Actually worked and tinkered with hardware for awhile when I was programming lidar sensors 'I have some experience xd')
This repo is my learning log as much as it's an app. Each Commit is a step in that process, not a polished release.

## What this is

A personal coding assistant that runs a free, open-source AI model (qwen3 8B) entirely on my own laptop, and eventually wraps it in a simple web page where I can ask coding questions and get answers with explanations.

## Files

- `llm_call.py` — the first working piece: a Python script that sends a
  prompt to a locally running model and prints the response. This is the
  core request/response loop everything else builds on.
  *(more files will be added and described here as the project grows)*

## Running this yourself

1. Clone this repo and move into it:
git clone <https://github.com/YOUR-USERNAME/codemate.git>
cd codemate

2. Install [Ollama](https://ollama.com) — a free tool that runs open-source
   AI models locally on your machine, no cloud, no API key.
3. Download the model this project uses (this pulls several GB of model
   files onto your machine — they aren't stored in this repo):
   ollama pull qwen3:8b
4. Install this project's one Python dependency (a library the code
   needs that isn't built into Python): pip install requests
5. Run the script : python llm_call.py
