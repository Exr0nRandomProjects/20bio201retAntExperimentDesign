from matplotlib import pyplot as plt

def dist(a, b):
    from math import sqrt
    return sqrt(sum([(a[i] - b[i])**2 for i in range(len(a))]))

def proc_data(fname: str, center: (float, float)):
    dists = []
    with open(fname, 'r', newline='') as csvfile:
        from csv import reader
        from math import sqrt
        rf = reader(csvfile)
        for i, row in enumerate(rf):
            if i == 0: continue
            if not row[0] or not row[1]: continue
            dists.append(dist(center, [float(x) for x in row[:2]]))
    return dists

datasets = [
    ('isoamyl_fly1.csv', (300, 300)),
    ('isoamyl_fly2.csv', (300, 300)),
    ('trackfeet_fly1.csv', (300, 300)),
    ('trackfeet_fly2.csv', (300, 300)),
        ]

if __name__ == '__main__':
    # from os import scandir
    # for name in scandir('data'):
    for fname, center in datasets:
        plt.clf()
        plt.plot(proc_data('data/'+fname, center))
        plt.ylabel(f'distance from {center} for {fname}')
        plt.savefig('out/' + fname.replace('.csv', ''))
        from os import system
        system(f"qlmanage -p out/{fname.replace('.csv', '.png')} >/dev/null 2>&1")

