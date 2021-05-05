import json
import os
from pprint import pprint

# from test_pset import *
#from canvasapi import Canvas
#from environs import Env
from git import Repo
from pset_1.hash_str import *
from pset_1.canvas import *
from utils.io import atomic_write
import pandas as pd

def get_user_hash(username, salt=None):
    salt = salt or get_csci_salt()
    return hash_str(username, salt=salt)

# return filename only
def getFilename(fullname):
    return os.path.splitext(fullname)[0]

# return extension only
def getExtension(fullname):
    return os.path.splitext(fullname)[-1]

# This method does 2 things
# [1] write parquet file using atomic write
# [2] return name of the parquet file name with dir info str
def xlsxToParquet(data_source):
    # concat parquet extension with filename from data source
    parquetFileName = getFilename(data_source) + ".parquet"
    # need to remove in case if same file name exists
    os.path.exists(parquetFileName) and os.remove(parquetFileName)

    # xlsx to dataframe
    # print(data_source)
    metaDF = pd.read_excel(data_source)
    # run io
    # pandas documentation-> The default io.parquet.engine behavior is to try ‘pyarrow’, falling back to ‘fastparquet’ if ‘pyarrow’ is unavailable.
    # conversion
    with atomic_write(parquetFileName, as_file=False) as p:
        metaDF.to_parquet(p, engine="auto")
    # print("converted")
    return parquetFileName

def columnOfParquet(parquetFile, colName):
    return pd.read_parquet(parquetFile, engine="auto", columns=[str(colName)])




if __name__ == "__main__":
    # print(get_user_id("Jaemin Lee"))
    # print(get_user_id("dlwoalsgg"))

    data_source = "data/hashed.xlsx"
    # convert hashed xlsx file to parquet file and return the name of the parquet file
    parquetData = xlsxToParquet(data_source)
    # reading back the id col the parquet file to print out(first 5 sorted id to submit)
    print("here")
    # get sorted first five hashed id from the df
    col = columnOfParquet(parquetData,"hashed_id")
    colList = col.values.tolist()
    colListSorted = sorted(colList)
    colList = [i[0] for i in colListSorted]
    firstFive = colList[0:5]

    # salt question
    for user in ["gorlins", "dlwoalsgg"]:
        print("Id for {}: {}".format(user, get_user_id(user)))

    # TODO: read in, save as new parquet file, read back just id column, print
    repo = Repo(".")
    # Load environment
    env = Env()
    env.read_env()
    as_user_id = env.int("CANVAS_AS_USER_ID", 0)  # Optional - for test student

    if as_user_id:
        masquerade = dict(as_user_id=as_user_id)
    else:
        masquerade = {}

    if repo.is_dirty() and not env.bool("ALLOW_DIRTY", False):
        raise RuntimeError(
            "Must submit from a clean working directory - commit your code and rerun"
        )

    # Load canvas objects
    canvas = Canvas(env('CANVAS_URL'), env('CANVAS_TOKEN'))

    course = canvas.get_course(env('CANVAS_COURSE_ID'), **masquerade)
    assignment = course.get_assignment(env('CANVAS_ASSIGNMENT_ID'), **masquerade)
    quiz = course.get_quiz(env('CANVAS_QUIZ_ID'), **masquerade)

    # Begin submissions
    url = "https://github.com/csci-e-29/{}/commit/{}".format(
        os.path.basename(repo.working_dir), repo.head.commit.hexsha
    )  # you MUST push to the classroom org, even if CI/CD runs elsewhere (you can push anytime before peer review begins)

    qsubmission = None
    try:
        # Attempt quiz submission first - only submit assignment if successful
        qsubmission = quiz.create_submission(**masquerade)
        questions = qsubmission.get_submission_questions(**masquerade)

        # Get some basic info to help develop
        for q in questions:
            print("{} - {}".format(q.question_name, q.question_text.split("\n", 1)[0]))

            # MC and some q's have 'answers' not 'answer'
            pprint(
                {
                    k: getattr(q, k, None)
                    for k in ["question_type", "id", "answer", "answers"]
                }
            )
            print()

        # Submit your answers
        answers = get_answers(questions,firstFive)
        pprint(answers)
        responses = qsubmission.answer_submission_questions(
            quiz_questions=answers, **masquerade
        )

    finally:
        if qsubmission is not None:
            completed = qsubmission.complete(**masquerade)
            # Only submit assignment if quiz finished successfully
            submission = assignment.submit(
                dict(
                    submission_type="online_url",
                    url=url,
                ),
                comment=dict(
                    text_comment=json.dumps(get_submission_comments(repo, qsubmission))
                ),
                **masquerade,
            )

    pass
