""" 2 Month - OOP - Jan 22 - 06.01.2022"""

# class Laptop:
#     name = 'Asus'
#
# class GameLaptop(Laptop):
#     def __init__(self):
#         super(GameLaptop, self).__init__()

class Junior:
    def __init__(self, prog_lang, laptop, style, experience, salary):
        if isinstance(prog_lang, str):
            self.lang = prog_lang
        else:
            raise ValueError("Programming language is string")
        if isinstance(laptop, bool):
            self.laptop = laptop
        else:
            raise ValueError("Laptop is bool")
        if isinstance(style, str):
            self.style = style
        else:
            raise Exception("Style is string")
        if isinstance(experience, float):
            self.experience = experience
        else:
            raise ValueError("Experience is float")
        if isinstance(salary, int):
            self.salary = salary
        else:
            raise ValueError("Salary is integer")

    def can_copy_paste(self, source):
        return f'Can copy and paste from {source}, style is {self.style}\n'

    def __str__(self):
        return f'Programming language: {self.lang}\n' \
               f'Laptop : {self.laptop}\n' \
               f'Style : {self.style}\n' \
               f'Experience : {self.experience} years\n' \
               f'Salary : {self.salary}$\n'

junior_1 = Junior('Java', True, 'awful', 0.5, 250)
junior_2 = Junior('Python', True, style='good', experience=0.5, salary=300)

# print(junior_1)
# print(junior_1.can_copy_paste('Google'))
# print(junior_2)
# print(junior_2.can_copy_paste('StackOverFlow'))

class Middle(Junior):
    def __init__(self, prog_lang, laptop, style, experience, salary, responsibility):
        super().__init__(prog_lang, laptop, style, experience, salary)
        if isinstance(responsibility, bool):
            self.resp = responsibility
        else:
            raise ValueError("Responsibility is boolean")

    def can_be_mentor(self, junior):
        return f'Can be mentor to {junior}, because experience {self.experience}'

    def can_handle_project(self, project):
        return f'Can handle fully project, project name is {project}'

    def __str__(self):
        return super(Middle, self).__str__() + f'Responsibility : {self.resp}\n'

middle_1 = Middle(prog_lang='Python', laptop=True, style='good enough', experience=2.5,
                  salary=2000, responsibility=True)

# print(middle_1)
# print(middle_1.can_be_mentor(junior_2.lang))
# print(middle_1.can_handle_project('B2B project'))
# print(middle_1.can_copy_paste('Google'))

class Senior(Middle):
    def  __init__(self, prog_lang, laptop, style, experience, salary, responsibility, architecture):
        super().__init__(prog_lang, laptop, style, experience, salary, responsibility)
        if isinstance(architecture, str):
            self.arch = architecture
        else:
            raise ValueError("Architecture is string")

    def advanced_skills(self):
        if self.lang == 'Python':
            return f'Can write own OpenCV library'
        elif self.lang == 'C#':
            return f'Can do some GameDev'
        elif self.lang == 'JS':
            return f'FrontEnd King'
        elif self.lang == 'Golang':
            return f'Fastest Coroutine threads'

    def __str__(self):
        return super(Senior, self).__str__() + f'Architecture : {self.arch}\n'

senior_1 = Senior(prog_lang='Golang', laptop=True, style='Excellent', experience=5.0,
                  salary=6000, responsibility=True, architecture='MVC')

print(senior_1)
print(senior_1.advanced_skills())
print(senior_1.advanced_skills())
print(senior_1.can_copy_paste('Google'))

