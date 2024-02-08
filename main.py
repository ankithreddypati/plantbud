import boto3
import requests
from gpiozero import MCP3008  

# Amazon Polly setup
polly_client = boto3.client('polly',
                            aws_access_key_id='AWS_ACCESS_KEY_ID',
                            aws_secret_access_key='AWS_SECRET_ACCESS_KEY',
                            region_name='AWS_REGION')

def check_soil_moisture():
    adc = MCP3008(channel=0)  
    moisture_level = adc.value
    print(f"Moisture Level: {moisture_level}")
    return moisture_level

def generate_speech(text):
    response = polly_client.synthesize_speech(VoiceId='Joanna',
                                              OutputFormat='mp3',
                                              Text=text)
    file_url = 'path/to/speech.mp3'
    with open(file_url, 'wb') as file:
        file.write(response['AudioStream'].read())
    return file_url


def play_on_sonos(audio_url):
    print(f"Playing on Sonos: {audio_url}")

# Main logic
def monitor_plant():
    moisture_threshold = 0.3  
    moisture_level = check_soil_moisture()
    
    if moisture_level < moisture_threshold:
        print("Moisture level is low, generating alert...")
        audio_url = generate_speech("Your plant needs water.")
        play_on_sonos(audio_url)
    else:
        print("Plant is healthy.")

if __name__ == "__main__":
    monitor_plant()
