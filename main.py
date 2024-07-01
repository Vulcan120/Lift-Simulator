class lift():
  def __init__(self,CurrentFloor,Capacity,InOperation):
    self.CurrentFloor = CurrentFloor
    self.Capacity = Capacity
    self.InOperation = True

  def GetFloor(self):
    print(self.CurrentFloor)
  
  def MoveFloor(self,newFloor):
    self.CurrentFloor = newFloor

  def elevator():
    if lift1dist < lift2dist:
      if lift1dist < lift3dist:
        Lift1.MoveFloor(floorOn)
        print("Moving Lift 1...")
      else:
        Lift3.MoveFloor(floorOn)
        print("Moving Lift 3...")
    else:
      if lift2dist < lift3dist:
        Lift2.MoveFloor(floorOn)
        print("Moving Lift 2...")
      else:
        Lift3.MoveFloor(floorOn)
        print("Moving Lift 3...")


Lift1 = lift(1,5,True)
Lift2 = lift(5,5,True)
Lift3 = lift(10,15,True)

floorOn = int(input("What floor are you on?: ")) #9
lift1dist = abs(Lift1.CurrentFloor - floorOn) #8
lift2dist = abs(Lift2.CurrentFloor - floorOn) #4
lift3dist = abs(Lift3.CurrentFloor - floorOn) #1

lift.elevator()
