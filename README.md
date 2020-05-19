# automated_attendance_system
Automated attendance system based on neural networks and KNN algorithm

Many educators include classroom
attendance as part of their grading practice. Tracking attendance is typically accomplished with a manual method, which consumes a lot of time and is difficult to maintain. In this paper we describe a method for automated attendance tracking through the biometric processes of facial recognition. In this method a camera is fixed in the classroom. The camera will capture an image of the room. From the image, faces are detected and then are recognized within a database, and finally the attendance is marked. There are various methods for comparing the faces. We are using nearest neighbors(NN) methods for finding similar patches in images. We can exploit various properties of images to develop very efficient implementations of the Ball Tree algorithm. A Ball Tree is a special data structure that attempts to partition the training data in such a way that only a portion of the training data has to be searched.



Currently, if an instructor wants to record the student attendance, they need to take it manually in an attendance book, which might lead to unneeded paperwork. While taking attendance, a student may not give a proper response, and if the attendance book gets misplaced or lost, then teachers can’t retrieve the attendance details. While it may be possible to use a biometric system like
RFID barcode read, thumb impression, etc. for taking student attendance, but systems are time consuming and expensive. To overcome the above problems, we suggest implementing the classroom attendance system using a machine learning technique that is both time and cost effective.



In today’s emerging generation growth in connectivity, flexibility, and intelligence has
paved  path for machine learning . Of course, many previous technologies or languages are there to fulfill the same
requirements. If using those languages, it might take lengthy code and become a
complexity for achieving high requirements like facial detection, driver drowsy detection, smart traffic controls, etc. As the present technology is evolving, many are willing to learn and develop on machine learning  projects as they can predict heart disease,
diabetes, cancer as positive or negative and forecasting reports like weather reports.



 



Machine Learning can be classified as a subset of Artificial Intelligence. AI can perform natural language process which is useful for any customer support service helping system. In this, a customer sends a message request regarding his/her problem, then the system automatically responds with an answer to the customer which reduces the manpower. The customer agent doesn’t need to respond directly for every query. A related application of AI is “smart traffic controlling systems”. Traffic AI systems are capable of processing and analyzing a variety of data types, including images and videos. Aided by computer vision techniques, traffic AI systems can recognize objects in images and video from traffic cameras. They can do this by breaking them down into identifying features, and matching them to classes, such as “car,” “motorcycle” or “pedestrian”. 



Deep learning is useful for recognizing objects in images. Neural networks form the basis for deep learning. Deep learning, a subset of machine learning, utilizes a hierarchical level of artificial neural networks to carry out the process of machine learning. Artificial neural networks are built like the human brain, with neuron nodes connected like a web. While traditional programs
build analysis with data in a linear way, the hierarchical function of deep learning systems enables machines to process data with a nonlinear approach. For example, if we give input image as flower, deep learning is performed on it with the help of neural networks and it gives results as flower. Depending on the training dataset, it can also name the object in the image. Face detection can be easily performed by deep learning and machine learning. The supervised algorithms Haar-AdaBoost, LBP-AdaBoost, and neural networks algorithms are also used for multiple face detection. In this system both Haar-AdaBoost and LBP-AdaBoost, with the help of cascade file, can detect faces from input images. Neural networks, which uses inbuilt functions like face-recognition module, can detect
multiple faces from the given input image that has multiple faces.



Image Processing is processing a signal
for which the input should be a photograph or an image. There are two types of image
processing methods: analog and digital. Analog image processing is used for
hard copies such as photographs and printouts. Today, student attendance is
playing a significant role in many colleges, universities and schools. An automated
attendance system will capture the image of a person in the classroom and will
accordingly mark the attendance. On the other hand, a manual attendance system
will verify and manage each and every record of the student on paper, which
requires more time and effort of the faculty or staff. Also, there might be
chances of proxies in manual attendance [1] [2], human errors, etc. An
automatic system will be efficient and more user friendly as it can be run on the
devices that are used daily. This study is the first attempt to provide an
automated attendance system that identifies the students using face recognition
technology through an image or video stream for recording attendance in any
classroom environment and estimating the efficiency accordingly. Through
constantly detecting the facial info, this method incorporates the existing
technologies that are less efficient and advances the accurateness of face
recognition [8][6].



 



