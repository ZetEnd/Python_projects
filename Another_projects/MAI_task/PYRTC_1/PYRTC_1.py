#from serial import Serial
from pyrtcm import RTCMReader

stream = open('C:\Users\ptimo\Downloads\1019.rtcm','rb')

rtr = RTCMReader(stream)

rtr1 = RTCMReader.parse(stream)

for (raw_data, parsed_data) in rtr1: print(parsed_data)
