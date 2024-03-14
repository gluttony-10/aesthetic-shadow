# aesthetic-shadow
## Introduction
Aesthetic Shadow is a 1.1b parameters visual transformer designed to evaluate the quality of anime images. It accepts high-resolution 1024x1024 images as input and provides a prediction score that quantifies the aesthetic appeal of the artwork. Leveraging cutting-edge deep learning techniques, this model excels at discerning fine details, proportions, and overall visual coherence in anime illustrations.
## Installation

Installing OneTrainer requires Python 3.10. You can download Python here https://www.python.org/downloads/windows/.
Then follow these steps:

Automatic installation

- Clone the repository `git clone https://github.com/Nerogar/OneTrainer.git`
- Run:
    - Windows: `install.bat`
    - Unix based systems: `install.sh`

Manual installation

- Clone the repository `git clone https://github.com/Nerogar/OneTrainer.git`
- Navigate into the cloned directory `cd OneTrainer`
- Set up a virtual environment `python -m venv venv`
- Activate the new venv:
    - Windows: `venv\scripts\activate`
    - Unix based systems: `source venv/bin/activate`
- Install the requirements `pip install -r requirements.txt`

In some linux distribution, you might need to install libGL, for instance on ubuntu you will need to run:
```
sudo apt-get update
sudo apt-get install libgl1
```

## Updating

Automatic update

- Run `update.bat` or `update.sh`

Manual update

- Pull changes `git pull`
- Activate the venv `venv\scripts\activate`
- Re-Install all requirements `pip install -r requirements.txt --force-reinstall`

