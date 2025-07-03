from flask import render_template, request, redirect, url_for
from app.utils import generate_random_string, load_data, save_data
from flask import session
from app.sensitivity.passwords import _user_, _password_

def setup_routes(app):
    @app.route("/")
    def index():
        projects_list = load_data()
        return render_template("index.html", projects=projects_list)
    
   
    @app.route("/admin", methods=['GET','POST'])
    def admin():
        print("usaurio logado", session.get("logged_in"))
        if not session.get("logged_in"):
            return redirect(url_for("loginadmin"))
        if request.method == "POST":
            name_project = request.form.get("name_project")
            description = request.form.get("description")
            link = request.form.get("link")
            linkedin = request.form.get("linkedin")
            projects_list= load_data()
            new_project = {
                "name": name_project,
                "description": description,
                "link": link,
                "linkedin": linkedin
            }
            projects_list.append(new_project)

            save_data(projects_list)
            return redirect(url_for("logout"))
            


        return render_template("admin.html")

    @app.route("/loginadmin", methods=["GET", "POST"])
    def loginadmin():
        if request.method == "POST":
            user = request.form.get("user")
            password = request.form.get("password")
            print("test")
            if user == _user_ and password == _password_:
                session["logged_in"] =  True
                return redirect(url_for("admin"))

        return render_template("loginadmin.html")
    
    @app.route("/logout")
    def logout():
        session.pop("logged_in", None)
        return redirect(url_for("loginadmin"))