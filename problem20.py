# https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
def sorting(name_score):
    # Extract all scores
    marks = [student[1] for student in name_score]
    
    # Remove duplicates and sort the scores
    sorted_marks = sorted(set(marks))
    
    # Check if we have at least two distinct scores
    if len(sorted_marks) < 2:
        print("Not enough distinct scores.")
        return
    
    # Find the second-lowest score
    second_lowest = sorted_marks[1]
    
    # Collect names of students with the second-lowest score
    sorted_names = [student[0] for student in name_score if student[1] == second_lowest]
    
    # Sort names alphabetically
    final_names = sorted(sorted_names)
    
    # Print the names
    for student in final_names:
        print(student)


# Executing
if __name__ == '__main__':
    name_score = []
    
    # Read the number of students
    num_students = int(input())
    
    # Collect student data
    for _ in range(num_students):
        name = input()
        score = float(input())
        name_score.append([name, score])
    
    # Call the sorting function after all data is collected
    sorting(name_score)
