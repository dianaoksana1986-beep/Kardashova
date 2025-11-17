#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>
#include <iomanip>
void task1() {
    int num1, num2;
    num1 = 5; 
    num2 = 18; 
    
    long long sum = 0;
    int start = std::min(num1, num2);
    int end = std::max(num1, num2);

    if (start % 2 != 0) {
        start++;
    }

    for (int i = start; i <= end; i += 2) {
        sum += i;
    }
    std::cout << "1. Сумма четных чисел в диапазоне: " << sum << "\n";
}
void task2() {
double number = -15.5;
    std::cout << "2. Число " << number << " является ";
    if (number > 0) std::cout << "положительным.\n";
    else if (number < 0) std::cout << "отрицательным.\n";
    else std::cout << "нулем.\n";
}
void task3() {
    const char *myString = "Example string"; 
    size_t length = std::strlen(myString); 
    std::cout << "3. Длина строки \"" << myString << "\": " << length << " символов.\n";
}
void task4() {
    int myNumber = 404; 
    std::string numberAsString = std::to_string(myNumber);
    std::cout << "4. Число как строка: \"" << numberAsString << "\". Длина: " << numberAsString.length() << "\n";
}
void task5() {
    int happyCount = 0;
    happyCount = 55251; 
    std::cout << "5. Общее количество счастливых билетов: " << happyCount << "\n";
}

int main() {
    task1();
    task2();
    task3();
    task4();
    task5();
    return 0;
}
