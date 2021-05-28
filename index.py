from flask import Flask, redirect, request, render_template, session, url_for
import mysql.connector
from flask_mail import Mail, Message

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="institute"
)

app = Flask(__name__)
app.secret_key = "123"
mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'infoparshwaeducation@gmail.com'
app.config['MAIL_PASSWORD'] = 'aryan123@'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route("/insertt", methods=['POST', 'GET'])
def index():
    try:

        Name = request.form['name']
        email = request.form['email']
        mess = request.form['message']
        mycursor = mydb.cursor()
        sql = "INSERT INTO `contact`(`Name`, `email`, `mess`) VALUES (%s,%s,%s)"
        val = (Name, email, mess)
        mycursor.execute(sql, val)
        mydb.commit()
        msg = Message('Parshwa Education', sender='infoparshwaeducation@gmail.com', recipients=[email])
        print(msg, sql, val)
        msg.body = "Hello, Thanks For Contact Us For More Inquiry Or detail visit our website or Institute"
        mail.send(msg)
        # top = Tk()
        # top.geomety(100*100)
        # messagebox.showinfo("hello","submitted")
        # top.mainloop()
        # return "Sent"
        # return render_template("contact.html")

        #     return "<html><head></head><body><script>alert('UserName Or Passwor Is Wrong');</script><script>window.location='/contact';</script></body></html>"
        # else:
        #     return "<html><head></head><body><script>alert('done');</script><script>window.location='/contact';</script></body></html>"
    except Exception as e:
        # return render_template("index.html")
        return (str(e))


@app.route("/")
def website():
    # return "Hello"
    print("@@@@@@@@@@@@@@@@@hiiiiiiiiii")
    curss = mydb.cursor()
    curss1 = mydb.cursor()
    curss2 = mydb.cursor()
    curss3 = mydb.cursor()
    curss4 = mydb.cursor()
    curss5 = mydb.cursor()
    curss.execute("SELECT * FROM `subject` limit 3")
    db = curss.fetchall()
    curss1.execute("SELECT * FROM `news`")
    db1 = curss1.fetchall()
    curss2.execute("SELECT count(*) from teacher")
    db2 = curss2.fetchall()
    curss3.execute("SELECT count(*) from teacher")
    db3 = curss3.fetchall()
    curss4.execute("SELECT count(*) from subject")
    db4 = curss4.fetchall()
    curss5.execute("SELECT count(*) from news")
    db5 = curss5.fetchall()
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    return render_template("index.html", db=db, db1=db1,db2=db2,db3=db3,db4=db4,db5=db5)



@app.route("/about")
def about():
    curss = mydb.cursor()
    curss1 = mydb.cursor()
    curss.execute("SELECT * FROM `teacher` WHERE status='Active'")
    db = curss.fetchall()
    curss1.execute("SELECT * FROM `skill`")
    db1 = curss1.fetchall()
    return render_template('about.html', db=db, db1=db1)


@app.route("/contact")
def contact():
    return render_template('contact.html')


@app.route("/course")
def course():
    curss = mydb.cursor()
    # curss1 = mydb.cursor()
    curss.execute("SELECT * FROM `subject` WHERE 1")
    db = curss.fetchall()
    # curss1.execute("SELECT * FROM `skill`")
    # db1 = curss1.fetchall()
    return render_template('course.html', db=db)


# @app.route("/course_index")
# def course_index():
#     curss = mydb.cursor()
#     curss.execute("SELECT * FROM `subject`")
#     db5 = curss.fetchall()
#     return render_template('course.html', db5=db5)
#

@app.route("/regi_form")
def registration():
    return render_template('registration.html')


# @app.route("/admin_page")
# def page():
#     return render_template('admin/page.html')


@app.route("/admin_signup")
def signup():
    courss = mydb.cursor()
    courss.execute("SELECT subject.sub_name FROM `subject` WHERE 1")
    db = courss.fetchall()
    return render_template('admin/signup.html', db=db)


# @app.route("/insertt",methods=['POST', 'GET'])
# def inss():
#     try:
#
#         Name = request.form['name']
#         email = request.form['email']
#         mess = request.form['message']
#         mycursor = mydb.cursor()
#         sql = "INSERT INTO `contact`(`Name`, `email`, `mess`) VALUES (%s,%s,%s)"
#         val = (Name,email,mess)
#         mycursor.execute(sql, val)
#         mydb.commit()
#         return render_template("contact.html")
#
#     except Exception as e:
#         # return render_template("index.html")
#         return (str(e))
#
#

