if __name__ == '__main__':

    student_course_pairs_1 = [
    ["58", "Linear Algebra"],
    ["94", "Art History"],
    ["94", "Operating Systems"],
    ["17", "Software Design"],
    ["58", "Mechanics"],
    ["58", "Economics"],
    ["17", "Linear Algebra"],
    ["17", "Political Science"],
    ["94", "Economics"],
    ["25", "Economics"],
    ["58", "Software Design"]
    ]

    input_case = {}
    for x in student_course_pairs_1:
        if x[0] not in input_case:
            input_case[x[0]] = set()

        input_case[x[0]].add(x[1])



    stu_ids  = list(input_case.keys())
    res = {}
    for i in range(len(stu_ids)):
        x = input_case[stu_ids[i]]
        for j in range(i + 1, len(stu_ids)):
            y = input_case[stu_ids[j]]
            key = ', '. join([stu_ids[i], stu_ids[j]])

            res[key] = list(x.intersection(y))


    print(res)

# creating a map of studet ids to the courses they have taken then we are iteratong on every student id then we are finding the common courses through set intersection