# Whatsapp

## This project mainly consists html and css and javascript with a two scripts of python.

#### This project can be used without knowledge about flask.
#### Although it is advised to use flask for future projects as it is much easy to deploy and work upon.

### Basic flow of the Front-end:
* **Index page/Home page is just a start to welcome all the users and take them to the uploading page or collaborators page.**
* **Analyse page shows you the instructions on how to extract chats either from Android or iOS. It also has an upload space to chose file and upload.**
* **It is clearly mentioned in analyse.html that any file above 3000000 bytes(3Mb) won't be allowed to upload.**
* **The button click will take to analysis.html where you can see all the graphs created by matplotlib in the python script(```final.py```).**

----------

### How to store the python scripts:
* **The script ```final.py``` is just using the pre-trained model(we have a model file).**
* **The exported chats in .txt file is transformed into a table of data so it can be accessible by dataframes of pandas.**
* **All the graphs are stored in 'images/' and it will be accessed by analysis.html .**

----------

### How to train your own model?

* **Open a jupyter notebook in your project directory and compile this statement =>`nltk.download('movie_reviews') `**
* **After doing that copy the code of ```train.py``` in the next cell and run it.** 

* **You can see how to train your own model and store that .model file in your directory in ```train.py```.**
* **We separated the training code from the whole main script as you don't need to run it everytime you need an output.**
* **Before compiling ```final.py``` run ```train.py``` and then you don't have any work with train.py**

----------
#### Note: The images in 'images' folder are mostly not relevent to the project. The images with commit ```new works``` are the ones you get as output after running the ```final.py```. So delete all the pics in images folder and then start doing the project(It contains bg-image for the html page too).
----------
#### We are deleting our exported chats from this repo. You may come across an error on line '54' in ```final.py``` so export your own chats and rename them or change the path in he python script.
----------

### To install the required packages run this command in you command_prompt(terminal/shell):

```pip install -r requirements.txt```

#### Note: You have to be in the project directory and then run this command, not in the admin or system32.
#### Note: Create a folder named 'upload' in the main directory of the project. After uploading the chats in html page, the .txt file will get uploaded here so that ```final.py``` can access it to analyse it.
#### Note: Remember to run ```train.py``` and create a model file first. You can understand how it is trained from the same.
# Thank You
