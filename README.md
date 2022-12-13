# commentractor
Python script to extract comments from a url or a file containing multiple urls

## How to use
### Executable File
- Compatible with Windows, Linux and MacOS. Downlaod the zip, extract it and use the commentractor.
### Python Script
- Download the `commentractor.py` and `requirements.txt`.
- Install the requirements with `pip -r requirements.txt`
### Run the script 
  - With a single url: `python3 commentractor.py -u https://en.m.wikipedia.org/wiki/Extractor`
  - With a file containing multiple urls: `python3 commentractor.py -f urls.txt`
  - With a single url and custom output: `python3 commentractor.py -u https://en.m.wikipedia.org/wiki/Extractor -o wiki.txt`

```sh
A URL to scan for comments or a file containing multiple urls is required.
Usage: commentractor.py [OPTIONS]

Options:
  -u, --url TEXT     Url to scan for comments.
  -f, --file TEXT    File containing URLs to scan for comments.
  -o, --output TEXT  Output location.
  --help             Show this message and exit.
```
