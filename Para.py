from datetime import datetime
from joblib import Parallel, delayed
import Monte
import Plot

def Para(n):
    start_time = datetime.now()
    r = Parallel(n_jobs=n)( [delayed(Monte.monte)(i) for i in range(10000)] )
    print(r[-1])
    end_time = datetime.now()
    return print('Duration: {}'.format(end_time - start_time))

def Para2(n,N):
    start_time = datetime.now()
    r = Parallel(n_jobs=n)( [delayed(Monte.monte2)(i) for i in range(N)] )
    print(r[-1][0])
    end_time = datetime.now()
    Plot.plot_graph(r[-1][1],r[-1][2],n,N)
    return print('Duration: {}'.format(end_time - start_time))