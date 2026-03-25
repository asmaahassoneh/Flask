from flask import Blueprint, render_template, request, redirect, url_for
from data.store import students

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return render_template("index.html")


@main.route("/register", methods=["GET", "POST"])
def register():
    error = None

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        student_id = request.form.get("student_id", "").strip()
        gpa_raw = request.form.get("gpa", "").strip()
        major = request.form.get("major", "").strip()

        if not name or not student_id or not gpa_raw or not major:
            error = "All fields are required."
            return render_template("register.html", error=error)

        for student in students:
            if student["student_id"] == student_id:
                error = "Student ID already exists."
                return render_template("register.html", error=error)

        try:
            gpa = float(gpa_raw)
            if not (0 <= gpa <= 4):
                error = "GPA must be between 0 and 4."
                return render_template("register.html", error=error)
        except ValueError:
            error = "GPA must be a valid number."
            return render_template("register.html", error=error)

        student = {
            "name": name,
            "student_id": student_id,
            "gpa": gpa,
            "major": major,
        }

        students.append(student)
        return redirect(url_for("main.student_list"))

    return render_template("register.html", error=error)


@main.route("/students")
def student_list():
    return render_template("students.html", students=students)
