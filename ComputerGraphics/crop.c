#include <Windows.h>  
#include <gl/glut.h>  
//////////////////////////////////////////////////////////////////////////  
//区域码  
const GLint leftBitCode=0x1;  
const GLint rightBitCode=0x2;  
const GLint buttonBitCode=0x4;  
const GLint topBitCode=0x8;  
GLint winWidth=640,winHeight=480;  
class screenPT  
{  
public:  
    GLfloat x,y;  
};  
inline GLint inside(GLint code){return GLint(!code);}   //判断点是否在裁剪区内  
inline GLint reject(GLint code1,GLint code2){return GLint(code1&code2);}    //判断能否完全排除一条线段  
inline GLint accept(GLint code1,GLint code2){return GLint(!(code1 | code2));}   //判断能否完全接受一条线段  
inline void swapPT(screenPT& a,screenPT& b){screenPT t=a;a=b;b=t;}  //交换两个点  
inline void swapCode(GLubyte& a,GLubyte& b){GLubyte t=a;a=b;b=t;}   //交换两个区域码  
//确定一个点所在位置的区域码  
GLubyte encode(const screenPT& p,const screenPT& winMin,const screenPT& winMax)  
{  
    GLubyte code=0x00;  
    if(p.x<winMin.x)  
        code |= leftBitCode;  
    if(p.x>winMax.x)  
        code |= rightBitCode;  
    if(p.y<winMin.y)  
        code |= buttonBitCode;  
    if(p.y>winMax.y)  
        code |= topBitCode;  
    return code;  
}  
//在屏幕上画一条未裁剪的线，由裁剪函数调用  
void drawOneLine(const screenPT& a,const screenPT& b)  
{  
    glBegin(GL_LINES);  
        glVertex2f(a.x,a.y);  
        glVertex2f(b.x,b.y);  
    glEnd();  
}  
//裁剪函数  
void lineClip(screenPT winMin,screenPT winMax,screenPT lineBegin,screenPT lineEnd)  
{  
    GLubyte code1,code2;    //保存两个端点的区域码  
    GLboolean done=false,plotLine=false;    //判断裁剪是否结束和是否要绘制直线  
    GLfloat k;              //斜率  
    while(!done)  
    {  
        code1 = encode(lineBegin,winMin,winMax);  
        code2 = encode(lineEnd,winMin,winMax);  
        if(accept(code1,code2))         //当前直线能完全绘制  
        {  
            done=true;  
            plotLine=true;  
        }  
        else  
        {  
            if(reject(code1,code2))     //当前直线能完全排除  
                done = true;  
            else  
            {  
                if(inside(code1))   //若lineBegin端点在裁剪区内则交换两个端点使它在裁剪区外  
                {  
                    swapPT(lineBegin,lineEnd);  
                    swapCode(code1,code2);  
                }  
                //计算斜率  
                if(lineBegin.x != lineEnd.x)  
                    k = (lineEnd.y-lineBegin.y)/(lineEnd.x-lineBegin.x);  
                //开始裁剪,以下与运算若结果为真，  
                //则lineBegin在边界外，此时将lineBegin移向直线与该边界的交点  
                if(code1 & leftBitCode)  
                {  
                    lineBegin.y += (winMin.x-lineBegin.x)*k;  
                    lineBegin.x = winMin.x;  
                }  
                else if(code1 & rightBitCode)  
                {  
                    lineBegin.y += (winMax.x-lineBegin.x)*k;  
                    lineBegin.x = winMax.x;  
                }  
                else if(code1 & buttonBitCode)  
                {  
                    if(lineBegin.x != lineEnd.x)  
                        lineBegin.x += (winMin.y-lineBegin.y)/k;  
                    lineBegin.y = winMin.y;  
                }  
                else if(code1 & topBitCode)  
                {  
                    if(lineBegin.x != lineEnd.x)  
                        lineBegin.x += (winMax.y-lineBegin.y)/k;  
                    lineBegin.y = winMax.y;  
                }  
            }  
        }  
    }  
    if(plotLine)  
        drawOneLine(lineBegin,lineEnd); //绘制裁剪好的直线  
}  
//////////////////////////////////////////////////////////////////////////  
void rect(screenPT winMin,screenPT winMax)  
{  
    glBegin(GL_LINE_LOOP);  
        glVertex2f(winMin.x,winMin.y);  
        glVertex2f(winMax.x,winMin.y);  
        glVertex2f(winMax.x,winMax.y);  
        glVertex2f(winMin.x,winMax.y);  
    glEnd();  
}  
void init()  
{  
    glViewport(0,0,winWidth,winHeight);  
    glClearColor(1.0,1.0,1.0,0.0);  
    glMatrixMode(GL_PROJECTION);  
    glLoadIdentity();  
    gluOrtho2D(0,winWidth,0,winHeight);  
    glMatrixMode(GL_MODELVIEW);  
}  
void display()  
{  
    screenPT winMin,winMax,lineBegin,lineEnd;  
    winMin.x=100.0; winMin.y=50.0;  
    winMax.x=400.0; winMax.y=300.0;  
    lineBegin.x=0.0;    lineBegin.y=0.0;  
    lineEnd.x=winWidth; lineEnd.y=winHeight;  
    glClear(GL_COLOR_BUFFER_BIT);  
    glColor3f(0.0,0.0,0.0);  
    rect(winMin,winMax);    //为裁剪区域绘制一个边框  
    lineClip(winMin,winMax,lineBegin,lineEnd);    
    lineBegin.y=240.0;  lineEnd.y=240.0;  
    lineClip(winMin,winMax,lineBegin,lineEnd);    
    lineBegin.x=320.0;  lineBegin.y=0.0;  
    lineEnd.x=320.0;    lineEnd.y=winHeight;  
    lineClip(winMin,winMax,lineBegin,lineEnd);  
    glFlush();  
}  
int main(int argc,char** argv)  
{  
    glutInit(&argc,argv);  
    glutInitWindowPosition(100,100);  
    glutInitWindowSize(winWidth,winHeight);  
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);  
    glutCreateWindow("my app");  
    init();  
    glutDisplayFunc(display);  
    glutMainLoop();  
    return 0;  
}  
