#include "gl/glut.h"  
#include "windows.h"  
const int POINTNUM=7;      //多边形点数.  
  
/******定义结构体用于活性边表AET和新边表NET***********************************/  
 typedef struct XET  
 {  
	float x;  
	float dx,ymax;  
	XET* next;  
 }AET,NET;  
  
/******定义点结构体point******************************************************/  
 struct point  
 {  
	float x;  
	float y;  
 }  
 polypoint[POINTNUM]={250,50,550,150,550,400,250,250,100,350,100,100,120,30};//多边形顶点  
  
 void PolyScan()  
{  
/******计算最高点的y坐标(扫描到此结束)****************************************/  
	 int MaxY=0;  
	 int i;  
	 for(i=0;i<POINTNUM;i++)  
		if(polypoint[i].y>MaxY)  
			MaxY=polypoint[i].y;  
    
	/*******初始化AET表***********************************************************/  
	 AET *pAET=new AET;  
	 pAET->next=NULL;  
    
	/******初始化NET表************************************************************/  
	 NET *pNET[1024];  
	 for(i=0;i<=MaxY;i++)  
	 {  
		 pNET[i]=new NET;  
		 pNET[i]->next=NULL;  
	 }  
	 glClear(GL_COLOR_BUFFER_BIT);        //赋值的窗口显示.    
	 glColor3f(0.0,0.0,0.0);             //设置直线的颜色红色  
	 glBegin(GL_POINTS);  
	/******扫描并建立NET表*********************************************************/  
	for(i=0;i<=MaxY;i++)  
	{  
		for(int j=0;j<POINTNUM;j++)  
			if(polypoint[j].y==i)  
			{  //一个点跟前面的一个点形成一条线段，跟后面的点也形成线段     
				if(polypoint[(j-1+POINTNUM)%POINTNUM].y>polypoint[j].y)  
				{  
					NET *p=new NET;  
					p->x=polypoint[j].x;  
					p->ymax=polypoint[(j-1+POINTNUM)%POINTNUM].y;  
					p->dx=(polypoint[(j-1+POINTNUM)%POINTNUM].x-polypoint[j].x)/(polypoint[(j-1+POINTNUM)%POINTNUM].y-polypoint[j].y);  
					p->next=pNET[i]->next;  
					pNET[i]->next=p;  
        
				}  
				if(polypoint[(j+1+POINTNUM)%POINTNUM].y>polypoint[j].y)  
				{  
					NET *p=new NET;        
					p->x=polypoint[j].x;  
					p->ymax=polypoint[(j+1+POINTNUM)%POINTNUM].y;  
					p->dx=(polypoint[(j+1+POINTNUM)%POINTNUM].x-polypoint[j].x)/(polypoint[(j+1+POINTNUM)%POINTNUM].y-polypoint[j].y);  
					p->next=pNET[i]->next;  
					pNET[i]->next=p;  
				}  
			}  
	 }  
	/******建立并更新活性边表AET*****************************************************/  
	for(i=0;i<=MaxY;i++)  
	{  
		//计算新的交点x,更新AET  
			NET *p=pAET->next;  
		while(p)  
		{  
			p->x=p->x + p->dx;  
			p=p->next;  
		}  
		//更新后新AET先排序*************************************************************/  
		//断表排序,不再开辟空间  
		AET *tq=pAET;  
		p=pAET->next;  
		tq->next=NULL;  
		while(p)  
		{  
			while(tq->next && p->x >= tq->next->x)  
			tq=tq->next;  
			NET *s=p->next;  
			p->next=tq->next;  
			tq->next=p;  
			p=s;  
			tq=pAET;  
		}  
		//(改进算法)先从AET表中删除ymax==i的结点****************************************/  
	   AET *q=pAET;  
	   p=q->next;  
	   while(p)  
	   {  
			if(p->ymax==i)  
			{  
				q->next=p->next;  
				delete p;  
				p=q->next;  
			}  
			else  
			{  
				q=q->next;  
				p=q->next;  
			}  
		}  
		//将NET中的新点加入AET,并用插入法按X值递增排序**********************************/  
		p=pNET[i]->next;  
		q=pAET;  
		while(p)  
		{  
			while(q->next && p->x >= q->next->x)  
				q=q->next;  
			NET *s=p->next;  
			p->next=q->next;  
			q->next=p;  
			p=s;  
			q=pAET;  
		}  

	   /******配对填充颜色***************************************************************/   
		p=pAET->next;  
		while(p && p->next)  
		{  
			for(float j=p->x;j<=p->next->x;j++)  
				glVertex2i(static_cast<int>(j),i);  
			p=p->next->next;//考虑端点情况  
		}  
            
	}  
    glEnd();  
	glFlush();   
}  
void init(void)  
{
	glClearColor(1.0,1.0,1.0,0.0);  
	//窗口的背景颜色设置为白色  
	glMatrixMode(GL_PROJECTION);  
	gluOrtho2D(0.0,600.0,0.0,450.0);  
}  
  
void main(int argc,char* argv)  
{  
    glutInit(&argc,&argv);                //I初始化 GLUT.  
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);    //设置显示模式：单个缓存和使用RGB模型  
    glutInitWindowPosition(50,100);        //设置窗口的顶部和左边位置  
    glutInitWindowSize(400,300);        //设置窗口的高度和宽度  
    glutCreateWindow("An Example OpenGL Program");    //创建显示窗口  
  
    init();                                //调用初始化过程  
    glutDisplayFunc(PolyScan);        //图形的定义传递给我window.  
    glutMainLoop();                        //显示所有的图形并等待  
}  