We studied and planned a technique that
marks the presence or absence of a student in the classroom using face
recognition constructed on non-stop surveillance. The
automatic attendance system captures photos from a camera, which becomes the
input. Later, it detects faces and recognizes the people with the help of
machine learning libraries. After detecting and recognizing student faces, it
automatically marks the students whether they are present or absent, and it
generates monthly reports. In this system, student attendance details can be
stored in a database where the data will be available until it is deleted. In
this proposed method, our aim and purpose is to gain the images or video of the
students face, their position and their attendance, which is very beneficial
info in the classroom environment.



 



 



 



 







Previous work



Identifying
faces from images is a difficult task for which there is much research
literature. Zhongfei et al. [3] proposed a face identification and detection
model by combining the images and collateral text of the people. Here, the
Authors compared the images of the same text to the images with Bayesian rule
after converting the image into binary format. Jie Chen et al. proposed an
AdaBoost algorithm [1] based on the features of the images. He proposed a
classifier using Harr features in n stages. Where n is a classifier
depending on the Harr features. Edgar Osuna et al [2] provided survey on the
face detection model of single face in a group of images of faces by using
support vector machine (SVM).  By using
the SVM algorithm they demonstrated an application to identify a single face
from a group of faces. The images of the faces compared are categorized into
one class, and the remaining images are categorized into a different class.
Also, Rowley et al [4] proposed single face identification by using a neural
network-based classifier. 



 



Chang et al. [7]
proposed face detection by using the linear discriminant analysis (LDA)
algorithm by converting image to Gradient image by applying the Euclidean
distance algorithm for distance calculation of marked pixels. Ke et al. [8]
proposed PCA-based identification after conversion of the image into gradient
image. Abdul Rahim et al. [5] proposed binary pattern comparison-based face
identification. In this system, after conversion of image into n regions for
the face recognition, the sub image converts each sub part of the image into
binary format. After conversion of the binary image, it is compared with other
images. Herbert et al. [6] proposed a novel and complex technique, Speeded Up
Robust Features (SURF), which works by comparing matrix values. They used
Hessian matrix-based measures to identify the objects in images.



 



4.2 Using Principal Component Analysis(PCA)



Nirmalya Kar et al. proposed Student’s
Attendance System [3], which will integrate with the face recognition
technology using the Personal Component Analysis (PCA) algorithm[12]. PCA has
been widely used in applications, such as facial recognition and image
compression. PCA is a common technique for finding patterns in data and
expressing the data as eigen vectors to highlight the similarities and
differences between different data [6]. The following steps summarize the PCA
process.



Let D be the training dataset, {D1,D2, D3, …Dm} 
Each element in the training data set
differs from Avg by the vector Yi=Di-Avg.
The covariance matrix Cov is obtained as:
Choose M’ significant eigenvectors of Cov
as EK’s, and compute the weight vectors Wik





 



Using LDA



Kamran Etemad and Rama Chellappa’s [11] face recognition technology uses most of the traditional linear discriminate
analysis (LDA)-based methods. By defining all instances of the same person’s face as being in one class, and the faces of different subjects as being in different classes for all subjects in the training set, we establish a framework for performing a cluster separation analysis in the feature space. Also, having labeled all instances in the training set, and having defined all the classes, we compute the within- and between-class scatter matrices as
follows: 
Here Sw is the
within-class scatter matrix showing the average scatter i of the sample
vectors (V) of different classes Ci around their
respective mean, vectors µi :



Another available biometric method uses
RFID [4][5] and eyeball detection. In this method, an eyeball sensor is used.
It senses the blinking rate of the eyeball and also senses the location of the iris.
An image of the eyeball or iris of each individual is stored in a database [9].
These images are unique to individuals. The obtained image of an eyeball is
then compared with the eyeball in the database. If a match is found, then the
attendance is marked.. But practically, all
of this is not possible. We define some problems in the existing methods:

Takes a lot of time to process the output using existing methods.

 Capturing the datasets like eyeball is practically not possible.

 Using hardware, manual efforts should be put. 



 



 



OUR SYSTEM



