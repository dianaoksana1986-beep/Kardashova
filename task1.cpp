#include <iostream>
#include <string>

struct Book {
std::string title;
std::string author;
int year;
};

int main() {
Book myBook;
std::cout << "Введіть назву: ";
std::getline(std::cin, myBook.title);

std::cout << "Введіть автора: ";
std::getline(std::cin, myBook.author);

std::cout << "Введіть рік видання: ";
std::cin >> myBook.year;

std::cout << "\n\"" << myBook.title << "\" by " << myBook.author << " (" << myBook.year << ")" << std::endl;

return 0;
}

