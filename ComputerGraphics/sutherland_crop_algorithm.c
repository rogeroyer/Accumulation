// openGL.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


#include <GL/glut.h>
#include <stdlib.h>
#include <math.h>
#include <stdio.h>

#define LEFT 1
#define RIGHT 2
#define BOTTOM 4
#define TOP 8

int x1 = 150, y01 = 50, x2 = 50, y2 = 250, XL = 100, XR = 300, YB = 100, YT = 200;  //(x1,y1)、(x2,y2)为直线段的端点，XL为左边界，XR为右边界，YB为下边界，YT为上边界
int x1_init = 150, y1_init = 50, x2_init = 50, y2_init = 250;  //将直线段端点备份，以便画出裁剪前的直线段

int encode(int x, int y)
{
	int c = 0;
	if (x < XL) c |= LEFT;
	if (x > XR) c |= RIGHT;
	if (y < YB) c |= BOTTOM;
	if (y > YT) c |= TOP;
	return c;
}

void CS_LineClip()  //Cohen-Sutherland裁剪算法
{
	int x, y;
	int code1, code2, code;
	code1 = encode(x1, y01);
	code2 = encode(x2, y2);

	while (code1 != 0 || code2 != 0)
	{
		if (code1 & code2)
			return;
		if (code1 != 0)
			code = code1;
		else
			code = code2;

		if (LEFT & code)
		{
			x = XL;
			y = y01 + (y2 - y01)*(XL - x1) / (x2 - x1);
		}
		else if (RIGHT & code)
		{
			x = XR;
			y = y01 + (y2 - y01)*(XR - x1) / (x2 - x1);
		}
		else if (BOTTOM & code)
		{
			y = YB;
			x = x1 + (x2 - x1)*(YB - y01) / (y2 - y01);
		}
		else if (TOP & code)
		{
			y = YT;
			x = x1 + (x2 - x1)*(YT - y01) / (y2 - y01);
		}
		if (code == code1)
		{
			x1 = x; y01 = y; code1 = encode(x1, y01);
		}
		else
		{
			x2 = x; y2 = y; code2 = encode(x2, y2);
		}
	}

}


void init()  //初始化函数
{
	glClearColor(0.0, 0.0, 0.0, 0.0);  //设置背景颜色
	glMatrixMode(GL_PROJECTION);       // 设置投影参数
	gluOrtho2D(0.0, 600.0, 0.0, 400.0); // 设置场景的大小
	CS_LineClip();  //执行一次裁剪算法
}

void mydisplay()  //显示函数
{
	//绘制方形边界
	glClear(GL_COLOR_BUFFER_BIT);
	glColor3f(1.0, 0.0, 0.0);
	glPointSize(2);
	glBegin(GL_LINE_LOOP);
	glVertex2i(XL, YT);
	glVertex2i(XL, YB);
	glVertex2i(XR, YB);
	glVertex2i(XR, YT);
	glEnd();
	glFlush();
	//绘制未裁剪前的线段
	glBegin(GL_LINES);
	glVertex2i(x1_init, y1_init);
	glVertex2i(x2_init, y2_init);
	glEnd();
	glFlush();
	//绘制裁剪后的线段
	glColor3f(0.0, 0.0, 0.0);
	glBegin(GL_LINES);
	glVertex2i(x1, y01);
	glVertex2i(x2, y2);
	glEnd();
	glFlush();
}

int main(int argc, char *argv[])
{
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE);
	glutInitWindowPosition(100, 100);
	glutInitWindowSize(400, 400);
	glutCreateWindow("Cohen-Sutherland裁剪算法");
	init();
	glutDisplayFunc(&mydisplay);
	glutMainLoop();
	return 0;
}

