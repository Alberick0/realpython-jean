def enrollment_stats(list):
    enrolled_students = []
    tuition_fees = []

    for i in range(len(list)):
        enrolled_students.append(list[i][1])
        tuition_fees.append(list[i][2])

        
    return [enrolled_students, tuition_fees]


def mean(list):
    mean = 0
    for i in range(len(list)):
        mean += list[i]

    return mean

def median(list):
    sorts = sorted(list)
    length = len(sorts)
    if not length % 2:
        return (sorts[int(length / 2)] + sorts[int(length / 2 - 1)]) / 2.0
    return sorts[int(length / 2)]


universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

total_students = enrollment_stats(universities)[0]
total_tuition = enrollment_stats(universities)[1]
student_mean = mean(total_students)
tuition_mean = mean(total_tuition)
student_median = median(total_students)
tuition_median = median(total_tuition)

print '*************************'
print 'Total students: {}'.format(student_mean)
print 'Total tuition: $ {}'.format(tuition_mean)
print ''
print 'Student mean: {}'.format(student_mean/len(universities))
print 'Student median: {}'.format(student_median)
print ''
print 'Tuition mean: {}'.format(tuition_mean/len(universities))
print 'Tuition mean: {}'.format(tuition_median)
print '*************************'
