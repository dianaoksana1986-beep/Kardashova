def search_dictionary(dictionary: list, word: str) -> str:
    left = 0
    right = len(dictionary) - 1
    
    while left <= right:
        mid = (left + right) // 2
        current_word = dictionary[mid][0]  
        
        if current_word == word:
            return dictionary[mid][1]     
        elif current_word < word:
            left = mid + 1                 
        else:
            right = mid - 1               
            
    return "Слово не знайдено"

dict_data = [
    ["API", "Інтерфейс прикладного програмування"],
    ["Bug", "Помилка в програмуванні"],
    ["Code", "Текст програми, написаний мовою програмування"],
    ["Compiler", "Програма, що перетворює код у машинний вигляд"]
]

print(search_dictionary(dict_data, "Bug"))   
print(search_dictionary(dict_data, "Python"))    