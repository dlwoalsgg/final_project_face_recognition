# Final Project


Add any badges to your ***published documentation*** up here!


Detect Age and Gender to create personalized formulation
========================================================


face recognition: Age and Gender
================================

<p align="center">
  <img src="https://www.dropbox.com/home/face_recog_github_pic?preview=directory_deeplearning.png" width="350" title="hover text">
</p>


![alt text](https://www.dropbox.com/home/face_recog_github_pic?preview=directory_deeplearning.png)



Workflow:

1. Run prepared deepl earning files (path: final_project_face_recognition/final_project_face_recognition.py)

2. Type First name, Last name and Age

3. Computer live cam video open

4. Detect predicted age with accuracy, predicted gender with accuracy and difference between predicted age and real age

5. After predicting 30 frame of video picture automatically turn off live cam video

6. Sort age lists (example sorted age: [37,37,35,35,34,34,34........27,27,26,26,26,24] )

7. Only use age list 10:20 (excluded 1 to 9 and 20 to 30), then find average of predicted age

8. Save hashed name, real age, predicted age, difference between age and real age and recommended Ingredient for user treatment (ex ingredient A or B) to output.csv

9. Atomically save file to outputCumm.csv (When new user run again, data keep appended)

Note:

- output.csv: save currently run file only

- outputCumm.csv: keep append data from output.csv information




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
