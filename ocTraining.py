'''
Created on Oct 13, 2018

@author: maddo
'''

import sys
import time
import ovr

ovr.initialize(None)
session, luid = ovr.create()
hmdDesc = ovr.getHmdDesc(session)
print(hmdDesc.ProductName)
ts  = ovr.getTrackingState(session, ovr.getTimeInSeconds(), True)
if ts.StatusFlags & (ovr.Status_OrientationTracked | ovr.Status_PositionTracked):
    pose = ts.HeadPose
for t in range(100):
    # Query the HMD for the current tracking state.
    ts  = ovr.getTrackingState(session, ovr.getTimeInSeconds(), True)
    if ts.StatusFlags & (ovr.Status_OrientationTracked | ovr.Status_PositionTracked):
        pose = ts.HeadPose
        #print(pose.ThePose.Orientation.x) #ovr.Quatf = Orientation, ovr.Vector3f = Position
        #print(pose)
        nextupdown = pose.ThePose.Orientation.z
        nextleftright = pose.ThePose.Orientation.y
        print(nextupdown)
        print(nextleftright)
        sys.stdout.flush()
    time.sleep(0.100)
ovr.destroy(session)
ovr.shutdown()