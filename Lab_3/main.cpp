#include <SFML/Graphics.hpp>
#include <SFML/System.hpp>
#include <SFML/Window.hpp>
int main()
{
	int n = 10;

	sf::RenderWindow window(sf::VideoMode({ 500, 500 }), "matrica");

	const int cellSize = 50;
	const int gridSize = 10;

	sf::RectangleShape cells[gridSize][gridSize];

	for (int i = 0; i < gridSize; ++i)
	{ 
		for (int j = 0; j < gridSize; ++j)
		{
			cells[i][j].setSize(sf::Vector2f(cellSize - 2, cellSize - 2));
			cells[i][j].setPosition(i * cellSize, j * cellSize);
			cells[i][j].setFillColor(sf::Color::White);
			cells[i][j].setOutlineColor(sf::Color::Black);
			cells[i][j].setOutlineThickness(1);
		}
	}
	sf::RectangleShape cells1[gridSize][gridSize];

	for (int i = 0; i < gridSize; ++i)
	{
		for (int j = 0; j < gridSize; ++j)
		{
			cells1[i][j].setSize(sf::Vector2f(cellSize - 2, cellSize - 2));
			cells1[i][j].setPosition(i * cellSize, j * cellSize);
			cells1[i][j].setFillColor(sf::Color::Green);
			cells1[i][j].setOutlineColor(sf::Color::Black);
			cells1[i][j].setOutlineThickness(1);
		}
	}

	while (window.isOpen())
	{
		sf::Event event;
		while (window.pollEvent(event))
		{
			if (event.type == sf::Event::Closed)
				window.close();
		}

		window.clear(sf::Color::White);
		for (int i = 0; i < gridSize; ++i)
		{
			for (int j = 0; j < gridSize; ++j)
			{
				window.draw(cells[i][j]);
				if (i >= abs(j - n / 2 + 1) and i < n - abs(j - n / 2 + 1) and j>n / 2 - 2)
				{
					cells[i][j].setFillColor(sf::Color::Green);
				}

			}
		}
		window.display();
		
	}
	return 0;
}