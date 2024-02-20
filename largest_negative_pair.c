#include <stdio.h>
#include "main.h"

int findMaxK(int* nums, int numsSize)
{
	int i, j;
	int num = 0;

	for (i = 0; i < numsSize; i++)
	{
		for (j = i + 1; j < numsSize; j++)
		{
			if (nums[i] + nums[j] == 0)
			{
				if (num < abs(nums[i]))
				   num = abs(nums[i]);
			
		}
	}

	if (num == 0)
	{
		return (-1);
	}
	else
	{
		return (num);
	}
}
}
