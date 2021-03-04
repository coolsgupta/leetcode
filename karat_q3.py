def find_mid(input_case):
    prereqs = set()
    following = set()
    course_map = {}
    for x in input_case:
        prereqs.add(x[0])
        following.add(x[1])
        course_map[x[0]] = x[1]

    starting_course = list(prereqs - following)[0]
    curr = starting_course
    for i in range(len(input_case) // 2):
        curr = course_map[curr]

    return curr


if __name__ == '__main__':
    prereqs_courses = [
        ["Foundations of Computer Science", "Operating Systems"],
        ["Data Structures", "Algorithms"],
        ["Computer Networks", "Computer Architecture"],
        ["Algorithms", "Foundations of Computer Science"],
        ["Computer Architecture", "Data Structures"],
        ["Software Design", "Computer Networks"]
    ]
    prereqs_courses_3 = [
        ["Data Structures", "Algorithms"],
        ["Algorithms", "Foundations of Computer Science"],
        ["Foundations of Computer Science", "Operating Systems"]
    ]
    input_case = prereqs_courses_3
    print(find_mid(input_case))

