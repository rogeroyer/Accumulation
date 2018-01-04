#include"stdafx.h"

#include <windows.h>    
#include <math.h>    
#include <gl/GL.h>    
#include <gl/glut.h>    
int SCREEN_HEIGHT = 480;    
int NUMPOINTS = 0;    
class Point    
{    
public:    
    float x, y;    
    void setxy(float x2, float y2)    
    {    
        x = x2;    
        y = y2;    
    }    
    Point  operator&(const Point & rPoint)    
    {    
        x = rPoint.x;    
        y = rPoint.y;    
        return * this;    
    }    
};
Point abc[4];    
void myInit()    
{    
    glClearColor(0.0,0.0,0.0,0.0);    
    glColor3f(1.0f, 0.0, 0.0);    
    glPointSize(4.0);    
    glMatrixMode(GL_PROJECTION);    
    glLoadIdentity();    
    gluOrtho2D(0.0, 640, 0.0, 480.0);    
}    
void drawDot(Point pt)     
{    
    glBegin(GL_POINTS);    
    glVertex2f(pt.x, pt.y);    
    glEnd();    
    glFlush();    
}    
void drawLine(Point p1, Point p2)    
{    
    glBegin(GL_LINES);    
    glVertex2f(p1.x, p1.y);    
    glVertex2f(p2.x, p2.y);    
    glEnd();    
    glFlush();    
}    
//四个控制点的贝塞尔曲线 即三次Bezier曲线  
Point drawBezier(Point A, Point B, Point C, Point D,double t)     
{    
    Point P;  
    double a1 = pow((1-t),3);  
    double a2 = pow((1-t),2)*3*t;  
    double a3 = 3*t*t*(1-t);  
    double a4 = t*t*t;  
  
    P.x = a1*A.x+a2*B.x+a3*C.x+a4*D.x;  
    P.y = a1*A.y+a2*B.y+a3*C.y+a4*D.y;  
    return P;    
}    
void myMouse(int button, int state, int x, int y)    
{    
    if(button == GLUT_LEFT_BUTTON && state == GLUT_DOWN)    
    {    
        abc[NUMPOINTS].setxy((float)x, (float)(SCREEN_HEIGHT - y));    
        NUMPOINTS++;    
        if (NUMPOINTS == 4)    
        {    
            glColor3f(1.0, 0.0, 1.0);    
  
            drawDot(abc[0]);    
            drawDot(abc[1]);    
            drawDot(abc[2]);    
            drawDot(abc[3]);    
            glColor3f(1.0, 1.0, 0.0);    
            drawLine(abc[0], abc[1]);    
            drawLine(abc[1], abc[2]);    
            drawLine(abc[2], abc[3]);    
            glColor3f(0.0, 1.0, 1.0);    
            Point POld = abc[0];    
            for (double t = 0.0; t<=1.0;t+=0.1)    
            {    
                Point P = drawBezier(abc[0], abc[1], abc[2],  abc[3], t);    
                drawLine(POld, P);    
                POld = P;    
            }    
            glColor3f(1.0, 0.0, 0.0);    
            NUMPOINTS = 0;    
        }    
    }    
}    
void myDisplay()    
{    
    glClear(GL_COLOR_BUFFER_BIT);    
    glFlush();    
}    
int main(int argc, char * agrv[])    
{    
    glutInit(&argc, agrv);    
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);    
    glutInitWindowSize(640, 480);    
    glutInitWindowPosition(100, 150);    
    glutCreateWindow("Bezier Curve");    
    glutMouseFunc(myMouse);    
    glutDisplayFunc(myDisplay);    
    myInit();    
    glutMainLoop();    
    return 0;    
}   
