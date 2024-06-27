import click
import requests
import os
import subprocess
import json

GROQ_API_KEY = os.environ.get('GROQ_API_KEY')
CONFIG_FILE = os.path.expanduser('~/.gut_config')

def load_api_key():
    global GROQ_API_KEY
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            GROQ_API_KEY = f.read().strip()
    return GROQ_API_KEY

def save_api_key(api_key):
    with open(CONFIG_FILE, 'w') as f:
        f.write(api_key)

def request_api_key():
    api_key = click.prompt('Please enter your GROQ API key', type=str)
    save_api_key(api_key)
    return api_key

def send_to_groq(git_output):
    with open('prompt.txt', 'r') as f:
        prompt = f.read().strip()
    
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "messages": [{"role": "user", "content": prompt + git_output}],
        "model": "llama3-8b-8192"
    }
    
    response = requests.post(url, headers=headers, json=data)
    return response.json()['choices'][0]['message']['content']

@click.group()
def cli():
    global GROQ_API_KEY
    GROQ_API_KEY = load_api_key()
    if not GROQ_API_KEY:
        GROQ_API_KEY = request_api_key()

@cli.command()
def status():
    git_output = subprocess.check_output(['git', 'status']).decode('utf-8')
    result = send_to_groq(git_output)
    click.echo(result)

if __name__ == '__main__':
    cli()