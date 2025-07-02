class Head:
    def __init__(self,):
        self.eyes= 2
        self.nose = 1
        self.mouth = 1
        self.ears = 2
class Torso:
    def __init__(self,right_arm, left_arm, right_leg, left_leg, head):
        self.rigt_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg
        self.head = head
class Arm:
    def __init__(self, hand):
        self.hand = hand
class Hand:
    def __init__(self):
        self.fingers = 5
class Leg:
    def __init__(self, feet):
        self.feet = feet
class Feet:
    def __init__(self,):
        self.fingers = 5
class Human:
    def __init__(self, torso):
        self.torso = torso


right_hand = Hand()
left_hand = Hand()
right_arm = Arm(right_hand)
left_arm = Arm(left_hand)
rigth_feet = Feet()
left__feet = Feet()
right_leg = Leg(rigth_feet)
left_leg = Leg(left__feet)
head= Head()
torso = Torso (right_arm, left_arm, right_leg, left_leg, head)
human= Human(torso)