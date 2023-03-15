import argparse
import random
import time
from inputs import devices
import speech_recognition as sr

from pythonosc import udp_client


mic = sr.Microphone(device_index=8)
r = sr.Recognizer()
print("Speak Now")

with mic as source:
  audio = r.listen(source)

output = r.recognize_google(audio)


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip", default="127.0.0.1",
      help="The ip of the OSC server")
  parser.add_argument("--port", type=int, default=9000,
      help="The port the OSC server is listening on")
  args = parser.parse_args()

  client = udp_client.SimpleUDPClient(args.ip, args.port)

client.send_message("/chatbox/input", f"{output}")