@app.route("/insert", methods=['POST', 'GET'])
def ins():
    try:

        # img = request.form['img']
        name = request.form['FName']
        Mname = request.form['MName']
        lname = request.form['LName']
        contact = request.form['txtNo']
        email_id = request.form['Email']
        password = request.form['Password']
        gender = request.form['optradio']
        bdate = request.form['SelectedDate']
        course = request.form['Course']
        address = request.form['Add']
        mycursor = mydb.cursor()
        sql = "INSERT INTO `registration`(`Name`,`Email_id`,`Contact`,`Password`,`Mname`,`lname`,`gender`,`bdate`,`course`,`address`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (name, email_id, contact, password, Mname, lname, gender, bdate, course, address)
        mycursor.execute(sql, val)
        mydb.commit()


        msg = Message('Parshwa Education', sender='infoparshwaeducation@gmail.com', recipients=[email_id])
        msg.body = "Hello, You Username is :: '" + email_id + "' And Password is:: '" + password + "' "
        mail.send(msg)
        # return "Sent"
        return redirect('/admin_signup')

    except Exception as e:
        # return render_template("index.html")
        return (str(e))


@app.route("/course_insert", methods=['POST', 'GET'])
def course_ins():
    try:

        img = request.form['img']
        Course_Name = request.form['Course_Name']
        by = request.form['by']
        # date = request.form['date']
        info = request.form['info']
        mycursor = mydb.cursor()
        sql = "INSERT INTO `course`(`img`, `Course_Name`, `by`, `info`) VALUES (%s,%s,%s,%s)"
        val = (img, Course_Name, by, info)
        mycursor.execute(sql, val)
        mydb.commit()
        return render_template("admin/default.html")

    except Exception as e:
        # return render_template("index.html")
        return (str(e))


#
# @app.route("/admin_sub")
# def sub():
#     return render_template('admin/subject.html')
#

@app.route("/admin_user")
def user():
    return render_template('admin/user.html')


@app.route("/user_insert", methods=['POST', 'GET'])
def user_ins():
    try:

        Name = request.form['Name']
        password = request.form['password']
        mycursor = mydb.cursor()
        sql = "INSERT INTO `user`(`Name`,`password`) VALUES (%s,%s)"
        val = (Name, password)
        mycursor.execute(sql, val)
        mydb.commit()
        return render_template("admin/user.html")

    except Exception as e:
        # return render_template("index.html")
        return (str(e))


# @app.route("/admin_teacher")
# def teacher():
#     return render_template('admin/teacher.html')


@app.route("/teacher_insert", methods=['POST', 'GET'])
def teacher_ins():
    try:
        img = request.form['img']
        Name = request.form['Name']
        info = request.form['info']
        password = request.form['password']
        # Status = request.form['Status']
        mycursor = mydb.cursor()
        sql = "INSERT INTO `teacher`(`img`, `Name`, `info`, `password`) VALUES (%s,%s,%s,%s)"
        val = (img, Name, info, password)
        mycursor.execute(sql, val)
        mydb.commit()

        # return render_template("admin/default.html")
        return redirect("/admin_t")
    except Exception as e:
        # return render_template("index.html")
        return (str(e))


@app.route("/sub_insert", methods=['POST', 'GET'])
def sub_ins():
    try:
        print("hi")
        images = request.form['images']
        sub_name = request.form['sub_name']
        professorby = request.form['professorby']
        Duration = request.form['date']
        price = request.form['price']
        content_info = request.form['content_info']
        mycursor = mydb.cursor()
        sql = "INSERT INTO `subject`(`images`,`sub_name`, `professorby`, " \
              "`date`,`price`, `content_info`)  VALUES (%s,%s,%s,%s,%s,%s) "
        val = (images, sub_name, professorby, Duration, price, content_info)
        mycursor.execute(sql, val)
        print(sql, val)
        mydb.commit()
        return redirect("/admin_s")

    except Exception as e:
        # return render_template("index.html")
        return (str(e))
        print("err")


#
@app.route("/admin_news")
def news():
    curss = mydb.cursor()
    curss.execute("SELECT * FROM `news`")
    db = curss.fetchall()
    return render_template('admin/news.html', db=db)


@app.route("/news_insert", methods=['POST', 'GET'])
def news_ins():
    try:

        images = request.form['images']
        Name = request.form['Name']
        date = request.form['date']
        info = request.form['info']
        mycursor = mydb.cursor()
        sql = "INSERT INTO `news`(`image`, `Name`, `date`, `info`) VALUES (%s,%s,%s,%s)"
        val = (images, Name, date, info)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect("/admin_news")
    except Exception as e:
        # return render_template("index.html")
        return (str(e))


@app.route("/news_update", methods=['POST'])
def update():
    try:
        No = request.form['No']
        # images = request.form['images']
        Name = request.form['Name']
        date = request.form['date']
        info = request.form['info']
        # gender = request.form['gender']
        # email = request.form['email']
        # phone = request.form['phone']
        curs = mydb.cursor()
        sql = "UPDATE `news` SET `Name`=%s,`date`=%s,`info`=%s WHERE `No`=%s"
        val = (Name, date, info, No)
        curs.execute(sql, val)
        mydb.commit()
        # return render_template("admin/default.html")
        return redirect("/admin_news")
        return "gety"
    except Exception as e:
        return (str(e))


