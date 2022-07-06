  
import PicoRobotics
import utime

board = PicoRobotics.KitronikPicoRobotics()
directions = ["f","r"]

while True:
    board.step(1,"f",200,20)
        #for direction in directions:
        #     for stepcount in range(200):
        #        board.step(1,direction,8)
                #board.step(2,direction,8)
        #utime.sleep_ms(1)#pause between motors 