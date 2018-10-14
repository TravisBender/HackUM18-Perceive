import socket

import sys
import time
import ovr

ovr.initialize(None)
session, luid = ovr.create()
hmdDesc = ovr.getHmdDesc(session)
print(hmdDesc.ProductName)



TCP_IP = '169.254.33.178' #put the ip of the server here (machine running this code) or "169.254.233.235"
TCP_PORT = 5005
BUFFER_SIZE = 1024 # Set to 20 for fast response time, otherwise 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((TCP_IP, TCP_PORT))
sock.listen(1)

conn, addr = sock.accept()
print('Connection address:', addr)
while 1:
# Query the HMD for the current tracking state.
    ts  = ovr.getTrackingState(session, ovr.getTimeInSeconds(), True)
    #if ts.StatusFlags & (ovr.Status_OrientationTracked | ovr.Status_PositionTracked):
    pose = ts.HeadPose
    #print(pose.ThePose.Orientation.x) #ovr.Quatf = Orientation, ovr.Vector3f = Position
    #print(pose)
    #nextupdown = pose.ThePose.Orientation.z
    #nextleftright = pose.ThePose.Orientation.y
    data = (pose.ThePose.Orientation.y, pose.ThePose.Orientation.z)
    #print(nextupdown)
    #print(nextleftright)
    print("Y Orientation: ", data[0])
    print("Z Orientation: ", data[1])
    for x in range(len(data)):
        if 'e' in str(data[x]):
            data[x] = 0.04
            
    data = b"%s,%s," % (str(data[0]).encode(),str(data[1]).encode())
    print("dada", data)
    sys.stdout.flush()
    #time.sleep(0.100)
    #print("received data:", data)
    conn.send(data)  # echo
conn.close()

ovr.destroy(session)
ovr.shutdown()