Our system uses the k-Nearest Neighbors
algorithm (KNN), which is a very simple technique. In this, the entire training dataset is stored. When a
prediction is required, the k most similar records to a new record (the
"neighbors" to the new record) from the training dataset are  located. From these neighbors, a summarized
prediction is made. The
disadvantages of the existing systems are overcome with the help of an
automated attendance management system which doesn’t consume as much time and
for which the data is retained until we erase it. This method is most efficient
now-a-days. In facial detection, the faces in the images are marked with the
help of rectangle. The face detected after background subtraction is accurate
as compared to the face detected from an image for which the background is not
subtracted. The detected face is then cropped. Finally, all the faces of
individuals are detected and cropped from the image. Each cropped image is
compared against images within the database and finally the attendance is
marked. We enhanced this system by using the KNN algorithm with the help of
ball trees[3].



 



The metric tree (which is a space
partitioning data structure for organizing points in a multi-dimensional space)
that we will look at is ball trees [3]. In their original form, each node point
in the space tree are assigned to the closest center of the node’s two
children. The children are chosen to have maximum distance between them,
typically using the following construction at each level of the tree. First,
the centroid of the points is located, and the point with the greatest distance
from this centroid is chosen as the center of the first child. Then, the second
child’s center is chosen to be the point farthest from the first one. The
resulting division of points can be understood as finding the hyper plane that
bisects the line connecting the two centers, and perpendicular to it. The
Figure 1 shows an example of  ball tree
partitions and the Figure 2 represents the outline of the K-NN algorithm using
ball trees.



 





                                                          



 



 



 



 



 



 



 



 



 



 



 



 



 



 



 



 






 





 







 



IMPLEMENTATION 



6.1 Description of the project



I have implemented a prototype of an automated
classroom attendance system using machine learning techniques that is both
time- and cost-effective.  This system
was implemented by using Python 3.6 with the PyCharm IDE. For generating the
user interface, we used the PyQt5 tool. For data storage purposes, we used
MySQL 5.5 version with the SQLyog user interface tool. 



In the system developed, system admin and faculty
are actors. The admin can add student details into a database which contains
student photos as well and can monitor the attendance reports in a monthly
manner. Faculty can take attendance by capturing students’ pictures with the
help of a camera where attendance can be recorded automatically and stores the
attendance details into the database. 



6.2 Method of evaluation       



·       This system will use the CNN (Convolutional Neural
Network) model for face detection by using of Python language.



·       As well as after face detection, for facial
recognition it will use KNN (K-Nearest Neighbor) classifier.



·       OpenCV is used for running the camera, image
reading, and displaying the image with facial recognition system. It will also
display the students’ roll number if their faces are matched with our database.



6.3 Face detection 



A simple approach to extracting the
information contained in an image of a face is to somehow capture the variation
in a collection of face images, independent of any judgment of features, and
use this information to encode and compare individual face images. In face detection the face of images is marked
with the help of rectangle or circle. The face detected after background
subtraction is accurate as compared to the face detected from an image which is
not background subtracted.



6.4 Face recognition



Face recognition
is used to identify the detected faces. There are many methods available for
face detection. But the eigen value method[12] is the more suitable method  because of its speed. Thus, the eigen value
method will be used to recognize the faces.








 



8.1 FUNCTIONAL REQUIREMENTS




 Admin Login



He is the super user of the
application where he can login with his/her username and password.  The admin has full access to all system
modules.




 Adding Students



Student
details can be added using this module




 View Students



Student
details can be viewed using this module




 Faculty Login



A faculty can login with his/her username using this module and can take
attendance and download the monthly reports of the students attendance




 Reports 



Monthly
reports of the students can be downloaded here



 NON-FUNCTIONAL REQUIREMENTS




 The software is portable. So, moving from one OS to other OS does not create
     any problem.

 The privacy of information, and intellectual property rights will be
     protected.

 The time taken by the system for reacting to the admin or the faculty’s request
     will be so quick.

 The system can run on a laptop, is easily useable by non-technical faculty
     members and can handle up to 300 students. 

 The overseer to eschew the abuse of the application by PC should be
     exceptionally secured and available.







 




 



 



 



 





                                                         



 



 



 



 



 



 





 



                                                            



 



 








 

















 



 



 



 



 











 



 



 







11.ABOUT THE PROJECT’S SOFTWARE



11.1 About Python



Python is an interpreted, object-oriented, high-level
programming language with dynamic semantics. Its high-level built
in data structures, combined with dynamic typing and dynamic binding, make it
very attractive for Rapid Application Development, as well as for use as a
scripting or glue language to connect existing components together. Python's
simple, easy to learn syntax emphasizes readability and therefore reduces the
cost of program maintenance. Python supports modules and packages, which
encourages program modularity and code reuse. 



 



Often, programmers fall in love with Python because of the
increased productivity it provides. Since there is no compilation step, the
edit-test-debug cycle is incredibly fast. Debugging Python programs is easy: a
bug or bad input will never cause a segmentation fault. Instead, when the
interpreter discovers an error, it raises an exception. When the program
doesn't catch the exception, the interpreter prints a stack trace. A source
level debugger allows inspection of local and global variables, evaluation of
arbitrary expressions, setting breakpoints, stepping through the code a line at
a time, and so on.  Often the quickest way to debug a program is to add a
few print statements to the source: the fast edit-test-debug cycle makes this
simple approach very effective.



 



11.2 Input as CSV File



Reading records from CSV (Comma Separated
Values) is a fundamental necessity in Data Science. Often, we get information
from diverse sources that could be exported in CSV format so that they can be
used by different systems. The Pandas library provides and features the usage
of CSV, by which we are able to study the CSV record in full as well as in
elements for a particular institution of columns and rows.



A CSV document is a textual content
record wherein the values inside the columns are separated by way of a comma. We
should bear in mind that the following records are gift in the file named
input.Csv. You can create this record using home windows notepad through
copying and pasting this data. Save the document as input.Csv by using store As
All documents (*.*) option in notepad. The following code represents how to
import the pandas to an input csv file and read the data from it.



 



 



Import pandas as pd



facts = pd.Read_csv('route/input.Csv')



print (facts)



 



 



11.3 Operations with the use of NumPy



NumPy  ('Numerical Python') is a Python package that
supports numerical calculations. It is a library including multidimensional
array gadgets and a group of workouts for processing arrays.



Using NumPy, a developer can carry out
the subsequent operations:



•           Mathematical
and logical operations on arrays.



•           Fourier
transforms and exercises for form manipulation.



•           “Operations”
related to linear algebra. 



NumPy has built in functions for linear algebra
and random quantity arrays.



11.4 Key Features of Pandas



•           It
is fast and provides an intuitive interface in which  elements of a data frame are colored   green if the result is positive and red if
the result is negative.  Data can be
presented in tables using either default or customized indexing.



•           Includes
tools for loading information into in-reminiscence records gadgets from one-of-     a-kind report codecs.



•           Includes
data alignment and incorporated handling of lacking information.



•           Reshaping
and pivoting of date units.



•           Label-based
cutting, indexing and sub setting of big facts units.



•           Columns
from a data shape may be deleted or inserted.



•           Group
with the aid of information for aggregation and ameliorations.



•           High
overall performance merging and joining of records.



•           Time
Series functionality.







 



 



12.EVALUATION RESULTS



We have developed our proposed system in Pycharm, a desktop
application using Python, PyQT5 and Mysql database. We have created a desktop
application in PyQT5. We store required data in MySQL. We use the Windows
operating system with a 2.20 GHz i5 processor and 8 GB RAM. 



 



For our system we have done two evaluations to find the accuracy of
the KNN ball tree algorithm.



First, we have tested our system using images 37 different images
from the M2VTS Multimodal Face Database which contains human faces with
different face orientations. This was the input data. Later ,we trained those
group of images using the KNN ball tree algorithm .The faces were then detected
and recognized for various face orientations .The detection and recognition
rate was calculated for each face orientation. We can refer to Table 1, below.



In the second evaluation, we have trained the input data with PCA
and LDA algorithms for the frontal face orientation. The detection and
recognition rate were tabulated and was compared with the results of KNN
algorithm and are shown in Table 2, below. 



12.1 Evaluation 1: 



We compared  the results of our
KNN approach with different face orientations and checked the results of face
detection rate and face recognition rate. In Table 1 we can see the result
analysis of Face Orientations vs. KNN Algorithm results.




 
  
  



