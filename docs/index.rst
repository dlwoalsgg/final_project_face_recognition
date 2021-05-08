<<<<<<< HEAD
Detect Age and Gender to create personalized formulation
========================================================


face recognition: Age and Gender
================================

Workflow:

1. Run prepared deepl earning files (path: final_project_face_recognition/final_project_face_recognition.py)

2. Type First name, Last name and Age

3. Computer live cam video open

4. Detect predicted age with accuracy, predicted gender with accuracy and difference between predicted age and real age

5. After predicting 30 frame of video picture automatically turn off live cam video

6. Sort age lists (example sorted age: [37,37,35,35,34,34,34........27,27,26,26,26,24] )

7. Only use age list 10:20 (excluded 1~9 and 20~30), then find average of predicted age

8. Save hashed name, real age, predicted age, difference between age and real age and recommended Ingredient for user treatment (ex ingredient A or B) to output.csv

9. Atomically save file to outputCumm.csv (When new user run again, data keep appended)

Note:

- output.csv: save currently run file only

- outputCumm.csv: keep append data from output.csv information


    print 'hello'
    >> hello

Guide
^^^^^

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   readme
   installation
   modules
   usage
   modules
   contributing
   authors
   history

Indices and tables
==================
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
