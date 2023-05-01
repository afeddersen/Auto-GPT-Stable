# Auto-GPT-Stable

Stable clone of [Auto-GPT](https://github.com/Significant-Gravitas/Auto-GPT)

## Setup

Create a virtual environment.

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies.

```bash
pip3 install -r requirements.txt
```

Rename `.env.template` to `.env` and populate your environment variables.

The OpenAI API Key is the only requirement.  The rest of the services are optional.

## Run

Start Auto-GPT.

```bash
python3 scripts/main.py
```

### Pre-Load Data

**Note:** You can preload data _after_ starting Auto-GPT.  I'm using the free trial of Pinecone.

* `auto_gpt_workspace/seed_data/...` is the place to add any data that you want to preload.  
* Run this command to pre-load: `python3 scripts/data_ingestion.py --dir auto_gpt_workspace/seed_data --init --overlap 200 --max_length 1000`

## Bonus

If you have the Eleven Labs API key the Auto-GPT use text-to-voice to share the results of each stage.  Use `python3 scripts/main.py --speak`