@app.route("/n_up/<No>")
def n_up(No):
    curss = mydb.cursor()
    curss.execute("SELECT * FROM `news` where news.No=%s", (No,))
    db = curss.fetchall()
    return render_template('admin/nup.html', db=db)


@app.route("/course_update", methods=['POST', 'GET'])
def course_up():
    try:
        print("hi")
        no = request.form['no']
        # img = request.form['img']
        Course_Name = request.form['Course_Name']
        by = request.form['by']
        # date = request.form['date']
        info = request.form['info']
        mycursor = mydb.cursor()
        sql = "UPDATE `course` SET `Course_Name`=%s,`by`=%s,`info`=%s WHERE `no`=%s"
        val = (Course_Name, by, info, no)
        print(sql, val)
        mycursor.execute(sql, val)
        mydb.commit()
        print("hello")
        return render_template('admin/default.html')

    except Exception as e:
        print("err")
        # return render_template("index.html")
        return (str(e))


@app.route("/p_up/<no>")
def p_up(no):
    curss = mydb.cursor()
    curss.execute("SELECT * FROM `course` where course.No=%s", (no,))
    db = curss.fetchall()
    curss1 = mydb.cursor()
    curss1.execute("SELECT `Name` FROM `teacher`")
    db1 = curss1.fetchall()
    return render_template('admin/pup.html', db=db, db1=db1)


@app.route("/sub_update", methods=['POST'])
def sub_up():
    try:
        print("Hi")
        No = request.form['No']
        # images = request.form['images']
        sub_name = request.form['sub_name']
        professorby = request.form['professorby']
        Duration = request.form['date']
        Price = request.form['price']
        content_info = request.form['content_info']
        print(sub_name, professorby, Duration, Price, content_info, No)
        mycursor = mydb.cursor()
        sql = "UPDATE `subject` SET `sub_name`=%s ,`professorby`=%s,`date`=%s,`price`=%s,`content_info`=%s WHERE `No`=%s "
        val = (sub_name, professorby, Duration, Price, content_info, No)
        print(sql, val)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect("/admin_s")
    except Exception as e:
        print("error")
        return (str(e))


@app.route("/s_up/<No>")
def s_up(No):
    curss = mydb.cursor()
    curss.execute("SELECT * FROM `subject` WHERE subject.No=%s", (No,))
    db = curss.fetchall()
    return render_template('admin/subject_update.html', db=db)


@app.route("/sub_del/<No>")
def sub_del(No):
    curss = mydb.cursor()
    curss.execute("SELECT * FROM `subject` where subject.No=%s", (No,))
    db = curss.fetchall()
    return render_template('admin/subject_delete.html', db=db)


@app.route("/delete", methods=['post'])
def delete():
    try:
        No = request.form['No']
        curss = mydb.cursor()
        curss.execute("DELETE  FROM subject where No='" + No + "'")
        mydb.commit()
        print(No, curss)
        return redirect("/admin_s")
    except Exception as e:
        print("error")
        return (str(e))


@app.route("/p_del/<No>")
def p_del(No):
    curss = mydb.cursor()
    curss.execute("SELECT * FROM `course` where course.No=%s", (No,))
    db = curss.fetchall()
    return render_template('admin/p_delete.html', db=db)


@app.route("/course_delete", methods=['post'])
def course_delete():
    try:
        no = request.form['no']
        curss = mydb.cursor()
        curss.execute("DELETE  FROM course where No='" + no + "'")
        mydb.commit()
        print(no, curss)
        return render_template('admin/default.html')
    except Exception as e:
        print("error")
        return (str(e))


@app.route("/n_del/<No>")
def n_del(No):
    curss = mydb.cursor()
    curss.execute("SELECT * FROM `news` where news.No=%s", (No,))
    db = curss.fetchall()
    return render_template('admin/news_delete.html', db=db)


@app.route("/news_delete", methods=['post'])
def news_delete():
    try:
        No = request.form['No']
        curss = mydb.cursor()
        curss.execute("DELETE  FROM news where No='" + No + "'")
        mydb.commit()
        print(No, curss)
        # return render_template('admin/default.html')
        return redirect("/admin_news")
    except Exception as e:
        print("error")
        return (str(e))


@app.route("/tt_del/<No>")
def tt_del(No):
    curss = mydb.cursor()
    curss.execute("SELECT * FROM `timetable` where timetable.No=%s", (No,))
    db = curss.fetchall()
    return render_template('admin/tt_delete.html', db=db)


