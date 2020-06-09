#include<iostream>
#include<cmath>
using namespace std;

int main()
{
    float p=0.0;
    for (float i=1; i<1000;i++)
    {
        p=p+(1/(i*i));
    }
    float pi= 6*p;
    cout<<"pi is: "<<sqrt(pi)<<endl;
    return 0;
}