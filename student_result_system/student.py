class Student:
    def __init__(self, student_id, full_name, class_form, gender, date_of_birth):
        self.student_id = student_id
        self.full_name = full_name
        self.class_form = class_form
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.scores = {}
        self.result_date = ""

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, data):
        student = cls(data["student_id"], data["full_name"], data["class_form"],
                      data["gender"], data["date_of_birth"])
        student.scores = data.get("scores", {})
        student.result_date = data.get("result_date", "")
        return student
