# Advanced Laser Guided Weapon System with Automatic Target Identification and Tracking.
> Major Model
## Submitted by
* Akhil Menghare       
* Akhilesh Ramteke   
* Akshay Hallagade  
* Akshay Sontakke    
* Ankit Dhongadi

## #Content
#### 1. Introduction
   - Overview 
   - Objective
   - History
   - Advantage 
   - Application
#### 2. Literature Review
#### 3. Tools and Methodology
   - Tools
   - Methodology
   - Library used
#### 4. Design and Implementation
   - Hardware Design
   - Software (Code) Design
   - Image Capture
   - Working and Testing
#### 5. Result and Conclusion
   - Result
   - Conclusion
   - Future Scope
#### 6. References
#### 7. Photograph

## 1. Abstract

The goal of an Automatic target-recognition system is to detect and identify enemy targets. The use of computer processing to detect and identify targets automatically-is becoming critically important in several military applications. ATR systems can reduce the workload of tactical aircraft crews. Automatic target-recognition with weapon system will also be a crucial component of future "smart" weapons, missiles programmed to seek out and destroy specified targets. Furthermore, automatic target-recognition technology has potential commercial application in the field of robotic vision. The development of a comprehensive automatic target-recognition system is difficult because the system must handle a variety of targets under a variety of conditions. 
By using techniques from the field of artificial intelligence, often called machine intelligence, we have developed an experimental automatic target-recognition system that processes image data from a laser radar and then automatically detects and recognizes specified targets in the data.

## 2. Introduction
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
    <img src="6. Images/History.jpg" alt="Logo" width="500" height="280">
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
<img src="6. Images/diagram1.jpg" align="center" />


## 3.	Literature Review

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

## 4. Tool and Methodology
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