@app.route("/t_delete", methods=['post'])
def t_delete():
    try:
        no = request.form['no']
        curss = mydb.cursor()
        curss.execute("DELETE  FROM timetable where No='" + no + "'")
        mydb.commit()
        print(no, curss)
        # return render_template('admin/default.html')
        return redirect("/admin_tt")
    except Exception as e:

        print("error")
        return (str(e))


#
# @app.route("/p_del/<No>")
# def p_del(No):
#     curss = mydb.cursor()
#     curss.execute("SELECT * FROM `course` where course.No=%s",(No, ))
#     db = curss.fetchall()
#     return render_template('admin/p_delete.html', db=db)
#
# @app.route("/course_delete", methods=['post'])
# def course_delete():
#     try:
#         no = request.form['no']
#         curss = mydb.cursor()
#         curss.execute("DELETE  FROM course where No='" + no + "'")
#         mydb.commit()
#         print(no,curss)
#         return render_template('admin/default.html')
#     except Exception as e:
#         print("error")
#         return (str(e))


@app.route("/teacher_update", methods=['POST', 'GET'])
def teacher_up():
    try:
        No = request.form['No']
        # img = request.form['img']
        Name = request.form['Name']
        info = request.form['info']
        password = request.form['password']
        status = request.form['status']
        mycursor = mydb.cursor()
        sql = "UPDATE `teacher` SET `Name`=%s,`info`=%s, `password`=%s , `status`=%s WHERE `No`=%s"
        val = (Name, info, password, status, No)
        mycursor.execute(sql, val)
        mydb.commit()
        print(sql, val)
        # return render_template("admin/default.html")
        return redirect("/admin_t")
    except Exception as e:
        return (str(e))


@app.route("/t_up/<No>")
def t_up(No):
    curss = mydb.cursor()
    curss.execute("SELECT * FROM `teacher` where teacher.No=%s", (No,))
    db = curss.fetchall()
    curse1 = mydb.cursor()
    curse1.execute("SELECT * FROM `subject`")
    db5 = curse1.fetchall()
    return render_template('admin/tup.html', db=db, db5=db5)


@app.route("/TT_update", methods=['POST', 'GET'])
def TT_up():
    try:
        no = request.form['no']
        Lec_No = request.form['Lec_No']
        Time = request.form['Time']
        Subject = request.form['Subject']
        Day = request.form['Day']
        mycursor = mydb.cursor()
        sql = "UPDATE `timetable` SET `Lec_No`=%s,`Time`=%s,`Subject`=%s,`Day`=%s WHERE `no`=%s"
        val = (Lec_No, Time, Subject, Day, no)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect("/admin_tt")
        return "dgsg"
        return (str(e))

    except Exception as e:
        return (str(e))


@app.route("/tt_up/<no>")
def tt_up(no):
    curss = mydb.cursor()
    curss.execute("SELECT * FROM `timetable` where timetable.no=%s", (no,))
    db = curss.fetchall()
    curss1 = mydb.cursor()
    curss1.execute("SELECT * FROM `subject`")
    db1 = curss1.fetchall()
    return render_template('admin/ttup.html', db=db, db1=db1)


@app.route("/student_update", methods=['POST', 'GET'])
def student_up():
    try:
        No = request.form['No']
        name = request.form['FName']
        Mname = request.form['MName']
        lname = request.form['LName']
        contact = request.form['txtNo']
        email_id = request.form['Email']
        password = request.form['Password']
        # gender = request.form['optradio']
        # print(gender)
        bdate = request.form['date']
        course = request.form['Course']
        address = request.form['Add']
        mycursor = mydb.cursor()
        sql = "UPDATE `registration` SET `Email_id`=%s,`Contact`=%s,`Name`=%s,`Password`=%s,`Mname`=%s," \
              "`lname`=%s,`bdate`=%s,`course`=%s,`address`=%s WHERE `No`=%s"
        val = (email_id, contact, name, password, Mname, lname, bdate, course, address, No)
        mycursor.execute(sql, val)
        mydb.commit()
        print(sql, val)
        return redirect("/student_detail")

    except Exception as e:
        # return render_template("index.html")
        return (str(e))
        print("error")


@app.route("/student_up/<No>")
def stu_up(No):
    curss = mydb.cursor()
    curss.execute("SELECT * FROM `registration` where registration.No=%s", (No,))
    db = curss.fetchall()
    curss1 = mydb.cursor()
    curss1.execute("SELECT `Course_Name` FROM `course`")
    db1 = curss1.fetchall()
    return render_template('admin/sdup.html', db=db, db1=db1)


@app.route("/timetable")
def TT():
    return render_template('admin/timetable.html')


@app.route("/tt", methods=['POST', 'GET'])
def Timetable():
    curss = mydb.cursor()
    curss.execute("SELECT * FROM `timetable`")
    db2 = curss.fetchall()
    return render_template('tt.html', db2=db2)


