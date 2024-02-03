# This is a server file which basically connects our files from the back to the browser via the flask framework. How to install and activate the flask framework is pretty easy and can be seen in the flask documentation. Once set up, we can go ahead and grab those files which we need to put on server and connect to the front using these steps.

# after installinng and activating Flask in the terminal and afetr creating the virtual environment, we will import like this.
import csv
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
print(__name__)


# These decorators help us grabbing the files which we need by a function in flask called render_template(). This function by default grabs HTML files by looking in a "templates" folder so we can create one and put our files in it.
#Main page
@app.route("/")
def my_home():
    return render_template("./index.html")

# Similarly like above the root file, we can add different routes to our link and display them with differemt html files.

# The parameters passed will automatically take the file name or the page name and display them accordingly. That way we don't have to write the same piece of code again and again for different pages.
@app.route("/<string:page_name>")
def html_pages(page_name):
    return render_template(page_name)

# This function will get the data the user entered in the contact form and will save that information in a separate file which we created database.txt
def write_to_file(data):
    with open("./templates/database.txt", mode="a") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f"\n{email}, {subject}, {message}")

# Here we are doing the same thing as above but in a more professional format that is CSV file rather than just text. For this we need to import the csv library. Refer to the Python documentation.
def write_to_csv(data):
    with open("./templates/database.csv", newline='',mode="a") as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=",", quotechar="'", quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


# We can put the <username>, so that whatever name is enetered via html file, it can be directly shown. These are called as URL paramters in Flask documentation. Basically, we put parameters to our URL through which a person can get to the desired page.

# Now all these HTML fils would run but without any CSS and JS functionality.

# We can connect the CSS and JS files (static files) too but we don't need specific decorators for that as they are already connected and referenced in HTML files. Normally what flask does is that it looks for static files in specifically a folder named "static" so we need to create this folder and put our CSS and JS files in it. So, after creating this folder, make sure that you change the path of these files in your HTML files as well.

# Normally the way we would turn the server on would be:
#               $ flask --app (name of file) run
# This would start the server running but the debug mode would be off. And any change we do in the files, the server will have to be restarted in order to view the change. But we can turn the debug mode on which will help us to make changes and not restart the server again and again to view changes made. That can be done by:
#               $ flask --app (name of file) run --debug

# Getting data entered in the contact form
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST": # This POST will send the entered info to the server
        try: 
            data = request.form.to_dict() # Here we are getting that data and turning it into a dictionary
            write_to_file(data)
            write_to_csv(data)
            return redirect("thankyou.html")
        except:
            return "did not save to database"
    else:
        return ("Something went wrong....")