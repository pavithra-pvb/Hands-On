// C++ Program for Arrays


#include<iostream>

using namespace std;

int main()
{
    /*int A[5];
    A[0] = 12;
    A[1] = 15;
    A[2] = 25;*/

    int n;
    cout<<"Enter Array Size:"<<endl;
    cin>>n;
    //int A[10] = {2,4,6,8,10,12,14};
    int A[n];
    A[0] = 2;
    /* cout<<sizeof(A)<<endl;
    cout<<A[1]<<endl;
    printf("%d\n", A[4]); */

    //for(int i = 0; i < 10; i++)
    for(int x:A)
    {
        //cout<<A[i]<<endl;
        cout<<x<<endl;
    }

    return 0;
}