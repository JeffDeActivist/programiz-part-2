def key_word(date, *names):
    for i in names:
        print("Hello", i, "...How are you", date,"?")


key_word("today", "Jeff", 'Pyhton', "Angayo", 'Hp')


def student_marks(name, **subject):
    print(name, "you are taking", len(subject), "units")
    for key, value in subject.items():
        print(key, ":", value)


student_marks("JeffDeActivist", OOP=70, Stats=67, Calc=54, Algeb=88, Vect=44, Data=66)
student_marks("Jeff", OOP=73, Stats=47, Calc=34, Algeb=88, Vect=64, Data=6, Python=89)


def listNames(names=None, marks=None):
    if names is None and marks is None:
        names, marks = [], []
    print(names, marks)


listNames(['Jeff', 'Angayo', 'DeActivist'], [56, 66, 87])
