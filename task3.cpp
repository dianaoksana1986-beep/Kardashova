#include <iostream>
#include <cmath>
#include <iomanip>

struct Point {
	double x;
	double y;
};

int main() {
	Point p;

	std::cout << "Введіть x: ";
	std::cin >> p.x;

	std::cout << "Введіть y: ";
	std::cin >> p.y;

	double distance = std::sqrt(p.x * p.x + p.y * p.y);

	std::cout << std::fixed << std::setprecision(2);
	std::cout << "Відстань від початку координат: " << distance << std::endl;

	return 0;
}

