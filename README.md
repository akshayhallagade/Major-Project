# Advanced Laser Guided Weapon System with Automatic Target Identification and Tracking.
> Major Model
## Submitted by
* Akhil Menghare       
* Akhilesh Ramteke   
* Akshay Hallagade  
* Akshay Sontakke    
* Ankit Dhongadi       

## 1.Abstract

The goal of an Automatic target-recognition system is to detect and identify enemy targets. The use of computer processing to detect and identify targets automatically-is becoming critically important in several military applications. ATR systems can reduce the workload of tactical aircraft crews. Automatic target-recognition with weapon system will also be a crucial component of future "smart" weapons, missiles programmed to seek out and destroy specified targets. Furthermore, automatic target-recognition technology has potential commercial application in the field of robotic vision. The development of a comprehensive automatic target-recognition system is difficult because the system must handle a variety of targets under a variety of conditions. 
By using techniques from the field of artificial intelligence, often called machine intelligence, we have developed an experimental automatic target-recognition system that processes image data from a laser radar and then automatically detects and recognizes specified targets in the data.

## 2. Introduction

Over the centuries there have been many important innovations in weaponry: the spear, the bow and arrow, the catapult and other siege machinery, the gun and the cannon, steam vessels and metal-hulled ships, the submarine and the aircraft. This project mainly comprises of a camera-based weapon system that uses software to locate and attack a moving target. It will encompass a combination of hardware and software to match a mounted air soft weapon’s point of aim to the located target in the camera’s view.The basic idea of the turret is to put the laser module on top of one servo to provide horizontal rotation; then mount that package onto another servo placed at a 90degree angle to provide vertical movement. Using two servos, this add-on enables our camera to move left-to-right and up-and-down simultaneously, allowing us to detect and track objects, even if they were to go “out of frame”.

## 3.Library Used 

### 3.1 NUMPY

Numpy makes the task easier. Numpy is a highly optimized library for numerical operations. It gives MATLAB-style syntax. All the OpenCV array structures are converted to-and-from Numpy arrays. So whatever operations you can do in Numpy, you can combine it with OpenCV, which increases number of weapons in your arsenal. Besides that, several other libraries like SciPy, Matplotlib which supports Numpy can be used with this.


### 3.2 OPEN CV2

OpenCV is the huge open-source library for the computer vision, machine learning, and image processing and now it plays a major role in real-time operation which is very important in today’s systems. By using it, one can process images and videos to identify objects, faces, or even handwriting of a human. When it integrated with various libraries, such as Numpy, python is capable of processing the OpenCV array structure for analysis. 


### 3.3 PICKLE

The pickle module implements binary protocols for serializing and de-serializing a Python object structure. “Pickling” is the process whereby a Python object hierarchy is converted into a byte stream and “unpickling” is the inverse operation, whereby a byte stream (from a binary file or bytes-like object) is converted back into an object hierarchy. Pickling (and unpickling) is alternatively known as “serialization”, “marshalling,” 1 or “flattening”; however, to avoid confusion, the terms used here are “pickling” and “unpickling”.


### 3.4 PYSERIAL

This library encapsulates the access for the serial port. It provides backend for Python running on Windows, OSX, Linux, BSD (possibly any POSIX compliant system) and Iron Python. The module named “serial” automatically selects the appropriate backend.
PySerial is a library which provides support for serial connections ("RS-232") over a variety of different devices: old-style serial ports, Bluetooth dongles, infra-red ports, and so on.


### 3.5 PYQT-5

Qt is set of cross-platform C++ libraries that implement high-level APIs for accessing many aspects of modern desktop and mobile systems. These include location and positioning services, multimedia, NFC and Bluetooth connectivity, a Chromium based web browser, as well as traditional UI development.
PyQt5 is a comprehensive set of Python bindings for Qt v5. It is implemented as more than 35 extension modules and enables Python to be used as an alternative application development language to C++ on all supported platforms including iOS and Android.
PyQt5 may also be embedded in C++ based applications to allow users of those applications to configure or enhance the functionality of those applications.

### 3.6. Haar cascade
Haar Cascade is a machine learning object detection algorithm used to identify objects in an image or video and based on the concept of  features proposed by Paul Viola and Michael Jonh. It is a machine learning based approach where a cascade function is trained from a lot of positive and negative images. It is then used to detect objects in other images. The algorithm has four stages:
