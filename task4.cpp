#include <iostream>

struct Time {
	int hours;
	int minutes;
	int seconds;
};

int main() {
	Time t;

	std::cout << "Введіть години: ";
	std::cin >> t.hours;
	
	std::cout << "Введіть хвилини: ";
	std::cin >> t.minutes;

	std::cout << "Введіть секунди: ";
	std::cin >> t.seconds;

	long totalSeconds = (t.hours * 3600) + (t.minutes * 60) + t.seconds;

	std::cout << "Загальна кількість секунд: " << totalSeconds << std::endl;

	return 0;
}


