# Binface: macOS Trash Recovery Tool

Binface is a macOS tool designed to recover items from the Trash by copying them to a designated folder. This tool is particularly useful for incident response and digital forensics, allowing quick retrieval of recently deleted files and directories.

## Features
- Recovers both files and directories (including .app bundles) from the macOS Trash
- Uses AppleScript to interact with Finder
- Provides detailed logging for audit trails
- Non-destructive: copies items instead of moving them

## Requirements
- macOS (tested on macOS 10.15 and later)
- Python 3.6 or higher

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/generalplantain/binface
    cd binface
    ```

## Usage
1. Run the script:
    ```bash
    python3 binface.py
    ```
   By default, recovered items will be saved to `~/Documents/RecoveredItems`. To change this, modify the `recovery_destination` variable in the script.

## Customization
To change the recovery destination:
1. Open `binface.py` in a text editor.
2. Locate the following line near the bottom of the file:
    ```python
    recovery_destination = os.path.expanduser("~/Documents/RecoveredItems")
    ```
3. Change `"~/Documents/RecoveredItems"` to your desired path.

## Logging
The script logs its actions to the console. Set the logging level in the script to adjust verbosity.

## Planned Future Updates
- **Directory and Apps Recovery**: Allow users to recover directories and applications 
