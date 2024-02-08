# plantbud

## Overview
This repository contains code for an advanced plant health monitoring system developed using a Raspberry Pi. The system utilizes soil moisture sensing to determine when a plant needs watering and integrates with Amazon Polly for vocal alerts. These alerts are played through a Sonos speaker using the Sonos Control API, providing an interactive and user-friendly way to manage plant care.

## Features
- **Soil Moisture Monitoring:** Automatically checks the soil's moisture level and determines when watering is needed.
- **Vocal Alerts:** Uses Amazon Polly to generate speech from text alerts, offering a natural interface for plant care instructions.
- **Sonos Speaker Integration:** Plays alerts through a Sonos speaker using the Sonos Control API, ensuring you receive timely notifications.

## Hardware Requirements
- Raspberry Pi (3B or newer recommended)
- Soil moisture sensor compatible with Raspberry Pi
- Raspberry Pi Camera Module (for future ML integration)
- Sonos speaker with network connectivity

## Software Requirements
- Python 3.x
- RPi.GPIO (for interacting with the GPIO pins on the Raspberry Pi)
- Boto3 (for Amazon Polly integration)
- Requests (for making HTTP requests to the Sonos Control API)

## Setup Instructions

### 1. Raspberry Pi Setup
Ensure your Raspberry Pi is set up with Raspberry Pi OS and connected to your local network. Instructions for initial setup and OS installation can be found at the [Raspberry Pi Documentation](https://www.raspberrypi.org/documentation/).

### 2. Sensor and Camera Module Installation
Connect your soil moisture sensor and Pi Camera to the Raspberry Pi. Test each component to ensure proper functionality.

### 3. Amazon Polly and Sonos API Configuration
- **Amazon Polly:** Set up an AWS account and obtain credentials (Access Key ID and Secret Access Key) for Amazon Polly. Configure Boto3 in your project to use these credentials.
- **Sonos Control API:** Register for a Sonos developer account, create an application to obtain the Client ID and Client Secret, and set up the Sonos Control API on your network.

### 4. Installing Required Libraries
Install the necessary Python libraries by running:
```bash
pip install RPi.GPIO boto3 requests
```

### 5. Running the Application
Clone this repository to your Raspberry Pi, navigate to the project directory, and run:
```bash
python3 monitor_plant.py
```

## Usage
Once started, the application will periodically check the soil moisture level. If the moisture level is below the predefined threshold, it will generate a vocal alert using Amazon Polly and play this alert through your Sonos speaker.

## Future Enhancements
- Integrate Raspberry Pi Camera Module for visual plant health monitoring using TensorFlow Lite.
- Implement OAuth for secure communication with the Sonos Control API.
- Expand the system to monitor multiple plants and speakers throughout the home.

## Contributing
Contributions to this project are welcome! Please fork the repository and submit a pull request with your enhancements or fixes.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to customize this README to fit your project's specific details, instructions, and progress.