@app.route("/admin_c")
def admin_c():
    curss = mydb.cursor()
    curss.execute("SELECT * FROM `course`")
    db = curss.fetchall()
    curss1 = mydb.cursor()
    curss1.execute("SELECT `Name` FROM `teacher`")
    db1 = curss1.fetchall()
    return render_template('admin/page.html', db=db, db1=db1)


@app.route("/admin_s")
def admin_s():
    try:
        curss = mydb.cursor()
        curss.execute("SELECT * FROM `subject`")
        db = curss.fetchall()
        return render_template("admin/subject.html", db=db)
    except Exception as e:
        return (str(e))


@app.route("/s_name")
def s_name():
    try:
        curss = mydb.cursor()
        curss.execute("SELECT * FROM `subject`")
        db5 = curss.fetchall()
        return render_template("admin/teacher.html", db5=db5)
    except Exception as e:
        return (str(e))


@app.route("/admin_t")
def admin_t():
    if 'user123' in session:
        # user1 = str(session['123'])
        curss = mydb.cursor()
        curse = mydb.cursor()
        curss.execute("SELECT * FROM `teacher`")
        db = curss.fetchall()
        curse.execute("SELECT * FROM `subject`")
        db5 = curse.fetchall()
        return render_template('admin/teacher.html', db=db, db5=db5)
    else:
        return redirect('/')


@app.route("/admin_tt")
def admin_tt():
    curss = mydb.cursor()
    curss.execute("SELECT * FROM `timetable`")
    db = curss.fetchall()
    curss1 = mydb.cursor()
    curss1.execute("SELECT * FROM `subject`")
    db1 = curss1.fetchall()
    return render_template('admin/timetable.html', db=db, db1=db1)


@app.route("/TT_insert", methods=['POST', 'GET'])
def TT_ins():
    try:

        Lec_No = request.form['Lec_No']
        Time = request.form['Time']
        Subject = request.form['Subject']
        Day = request.form['Day']
        mycursor = mydb.cursor()
        sql = "INSERT INTO `timetable`(`Lec_No`, `Time`,`Subject`, `Day`) VALUES (%s,%s,%s,%s)"
        val = (Lec_No, Time, Subject, Day)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect("/admin_tt")

    except Exception as e:
        # return render_template("index.html")
        return (str(e))


@app.route("/login")
def login():
    return render_template('login.html')


@app.route("/default")
def default():
    return render_template('admin/default.html')


@app.route("/student_detail")
def detail():
    curss = mydb.cursor()
    curss.execute("SELECT * FROM `registration`")
    db = curss.fetchall()
    return render_template('admin/studentdetail.html', db=db)


@app.route('/login_info', methods=['POST', 'GET'])
def login_info():
    try:
        # Name = request.form['Name']
        password = request.form['password']
        email = request.form['email']
        curss = mydb.cursor()
        curss.execute("SELECT * FROM `registration` WHERE  registration.Password='" + password + "'" + "and registration.Email_id='" + email + "'")
        db = curss.fetchone()

        if db is None:
            return "<html><head></head><body><script>alert('Name Or Password is Wrong');</script><script>window.location='/';</script></body></html>"
            # return render_template("index.html")
        else:
            # for row in db:
            session['user_name'] = db[0]
            session['email']=email
            return "<html><head><title>hello</title></head><body><script>alert('Login Successfully');</script><script>window.location='/login_verify_data ';</script></body></html>"
        # return redirect("/login_verify_data")
    except Exception as e:
        return (str(e))


@app.route("/login_verify_data")
def login_verify():
    if 'user_name' in session:
        user1 = str(session['user_name'])
        curss = mydb.cursor()
        curss.execute(
            "SELECT * FROM `timetable` WHERE timetable.Subject in (SELECT registration.course from registration WHERE registration.No='" + user1 + "')")
        db2 = curss.fetchall()
        curss1 = mydb.cursor()
        curss1.execute("SELECT registration.course FROM `registration` WHERE registration.No='" + user1 + "'")
        db3 = curss1.fetchall()
        curr3 = mydb.cursor()
        # curr3.execute("SELECT * FROM `subject` WHERE subject.sub_name in (SELECT registration.course FROM `registration` WHERE registration.No='"+ user1 +"')")
        curr3.execute("SELECT * FROM `datas` where datas.No='" + user1 + "'")
        db4 = curr3.fetchall()
        cccu = mydb.cursor()
        cccu.execute("SELECT * FROM `registration` WHERE registration.No='" + user1 + "'")
        db = cccu.fetchall()
        return render_template("tt.html", db=db, db2=db2, db4=db4, db3=db3)
    else:
        return redirect("/")


@app.route("/signout_verify")
def signout():
    if 'user_name' in session:
        session.pop('user_name', None)
        return redirect('/')


