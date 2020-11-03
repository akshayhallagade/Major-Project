import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon, QPixmap, QImage
from PyQt5.uic import loadUi
import opr
import comm_ard
import random
import pickle

import cv2


class App(QWidget):

    def __init__(self):
        super().__init__()

        self.ui = loadUi('tracking.ui', self)    

        self.setMouseTracking(True)    
        self.manual_mode = False       
        self.LED_ON = True             
        self.CameraID = 0              

        self.rec = True                
        self.cap = cv2.VideoCapture(self.CameraID)  
        self.cap.set(3, 960)                        
        self.cap.set(4, 540)                        
        

        self.min_tilt = 22          
        self.current_tilt = 0       
        self.target_tilt = 90     

        self.min_pan = 80           
        self.max_pan = 100         
        self.current_pan = 80     
        self.target_pan = 90       

        self.roam_target_pan = 90
        self.roam_target_tilt = 90
        self.roam_pause = 40      
        self.roam_pause_count = self.roam_pause   


        self.is_connected = False    

        self.InvertPan = False       
        self.InvertTilt = False      

        self.face_detected = False     
        self.target_locked = False     
        self.max_target_distance = 40  
        self.max_empty_frame = 50      
        self.empty_frame_number = self.max_empty_frame   
        self.ard = comm_ard.ard_connect(self)     
        self.initUI()    )

    def initUI(self):     #UI related stuff
        self.setWindowTitle('LFK Tracker')              
        self.label = self.ui.label                      
        self.QuitButton = self.ui.QuitButton            
        self.PauseButton = self.ui.PauseButton          
        self.Pan_LCD = self.ui.Pan_LCD                  
        self.Tilt_LCD = self.ui.Tilt_LCD                
        self.Manual_checkbox = self.ui.Manual_checkbox  
        self.ConnectButton = self.ui.ConnectButton
        self.COMlineEdit = self.ui.COMlineEdit
        self.COMConnectLabel = self.ui.COMConnectLabel
        self.UpdateButton = self.ui.UpdateButton
        self.MinTiltlineEdit = self.ui.MinTiltlineEdit
        self.MaxTiltlineEdit = self.ui.MaxTiltlineEdit
        self.InvertTilt_checkbox = self.ui.InvertTilt_checkbox
        self.InvertTilt = self.InvertTilt_checkbox.isChecked()
        self.MinPanlineEdit = self.ui.MinPanlineEdit
        self.MaxPanlineEdit = self.ui.MaxPanlineEdit
        self.InvertPan_checkbox = self.ui.InvertPan_checkbox
        self.InvertPan = self.InvertPan_checkbox.isChecked()
        self.TiltSensivityEdit = self.ui.TiltSensivityEdit
        self.TiltSensivity = 1
        self.PanSensivityEdit = self.ui.PanSensivityEdit
        self.PanSensivity = 1
        self.LED_checkbox = self.ui.LED_checkbox
        self.CameraIDEdit = self.ui.CameraIDEdit

        self.QuitButton.clicked.connect(self.quit)               
        self.PauseButton.clicked.connect(self.toggle_recording)  
        self.Manual_checkbox.stateChanged.connect(self.set_manual_mode)  
        self.ConnectButton.clicked.connect(self.connect)
        self.UpdateButton.clicked.connect(self.update_angles)

        self.load_init_file()
        self.update_angles() 
        self.record()  

    def load_init_file(self):
        
        try:         
            with open('init.pkl', 'rb') as init_file:
                var = pickle.load(init_file)  
                self.COMlineEdit.setText(var[0])
                if(var[4]):
                    self.MinTiltlineEdit.setText(str(var[2]))
                    self.MaxTiltlineEdit.setText(str(var[1]))
                else:
                    self.MinTiltlineEdit.setText(str(var[1]))
                    self.MaxTiltlineEdit.setText(str(var[2]))
                self.TiltSensivityEdit.setText(str(var[3]))
                self.InvertTilt_checkbox.setChecked(var[4])
                if (var[8]):
                    self.MinPanlineEdit.setText(str(var[6]))
                    self.MaxPanlineEdit.setText(str(var[5]))
                else:
                    self.MinPanlineEdit.setText(str(var[5]))
                    self.MaxPanlineEdit.setText(str(var[6]))
                self.PanSensivityEdit.setText(str(var[7]))
                self.InvertPan_checkbox.setChecked(var[8])
                #self.CameraIDEdit.setText(str(var[9]))
                self.LED_checkbox.setChecked(var[10])
            print(var)
            
        except:
            pass

    def save_init_file(self):
        init_settings = [self.COMlineEdit.text(),
        self.min_tilt, self.max_tilt, self.TiltSensivity, self.InvertTilt,
        self.min_pan, self.max_pan, self.PanSensivity, self.InvertPan,
        self.CameraID, self.LED_ON]
        with open('init.pkl', 'wb') as init_file:
            pickle.dump(init_settings, init_file)


    def connect(self):    #set COM port from text box if arduino not already connected
        if(not self.is_connected):
            port = self.COMlineEdit.text()
            if (self.ard.connect(port)):    #set port label message
                self.COMConnectLabel.setText("..................... Connected to port : " + port + " ......................")
            else:
                self.COMConnectLabel.setText(".................... Cant connect to port : " + port + " .....................")

    def update_angles(self):  
        try:
            self.InvertTilt = self.InvertTilt_checkbox.isChecked()
            self.InvertPan = self.InvertPan_checkbox.isChecked()
            self.TiltSensivity = float(self.TiltSensivityEdit.text())
            self.PanSensivity = float(self.PanSensivityEdit.text())
            self.LED_ON = self.LED_checkbox.isChecked()

            self.cap.release()    
            self.CameraID = int(self.CameraIDEdit.text())
            self.cap = cv2.VideoCapture(self.CameraID)

            if(self.InvertPan):
                self.max_pan = int(self.MinPanlineEdit.text())
                self.min_pan = int(self.MaxPanlineEdit.text())
            else:
                self.min_pan = int(self.MinPanlineEdit.text())
                self.max_pan = int(self.MaxPanlineEdit.text())

            if(self.InvertTilt):
                self.max_tilt = int(self.MinTiltlineEdit.text())
                self.min_tilt = int(self.MaxTiltlineEdit.text())
            else:
                self.min_tilt = int(self.MinTiltlineEdit.text())
                self.max_tilt = int(self.MaxTiltlineEdit.text())

            self.save_init_file()
            print("values updated")
        except:
            print("can't update values")

    def mouseMoveEvent(self, event):

       

        if(self.manual_mode): 
            if(35<event.y()<470 and 70<event.x()<910):
                if(self.InvertTilt):  
                    self.target_tilt = opr.remap(event.y(), self.max_tilt, self.min_tilt, 470, 35)
                    
                else:
                    self.target_tilt =  opr.remap(event.y(), self.min_tilt, self.max_tilt, 35, 470)

                if (self.InvertPan):
                    self.target_pan = opr.remap(event.x(), self.max_pan, self.min_pan, 910, 70)  # event.x()
                else:
                    self.target_pan = opr.remap(event.x(), self.min_pan, self.max_pan, 70, 910)  # event.x()

    def update_LCD_display(self):

        
        self.Pan_LCD.display(self.current_pan)
        self.Tilt_LCD.display(self.current_tilt)

    def quit(self):
        print('Quit')
        self.rec = False
        sys.exit()

    def closeEvent(self, event):
        self.quit()

    def set_manual_mode(self):
        self.manual_mode = self.Manual_checkbox.isChecked()
        if(not self.manual_mode):          
            self.random_servos_position()  
        print(self.manual_mode)

    def random_servos_position(self):
        self.target_tilt = random.uniform(self.min_tilt, self.max_tilt)
        self.target_pan = random.uniform(self.min_pan, self.max_pan)


    def toggle_recording(self):
        if(self.rec):
            self.rec = False                   #stop recording
            self.PauseButton.setText("Resume") #change pause button text
        else:
            self.rec = True
            self.PauseButton.setText("Pause")
            self.record()


    def record(self):  #video recording

        while(self.rec):
            ret, img = self.cap.read() #CAPTURE IMAGE

            if(self.is_connected):            #if arduino connected
                if(self.manual_mode):         #and manual mode on
                    processed_img = img       #don't process image
                else:
                    processed_img = self.image_process(img) #process image (check for faces and draw circle and cross)
            else:                             #if arduino  not connected
                processed_img = img           #don't process image

            self.update_GUI(processed_img)    #update image in window
            cv2.waitKey(0)                    #no delay between frames

            self.move_servos() #move servos

            if (not self.rec):     #allows while loop to stop if pause button pressed
                break

    def update_GUI(self, openCV_img): # Convert openCV image and update pyQt label

        try: #if this doesn't work check camera ID
            openCV_img = cv2.resize(openCV_img, (960, 540))  #this is stretching the image a bit but if not done it won't fit the UI
            height, width, channel = openCV_img.shape
            bytesPerLine = 3 * width
            qImg = QImage(openCV_img.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()

            pixmap = QPixmap(qImg)
            self.label.setPixmap(pixmap)

        except:
            self.label.setText("check camera ID")

        self.show()

    def move_servos(self):
        if (self.is_connected):

            if self.LED_ON and not self.manual_mode:
                if not self.face_detected: #set led mode (0:red, 1:yellow 2:green)
                    led_mode = 0
                else:
                    if self.target_locked:
                        led_mode = 1
                    else :
                        led_mode = 2

            elif self.LED_ON and self.manual_mode:
                led_mode = 3 #turn all led's on
            else:
                led_mode = 4 #turn led's off

            data_to_send = "<" + str(int(self.target_pan)) + "," + str(int(self.target_tilt)) + "," + str(led_mode) + ">"
            self.ard.runTest(data_to_send)
            


    def roam(self):
        if(self.roam_pause_count < 0 ):      
            self.roam_pause_count = self.roam_pause                                        #reset roam count
            self.roam_target_pan = int(random.uniform(self.min_pan, self.max_pan))
            self.roam_target_tilt = int(random.uniform(self.min_tilt, self.max_tilt))

        else:        #if roam count > 1
                     #increment pan target toward roam target
            if (int(self.target_pan) > self.roam_target_pan):
                self.target_pan -= 1
            elif (int(self.target_pan) < self.roam_target_pan):
                self.target_pan += 1
            else:    #if roam target reached decrease roam pause count
                self.roam_pause_count -= 1

            if (int(self.target_tilt) > self.roam_target_tilt):
                self.target_tilt -= 1
            elif (int(self.target_tilt) < self.roam_target_tilt):
                self.target_tilt += 1
            else:
                self.roam_pause_count -= 1


    def image_process(self, img):  #handle the image processing
        #to add later : introduce frame scipping (check only 1 every nframe)

        processed_img = opr.find_face(img, self.max_target_distance)  # try to find face and return processed image
        # if face found during processing , the data return will be as following :
        #[True, image_to_check, distance_from_center_X, distance_from_center_Y, locked]
        #if not it will just retun False

        if(processed_img[0]):             #if face found
            self.face_detected = True
            self.empty_frame_number = self.max_empty_frame  
            self.target_locked = processed_img[4]
            self.calculate_camera_move(processed_img[2], processed_img[3])  
            return processed_img[1]
        else:
            self.face_detected = False
            self.target_locked = False
            if(self.empty_frame_number> 0):
                self.empty_frame_number -= 1 
            else:
                self.roam()              
            return img


    def calculate_camera_move(self, distance_X, distance_Y):

        #self.target_pan += distance_X * self.PanSensivity

        if(self.InvertPan): 
            self.target_pan -= distance_X * self.PanSensivity
            if(self.target_pan>self.min_pan):
                self.target_pan = self.min_pan
            elif (self.target_pan < self.max_pan):
                self.target_pan = self.max_pan

        else:
            self.target_pan += distance_X * self.PanSensivity
            if(self.target_pan>self.max_pan):
                self.target_pan = self.max_pan
            elif (self.target_pan < self.min_pan):
                self.target_pan = self.min_pan


        #self.target_tilt += distance_Y * self.TiltSensivity

        if(self.InvertTilt): 
            self.target_tilt -= distance_Y * self.TiltSensivity
            if(self.target_tilt>self.min_tilt):
                self.target_tilt = self.min_tilt
            elif (self.target_tilt < self.max_tilt):
                self.target_tilt = self.max_tilt
        else:
            self.target_tilt += distance_Y * self.TiltSensivity
            if(self.target_tilt>self.max_tilt):
                self.target_tilt = self.max_tilt
            elif (self.target_tilt < self.min_tilt):
                self.target_tilt = self.min_tilt

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    app.exec_()
    #sys.exit(app.exec_())
