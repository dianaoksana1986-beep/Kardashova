def create_rating(students: list) -> list:
    rating = list(students)
    n = len(rating)
    
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if rating[j][1] > rating[max_idx][1]:
                max_idx = j
                
        rating[i], rating[max_idx] = rating[max_idx], rating[i]
        
    return rating
students_list = [
    ["Катерина", 4.8],
    ["Олексій", 4.2],
    ["Дмитро", 5.0],
    ["Ганна", 4.5]
]

sorted_rating = create_rating(students_list)
print(sorted_rating)