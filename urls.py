from datetime import date

from views import Index, About, Code, StudyPrograms, CoursesList, \
    CreateCourse, CreateCategory, CategoryList, CopyCourse



# front controller
def secret_front(request):
    request['date'] = date.today()


def other_front(request):
    request['key'] = 'some_key'


fronts = [secret_front, other_front]

routes = {
    '/': Index(),
    '/code/': Code(),
    '/about/': About(),

    '/study_programs/': StudyPrograms(),
    '/courses-list/': CoursesList(),
    '/create-course/': CreateCourse(),
    '/create-category/': CreateCategory(),
    '/category-list/': CategoryList(),
    '/copy-course/': CopyCourse()
}
