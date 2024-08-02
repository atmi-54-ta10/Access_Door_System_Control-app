# Access Door System Control (Raspberry Pi)

## Overview
This repository contains the control application for the Access Door System using Python, designed to run on a Raspberry Pi, communicates with the server for real-time operations.

## Features
- Real-time control of door locks and indicators via GPIO pins
- Secure access control with real-time updates

## Setup and Installation

### Prerequisites
- Raspberry Pi with Raspbian OS installed
- Python 3.x installed on the Raspberry Pi
- `pip` package manager

### Installation Steps

1. **Clone the repository:**
    ```sh
    git clone https://github.com/atmi-54-ta10/Access_Door_System_Control-rasp5.git
    cd Access_Door_System_Control-rasp5
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies with copy command line from requirements.txt:**

4. **Configure environment variables:**
    - manage the uri.py file

### Running the Scripts
    ```sh
    sudo /path/to/venv/bin/python3 /path/to/app/main.py
    ```

### Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

### License
This project is licensed under the MIT License.
