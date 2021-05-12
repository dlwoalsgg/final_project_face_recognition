# Final Project

The documentation for this project is available here:

Add any badges to your ***published documentation*** up here!

https://final-project-face-recognition.readthedocs.io/en/latest/?version=latest

[![Documentation Status](https://readthedocs.org/projects/final-project-face-recognition/badge/?version=latest)](https://final-project-face-recognition.readthedocs.io/en/latest/?badge=latest)

[![Build Status](https://travis-ci.com/dlwoalsgg/final_project_face_recognition.svg?branch=main)](https://travis-ci.com/dlwoalsgg/final_project_face_recognition)

[![Maintainability](https://api.codeclimate.com/v1/badges/26bc0db340ad87ec9500/maintainability)](https://codeclimate.com/github/dlwoalsgg/final_project_face_recognition/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/26bc0db340ad87ec9500/test_coverage)](https://codeclimate.com/github/dlwoalsgg/final_project_face_recognition/test_coverage)


![alt text](https://usister.com/usister_uploads/2021/05/face_detection.gif)


Preparation: After Download Large File Following Below, and Run it. Otherwise Travis, Codeclimate and program will fail.
===========================================================================================================

https://www.dropbox.com/sh/udxkj8udbc2z9wp/AAAWcpLN7s-VJ1Im1CN5Rme6a?dl=0

File Directory: final_project_face_recognition/age_prediction_data(Downloaded File HERE)


Detect Age and Gender to create personalized formulation
========================================================


Workflow
=========

Recommended Program:

Pycharm (Version: 2021.1.1,  Build: 211.7142.13)

Preparation

Download Large file following below.

https://www.dropbox.com/sh/udxkj8udbc2z9wp/AAAWcpLN7s-VJ1Im1CN5Rme6a?dl=0

File Directory: final_project_face_recognition/ <<Downloaded File HERE>

![alt text](https://usister.com/usister_uploads/2021/05/directory_deeplearning.png)


Workflow:
^^^^^^^^^

1. "Run 'final_project_face_r....' prepared deep learning files (path: final_project_face_recognition/final_project_face_recognition.py)

![alt text](https://usister.com/usister_uploads/2021/05/Screen-Shot-2021-05-02-at-6.44.28-PM.png)

![alt text](https://usister.com/usister_uploads/2021/05/Screen-Shot-2021-05-11-at-4.36.47-PM.png)


2. Type First name, Last name and Age on pycharm or similar program

![alt text](https://usister.com/usister_uploads/2021/05/Screen-Shot-2021-05-11-at-4.40.46-PM.png)

3. Computer live cam video open (After 30 frame, the live video will automatically turn off.
If you want to quit the program before 30 frame, click "q" button.)


    while cap.isOpened():
        try:


4. Detect predicted age with accuracy, predicted gender with accuracy and difference between predicted age and real age

![alt text](https://usister.com/usister_uploads/2021/05/face_video.jpg)

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


![alt text](https://usister.com/usister_uploads/2021/05/Screen-Shot-2021-05-11-at-9.41.09-PM.png)

![alt text](https://usister.com/usister_uploads/2021/05/Screen-Shot-2021-05-11-at-9.41.18-PM.png)


9. Atomically save file to outputCumm.csv (When new user run again, data keep appended)

Note:
- output.csv: save currently run file only

- outputCumm.csv: atomically save and keep append data from output.csv information


![alt text](https://usister.com/usister_uploads/2021/05/Screen-Shot-2021-05-11-at-9.43.22-PM.png)

![alt text](https://usister.com/usister_uploads/2021/05/Screen-Shot-2021-05-11-at-9.41.25-PM.png)



###################################################################

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Documenting your project](#documenting-your-project)
  - [Set up](#set-up)
  - [The writeup](#the-writeup)
    - [Requirements](#requirements)
  - [Build and publish](#build-and-publish)
    - [Read the Docs](#read-the-docs)
    - [GithubPages](#githubpages)
    - [Your own host](#your-own-host)
    - [Private options](#private-options)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Documenting your project

The main deliverable for your final project is the ***documentation*** you
provide here, in this repo, and where it is build.

We will be using [Sphinx](https://www.sphinx-doc.org/) to build static
documentation for your project, including any overview writeup, etc.

### Set up

Sphinx is trivial to set up.  You can use a cookiecutter template that includes
Sphinx, eg [cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage), or just follow the [quickstart](https://www.sphinx-doc.org/en/master/usage/quickstart.html).

### The writeup

Whether or not you actually add your main project code to this repository is up
to you.  Because we cannot assume you can deliver your code entirely to us (and
it would be hard for us to evaluate, anyways), you should treat the deliverable
here more like a paper than a code submission.

Please 'document' your project using Sphinx, a static site generator, to build
an HTML page that describes your project.

#### Requirements

Requirements are loose due to project flexibility, but as a guideline you should
include:

* An intro page to the problem

* An overview of your solution

* Ideally some diagram of the architecture

* Tangible snippets of python code in your discussion

* Some amount of [sphinx
autodoc](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html),
either from your 'real' code, or from toy snippets you include to describe
your approach, and some other sphinx cross references.

* A conclusion of the main learnings or contributions of your project

* Your Science Fair presentation should be similar to the content in the
writeup, but the writeup is your chance to go deeper into the topics and
really explain/demonstrate etc in more depth.

### Build and publish
It is easy to build sphinx documentation locally, but that is not good enough
for sharing.  You need to find a way to share your write up with us!  You have
a few options.

The biggest decision is whether you want your documentation and/or this repo
to be publicly viewable.

Note: you still need to 'submit' your assignment via CI/CD, just to ensure we
have the correct commit/tag of your repo, even if RTD/Github is doing most of
the build.  However, there is no explicit need for testing.

#### Read the Docs

It is very easy to publish sphinx docs on [Read the
Docs](https://readthedocs.org/)! The only caveat is that it requires your repo
to be public (that's fine from the teaching staff's point of view) and your docs
will be public too.  Go ahead and sign up, hook up your repo, and you are good
to go!

#### GithubPages

Github also can publish a webpage for you, based on sphinx in your repo.  The
Pages will be publicly viewable, but your repo can remain private.  Here is
[one example
walkthrough](https://www.docslikecode.com/articles/github-pages-python-sphinx/).

#### Your own host

Feel free to find another way to publish your docs!  We just require that it use
Sphinx and is automatically built from your master branch using CI/CD.

#### Private options

If you are not comfortable publishing your documentation publicly, you can still
build your sphinx project in CI/CD, zip up the build artifact, and upload that
to Canvas.  Your submission in this case will be the zipped html rather than the
link to this repo; ensure you still have the repo link in the submission
comments.
