#include<iostream>
#include<cmath>
#include<time.h>

using namespace std;
int main()
{
    srand((unsigned)time (NULL));
    float x;
    float y;
    float cnt1=0;
    float cnt2=0;
    for (int i=0; i<1000;i++)
    {
        x=(float) rand()/RAND_MAX;
        y=(float) rand()/RAND_MAX;
        if (sqrt(x*x+y*y)<1)
        {
            cnt1++;
        }
        cnt2++;
    }
    float p= cnt1/cnt2;
    cout<<"pi is: "<<4*p<<endl;
    return 0;
      
}