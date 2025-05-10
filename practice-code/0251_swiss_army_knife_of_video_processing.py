# pip install vidgear

from vidgear.gears import CamGear


stream = CamGear(source='test_video.mp4').start()
frame = stream.read()

while frame is not None:
    # Process the frame
    frame = stream.read()

stream.stop()