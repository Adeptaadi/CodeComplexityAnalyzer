#include <stdio.h>

int helper(int x) {
    if (x < 0) {
        return -x;
    } else if (x == 0) {
        return 0;
    }
    return x;
}

int compute(int n) {
    int sum = 0;

    for (int i = 0; i < n; i++) {
        if (i % 2 == 0) {
            for (int j = 0; j < i; j++) {
                if (j % 3 == 0) {
                    sum += helper(j);
                } else {
                    sum += j;
                }
            }
        } else {
            sum += i;
        }
    }

    switch (n) {
        case 0:
            return 0;
        case 1:
            return 1;
        default:
            return sum;
    }
}

int main() {
    int value = compute(10);

    while (value > 0) {
        if (value % 5 == 0) {
            printf("Divisible by 5\n");
        }
        value--;
    }

    return 0;
}