We compared the results of our KNN approach with PCA and LDA
algorithms for Face Orientations. It is done by
comparing the results of face detection rate and face recognition rate. In
Table 2 we can see the result analysis of KNN vs LDA vs PCA.




 
  
  Algorithm Face Orientations


  
  
  Detection Rate


  
  
  Recognition Rate


  
 
 
  
  KNN


  
  
  (Frontal
  face)


  
  
  98.7%


  
  
  95%


  
 
 
  
  PCA


  
  
  (Frontal
  face)


  
  
  85.0%


  
  
  82%


  
 
 
  
  LDA


  
  
  (Frontal
  face)


  
  
  79.0%


  
  
  74%


  
 





 



 



 



 



 



 



 



 



 



 





 



 









 



 



 



 



 



 



 



 



 



 



 



 


CONCLUSION 



This paper introduces the overall design
idea of the intelligent classroom attendance system. We verify the necessity
and effectiveness of the improvement of face detection and recognition from
multiple angles. We created different modules for our system which are feasible
for the faculty to take the student attendance and for the admin to add student
details into database.  We introduced the
K-NN ball tree algorithm for better facial recognition and detection rates .
Finally, the function and description of the back-end attendance management
system are carried out. The experiment proves that the smart classroom
attendance system based on face recognition technology is efficient and stable,
which effectively reduces the classroom attendance cost. 



 



15.REFERENCES



[1] Jie
Chen, Shiguang Shan, Peng Yang, Shengye Yan, Xilin Chen and Wen Gao1.Novel Face
Detection Method Based on Gabor Features, Sinobiometrics 2004 : Chinese
conference on biometric recognition, vol. 3338, pp. 90-99, 2004



[2]
"Training Support Vector Machines: an Application to Face Detection.”
Edgar Osuna, Robert M. Freund, and Federico Girosi. In Proceedings of 1997 IEEE
Computer Society Conference on Computer Vision and Pattern Recognition, edited
by Deborah Plummer and Ian Torwick. Los Alamitos, CA: June 19



[3]
Zhongfei Zhang;Srihari, R.K.; Rao,A. Face detection and its applications in
intelligent and focused image retrieval [archive], IEEE International
Conference on Tools with Artificial In-telligence, 1999.



[4]  H.A. Rowley, S. Baluja, and T. Kanade. Neural
network-based face detection. Trans. on PAMI, 20(1), 1998.



[5] Md.
Abdur Rahim, Md. Najmul Hossain, Tanzillah Wahid, Md. Shafiul Azam, "Face
Recognition using Local Binary Patterns", Global Journal of Computer
Science and Technology Graphics & Vision, vol. 13, no. 4, 2013.



[6] H.
Bay, A. Ess, T. Tuytelaars, L. V. Gool, "Speeded-Up Robust Features
(SURF)", Computer Vision and Image Understanding, vol. 110, no. 3, pp.
346-359, 2008.



[7]  Chuan-Yu Chang, Chang-Wang Chang, Ching-Yu
Hsieh, "Applications of Block Linear Discriminant Analysis for Face
Recognition", Journal of Information Hiding and Multimedia Signal
Processing, vol. 2, no. 3, pp. 259-269, 2011.



[8] Ke,
Y., Sukthankar, R.: PCA-SIFT: A more distinctive representation for local image
descriptors. In: CVPR (2). (2004) 506 – 513.[9] Y. Li, Xiang-lin
Qi, Yun-jiu Wang, Eye detection by using fuzzy template matching and
feature-parameter based judgement Pattern Recognition Letters 22 (2001)
1111-1124



[10] Anil K. Jain, Arun Ross and
SalilPrabhakar, “An introductionto biometric recognition”, Circuits and Systems
for VideoTechnology, IEEE Transcations on Volume 14, Issu 1, Jan 2004



Page(s):4-2



[11] Kamran Etemad and Rama Chellappa,
Discriminant analysis for recognition of human face images, Optical Society of
America,  Vol. 14, No. 8/ August 1997.



[12] Dulal Chakraborty
Lecturer Department of Information & Communication Technology, Comilla
University, Comilla, Bangladesh: Face Recognition using Eigenvector and
Principle Component Analysis  International
Journal of Computer Applications (0975 – 8887) Volume 50 – No.10, July 2012



 



 



 



 



 
