Workflow
=========

Recommended Program:
^^^^^^^^^^^^^^^^^^^^

Pycharm (Version: 2021.1.1,  Build: 211.7142.13)

Preparation:
^^^^^^^^^^^^

Download Large file following below.

https://www.dropbox.com/sh/udxkj8udbc2z9wp/AAAWcpLN7s-VJ1Im1CN5Rme6a?dl=0

File Directory: final_project_face_recognition/ <<Downloaded File HERE>

.. image:: https://usister.com/usister_uploads/2021/05/directory_deeplearning.png
  :width: 800
  :alt: File Dicrectory



Workflow:
^^^^^^^^^

1. "Run 'final_project_face_r....' prepared deep learning files (path: final_project_face_recognition/final_project_face_recognition.py)

.. image:: https://usister.com/usister_uploads/2021/05/Screen-Shot-2021-05-02-at-6.44.28-PM.png
  :width: 800
  :alt: Load deep learning files

.. image:: https://usister.com/usister_uploads/2021/05/Screen-Shot-2021-05-11-at-4.36.47-PM.png
  :width: 800
  :alt: Run deep learning files

2. Type First name, Last name and Age on pycharm or similar program

.. image:: https://usister.com/usister_uploads/2021/05/face_detection.gif
  :width: 800
  :alt: Type name and age


3. Computer live cam video open (After 30 frame, the live video will automatically turn off.
If you want to quit the program before 30 frame, click "q" button.)


    while cap.isOpened():
        try:


4. Detect predicted age with accuracy, predicted gender with accuracy and difference between predicted age and real age

.. image:: https://usister.com/usister_uploads/2021/05/face_video.jpg
  :width: 800
  :alt: File Dicrectory

1 = Gender

2 = Gender accuracy

3 = predicted Age

4 = Predicted Age accuracy

5 = Compare real age and predicted Age

    # age different print
    ageDiff = int(age_input) - int(age)
    age_exp.append(int(age))
    outStr = ""
    if ageDiff >=0:
        outStr = "You look " + str(ageDiff) + " years younger than actual age"
    else:
        ageDiff = abs(ageDiff)
        outStr = "You look " + str(ageDiff) + " years order than actual age"


5. After predicting 30 frame of video picture, it will automatically turn off live cam video. (these input and output information will be used to select personalized cosematics.)

    while cap.isOpened():
        try:

     . . . . . . . . . . . . . . . .

            cv2.imshow('frame', read_frame)
            if frameCount == 30:
                break
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break


6. Sort age lists (example sorted age: [37,37,35,35,34,34,34........27,27,26,26,26,24] )

    age_exp = []

    . . . .

    age_exp.sort()


7. Only use age list 10:20 (excluded 1~9 and 20~30), then find average of predicted age. (Note: Considered 1/3 of sorted front and 1/3 of sorted ends are outliers. You may lower percentage of outliers)

    age_exp = []
    age_exp.sort()
    age_extTemp = age_exp[10:20]
    ageTempSum=0
    for i in age_extTemp:
        ageTempSum += i
    age_expMean = ageTempSum / len(age_extTemp)
    age_expMean = round(age_expMean)
    age_diff = age_actual - age_expMean


8. Save hashed name, real age, predicted age, difference between age and real age and recommended Ingredient for user treatment (ex ingredient A or B) to output.csv
(saved data path: final_project_face_recogntion / data / )

Note:

- output.csv: save currently run file only

- outputCumm.csv: atomically save and keep append data from output.csv information

.. image:: https://usister.com/usister_uploads/2021/05/Screen-Shot-2021-05-11-at-9.41.09-PM.png
  :width: 800
  :alt: File Dicrectory

.. image:: https://usister.com/usister_uploads/2021/05/Screen-Shot-2021-05-11-at-9.41.18-PM.png
  :width: 800
  :alt: File Dicrectory


9. Atomically save file to outputCumm.csv (When new user run again, data keep appended)

Note:

- output.csv: save currently run file only

- outputCumm.csv: atomically save and keep append data from output.csv information

.. image:: https://usister.com/usister_uploads/2021/05/Screen-Shot-2021-05-11-at-9.43.22-PM.png
  :width: 800
  :alt: File Dicrectory

.. image:: https://usister.com/usister_uploads/2021/05/Screen-Shot-2021-05-11-at-9.41.25-PM.png
  :width: 800
  :alt: File Dicrectory
