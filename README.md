Advanced Laser Guided Weapon System with Automatic Target Identification and Tracking.
================
> Major Model


<br />
<p align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="6. Images/IMG20200828105544.jpg" alt="Logo" width="400">
  </a>
</p>

Submitted by
================
* Akhil Menghare       
* Akhilesh Ramteke   
* Akshay Hallagade  
* Akshay Sontakke    
* Ankit Dhongadi

Table of contents
=================

<!--ts-->
   * [0. Abstract](#1-abstract)
   * [1. Introduction](#2-introduction)
   * [2. Literature Review](#3-literature-review)
   * [3. Tool and Methodology](#4-tool-and-methodology)
   * [4. Design and Implementation](#5-design-and-implementation)
   * [5. Result and Conclusion](#6-result-and-conclusion)
   * [6. References](#7-references)
   * [7. Photograph](#8-photograph)
<!--te-->


## 1. Abstract

The goal of an Automatic target-recognition system is to detect and identify enemy targets. The use of computer processing to detect and identify targets automatically-is becoming critically important in several military applications. ATR systems can reduce the workload of tactical aircraft crews. Automatic target-recognition with weapon system will also be a crucial component of future "smart" weapons, missiles programmed to seek out and destroy specified targets. Furthermore, automatic target-recognition technology has potential commercial application in the field of robotic vision. The development of a comprehensive automatic target-recognition system is difficult because the system must handle a variety of targets under a variety of conditions. 
By using techniques from the field of artificial intelligence, often called machine intelligence, we have developed an experimental automatic target-recognition system that processes image data from a laser radar and then automatically detects and recognizes specified targets in the data.

## 2 Introduction
### 2.1. Overview

Over the centuries there have been many important innovations in weaponry: the spear, the bow and arrow, the catapult and other siege machinery, the gun and the cannon, steam vessels and metal-hulled ships, the submarine and the aircraft. This project mainly comprises of a camera-based weapon system that uses software to locate and attack a moving target. It will encompass a combination of hardware and software to match a mounted air soft weapon’s point of aim to the located target in the camera’s view.
This Project mainly based on use of Two Module:

* 2.1.1. Laser Guided Turret (Manually Controlled).
* 2.1.2. Automatic (AI Based) Target Identification and Tracking.

The basic idea of the turret is to put the laser module on top of one servo to provide horizontal rotation; then mount that package onto another servo placed at a 90degree angle to provide vertical movement. Using two servos, this add-on enables our camera to move left-to-right and up-and-down simultaneously, allowing us to detect and track objects, even if they were to go “out of frame”.

This project provides protection to the area it covers and also do not rely on the use of direct intervention humans to do so. This system can be used to provide protection to Defense systems houses, banks, and offices etc. Usually the existing CCTV cameras only provide as footage of actual environment but it is usually recorded and we cannot over the threat, robbery, intruders or any suspicious activity in the mean actual time. But using this system we can avoid the threat without direct human intervention in real time environment we can eliminate the threat.

It can be mounted on the house or any building and then it will track the moving object in this case in intraday or any suspicious activity and it eliminates it so the project has to part hardware and software the hardware parts is of two parts first is laser guided weapon to write and the second is high resolution camera and the server for the moment in 360 degrees and the programming including the Python Programming, C# and the Arduino codes for the smooth, error free execution of task.

### 2.2. Objective

The turret will be connected wirelessly to the control room surveillance system. Using Processing language-based user interface and Arduino IDE, surveillance system will detect movement, track objects, adjust the aim of the turret, and fire at a moving target. The user interface provided in the surveillance system control room will display a live video stream that will act as the eyes of the gun. While in automatic firing mode the system will recognize a moving object, follow the target, and fire until the threat is neutralized or out of site. By pressing a button on the mouse, the turret will switch into manual control mode to avoid any unwanted causalities. Displayed on-screen of the connected device is a live video feed where the user can move the gun in any direction, they please in 360-degree perspective by the use of two servos one for pan and the another one for tilt each for 180 degree. With the live video feed streaming the user or administrator can fire at any object with good accuracy.

### 2.3. History

The first video surveillance system was installed in 1942 in Nazi occupied Germany in order to observe the launch of long range guided ballistic missiles. Shortly thereafter, CCTV systems became available in the US as well, to both government entities and commercial users who wished to keep an eye on their business. At this point, however, the security camera system still needed the human touch; there was no technology available to record data, so someone had to monitor the screens for a security camera system to do any good.

<br />
<p align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="6. Images/History.jpg" alt="Logo" width="600" height="340">
  </a>
   <h5 align="center">Fig.1.1 : First surveillance system in Germany</h5>
</p>
 
The first commercial use of the technology in the United States appeared in 1949, via a system called Vericon, and it was advertised as being “designed to keep an eye on dangerous industrial processes or bring a close-up of demonstrations and surgical operations to large numbers of students.” Video surveillance emerged in the 1970s as an industry with “a viable commercial technology to deliver safety and security,”

But due to increasing Technology nowadays that rate is also increased drastically so to avoid such a suspicious activity in our environment to save our businesses when should switch to more advanced and smart surveillance systems which can monitor and act accordingly small businesses do not have fund to keep an extra employee or worker to monitor and handle surveillance system. So, they should switch to more advanced and AI based surveillance system that can-do equivalent work as an employee or a worker to handle the surveillance system without any extra cost it is the most cost-effective method for businesses. You can constantly monitor and eliminate the threat without direct contact with the threat.

### 2.4. Advantages

- Major advantage of utilizing artificial intelligence in security systems is its inherent ability to be scaled and therefore an inevitable efficiency and efficacy that simply cannot be achieved through human systems operation alone.

- For the analysis on the ground, in real time AI in smart surveillance can also simplify the identification, processing and response to security threats.

- Speed, accuracy, and efficiency are utmost compared to humans and existing technology security systems.

- A huge advantage to autonomous systems is that it can simultaneously undertake multiple tasks, monitoring and protecting vast numbers of devices and systems.

- By the use of laser guided to turret one can simply eliminate threat without the direct interaction with the trait itself.

- Just moving the mouse, the pointer in the actual environment moves and with one click the user of the system can eliminate the threat.

### 2.5 Applications

- AI technologies bring superior face recognition, object recognition and event recognition capabilities, thus providing proactive and real-time security. This has a massive application for police forces as they need to identify criminals from within a crowd in large spaces.

- CCTV monitoring is only as accurate and reliable as the person monitoring it on the screen. But using this project it will change the dimension for the user as it will automatically track the target.

- The security of an organization, institution or simply any house or place is guaranteed.

- The use of Automatic target identification has changed the picture completely through real-time monitoring of the video footage with intelligent analysis of how security incidents can possibly occur and what needs to be done to prevent them from occurring.

<br />
<p align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="6. Images/recongnize.jpg" alt="Logo" width="500" height="280">
  </a>
   <h5 align="center">Fig 1.2 Smart target tracking using AI</h5>
</p>

- Patterns of activities could also be observed and different deployment strategy can be implemented for different environments to single out criminal behaviour and thus secure neighbouring environment.

- This whole project would also enable security officers to interpret big data in a qualitative manner and allow them to take crucial steps to protect both humans and valuable assets.

<img src="6. Images/flow_chart.jpg" align="center" />



## 3 Literature Review

Laser technology has been used in military operations for applications including laser weapons, communication, remote sensing, information relaying, active imagers, illuminators, etc. Some of these systems have been experimentally demonstrated but none have been considered as a standard for military operations until date.

#### 3.1. The primary demonstration of lasers in 1960,
when a light was flashed through a crystal structure, at California’s Hughes Research lab, it has almost taken fifty years to bring lasers for effective use. Laser technology has established groundbreaking engineering enhancements and scientific developments that have been built for numerous scientific, industrial, military, medical and commercial applications. Laser technology has brought great enhancements in surgery, data storage, photography, holography, spectroscopy and numerous other fields.

#### 3.2. During the 1970se1990s,
Radio Frequency (RF) coupled with Digital Signal Processing (DSP) proved to be the most useful application for military warfare. Though, due to the constantly increasing demand for data capacity in electronic warfare, wider spectrum communications and broadband radar systems are needed. Radio Frequency isn’t capable of handling such high demands. For all such military applications, lasers are thought of as a decent alternative over Radio Frequency signals. Laser technology can handle the desired large capabilities and real-time dynamic range processing.

#### 3.3. The 1970s,
US Air Force initiated a 405B program to develop a laser communication link (up to 1 Gbps) between geostationary satellite and ground station. The program successfully transmitted and detected a modulated laser beam by engineering feasibility models developed by McDonnell-Douglas.

#### 3.4. Later, in 1975,
The space flight test system (SFTS) program demonstrated a high capacity transmission, both to a ground terminal and low-earth orbit (LEO) terminal.
During this era, a vast development and proliferation of laser technology has been observed in the support of the defense programs.

#### 3.5.In the1990s and early 2000s,
Various comprehensive studies were carried out for use of lasers to military missions such as laser mission study (1991), new world vistas (1995), cross-link studies for the follow-on early warning system (FEWS) program, which later became the space-based Infrared system (SBIRS, halted in 1993), laser com inter-satellite transmission experiment (LITE), terahertz optical reach back (THOR) (2002), optical RF combined link experiment (ORCLE) (2004) and transformational satellite communication system (TSAT) (canceled in 2009 due to cost and delay factors).

#### 3.6. Later in 2010,
Fast airborne laser communications optical node (FALCON) carried out research in collaboration with AFRL and Exiles, Inc. for developing 2.5 Gbps full duplex optical link between two aircraft.

#### 3.7. In 2013,
German-based company VI alight achieved success in demonstrating 1.25 Gbps link between a mobile jet aircraft and a transportable optical ground station (TOGS) over a distance of 50 km.

#### 3.8. Robust Electric Laser Initiative (RELI)
This is a joint project operated by the department of Defence (DoD), Lockheed Martin, Northrop Grumman and Boeing for developing high-energy advanced electric laser technology for tactical operations. Their aim is to produce 100 kW laser while they have successfully demonstrated 30 kW laser power in 2013.

#### 3.9. Boeing High Energy Laser Mobile Demonstrator.
The program was initiated to demonstrate that the army can eliminate threats such as rockets, mortar, and UAVs at the speed of light. In 2014, an experiment was carried out to generate a high energy laser weapon using a 10-kW solid state laser.

By researching on all the similar existing technologies implemented successfully in the past, the designers of this system intend to integrate several of them to make a specific design. The system will have several functions, mainly as a defense gun to guard. This system can also be further optimized depending on its use but initially it can be used for local security by businesses or home owners. It can even be used in battlefields in order to protect a military base from incoming enemies and can also have the ability to successfully detect and intercept incoming planes, helicopters, and missiles. The system’s concept does have several uses and one can use it according to his needs.

## 4 Tool and Methodology
### 4.1. Tools
#### 4.1.1.	MG996R Servo Motor

After selecting the right Servo motor for the project, comes the question how to use it. As we know there are three wires coming out of this motor. The description of the same is given on top of this page. To make this motor rotate, we have to power the motor with +5V using the Red and Brown wire and send PWM signals to the Orange color wire. Hence, we need something that could generate PWM signals to make this motor work, this something could be anything like a 555 Timer or other Microcontroller platforms like Arduino, PIC, ARM or even a microprocessor like Raspberry Pi. Now, how to control the direction of the motor? To understand that let us a look at the picture given in the datasheet.

#### 4.1.2.	Arduino uno

The board is equipped with sets of digital and analog input/output (I/O) pins that may be interfaced to various expansion boards (shields) and other circuits. The board has 14 digital I/O pins (six capable of PWM output), 6 analog I/O pins, and is programmable with the Arduino IDE (Integrated Development Environment), via a type B USB cable. It can be powered by the USB cable or by an external 9-volt battery, though it accepts voltages between 7 and 20 volts. It is similar to the Arduino Nano and Leonardo. 

#### 4.1.3. 5mv Laser Diode 

The 650nm 6mm 5V DC 5mW Mini Laser Dot Diode Module which is made of copper plastic. It is suitable for 3V 5mW standard, with 6mm outside diameter, can be used to connect diode tubes for multiple uses. Output Power: 5mWWorking Voltage: 5V DC, Working temperature: -10 ℃~＋40 ℃, Housing material: Copper Working life: more than 2000 hours, Spot mode: Dot Facula (continuous output), Laser wavelength: 650nm red-colored., Operating current: <40mA, Power lead length: 120mm.

#### 4.1.4. ESP32 Camera

ESP32 is a series of low-cost, low-power system on a chip microcontrollers with integrated Wi-Fi and dual-mode Bluetooth. The ESP32 series employs a Tensilica Xtensa LX6 microprocessor in both dual-core and single-core variations and includes built-in antenna switches, RF balun, power amplifier, low-noise receive amplifier, filters, and power-management modules. ESP32 is created and developed by Expressive Systems, a Shanghai-based Chinese company, and is manufactured by TSMC using their 40 nm process.[2] It is a successor to the ESP8266 microcontroller.

#### 4.1.5.	Node MCU

The Node MCU ESP8266 development board comes with the ESP-12E module containing ESP8266 chip having Tensilica Xtensa 32-bit LX106 RISC microprocessor. This microprocessor supports RTOS and operates at 80MHz to 160 MHz adjustable clock frequency. Node MCU has 128 KB RAM and 4MB of Flash memory to store data and programs. Its high processing power with in-built Wi-Fi / Bluetooth and Deep Sleep Operating features make it ideal for IoT projects. Node MCU can be powered using Micro USB jack and VIN pin (External Supply Pin). It supports UART, SPI, and I2C interface.

#### 4.1.6.	MLX9614 (IR sensor)

The MLX90614 is an infrared thermometer for non-contact temperature measurements. Both the IR sensitive thermopile detector chip and the signal conditioning ASIC are integrated in the same TO-39 can. Integrated into the MLX90614 are a low noise amplifier, 17-bit ADC and powerful DSP unit thus achieving high accuracy and resolution of the thermometer.

### 4.2. Methodology
Laser technology has observed a great advancement over the last few decades. This technology is used for a wide range of applications including medical sciences, military, industrial manufacturing, electronics, holography, spectroscopy, astronomy and much more. Military operations often demand a secure and timely transmission of a massive amount of information from one place to another. Until now, the military has relied on the radio spectrum for effective communication, which is vulnerable to security threats and susceptible to electromagnetic interference (EMI). Also, this spectrum is hard-pressed to meet the current bandwidth requirement for high-resolution images, on-air videoconferencing and real-time data transfer. Therefore, the focus has shifted to visible and infrared (IR) spectrum using laser technology which is capable of providing secure data transfer because of its immunity to EMI. The probability of intercepting a laser signal is very low due to its narrow beam divergence and coherent optical beam, making the laser a suitable candidate for secure military tactical operations. Besides the communication aspect, the highly directive nature of a laser beam is also used as a directed energy laser weapon. 

#### 4.2.1 Library Used 

##### 4.2.1.1 NUMPY

Numpy makes the task easier. Numpy is a highly optimized library for numerical operations. It gives MATLAB-style syntax. All the OpenCV array structures are converted to-and-from Numpy arrays. So whatever operations you can do in Numpy, you can combine it with OpenCV, which increases number of weapons in your arsenal. Besides that, several other libraries like SciPy, Matplotlib which supports Numpy can be used with this.


##### 4.2.1.2 OPEN CV2

OpenCV is the huge open-source library for the computer vision, machine learning, and image processing and now it plays a major role in real-time operation which is very important in today’s systems. By using it, one can process images and videos to identify objects, faces, or even handwriting of a human. When it integrated with various libraries, such as Numpy, python is capable of processing the OpenCV array structure for analysis. 


##### 4.2.1.3 PICKLE

The pickle module implements binary protocols for serializing and de-serializing a Python object structure. “Pickling” is the process whereby a Python object hierarchy is converted into a byte stream and “unpickling” is the inverse operation, whereby a byte stream (from a binary file or bytes-like object) is converted back into an object hierarchy. Pickling (and unpickling) is alternatively known as “serialization”, “marshalling,” 1 or “flattening”; however, to avoid confusion, the terms used here are “pickling” and “unpickling”.

##### 4.2.1.4 PYSERIAL

This library encapsulates the access for the serial port. It provides backend for Python running on Windows, OSX, Linux, BSD (possibly any POSIX compliant system) and Iron Python. The module named “serial” automatically selects the appropriate backend.
PySerial is a library which provides support for serial connections ("RS-232") over a variety of different devices: old-style serial ports, Bluetooth dongles, infra-red ports, and so on.


##### 4.2.1.5 PYQT-5

Qt is set of cross-platform C++ libraries that implement high-level APIs for accessing many aspects of modern desktop and mobile systems. These include location and positioning services, multimedia, NFC and Bluetooth connectivity, a Chromium based web browser, as well as traditional UI development.
PyQt5 is a comprehensive set of Python bindings for Qt v5. It is implemented as more than 35 extension modules and enables Python to be used as an alternative application development language to C++ on all supported platforms including iOS and Android.
PyQt5 may also be embedded in C++ based applications to allow users of those applications to configure or enhance the functionality of those applications.

##### 4.2.1.6 Haar cascade

Haar Cascade is a machine learning object detection algorithm used to identify objects in an image or video and based on the concept of  features proposed by Paul Viola and Michael Jonh. It is a machine learning based approach where a cascade function is trained from a lot of positive and negative images. It is then used to detect objects in other images. The algorithm has four stages:

1.	Haar Feature Selection
2.	Creating Integral Images
3.	Adaboost Training
4.	Cascading Classifiers

It is well known for being able to detect faces and body parts in an image, but can be trained to identify almost any object. Here we will work with face detection. Initially, the algorithm needs a lot of positive images (images of faces) and negative images (images without faces) to train the classifier. Then we need to extract features from it. For this, haar features shown in below image are used. They are just like our convolutional kernel. Each feature is a single value obtained by subtracting sum of pixels under white rectangle from sum of pixels under black rectangle.

Now all possible sizes and locations of each kernel is used to calculate plenty of features. (Even a 24x24 window results over 160000 features). For each feature calculation, we need to find sum of pixels under white and black rectangles. To solve this, they introduced the integral images. It simplifies calculation of sum of pixels, how large may be the number of pixels, to an operation involving just four pixels. It makes things super-fast.

## 5 Design and Implementation
At the conclusion of specifications, requirements and research, the project will progress to the hardware and software (Code) design stages. In this section, all design details, including diagrams and flowcharts for all sections, will be included. Hardware Block Diagram The hardware block diagram shown below illustrates the implementation of all hardware components.

### 5.1.	Hardware design 
It can be illustrated in the hardware block diagram that the central hardware controller for the turret can be found on the PCB. From the PCB, all motors receive the required modulated signal to operate, signals are received and transmitted in a serial manner from the tablet to the motor controller via XBee. It can be seen there are 5 major subsystems, camera, power, controller, motor, and tablet in which account for the final STATS design.

<br />
<p align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="6. Images/layout1.png" alt="Logo" width="750">
  </a>
</p>

#### 5.1.1.	Turret Design

The turret design will be broken down into three main sections consisting of the servo armature (including the weapon platform mount), the main housing, and the support legs. Based off of the requirements and specifications and research, the final design build will be modular, mobile, and accessory friendly. The aesthetic design will be robust, yet streamlined; representing a more militaristic look. For the initial design stage of the servo armature, material used will consist of wood. When an acceptable model is complete, the design will be represented in its final form using metal. The main housing will consist entirely of wood with all appropriate modular attachments for the camera and tablet. The support legs will be connected to the bottom of the housing and will be retractable in design. Material for the legs will consist of metal with rubber ends making contact with the ground surface for stability control. 

#### 5.1.2 Motors (Servo Motors)

Digital was chosen over analog for even faster response times and great performance out of the box with no additional programming needed. These servo motors are able to run on 4.8V to 7.4V. At 6 volts, the servo motors are capable 157 oz-in of power, which is close to 10lbs per inch. Additionally, the motor is rated at a speed of 0.20 seconds per 60-degree turn. Servo features include 180 degree turn radius, a neutral point, and multidirectional control. Two HS-5685MH servo motors will be integrating into the armature design; one for horizontal movement and another for vertical movement. The design of the trigger servo will not need to compete with the specifications of the directional servos. The main design feature for this servo is the ability to pull a trigger with up to 2lbs of force and come in a small form factor. Using servocity.com, an appropriate servo would be the Hitec HS-5485HB. This servo motor comes in the submicro size, comparable to a quarter in size. At 6V, this servo is able to produce over a pound of force with its metal gear box. The servo is also able to span over 120 degrees (60 degrees both clockwise and counterclockwise), which will be more than a sufficient margin for trigger pull. The design of the trigger servo will allow it to be attached close to the y-axis positioning servo to grant it access to the trigger of the mounted weapon platform.

#### 5.1.3 	Laser Device 

The system requirement to have a laser device was established early on in the project design. Initially it was thought that it would be implemented in some kind of range detection algorithm. With further research into the abilities of common airsoft rifles, the addition of range calculation to this project was deemed an unnecessary step. The distances that this turret is effective in is far less than the overall effective range of the airsoft gun. It was still decided that a laser should be implemented on the turret regardless, and would be used mainly for target testing. With the use of a weapon mounted laser, the accuracy and reliability of the tracking system was tested without the need for live fire. This enabled indoor calibration to be done to the system while the bugs were worked out of the code.

### 5.2. Code Design

The tablet device will be responsible for all the software requirements. By using the Atmel Mega 328 microcontroller the group was able to utilize the open-source Arduino library. There are abundant pre-existing Arduino libraries and functions that will help with this project’s goals. The tablet device will house all the software responsible for the turret project from tracking to automatic firing to manual control. The process begins with the camera sending the video stream to the tablet for user display. While in automatic firing mode, the tracking algorithms are waiting to encounter a moving target. Once that happens the range finder determines the target’s distance and sends the direction and speed signals to the microcontroller in order to move the servos. Once manual mode is activated, signals are sent to the microcontroller based on the user input.

#### 5.2.1. Arduino IDE

To program the custom-built microcontroller, the Arduino IDE version 1.5.6-r2 will be used, which is the latest version currently. This open source IDE from the Arduino website is written in Java. It can be run on Linux, Mac, and most importantly Windows, including 32-bit. By using the default environment, it makes writing code and uploading it to the board in an easy fashion that is aimed at beginner programmers. The language the user programs in C or C++. The IDE comes with a library called Wiring which makes many common input/outputs operations very simple to use. The basic Arduino code must have two function, setup and loop, described below:

*	setup (): A function run once at the start of a program that can initialize settings.
*	loop (): A function called repeatedly until the board powers off.

#### 5.2.2. Targeting Control (Servo Control)

The group was able to utilize the open-source Arduino environment and prebuilt libraries by creating a custom version of Arduino on PCB. One of those prebuilt libraries include the Servo library. This library allows up to 12 servos, each at various angles between 0 and 180 degrees. Below in Tables 4.2-4.7 are an outline of the various functions that will be applied from the Servo library. By applying these functions in the Arduino IDE, the below six methods are all that is needed for servo control.

### 5.3. Image Capture 

The very first step in this motion tracking system was to capture the images that are in the field of view of the turret system. This information is then processed by the image tracking software and used to send control signals to the servo motors as well as targeting data to the user interface so that a user can see what the tracking software can see. This is one of the first decisions that were required out of this project as well as one of the more daunting tasks to accomplish.

#### 5.3.1. Camera Working

The various options for the camera on the video subsystem brought forward a lot of difficult decisions for the group. Wireless cameras mostly seemed dependent on the manufacturer’s website in order to receive the video data wirelessly on a tablet. This did not seem like the best method of transmission due to the dependency on an internet connection. It seemed more logical to try and avoid using an established internet connection for device communication because the operating space of this system would most likely be outdoors. After researching multiple methods of sending video signal from a camera to a tablet separated by several meters of space, an Android phone camera along with an app called DroidCam was chosen as the best possible option. The phone used in this project is the Motorola Moto G. Any Android phone can be used but one group member allowed their phone to use for the demonstration. The Moto G has a 5 MP camera and shoots in 720p. The quality is downgraded by JMyron library to 480p for smoother transfer between the phone and tablet.

#### 5.3.2. Tracking System Design 

The decision between the multiple tracking methods came down to using open computer vision software and libraries or the Processing programming language and its open source libraries. The Processing programming language won out due to its versatility, abundant online support and the fact that the source code is written in Python and C++. The list of useful libraries that were used for this project included many options that aided in adding more complex abilities to this project. Among the multiple libraries that were used for this project are the JMyron library, the Blob Detection library, and the serial communications library Processing. Serial. When the user selects to run the Processing IDE as well as the associated program files the program must borrow heavily from the predefined libraries in order to function. The sequence of events that takes place after the user initiates the program is illustrated.

### 5.4. Working and Testing

The ability to track the objects that have been detected is the next logical requirement of this system. There must be a fast and accurate response from the tracking program as the objects/targets attempt to evade the system. If multiple targets are present then the system must follow the target that has priority, which is calculated by position in the field of view.

1.	Power on the system and Laptop for live video feed. 
2.	Open the Processing IDE and run the program and all related codes and programs.
3.	Have volunteer (Intruder) move across the field of view at multiple speeds and patterns. 
4.	Check agility of tracking system by having a volunteer move through the field of view in an varying path of varying speeds. 
5.	Check the responsiveness of the system by having a volunteer run past the camera at maximum speed and varying distances. 
6.	Have a volunteer come to a complete stop at any point during the pass and see if the tracking system maintains fire on target. 
7.	Monitor the user interface to see that the targets are being followed while they remain in the field of view. 
8.	Check to see if system resets to an origin at the center of the field of view after a preset time with no targets located. 
9.	Move an inanimate object into the field of view and check to see how the tracking system reacts. 
10.	Lock the target and try to shoot it using laser guided turret from live video-feed.

##### Required Outcome: 
Any targets detected in the field of view are followed by the turret system while the target remains moving in the viewing range. Targets are tracked and fired upon accurately while attempting evasive maneuvers. Targeting software detects threats even if they stop moving but are still in plain sight. Changes in background ignored after a period of time, items not matching target features not considered for attack.

#### 5.4.2 Manual Testing

1. Verify all power connections are working  
2. Test the direction of the servos by using the directional keys on the user interface of live video.
3. Move the turret via control from the live video feed to aim at a specified target 
4. Pull the trigger of the laser guided turret using the fire command button on the IDE.
5. Repeat steps 3 through 4 using a moving target 

##### Expected Result:
The sentry turret system is able to effectively track and fire upon a target with minimal delay time and with maximum accuracy. 


## 6 Result and Conclusion

### 6.1 Result

The performance of our system is studied for tracking and pointing a person moving randomly the person position does not jump quickly around the image. While it can slightly affect the accuracy of detection due to slight movement of a person. Despite of the delay, our system shows fairly well to track the desired target especially when the background is different, a person changes the appearance as the person moves different angles, and uneven terrain. Bigger object as a person is close to the camera and smaller object when the person is far to the camera is still robustly been detected.

The proposed and developed system for surveillance and tracking has tested under different conditions like facial positions and distances. We have used surveillance video camera to locate faces from live video and then used face identification to test the credibility of the system. Although the main goal of this developed system is to detect individuals by their faces from a video camera, we also discuss the performances of face detection methods under different conditions. Finally, the effectiveness of the face recognition method used in this system has been tested using different facial images of some persons.

One of its main advantages we found that its feature-based technique is relatively robust to position variations. It also offered compactness of representation of the face images and highspeed matching. However, in our experiment, we found that extreme variations in lighting conditions make it highly error-prone, as these approaches have difficulty selecting the features; consequently, they make arbitrary decisions about which features are important.

### 6.2	Conclusion

In this paper, we have proposed and developed a system that focuses on face detection and face tracking from a video camera for tactical military applications. Laser and face detection technology addresses the need of today’s battlefield, that require the ability to detect the target at longer distances and exchange massive amount of information in a secure and timely manner. Lasers tracking and face detection have revolutionized the warfare in their roles as accessories to high-energy weapons. Face detection is always a challenge, especially face identification under different lighting conditions, positions and image depths. We found good results when we gathered faces under reasonably varied illumination conditions, positions and depths similar to those of our database. However, the system is highly error-prone under varied illumination conditions, positions and image depths.

As the areas under surveillance usually have sufficient illumination condition and cameras can be placed anywhere, our proposed surveillance system can be implemented at border and different sensitive installations. To address the problem of different facial positions or image depths, we may consider more than one camera at different positions and angles. Intelligent techniques can then be used to help combining all the videos from the camera to make the system more efficient, robust and less error-prone to position variations and image depths. Although, we have not been able to demonstrate a multi-camera surveillance system with intelligent agents here, we think the system will work well at avoiding the constraints posed by the different facial positions and image depths. We also need to keep in mind that a well-trained database plays a crucial role in face detection. Therefore, to have a high percentage of face detection rates, we need to train our database with as much variations as possible. This work can be a basic step toward a more advanced system with hybrid methods for face detection and laser tracking system. In addition, many intelligent algorithms can be included with this system to make it a more robust and error free computer-based automatic system for surveillance. 

### 6.3. Other Applications and Future Scope

Lasers are used in numerous other applications, like battlefield illuminator, weather modifier, holographic projectors and power beamers. Laser illuminators are small and light weight devices that provide the finest night vision, to help soldiers to illuminate targets for reconnaissance systems. It also provides improved target acquisition, efficient landing in case of poor light conditions, enhanced night security for sensitive sites and augment infiltration and ex-filtration of special operation teams. Future battles may necessitate space-based battlefield illumination to improve the vision in dark target sites from any given satellite position. This would require a precise pointing system for both satellite and ground site, that is to be illuminated in order to permit a pointing vector calculation of the laser beam. Another dimension where lasers can improve the military capability in future battlefield operations is its use as weather modifier. Since weather plays a dominant role in military operations, therefore, any ability to control it can bring a significant change in the war scenario.

Laser and face detection are also used to beam power up to high-altitude unmanned aircraft to periodically recharge them, in order to stay aloft for longer durations of time. The narrow divergence of the laser beam allows most of the energy to be collected by the swarming unmanned aircraft, to ensure their continuous fly at high altitudes. These unmanned vehicles could provide tactical surveillance, telecommunication relay links or temporary navigation support during war missions. They could also be used to fly guard duty over a military combat area or fly in front of a convoy to warn against an ambush. Power beaming can be carried out using either a ground-based or space-based laser. While many challenges remain in ‘ground-to-space’ or ‘space-to-ground’ power beaming, ‘space-to-space’ power beaming could be less complex and transformational. The space-based laser has lesser power requirements as it has an advantage of avoiding losses due to atmospheric absorption, scattering and turbulence.

This offers an interactive and collaborative environment for military officials, to prioritize their next course of action in battlefields. Hologram technology will generate 3D patterns by overlapping a laser reference beam, that has a smooth phase front, with a laser beam that has been scattered from the object that is to be imaged. Although creating a holographic image is now a mature technology, however building them in an open air uncontrolled warlike scenario is a big challenge. In any war scenario, the army officials can use holographic projectors to present a bulk of information, in a huge shared display manner, in order to improve soldier’s performance in the decision-making process. Further, the touch surface technology, with interactive modules and embedded features like zooming, panning, rotating, etc., can provide an enriching environment for better decision making in the war scenarios. This idea was explored during the 1991 Persian Gulf War but was not implemented for some technical reasons. Therefore, this technology provides a collaborative and interactive environment, offering a geopolitics and geographic view of an operational area, resulting in a real-time picture of the battlefield scenario. Although this technology is yet not under development, however researchers are still working to understand the capabilities of this technology to improve battlefield intelligence and military planning.

Lasers and face detection are also used to beam power up to high-altitude unmanned aircraft to periodically recharge them, in order to stay aloft for longer durations of time. The narrow divergence of the laser beam allows most of the energy to be collected by the swarming unmanned aircraft, to ensure their continuous fly at high altitudes. These unmanned vehicles could provide tactical surveillance, telecommunication relay links or temporary navigation support during war missions. They could also be used to fly guard duty over a military combat area or fly in front of a convoy to warn against an ambush. Power beaming can be carried out using either a ground-based or space-based laser. While many challenges remain in ‘ground-to-space’ or ‘space-to-ground’ power beaming, ‘space-to-space’ power beaming could be less complex and transformational. The space-based laser has lesser power requirements as it has an advantage of avoiding losses due to atmospheric absorption, scattering and turbulence. Laser power beamers are also used for power transfer in space or at remote sites, where other sources of energy are not readily available. This technology is currently in a development stage to support future space missions.

## 7 References

1. [Muhammad Labiyb "Deep Features Representation for Automatic Targeting System of Gun Turret", Electronics Symposium on Engineering Technology and Applications (IES-ETA) 2018 International, pp. 107-112, 2018.]()
2. [Hidayatulloh, A. Khoirul Rizal "Towards an Automatic Aircraft Wreckage Detection Using A Monocular Camera of UAV", 2019 International, pp. 501-504, 2019. (Papers)]()
3. [https://www.britannica.com/technology/military-technology](https://www.britannica.com/technology/military-technology)
4. [https://www.newscientist.com/article/dn9980-introduction-weapons-technology/](https://www.newscientist.com/article/dn9980-introduction-weapons-technology/)
5. [https://statetechmagazine.com/article/2019/04/how-surveillance-cameras-evolved-curiosity-ubiquity](https://statetechmagazine.com/article/2019/04/how-surveillance-cameras-evolved-curiosity-ubiquity)
6. [https://www.farsight.co.uk/about-us/history/](https://www.farsight.co.uk/about-us/history/)
7. [https://www.viaresource.com/blog/advantages-and-disadvantages-of-an-artificial-intelligence-security-system](https://www.viaresource.com/blog/advantages-and-disadvantages-of-an-artificial-intelligence-security-system)
8. [https://memoori.com/new-tools-opened-opportunity-bring-ai-video-surveillance-market/](https://memoori.com/new-tools-opened-opportunity-bring-ai-video-surveillance-market/)
9. [https://www.researchgate.net/publication/324336184_Design_and_Implementation_of_Image_Capture_Sentry_Gun_Robot](https://www.researchgate.net/publication/324336184_Design_and_Implementation_of_Image_Capture_Sentry_Gun_Robot)
10. [https://docs.python.org/3/library/pickle.html](https://docs.python.org/3/library/pickle.html)
11. [https://opencvpythontutroals.readthedocs.io/en/latest/](https://opencvpythontutroals.readthedocs.io/en/latest/)
12. [https://www.geeksforgeeks.org/opencv-%20of%20a%20human.](https://www.geeksforgeeks.org/opencv-%20of%20a%20human.)
13. [https://pyserial.readthedocs.io/en/latest/pyserial.html#overview](https://pyserial.readthedocs.io/en/latest/pyserial.html#overview)
14. [https://pypi.org/project/PyQt5/](https://pypi.org/project/PyQt5/)

## 8 Photograph

<p float="left">
  <img src="6. Images/IMG20200828105034.jpg" width="480" />
  <img src="6. Images/IMG20200828105722.jpg" width="480" />
</p>
<img src="6. Images/IMG20200828105544.jpg" align="center" width="480" />
