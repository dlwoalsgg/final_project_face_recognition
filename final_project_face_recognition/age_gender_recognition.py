import cv2
import dlib

from os.path import join

# model_path -> basic model,
# pass to caffemodel to test
# prototxt -> arcitechture described


def load_model(model_path, caffemodel, prototxt):
    caffemodel_path = join(model_path, caffemodel)
    prototxt_path = join(model_path, prototxt)
    load_predict_model = cv2.dnn.readNet(prototxt_path, caffemodel_path)

    return load_predict_model


# model -> model , image -> imput data
def predict_func(load_predict_model, img, height, width):
    # generating binary blob data from image object
    face_blob = cv2.dnn.blobFromImage(img, 1.0, (height, width), (0.485, 0.456, 0.406))
    load_predict_model.setInput(face_blob)
    predictions = load_predict_model.forward()
    predict_result = predictions[0].argmax()
    confidence = predictions[0][predict_result]
    print(predict_result)
    ######
    # if 1 > confidence > 18
    #     print("add ")

    ####

    return predict_result, confidence
# predict_result -> return index of class 0= woman , 1 for man // age 1~100


# use dlib library to extract face detection
# detect face then crop it
face_detect = dlib.get_frontal_face_detector()
font, fontScale, fontColor, lineType = cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2

input_height = 224
input_width = 224

# load gender model (path to models)
gender_model_path = 'age_prediction_data/gender'
gender_caffemodel = 'gender.caffemodel'
gender_prototxt = 'gender.prototxt' # architecture
gender_model = load_model(gender_model_path, gender_caffemodel, gender_prototxt)

# load age model (path to models)
age_model_path = 'age_prediction_data/age'
age_caffemodel = 'age.caffemodel'
age_prototxt = 'age.prototxt' # arcjotectire
age_model = load_model(age_model_path, age_caffemodel, age_prototxt)


# input age
user_first_name = str(input("Enter your last name"))
user_last_name = str(input("Enter your first name"))
age_input = int(input("Enter age number only"))
print(age_input)


# capture video
cap = cv2.VideoCapture(0)

while cap.isOpened(): # while capture open
    try:
        _, read_frame = cap.read()  # reading frames

        if read_frame is not None:  # if the frame is fine
            frame_rgb = cv2.cvtColor(read_frame, cv2.COLOR_BGR2RGB)  # convert to color skim (convert from BGR to RGB)
            faces = face_detect(frame_rgb, 1)  # dectecting face or faces (if 2 or more faces, still detect

            #iterate all the face that detected on image
            for d in faces:
                left = int(0.6 * d.left())  # + 40% margin
                top = int(0.6 * d.top())  # + 40% margin
                right = int(1.4 * d.right())  # + 40% margin
                bottom = int(1.4 * d.bottom())  # + 40% margin
                face_segm = frame_rgb[top:bottom, left:right]  # segment top bottom, left and right
                # passing face segment to predict function
                gender, gender_confidence = predict_func(gender_model, face_segm, input_height, input_width)
                age, age_confidence = predict_func(age_model, face_segm, input_height, input_width)
                gender = 'man' if gender == 1 else 'woman'
                predict_text = '{} ({:.2f}%) {} ({:.2f}%)'.format(gender, gender_confidence * 100, age,  #to show lower age - x number
                                                                  age_confidence * 100)

                recommend_text = '{}'

                # age different print
                ageDiff = int(age_input) - int(age)
                outStr = ""
                if ageDiff >=0:
                    outStr = "You look " + str(ageDiff) + " years younger than actual age"
                else:
                    ageDiff = abs(ageDiff)
                    outStr = "You look " + str(ageDiff) + " years order than actual age"



                bottomLeftCornerOfText = (10, 50)
                lineType = 2
                # text = '{} ({:.2f}%) {} ({:.2f}%) your actual age is {}. '.format(gender, gender_confidence * 100, age, #to show lower age - x number
                #                                           age_confidence * 100, age_input)
                # adding text (slightly higer rectanglar -> -20)
                cv2.putText(read_frame, predict_text, (d.left(), d.top() - 20), font, fontScale, fontColor, lineType)
                cv2.rectangle(read_frame, (d.left(), d.top()), (d.right(), d.bottom()), fontColor, 2)
                cv2.putText(read_frame, outStr,bottomLeftCornerOfText, font, fontScale, fontColor, lineType)



        cv2.imshow('frame', read_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    except:
        print('Image quality do not meet qualification. Skipping frame')

cap.release()
cv2.destroyAllWindows()


# def enter_age(age_input):
#     age_input = int(input("Enter age number only"))
#     return age_input
#
#
# enter_age(cap).release()
# cv2.destroyAllWindows()