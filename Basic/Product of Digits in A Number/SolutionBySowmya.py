#include <iostream>
#include<string.h>
using namespace std;

int main()
{
    int n , i;
    int product = 1;
    cout<<"Enter the number: ";
    cin>>n;
    string str = to_string(n);
    for (i=0 ; i<str.length() ; i++)
    {
        if((str[i]-'0') != 0)
        {
            product = (str[i]-'0') * product; 
        }
    }
    cout<<"\nThe product of the digits is:"<<product; 
}