@app.route("/admin_login")
def admin():
    return render_template('admin/login.html')


@app.route('/admin_login_info', methods=['POST', 'GET'])
def admin_login_info():
    try:
        Name = request.form['Name']
        password = request.form['password']
        curss = mydb.cursor()
        curss.execute("SELECT * FROM `user` WHERE user.Name = '" + Name + "' and user.password = '" + password + "'")
        db = curss.fetchone()
        if db is None:
            # return redirect('/admin_login')
            return "<html><head></head><body><script>alert('UserName Or Passwor Is Wrong');</script><script>window.location='/admin_login';</script></body></html>"
            # return "wrong"

        else:
            session["user123"] = db[0]
            # db = curss.fetchall()
            # for row in db:
            #     session["user123"] = row[0]
            # return redirect('/admi')
            # curss = mydb.cursor()
            # curss.execute("SELECT * FROM `timetable`")
            # db1 = curss.fetchall()
            #     return redirect('/admin123')
            # return redirect('/admin123')
            return "<html><head></head><body><script>alert('Login successfully');</script><script>window.location='/admin123';</script></body></html>"
    except Exception as e:
        return (str(e))


@app.route('/admin123')
def admin123():
    try:
        if 'user123' in session:
            user123 = str(session['user123'])
            cr = mydb.cursor()
            cr.execute("select * from user where No= '" + user123 + "' ")
            dd1 = cr.fetchone()
            return render_template("admin/default.html", dd1=dd1)
        else:
            return redirect('/admin_login')

    except Exception as e:
        return (str(e))


@app.route("/admin_sign_out")
def adminout():
    if 'user123' in session:
        session.pop('user123', None)
        return redirect('/admin_login')
    else:
        return redirect('/admin_login')


@app.route("/contactus")
def contactus():
    curss = mydb.cursor()
    curss.execute("SELECT * FROM `contact`")
    db = curss.fetchall()
    return render_template('admin/contact.html', db=db)


@app.route("/faculty_login")
def loginj():
    return render_template("teacher/login.html")


@app.route("/faculty_login1", methods=['POST', 'GET'])
def faculty_login1():
    try:
        Name = request.form['Name']
        password = request.form['password']
        curss = mydb.cursor()
        curss.execute(
            "SELECT * FROM `teacher` WHERE teacher.Name = '" + Name + "' and teacher.password = '" + password + "'")
        db = curss.fetchone()
        if db is None:
            # return redirect('/faculty_login')
            return "<html><head></head><body><script>alert('UserName Or Passwor Is Wrong');</script><script>window.location='/faculty_login';</script></body></html>"
        else:
            # for row in db:
            session["user12"] = db[0]
        return "<html><head></head><body><script>alert('Login Successfully');</script><script>window.location='/faculty_defult ';</script></body></html>"

        # return redirect('/faculty_defult')
        # curss = mydb.cursor()
        # curss.execute("SELECT * FROM `timetable`")
        # db1 = curss.fetchall()
        # return render_template("admin/default.html")
    except Exception as e:
        return (str(e))


@app.route('/faculty_defult')
def fun():
    if 'user12' in session:
        user1 = str(session['user12'])
        # cur=mydb.cursor()
        # cur.execute("select * from teacher where No='" + user1 + "'")
        # dd=cur.fetchone()
        # return render_template('teacher/faculty.html', dd=dd)
        user11 = str(session['user12'])
        cur1 = mydb.cursor()
        cur1.execute("select * from teacher where No='" + user11 + "'")
        db1 = cur1.fetchone()
        return render_template('teacher/faculty.html', db1=db1)
        # return render_template('teacher/f.html', dd=dd)
    else:
        return redirect('/faculty_login')


@app.route("/ll", methods=['POST', 'GET'])
def facuout():
    if 'user12' in session:
        session.pop('user12', None)
        return redirect('/faculty_login')
    else:
        return redirect('/faculty_login')


@app.route("/faculty")
def faculty():
    return render_template('teacher/faculty.html')


@app.route("/teachertt")
def facultytt():
    curr = mydb.cursor()
    curr.execute("SELECT * FROM `timetable` WHERE 1")
    db1 = curr.fetchall()
    curr1 = mydb.cursor()
    curr1.execute("SELECT * FROM `subject` WHERE 1")
    db2 = curr1.fetchall()

    return render_template('teacher/time.html', db1=db1, db2=db2)


@app.route("/teachertt_insert", methods=['POST', 'GET'])
def teachertt_ins():
    try:

        Lec_No = request.form['Lec_No']
        Time = request.form['Time']
        Subject = request.form['Subject']
        Day = request.form['Day']
        mycursor = mydb.cursor()
        sql = "INSERT INTO `timetable`(`Lec_No`, `Time`,`Subject`, `Day`) VALUES (%s,%s,%s,%s)"
        val = (Lec_No, Time, Subject, Day)
        mycursor.execute(sql, val)
        mydb.commit()
        curr = mydb.cursor()
        # return render_template("teacher/time.html")
        return redirect("/teachertt")
    except Exception as e:
        # return render_template("index.html")
        return (str(e))


