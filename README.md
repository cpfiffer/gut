# gut - git with a gut feeling

`gut` is a sarcastic and somewhat critical command-line interface (CLI) tool that provides a humorous twist on the traditional `git status` command. It uses the [groq](https://groq.com/) API to generate witty and snarky comments about your Git repository's state.

If you like this, consider sponsoring me or sending me a tip on [GitHub Sponsors](https://github.com/sponsors/cpfiffer).

## Installation

To install `gut`, follow these steps:

1. Clone this repository
2. Navigate to the project directory
3. Run `pip install -e .`

This will install `gut` and its dependencies.

## Requirements

- Python 3.6+
- A [groq API key](https://groq.com/)
- click
- requests

For a complete list of dependencies, see `requirements.txt`.

## Configuration

Before using `gut`, you need to set up your [groq API key](https://groq.com/). You can do this in two ways:

1. Set an environment variable:
   ```
   export GROQ_API_KEY=your_api_key_here
   ```

2. Run `gut` for the first time, and it will prompt you to enter your API key. The key will be saved in `~/.gut_config` for future use. There's probably better ways to do this but honestly it's on you for not setting an environment variable in the first place.

## Usage

To use `gut`, simply run:

```
gut status
```

## Contributing

I guess submit whatever you want.
