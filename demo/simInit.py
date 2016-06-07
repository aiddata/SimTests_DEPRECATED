from mpi4py import MPI
from subprocess import Popen, PIPE, STDOUT, call, check_output, CalledProcessError
import random
import time

comm = MPI.COMM_WORLD

size = comm.Get_size()
rank = comm.Get_rank()
name = MPI.Get_processor_name()

sim_path = '/sciclone/home00/geogdan/SimTests/demo/pySims_h.R'

iterations = 1000
c = rank

version = "12b"

while c < iterations:
    print "Worker - rank %d on %s."%(rank, name) 
    out_path = '/sciclone/home00/geogdan/H/sim_'+str(c)+'.csv'


    nrandom = "5000"#str(500 + random.random()*4000)
    xvar_psill = "1.0"#str(0.1 + random.random()*0.9)
    minx = "-45.0"
    maxx = "45.0"
    miny = "-22.5"
    maxy = "22.5"

    var1_vrange = "2000"#str(250 + random.random()*2500)
    var1_error = "0.1"#str(0.1 + random.random()*0.9)
    prop_acc = "1.0"#str(0.1 + random.random()*.75)
    var1_error_vrange = "1000"#str(250 + random.random()*2500)
    mod_error_magnitude = "0"#str(0.1 + random.random()*2)
    trt_prc = str(0.05 + random.random() * 0.05)
    theta = "1.0"
    beta = "1.0"#str(0.2 + random.random()*5)
    spill_vrange = "1500"#str(250 + random.random()*2500)
    spill_magnitude= str(0.05 + random.random()*1.0)
    cal= str(0.25 + random.random()*1.75)
    sample_size = "0.5"#str(0.2 + random.random()*0.8)
    tree_split_lim= "5"#str(5 + random.random()*5)
    mod_error_vrange= "1000"#str(250 + random.random()*2500)
    xvar_error_psill = "1"#str(0.1 + random.random()*0.9)
    mod_error_psill = "1"#str(0.1 + random.random()*0.9)
    trt_spill_sill = "1"#str(0.1 + random.random()*0.9)
    tree_thresh = str(0.10 + random.random() * 0.30)
    thresh_est = str(0.05 + random.random() * 0.95)
    trtcon_overlap = str(0.2 + random.random() * 0.75)

    try:
      path = ("Rscript " +
      sim_path + " " +
      version + " " +
      nrandom+ " " +
      xvar_psill+ " " +
      minx+ " "+
      maxx+ " "+
      miny+ " "+
      maxy+ " "+
      var1_vrange+ " "+
      var1_error+ " "+
      prop_acc+ " "+
      var1_error_vrange+ " "+
      mod_error_magnitude+ " "+
      trt_prc+ " "+
      theta+ " "+
      beta+ " "+
      spill_vrange+ " "+
      spill_magnitude+ " "+
      cal+ " "+
      sample_size+ " "+
      tree_split_lim+ " "+
      mod_error_vrange+ " "+
      out_path+ " " +
      xvar_error_psill+ " "+
      mod_error_psill+ " "+
      trt_spill_sill + " "+
      tree_thresh + " "+
      thresh_est + " "+
      trtcon_overlap)
                        
      R_ret = check_output(path,
		                  	stderr=STDOUT,
                        shell=True)

      print c
      print R_ret
      print "========================"

    except CalledProcessError as sts_err:                                                                                                   
	    print c
	    print path
	    print ">> subprocess error code:", sts_err.returncode, '\n', sts_err.output
	    print "ERROR: Insufficient Matches or another error occured in the R Script. Specifics unknown.  Good luck."
	    print version
	    print nrandom 
	    print xvar_psill 
	    print minx
	    print maxx 
	    print miny
	    print maxy
	    print var1_vrange
	    print var1_error
	    print prop_acc 
	    print var1_error_vrange 
	    print mod_error_magnitude 
	    print trt_prc 
	    print theta 
	    print beta 
	    print spill_vrange 
	    print spill_magnitude
	    print cal
	    print sample_size
	    print tree_split_lim
	    print mod_error_vrange
	    print xvar_error_psill 
	    print mod_error_psill 
	    print trt_spill_sill
      
    c += size

