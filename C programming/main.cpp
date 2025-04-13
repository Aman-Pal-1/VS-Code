#include<stdio.h>
#include <graphics.h>
#include <conio.h>
#include <cmath>
#include <iostream>

using namespace std;

void drawDDALine(int x1, int y1, int x2, int y2) {
    int dx = x2 - x1;
    int dy = y2 - y1;

    int steps = abs(dx) > abs(dy) ? abs(dx) : abs(dy);

    float Xinc = dx / static_cast<float>(steps);
    float Yinc = dy / static_cast<float>(steps);

    float X = x1;
    float Y = y1;

    for (int i = 0; i <= steps; ++i) {
        putpixel(X, Y, WHITE); // Draw pixel at (X, Y)
        X += Xinc; // Increment X
        Y += Yinc; // Increment Y
    }
}

int main() {
    int gd = DETECT, gm;

    // Initialize graphics mode
    initgraph(&gd, &gm, "C:\\MinGW\\BGI");

    // Starting and ending points of the line
    int x1 = 100, y1 = 100, x2 = 300, y2 = 300;

    // Draw a line using DDA algorithm
    drawDDALine(x1, y1, x2, y2);

    // Wait for a key press
    getch();

    // Close graphics mode
    closegraph();

    return 0;
}
