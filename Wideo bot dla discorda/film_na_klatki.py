#Autor: NPCat (www.youtube.com/channel/UCFf2azJHYACCUIrt-a0LP2g)
#Zmodyfikował i dodał polskie komentarze: White Terraria (www.youtube.com/channel/UC2bVJ-dHcpOA1P5FWKkjzZg)

import cv2 
  
def FrameCapture(path): 
    
    vidObj = cv2.VideoCapture(path) 
    
    count = 0
    
    success = 1
  
    while success: 

        success, image = vidObj.read() 
  
        cv2.imwrite("frame%d.jpg" % count, image)
  
        count += 1
  
if __name__ == '__main__': 

    FrameCapture("film.mp4") #Nazwa filmu umieszczonego w głównym folderze 