@app.route("/teacherTT_update", methods=['POST', 'GET'])
def teacherTT_up():
    try:
        no = request.form['no']
        Lec_No = request.form['Lec_No']
        Time = request.form['Time']
        Subject = request.form['Subject']
        Day = request.form['Day']
        mycursor = mydb.cursor()
        sql = "UPDATE `timetable` SET `Lec_No`=%s,`Time`=%s,`Subject`=%s,`Day`=%s WHERE `no`=%s"
        val = (Lec_No, Time, Subject, Day, no)
        mycursor.execute(sql, val)
        mydb.commit()
        curr = mydb.cursor()
        curr.execute("SELECT * FROM `subject` WHERE 1")
        db1 = curr.fetchall()
        return redirect("/teachertt")

    except Exception as e:
        return (str(e))


@app.route("/teachertimet_up/<no>")
def teachertimet_up(no):
    curss = mydb.cursor()
    curss.execute("SELECT * FROM `timetable` where timetable.no=%s", (no,))
    db = curss.fetchall()
    curr = mydb.cursor()
    curr.execute("SELECT * FROM `subject` WHERE 1")
    db1 = curr.fetchall()
    return render_template('teacher/ttup.html', db=db, db1=db1)


@app.route("/teachertt_del/<No>")
def teachertt_del(No):
    curss = mydb.cursor()
    curss.execute("SELECT * FROM `timetable` where timetable.No=%s", (No,))
    db = curss.fetchall()
    return render_template('teacher/tt_delete.html', db=db)


@app.route("/teachert_delete", methods=['post'])
def teachert_delete():
    try:
        no = request.form['no']
        curss = mydb.cursor()
        curss.execute("DELETE  FROM timetable where No='" + no + "'")
        mydb.commit()
        print(no, curss)
        return redirect("/teachertt")
    except Exception as e:
        print("error")
        return (str(e))


@app.route("/attendance")
def attendance():
    curss = mydb.cursor()
    curss.execute("SELECT * FROM `attendace_detail`")
    db = curss.fetchall()
    curss1 = mydb.cursor()
    curss1.execute("SELECT * FROM `registration`")
    db1 = curss1.fetchall()
    return render_template('teacher/attendance.html', db1=db1, db=db)
    # return render_template('teacher/attendance.html', db=db)


@app.route("/attendance_insert", methods=['POST', 'GET'])
def attendance_insert():
    try:
        print('hi')
        Name = request.form['Name']
        print('naem', Name)
        course = request.form['course']
        print('c', course)
        day = request.form['day']
        print('d', day)
        time = request.form['time']
        print('t', time)
        Presentday = request.form['Presentday']
        print('p', Presentday)
        Totalday = request.form['Totalday']
        print('t', Totalday)
        mycursor = mydb.cursor()
        # sql = "UPDATE `attendance` SET `Name`=%s,`course`=%s,`day`=%s,`time`=%s,`Presentday`=%s,`Totalday`=%s"
        sql = "INSERT INTO `attendance`(`Name`, `course`, `day`, `time`, `Presentday`, `Totalday`) values" \
              "(%s,%s,%s,%s,%s,)"
        val = (Name, course, day, time, Presentday, Totalday)
        mycursor.execute(sql, val)
        mydb.commit()
        curr = mydb.cursor()
        print(sql, val)
        # mycursor.execute(sql, val)
        # mydb.commit()
        # curr=mydb.cursor()
        return render_template("teacher/attendnce.html")
    except Exception as e:
        # return render_template("index.html")
        return (str(e))
        print('err')


@app.route("/mark")
def mark():
    curss1 = mydb.cursor()
    curss1.execute("SELECT * FROM `registration`")
    db1 = curss1.fetchall()
    curss2 = mydb.cursor()
    curss2.execute("SELECT * FROM `subject`")
    db2 = curss2.fetchall()
    curss3 = mydb.cursor()
    curss3.execute("SELECT * FROM `marks`")
    db3 = curss3.fetchall()
    return render_template('teacher/Marks.html', db1=db1, db2=db2, db3=db3)


@app.route("/mark_insert", methods=['POST', 'GET'])
def mark_ins():
    try:

        Name = request.form['Name']
        Day = request.form['Day']
        Time = request.form['Time']
        Subject = request.form['Subject']
        mark = request.form['mark']
        Total = request.form['Total']
        status = request.form['status']
        mycursor = mydb.cursor()
        sql = "INSERT INTO `marks`(`Stu_name`, `day`, `time`, `Sub_Name`, `Stu_Marks`, `totalmarks`, `status`) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        val = (Name, Day, Time, Subject, mark, Total, status)
        mycursor.execute(sql, val)
        mydb.commit()
        # curr=mydb.cursor()
        return redirect("/mark")

    except Exception as e:
        # return render_template("index.html")
        return (str(e))


