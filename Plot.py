import matplotlib.pyplot as plt

def plot_graph(x,y,n,N):
    c1 = plt.Circle((0, 0), radius=1, fc="None", ec="r", linewidth=2, color = "black")
    ax = plt.gca()
    ax.add_patch(c1)
    plt.axis("scaled")
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("PLOT")

    plt.scatter(x, y, marker=".", color = "green", label = "POINT")
    plt.savefig('out_graph'+str(n)+'_'+str(N)+'.png', dpi=300, orientation='portrait', transparent=False, pad_inches=0.0)

