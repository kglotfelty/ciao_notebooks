from pycrates import read_file

from calc_dist import calc_distance

import sys

tol = float(sys.argv[1])/60.0


early = read_file("no_cal")
later = read_file("o_by_date.fits[obs_mode=POINTING,obspar_ver=7:][cols ra_pnt,dec_pnt,obs_id]")

er = early.get_column("ra_pnt").values
ed = early.get_column("dec_pnt").values
eo = early.get_column("obs_id").values
ej = early.get_column("object").values

lr = later.get_column("ra_pnt").values
ld = later.get_column("dec_pnt").values
lo = later.get_column("obs_id").values


early = { o : [r,d,j] for o,r,d,j in zip(eo,er,ed,ej) }
later = { o : [r,d] for o,r,d in zip(lo,lr,ld) }

#tol = 1.0/60.0 # 1 arcmin

for ee in early:
    for ll in later:
        d = calc_distance( early[ee][0],early[ee][1], later[ll][0],later[ll][1])
        if d <= tol:
            early[ee].append( ll )

unq = [ x for x in early if len(early[x])==3]

for u in unq: print("{}\t{}".format(u,early[u][2]))
