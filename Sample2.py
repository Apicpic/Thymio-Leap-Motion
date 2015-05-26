import sys
src_dir='/Users/alice/Documents/Polytech/Projet/LeapDeveloperKit_2.2.2+24469_mac/LeapSDK/lib'
sys.path.insert(0, src_dir)

import Leap

from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

class SampleListener(Leap.Listener):

    def on_connect(self, controller):
        print ("Connected")
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE)


    def on_frame(self, controller):
       frame = controller.frame()

#      print "Frame id: %d, timestamp: %d, hands: %d, fingers: %d, tools: %d, gestures: %d" % (frame.id, frame.timestamp, len(frame.hands), len(frame.fingers), len(frame.tools), len(frame.gestures()))
       if frame.hands:
           hand = frame.hands[0]
           position_X = hand.palm_position[0]
           position_Y = hand.palm_position[1]
           position_Z = hand.palm_position[2]
           self.position(position_X, position_Y, position_Z)
       else:
           self.rien()

    def Definir_position(self, position):
        self.position=position
    def Definir_rien(self, rien):
        self.rien=rien

class Leap_position:
    def __init__(self, position, rien):
        self.listener = SampleListener()
        self.listener.Definir_position(position)
        self.listener.Definir_rien(rien)
        self.controller = Leap.Controller()
        self.controller.add_listener(self.listener)


    def __del__(self):
        self.controller.remove_listener(self.listener)



def main():
    listener = SampleListener()
    controller = Leap.Controller()
    controller.add_listener(listener)
    # Keep this process running until Enter is pressed
    print ("Press Enter to quit...")
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)

if __name__ == "__main__":
    main()
