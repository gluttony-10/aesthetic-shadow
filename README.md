# aesthetic-shadow

## Introduction

Aesthetic Shadow is a 1.1b parameters visual transformer designed to evaluate the quality of anime images. It accepts high-resolution 1024x1024 images as input and provides a prediction score that quantifies the aesthetic appeal of the artwork. Leveraging cutting-edge deep learning techniques, this model excels at discerning fine details, proportions, and overall visual coherence in anime illustrations.
Base url https://huggingface.co/shadowlilac/aesthetic-shadow

## Installation

Installing requires Python 3.10. You can download Python here https://www.python.org/.
Then follow these steps:

- Clone the repository `git clone https://github.com/gluttony-10/aesthetic-shadow.git`
- Navigate into the cloned directory `cd aesthetic-shadow`
- Set up a virtual environment `python -m venv venv`
- Activate the new venv:
    - Windows: `venv\scripts\activate`
    - Unix based systems: `source venv/bin/activate`
- Install the requirements `pip install -r requirements.txt`

## Updating

- Pull changes `git pull`
- Activate the venv `venv\scripts\activate`
- Re-Install the requirements `pip install -r requirements.txt `

## Usage

- Activate the venv `venv\scripts\activate`
- For single image `python inference.py --image text/test.jpg`
- For batch `python batch.py --path test --output outputs --threshold 0.5 --batch 8`