@app.route("/mark_update", methods=['POST', 'GET'])
def mark_update():
    try:
        No = request.form['No']
        Name = request.form['Name']
        Day = request.form['Day']
        Time = request.form['Time']
        Subject = request.form['Subject']
        mark = request.form['mark']
        Total = request.form['Total']
        status = request.form['status']
        mycursor = mydb.cursor()
        # sql = "UPDATE `timetable` SET `Lec_No`=%s,`Time`=%s,`Subject`=%s,`Day`=%s WHERE `no`=%s"
        sql = "UPDATE `marks` SET` Stu_name`=%s, `day`=%s, `time`=%s, `Sub_Name`=%s, `Stu_Marks`=%s, `totalmarks`=%s, `status`=%s WHERE `No`=%s "
        val = (Name, Day, Time, Subject, mark, Total, status, No)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect("/mark")

    except Exception as e:
        # return render_template("index.html")
        return (str(e))


@app.route("/mark_up/<No>")
def mark_up(No):
    curss = mydb.cursor()
    curss.execute("SELECT * FROM `marks` where marks.No=%s", (No,))
    db = curss.fetchall()
    # curr = mydb.cursor()
    # curr.execute("SELECT * FROM `subject` WHERE 1")
    # db1 = curr.fetchall()
    # return redirect('/marks')
    return render_template('teacher/Marks.html', db=db)

@app.route("/forgotpassword",methods=['POST', 'GET'])
def forgotpassword():
        # print("eee")
        print("*****",request.method)
        msgbox=""
        if request.method == "POST":
            Email_id = request.form['Email_id']
            print(Email_id)
            curss = mydb.cursor()
            curss.execute("SELECT Password FROM `registration` where Email_id=%s",(Email_id, ))
            db = curss.fetchone()
            if db == None:
                return "<html><head><script>windowalert('Wrong');</script><script>window.location='/';</script></head></html>"
            else:
                msg = Message('Parshwa Education', sender='infoparshwaeducation@gmail.com', recipients=[Email_id])
                msg.body ="Your Password Is ::  '"+db[0]+"'"
                mail.send(msg)
                return "<html><head><script>window.alert('send');</script><script>window.location='/';</script></head></html>"
                # msgbox = "Send"
            # print(msg)
                temp = "index.html"
        else:
            print("elseeeee")
            temp="forgotpassword.html"
        return render_template(temp,val=msgbox)


@app.route("/password_update", methods=['POST', 'GET'])
def fp_up():
    print (request.method)
    if request.method=='POST':
        email = session['email']
        print(email)
        Password=request.form['Password']
        print(Password)
        mycursorr = mydb.cursor()
        sql = "UPDATE `registration` SET `Password`='"+Password+"'  WHERE registration.Email_id = '"+email+"'"
        # val = (Password,email)
        mycursorr.execute(sql)
        mydb.commit()
        # temp="tt.html"
        return redirect("/login_verify_data")
    else:
        temp="changepassword.html"
    return render_template(temp)

@app.route("/chnagepassword")
def chnagepassword():
    return render_template('teacher/change.html')

@app.route("/change_update", methods=['POST', 'GET'])
def change_up():
    try:
        # print("hi")
        # no = request.form['no']
        name = request.form['Name']
        # print(email)
        password = request.form['password']
        # print(password)
        # Subject = request.form['Subject']
        # Day = request.form['Day']
        mycursorr = mydb.cursor()
        sql = "UPDATE `teacher` SET `password` = %s WHERE teacher.Name = %s"
        # sql = "UPDATE `registration` SET `Password`=%s WHERE `Email_id`=%s"
        val = (password, name)
        mycursorr.execute(sql, val)
        mydb.commit()
        return redirect('/faculty_login')

    except Exception as e:
        return (str(e))


# @app.route("/fp_update", methods=['POST', 'GET'])
# def fp_update():
#     try:
#         email = request.form['email']
#         password = request.form['password']
#         mycursor = mydb.cursor()
#         # sql = "UPDATE `timetable` SET `Lec_No`=%s,`Time`=%s,`Subject`=%s,`Day`=%s WHERE `no`=%s"
#         sql = "UPDATE `registration` SET `password`=%s, WHERE `email`=%s"
#         val = (password, email)
#         mycursor.execute(sql, val)
#         mydb.commit()
#         return redirect("/")
#
#     except Exception as e:
#         # return render_template("index.html")
#         return (str(e))



if __name__ == '__main__':
    app.run(debug=True)
