#include <math.h>
#include <stdlib.h>
#include <stdio.h>
#include <fstream>
#include <set>
#include <iostream>
#include <time.h>
#include <vector>
#include <map>
#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <cmath>

using namespace std;
typedef set<int, std::less<int> > iset;
typedef std::map<int, iset> intiset;
typedef std::map<int, double> doublemap;

int main(int argc, char *argv[])
	{int nov=5;
    iset diag;
    intiset c,d;
    char *fh;fh=argv[1];FILE *lh;
    if(!(lh=fopen(fh,"r"))) {fprintf(stderr,"Input file error!\n");exit(-1);}
    char *fx;fx=argv[2];FILE *lx;
    if(!(lx=fopen(fx,"r"))) {fprintf(stderr,"Input file error!\n");exit(-1);}
    int size=atoi(argv[3]);
    int j=1,i=0,e;
    int rep = atoi(argv[4]);
    while (!feof(lh))
        {i++;
        if (i>size)
            {j++;
            i=1;
            }
        fscanf(lh,"%d",&e);
        if (j!=i)
            {if (e>0)
                {c[j].insert(i);
                c[i].insert(j);
                }
            }
        else
            {if (e>0)
                {diag.insert(i);
                }
            }
        }
    d=c;
    j=1;
    i=0;
    while (!feof(lx))
        {i++;
        if (i>size)
            {j++;
            i=1;
            }
        fscanf(lx,"%d",&e);
        if (e>0)
            {if (c.find(i)!=c.end())
                {if (c.find(j)!=c.end())
                    {if (i!=j)
                        {d[i].insert(j);
                        d[j].insert(i);
                        }
                    }
                }
            }
        }
    //get tmp for nodes in c
    doublemap tmp;
    for(intiset::iterator hi=c.begin();hi!=c.end();hi++)
        {tmp[hi->first]=2.0*((double) hi->second.size())/((double) d[hi->first].size());
        }
    //iterations:
    doublemap sa;
    for(int ii=1;ii<=rep;ii++)
        {for(intiset::iterator hi=c.begin();hi!=c.end();hi++)
            {sa[hi->first]=0;
            for(iset::iterator hk=d[hi->first].begin();hk!=d[hi->first].end();hk++)
                {sa[hi->first]+=1.0/(tmp[hi->first]+1.0/tmp[*hk]);
                }
            }
        for(intiset::iterator hi=c.begin();hi!=c.end();hi++)
            {tmp[hi->first]=((double) hi->second.size())/sa[hi->first];
            }
        }
    char fq[255];
    sprintf(fq,"alpha_%s_%s_%d.txt",argv[1],argv[2],rep);
    ofstream lq(fq, ios::out);
    for(intiset::iterator hi=c.begin();hi!=c.end();hi++)
        {lq << hi->first << "\11" << 1.0/tmp[hi->first] << "\n";
        }
    char fy[255];
    sprintf(fy,"alpha_exp_%s_%s_%d.csv",argv[1],argv[2],rep);
    ofstream ly(fy, ios::out);
    int v;
    for(int ii=1;ii<=size;ii++)
        {for(int ij=1;ij<=size;ij++)
            {v=0;
            if (ii!=ij)
                {if (d.find(ii)!=d.end())
                    {if (d[ii].find(ij)!=d[ii].end())
                        {v=1;
                        }
                    }
                }
            else
                {//If diagonals are meant to be kept unchanged:
                //v=1;
                //Currently diagonals are set to zero in the randomized networks
                }
            if (v==1)
                {if (ii!=ij)
                    {if (ij!=size)
                        {ly << 1.0/(1.0+1.0/tmp[ii]/tmp[ij]) << ",";
                        }
                    else
                        {ly << 1.0/(1.0+1.0/tmp[ii]/tmp[ij]);
                        }
                    }
                else
                    {if (diag.find(ii)!=diag.end())
                        {if (ij!=size)
                            {ly << 1 << ",";
                            }
                        else
                            {ly << 1;
                            }
                        }
                    else
                        {if (ij!=size)
                            {ly << 0 << ",";
                            }
                        else
                            {ly <<0;
                            }
                        }
                    }
                }
            else
                {if (ij!=size)
                    {ly << 0 << ",";
                    }
                else
                    {ly <<0;
                    }
                }
            }
        ly << "\n";
        }
    lq.close();
    return 0;
    }
