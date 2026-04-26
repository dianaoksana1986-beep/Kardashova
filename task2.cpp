#include <iostream>
#include <string>
#include <iomanip>
struct Product {
	std::string name;
	double price;
	int quantity;
};

int main() {
	Product myProduct;

	std::cout << "Введіть назву товару: ";
	std::getline(std::cin, myProduct.name);
	
	std::cout << "Введіть ціну: ";
	std::cin >> myProduct.price;
	
	std::cout << "Введіть кількість: ";
	std::cin >> myProduct.quantity;

	double total = myProduct.price * myProduct.quantity;

	std::cout << "Товар: " << myProduct.name << std::endl;
	std::cout << "Загальна вартість: " << std::fixed << std::setprecision(2) << total << "UAH" << std::endl;

	return 0;
}
