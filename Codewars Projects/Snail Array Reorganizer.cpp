#include <vector>
#include <iostream>
#include <tgmath.h>
std::vector<int> snail(const std::vector<std::vector<int>>& snail_map) {
	std::vector <int> answer;
	int side = snail_map[0].size();
	for (int number : snail_map[0])
		answer.push_back(number);

	for (int i = 1; i <= side - 1; i++)
	{
		for (int j = 1; j <= 2; j++)
		{
			if (j % 2 == 1 && i % 2 == 1)
			{
				for (int k = i - floor(i / 2); k < side - (floor(i / 2) + 1); k++)
				{
					answer.push_back(snail_map[k][side - (floor(i / 2) + 1)]);
				}
			}
			if (j % 2 == 0 && i % 2 == 1)
			{
				for (int k = side - (floor(i/2)+1); k >= (floor(i / 2)); k--)
				{
					answer.push_back(snail_map[side-(floor(i/2)+1)][k]);
				}
			}
			if (j % 2 == 1 && i % 2 == 0)
			{
				for (int k = side - (i/2 + 1); k >= i/2; k--)
				{
					answer.push_back(snail_map[k][i/2-1]);
				}
			}
			if (j % 2 == 0 && i % 2 == 0)
			{
				for (int k = i/2; k <= side - (i/2+1); k++)
				{
					answer.push_back(snail_map[i/2][k]);
				}
			}
		}
	}
	for (int number : answer)
		std::cout << number << ", ";
	return {answer};
}

void main() {
	std::vector<std::vector<int>> test = { {1,2,3,4,5},{6,7,8,9,10},{11,12,13,14,15}, {16,17,18,19,20}, {21,22,23,24,25 } };
	snail(test);
}