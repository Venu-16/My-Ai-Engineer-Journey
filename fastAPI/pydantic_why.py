# def insert_patient_data(name,age):
#
#     print(name)
#     print(age)
#     print("inserted into db")
#
# insert_patient_data("venu","twenty")

def insert_patient_data(name,age):
    if type(name)== str and type(age) == int:
        if(age<0):
            raise ValueError("value Error")
        else:
            print(name)
            print(age)
            print("inserted into db")
    else:
        raise TypeError("Incorrect Type")

insert_patient_data("venu","twenty")