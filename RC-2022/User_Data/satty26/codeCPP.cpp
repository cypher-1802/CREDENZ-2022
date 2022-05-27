#include "/home/rc/RC-2022/sandbox/filter/filter.h"
#include<iostream>
#include<vector>
#include<iomanip>
#include<algorithm>
#include<stack>
#include<bitset>
#include<string>
#include<queue>
#include<set>
#include<cstring>
#include<map>
#include<math.h>
 
 
using namespace std;

#define                       ll                                 long long int
#define                      mod                                    1000000007
#define 					array								long long int n; cin>>n;ll a[n];for(long long int i=0;i<n;i++) cin>>a[i];
#define 					printarray							for(long long int i=0;i<n;i++) cout<<a[i]<<"\n";
#define                     test                                ll t; cin>>t; while(t--)
#define   fastio  ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)
#define   infinity                                                             unsigned ll a = numeric_limits<unsigned ll>::max();
#define		pb 		push_back
#define   time cerr << "time taken : " << (float)clock() / CLOCKS_PER_SEC << " secs" << endl;
#define		maxel		*max_element(a,a+n)
#define		maxin		max_element(a,a+n)-a
#define		loop		for(int i=0;i<n;i++)
#define		mp 			make_pair
#define		pairvec		vector<pair<ll,ll> > v
#define all(c) (c).begin(), (c).end()
#define PI 3.141593
#define  mem(a,x)    memset(a,x,sizeof(a))

int main() {
put_filter();

	fastio;
	string pi = "3141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481117450284102701938521105559644622948954930381964428810975665933446128475648233786783165271201909145648566923460348610454326648213393607260249141273724587006606315588174881520920962829254091715364367892590360011330530548820466521384146951941511609433057270365759591953092186117381932611793105118548074462379962749567351885752724891227938183011949129833673362440656643086021394946395224737190702179860943702770539217176293176752384674818467669405132000568127145263560827785771342757789609173637178721468440901224953430146549585371050792279689258923542019956112129021960864034418159813629774771309960518707211349999998372978049951059731732816096318595024459455346908302642522308253344685035261931188171010003137838752886587533208381420617177669147303598253490428755468731159562863882353787593751957781857780532171226806613001927876611195909216420198938";
	ll n = 1000;
	ll eve[n];
	ll odd[n];
	ll o = 0;
	ll e = 0;
	loop{
		if ((pi[i] - '0') % 2 != 0) {
			o++;
		}
		else
			e++;
		eve[i] = e;
		odd[i] = o;
	}
	test{
		ll num;
		cin >> num;
		if (num % 2 == 0)
			cout << eve[num - 1] << "\n";
		else
			cout << odd[num - 1] << "\n";
	}
	return 0;
}



