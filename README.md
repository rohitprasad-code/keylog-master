# keylog-master

keylogMaster is a Python script that captures key presses and releases, providing a simple way to log keyboard activity. It uses the pynput library to record key events and stores the logged data in a file. Customize the script according to your needs and use it responsibly for monitoring or research purposes.

## Installation

1. Clone the repository.

```bash
git clone https://github.com/rohitprasad-code/keylog-master.git && cd keylog-master
```

2. Install the environment.

```bash
conda create -n keylog python=3.8 -y
conda activate keylog
```

3. Install the dependencies.

```bash
pip install -r requirements.txt
```

4. Run the script.

```bash
python keylog.py
```

## Usage

Run the script using Python 3.8 or higher. The script will start logging key presses and releases. Press the ESC key to stop logging and exit the script. The logged data will be stored in a file named `keylog.txt` in the same directory as the script.

## License

[BSD 2-Clause License]