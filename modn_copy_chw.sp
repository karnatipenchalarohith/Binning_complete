simulator lang=spectre insensitive=yes 
model modn bsim4  { 
     1: type=n 
+ lmin=1e-005 lmax=2e-05                wmin=1.003e-005
+ wmax=90.003e-05           version=4.5               rgeomod=1
+ binunit=2                 paramchk=1                mobmod=0
+ capmod=2                  igcmod=0                  igbmod=0
+ diomod=1                  rdsmod=1                  rbodymod=0
+ rgatemod=0                permod=1                  acnqsmod=0
+ trnqsmod=0                tempmod=0                 wpemod=1
+ tnom=25                   toxe=3.981e-09       toxm=3.981e-09
+ dtox=5.958e-010           epsrox=3.9                wint=1.02e-008
+ lint=2.595e-008           ll=0                      wl=0
+ lln=1                     wln=1                     lw=0
+ ww=0                      lwn=1                     wwn=1
+ lwl=0                     wwl=0                     llc=0
+ wlc=0                     lwc=0                     wwc=0
+ lwlc=0                    wwlc=0                    xl=-1.5e-08
+ xw=0        dlc=2.595e-008       dwc=0
+ xpart=1                   toxref=3e-009             dlcig=2.5e-009
+ vth0=0.43953                       k1=0.448
+ k2=0.044342           k3=-3.7                   k3b=1.2
+ w0=0                      dvt0=0.09708              dvt1=0.3053
+ dvt2=-0.6939              dvt0w=0                   dvt1w=0
+ dvt2w=0                   dsub=0.633                minv=-0.34
+ voffl=-1.22e-009          dvtp0=1.46e-006           dvtp1=0
+ lpe0=9.921e-009           lpeb=2.178e-008           web=0
+ wec=0                     scref=1e-006              kvth0we=0.0034927135
+ lkvth0we=0                wkvth0we=0                pkvth0we=0
+ k2we=0.0038               lk2we=0                   wk2we=0
+ pk2we=0                   xj=1.6e-007               ngate=9e+019
+ ndep=5.8e+017             nsd=1e+020                phin=0
+ cdsc=0                    cdscb=0                   cdscd=0
+ cit=0.00082854      voff=-0.13055      tvoff=1.500000e-03
+ nfactor=0.94972           eta0=0.22771       etab=-0.308
+ ud=0                      lud=0                     wud=0
+ pud=0                     ku0we=0                   lku0we=0
+ wku0we=0                  pku0we=0                  u0=0.030526
+ ua=-1.1118e-009           ub=2.3263e-018            uc=1.9167e-010
+ vsat=73329         a0=1.0724            ags=0.50072
+ a1=0                      a2=0.995                  b0=0
+ b1=0                      keta=-0.051375            dwg=0
+ dwb=0                     pclm=0.71887       pdiblc1=0
+ pdiblc2=0.000975                          pdiblcb=0
+ drout=0.5                 pvag=0.6279               delta=0.005
+ pscbe1=4.5e+008           pscbe2=1e-020             fprout=0
+ pdits=0                   pditsd=0                  pditsl=0
+ rsh=7.28                  rdsw=200                  rsw=90.88
+ rdw=90.88                 prwg=0                    prwb=0
+ wr=1                      alpha0=1.454e-007         alpha1=2.295
+ beta0=17.8                agidl=2.593e-009          bgidl=1.8508e+009
+ cgidl=0.25                egidl=0.2624              aigbacc=0.01213
+ bigbacc=0.006537          cigbacc=0.2809            nigbacc=4.05
+ aigbinv=0.35              bigbinv=0.03              cigbinv=0.006
+ eigbinv=1.1               nigbinv=1                 aigc=0.01
+ bigc=0.00144              cigc=1.515e-005           aigsd=0.008379
+ bigsd=0.0002699           cigsd=3.925e-020          nigc=1
+ poxedge=1                 pigcd=2.171               ntox=1
+ xrcrg1=12                 xrcrg2=1                  cgso=1e-10
+ cgdo=1e-10                 cgbo=0                    cgdl=1e-10
+ cgsl=1e-10                 clc=1e-007                cle=0.6
+ cf=1                    ckappas=0.6               ckappad=0.6
+ acde=0.4                  moin=5.346                noff=1.973
+ voffcv=-0.0904            kt1=-0.24611586           kt1l=0
+ kt2=-0.055191541          pkt2=0                    wkt2=0
+ lkt2=0                    ute=-1.8116912            ua1=2.3415359e-009
+ ub1=-4.4298745e-018       uc1=-8.0699954e-011       prt=0
+ at=117848.51              pat=0                     wat=0
+ lat=0                     jss=2.85e-07              jsd=2.85e-07
+ jsws=6.9e-13              jswd=6.9e-13              jswgs=6.9e-13
+ jswgd=6.9e-13             njs=1                     njd=1
+ ijthsfwd=0.01             ijthdfwd=0.01             ijthsrev=0.01
+ ijthdrev=0.01             bvs=11.25                 bvd=11.25
+ xjbvs=1                   xjbvd=1                   pbs=0.6882682
+ pbd=0.6882682             cjs=1e-10                   cjd=1e-10
+ mjs=0.359                 mjd=0.359                 pbsws=0.32
+ pbswd=0.32                cjsws=1.185e-10               cjswd=1.185e-10
+ mjsws=0.202               mjswd=0.202               pbswgs=0.952
+ pbswgd=0.952              cjswgs=3.82e-10             cjswgd=3.82e-10
+ mjswgs=0.541              mjswgd=0.541              tpb=1.49e-3
+ tcj=9.05e-4               tpbsw=8.94e-04            tcjsw=8.09e-04
+ tpbswg=0.00133            tcjswg=0.00088            xtis=3
+ xtid=3                    jtsswgs=1.09e-009         jtsswgd=1.09e-009
+ njtsswg=11.6              xtsswgs=0.2886            xtsswgd=0.2886
+ tnjtsswg=1.08             vtsswgs=10                vtsswgd=10
+ dmcg=2.05e-007            dmci=3.15e-007            dmdg=0
+ dmcgt=0                   dwj=0                     xgw=0
+ xgl=-3.1e-008             rshg=8.23                 gbmin=1e-012
+ rbpb=50                   rbpd=50                   rbps=50
+ rbdb=50                   rbsb=50                   saref=1.00e-05
+ sbref=1.00e-05            ngcon=1                   wlod=5e-007
+ kvth0=2.2e-009            lkvth0=-1e-008            wkvth0=2.2e-006
+ pkvth0=-5e-014            llodvth=1                 wlodvth=1
+ stk2=2.5e-009             lodk2=1                   lodeta0=2
+ ku0=-3.2e-008             lku0=2e-007               wku0=7e-007
+ pku0=-5e-014              llodku0=1                 wlodku0=1
+ kvsat=0.4                 steta0=-1.1e-010          tku0=0.03
+ lvth0=0            wvth0=0            pvth0=0
+ lk2=0                lcit=0             pcit=0
+ lvoff=0           pvoff=0           leta0=0
+ peta0=0           lu0=0               pu0=0
+ lvsat=0           pvsat=0           la0=0
+ pa0=0               lpclm=0           ppclm=0
+ lpdiblc2=0     ppdiblc2=0     fnoimod=1
+ noia=1.250e+42                noib=7.000e+23                noic=6.080e+7
+ em=3.00e7                 ef=0.904                  minr=1e-3
 
 
     2: type=n 
+ lmin=1.2e-006                         lmax=1e-005
+ wmin=1.003e-005                       wmax=90.003e-05
+ version=4.5               rgeomod=1                 binunit=2
+ paramchk=1                mobmod=0                  capmod=2
+ igcmod=0                  igbmod=0                  diomod=1
+ rdsmod=1                  rbodymod=0                rgatemod=0
+ permod=1                  acnqsmod=0                trnqsmod=0
+ tempmod=0                 wpemod=1                  tnom=25
+ toxe=3.981e-09       toxm=3.981e-09       dtox=5.958e-010
+ epsrox=3.9                wint=1.02e-008            lint=2.595e-008
+ ll=0                      wl=0                      lln=1
+ wln=1                     lw=0                      ww=0
+ lwn=1                     wwn=1                     lwl=0
+ wwl=0                     llc=0                     wlc=0
+ lwc=0                     wwc=0                     lwlc=0
+ wwlc=0                    xl=-1.5e-08 xw=0
+ dlc=2.595e-008       dwc=0                     xpart=1
+ toxref=3e-009             dlcig=2.5e-009            vth0=0.44000255
+ lvth0=-4.6939282e-009                        k1=0.448
+ k2=0.044420158        lk2=-7.763527e-010   k3=-3.7
+ k3b=1.2                   w0=0                      dvt0=0.09708
+ dvt1=0.3053               dvt2=-0.6939              dvt0w=0
+ dvt1w=0                   dvt2w=0                   dsub=0.633
+ minv=-0.34                voffl=-1.22e-009          dvtp0=1.46e-006
+ dvtp1=0                   lpe0=9.921e-009           lpeb=2.178e-008
+ web=0                     wec=0                     scref=1e-006
+ kvth0we=0.0035080237      lkvth0we=-1.5207765e-010  wkvth0we=0
+ pkvth0we=0                k2we=0.0038               lk2we=0
+ wk2we=0                   pk2we=0                   xj=1.6e-007
+ ngate=9e+019              ndep=5.8e+017             nsd=1e+020
+ phin=0                    cdsc=0                    cdscb=0
+ cdscd=0                   cit=0.00094159467   lcit=-1.1229833e-009
+ voff=-0.13088478   tvoff=1.500000e-03        lvoff=3.3253987e-009
+ nfactor=0.94802421        lnfactor=1.6844423e-008   eta0=0.2200075
+ leta0=7.650975e-008                         etab=-0.308
+ ud=0                      lud=0                     wud=0
+ pud=0                     ku0we=0                   lku0we=0
+ wku0we=0                  pku0we=0                  u0=0.031147016
+ lu0=-6.1686146e-009 ua=-1.0351999e-009        lua=-7.608768e-016
+ ub=2.2622927e-018         lub=6.3579065e-025        uc=1.9814412e-010
+ luc=-6.4308095e-017       vsat=73219.038     lvsat=0.0010922656
+ a0=1.0632966         la0=9.0425265e-008  ags=0.47288051
+ lags=2.7653248e-007       a1=0                      a2=0.995
+ b0=0                      b1=0                      keta=-0.044517814
+ lketa=-6.8113118e-008     dwg=0                     dwb=0
+ pclm=0.73030143    lpclm=-1.1354958e-007
+ pdiblc1=0                 pdiblc2=0.00083459861
+ lpdiblc2=1.3946211e-009                  pdiblcb=0
+ drout=0.5                 pvag=0.6279               delta=0.005
+ pscbe1=4.5e+008           pscbe2=1e-020             fprout=0
+ pdits=0                   pditsd=0                  pditsl=0
+ rsh=7.28                  rdsw=200                  rsw=90.88
+ rdw=90.88                 prwg=0                    prwb=0
+ wr=1                      alpha0=1.454e-007         alpha1=2.295
+ beta0=17.8                agidl=2.593e-009          bgidl=1.8508e+009
+ cgidl=0.25                egidl=0.2624              aigbacc=0.01213
+ bigbacc=0.006537          cigbacc=0.2809            nigbacc=4.05
+ aigbinv=0.35              bigbinv=0.03              cigbinv=0.006
+ eigbinv=1.1               nigbinv=1                 aigc=0.01
+ bigc=0.00144              cigc=1.515e-005           aigsd=0.008379
+ bigsd=0.0002699           cigsd=3.925e-020          nigc=1
+ poxedge=1                 pigcd=2.171               ntox=1
+ xrcrg1=12                 xrcrg2=1                  cgso=1e-10
+ cgdo=1e-10                 cgbo=0                    cgdl=1e-10
+ cgsl=1e-10                 clc=1e-007                cle=0.6
+ cf=1                    ckappas=0.6               ckappad=0.6
+ acde=0.4                  moin=5.346                noff=1.973
+ voffcv=-0.0904            kt1=-0.24355302           pkt1=0
+ wkt1=0                    lkt1=-2.5456989e-08       kt1l=0
+ kt2=-0.055236684          pkt2=0                    wkt2=0
+ lkt2=4.48417e-10          ute=-1.8758               lute=6.3679863e-007
+ ua1=2.2474837e-09         pua1=0                    wua1=0
+ lua1=9.3422973e-16        ub1=-4.4202733e-018       lub1=-9.5370005e-026
+ uc1=-7.421409e-11         puc1=0                    wuc1=0
+ luc1=-6.442474e-17        prt=0                     at=122782.95
+ pat=0                     wat=0                     lat=-0.049014274
+ jss=2.85e-07              jsd=2.85e-07              jsws=6.9e-13
+ jswd=6.9e-13              jswgs=6.9e-13             jswgd=6.9e-13
+ njs=1                     njd=1                     ijthsfwd=0.01
+ ijthdfwd=0.01             ijthsrev=0.01             ijthdrev=0.01
+ bvs=11.25                 bvd=11.25                 xjbvs=1
+ xjbvd=1                   pbs=0.6882682             pbd=0.6882682
+ cjs=1e-10                   cjd=1e-10                   mjs=0.359
+ mjd=0.359                 pbsws=0.32                pbswd=0.32
+ cjsws=1.185e-10               cjswd=1.185e-10               mjsws=0.202
+ mjswd=0.202               pbswgs=0.952              pbswgd=0.952
+ cjswgs=3.82e-10             cjswgd=3.82e-10             mjswgs=0.541
+ mjswgd=0.541              tpb=1.49e-3               tcj=9.05e-4
+ tpbsw=8.94e-04            tcjsw=8.09e-04            tpbswg=0.00133
+ tcjswg=0.00088            xtis=3                    xtid=3
+ jtsswgs=1.09e-009         jtsswgd=1.09e-009         njtsswg=11.6
+ xtsswgs=0.2886            xtsswgd=0.2886            tnjtsswg=1.08
+ vtsswgs=10                vtsswgd=10                dmcg=2.05e-007
+ dmci=3.15e-007            dmdg=0                    dmcgt=0
+ dwj=0                     xgw=0                     xgl=-3.1e-008
+ rshg=8.23                 gbmin=1e-012              rbpb=50
+ rbpd=50                   rbps=50                   rbdb=50
+ saref=1.00e-05            sbref=1.00e-05            rbsb=50
+ ngcon=1                   wlod=5e-007               kvth0=2.2e-009
+ lkvth0=-1e-008            wkvth0=2.2e-006           pkvth0=-5e-014
+ llodvth=1                 wlodvth=1                 stk2=2.5e-009
+ lodk2=1                   lodeta0=2                 ku0=-3.2e-008
+ lku0=2e-007               wku0=7e-007               pku0=-5e-014
+ llodku0=1                 wlodku0=1                 kvsat=0.4
+ steta0=-1.1e-010          tku0=0.03                 wvth0=0
+ pvth0=0            pcit=0             pvoff=0
+ peta0=0           pu0=0               pvsat=0
+ pa0=0               ppclm=0           ppdiblc2=0
+ fnoimod=1                 noia=1.250e+42                noib=7.000e+23
+ noic=6.080e+7                em=3.00e7                 ef=0.904
+ minr=1e-3
 
 
     3: type=n 
+ lmin=5e-007 lmax=1.2e-006
+ wmin=1.003e-005                       wmax=90.003e-05
+ version=4.5               rgeomod=1                 binunit=2
+ paramchk=1                mobmod=0                  capmod=2
+ igcmod=0                  igbmod=0                  diomod=1
+ rdsmod=1                  rbodymod=0                rgatemod=0
+ permod=1                  acnqsmod=0                trnqsmod=0
+ tempmod=0                 wpemod=1                  tnom=25
+ toxe=3.981e-09       toxm=3.981e-09       dtox=5.958e-010
+ epsrox=3.9                wint=1.02e-008            lint=2.595e-008
+ ll=0                      wl=0                      lln=1
+ wln=1                     lw=0                      ww=0
+ lwn=1                     wwn=1                     lwl=0
+ wwl=0                     llc=0                     wlc=0
+ lwc=0                     wwc=0                     lwlc=0
+ wwlc=0                    xl=-1.5e-08 xw=0
+ dlc=2.595e-008       dwc=0                     xpart=1
+ toxref=3e-009             dlcig=2.5e-009            vth0=0.42487782
+ lvth0=1.2443907e-008                         k1=0.448
+ k2=0.045638784        lk2=-2.1571775e-009  k3=-3.7
+ k3b=1.2                   w0=0                      dvt0=0.09708
+ dvt1=0.3053               dvt2=-0.6939              dvt0w=0
+ dvt1w=0                   dvt2w=0                   dsub=0.633
+ minv=-0.34                voffl=-1.22e-009          dvtp0=1.46e-006
+ dvtp1=0                   lpe0=9.921e-009           lpeb=2.178e-008
+ web=0                     wec=0                     scref=1e-006
+ kvth0we=0.0034998799      lkvth0we=-1.4284995e-010  wkvth0we=0
+ pkvth0we=0                k2we=0.0038               lk2we=0
+ wk2we=0                   pk2we=0                   xj=1.6e-007
+ ngate=9e+019              ndep=5.8e+017             nsd=1e+020
+ phin=0                    cdsc=0                    cdscb=0
+ cdscd=0                   cit=-0.00046662469  lcit=4.7267005e-010
+ voff=-0.12040787   tvoff=1.500000e-03        lvoff=-8.5459843e-009
+ nfactor=1.0247614         lnfactor=-7.0106516e-008  eta0=0.28753
+ etab=-0.308               ud=0                      lud=0
+ wud=0                     pud=0                     ku0we=0
+ lku0we=0                  wku0we=0                  pku0we=0
+ u0=0.021368288       lu0=4.9116625e-009  ua=-2.2464725e-009
+ lua=6.1161625e-016        ub=3.3377372e-018         lub=-5.8279547e-025
+ uc=1.5619583e-010         luc=-1.6776489e-017       vsat=81168.284
+ lvsat=-0.0079150256                         a0=1.6098828
+ la0=-5.289116e-007  ags=0.84742922            lags=-1.4786866e-007
+ a1=0                      a2=0.995                  b0=0
+ b1=0                      keta=-0.11739531          lketa=1.4464376e-008
+ dwg=0                     dwb=0                     pclm=0.61209779
+ lpclm=2.0386975e-008                        pdiblc1=0
+ pdiblc2=0.0024032799                      lpdiblc2=-3.8285168e-010
+ pdiblcb=0                 drout=0.5                 pvag=0.6279
+ delta=0.005               pscbe1=4.5e+008           pscbe2=1e-020
+ fprout=0                  pdits=0                   pditsd=0
+ pditsl=0                  rsh=7.28                  rdsw=200
+ rsw=90.88                 rdw=90.88                 prwg=0
+ prwb=0                    wr=1                      alpha0=1.454e-007
+ alpha1=2.295              beta0=17.8                agidl=2.593e-009
+ bgidl=1.8508e+009         cgidl=0.25                egidl=0.2624
+ aigbacc=0.01213           bigbacc=0.006537          cigbacc=0.2809
+ nigbacc=4.05              aigbinv=0.35              bigbinv=0.03
+ cigbinv=0.006             eigbinv=1.1               nigbinv=1
+ aigc=0.01                 bigc=0.00144              cigc=1.515e-005
+ aigsd=0.008379            bigsd=0.0002699           cigsd=3.925e-020
+ nigc=1                    poxedge=1                 pigcd=2.171
+ ntox=1                    xrcrg1=12                 xrcrg2=1
+ cgso=1e-10                 cgdo=1e-10                 cgbo=0
+ cgdl=1e-10                 cgsl=1e-10                 clc=1e-007
+ cle=0.6                   cf=1                    ckappas=0.6
+ ckappad=0.6               acde=0.4                  moin=5.346
+ noff=1.973                voffcv=-0.0904            kt1=-0.26648965
+ pkt1=0                    wkt1=0                    lkt1=5.32515e-10
+ kt1l=0                    kt2=-0.054653483          pkt2=0
+ wkt2=0                    lkt2=-2.124094e-10        ute=-1.3497898
+ lute=4.0776543e-008       ua1=3.2127884e-09         pua1=0
+ wua1=0                    lua1=-1.5955703e-16       ub1=-5.1065691e-018
+ lub1=6.8227184e-025       uc1=-2.2149083e-10        puc1=0
+ wuc1=0                    luc1=1.0245454e-16        prt=0
+ at=118385.18              pat=0                     wat=0
+ lat=-0.044031168          jss=2.85e-07              jsd=2.85e-07
+ jsws=6.9e-13              jswd=6.9e-13              jswgs=6.9e-13
+ jswgd=6.9e-13             njs=1                     njd=1
+ ijthsfwd=0.01             ijthdfwd=0.01             ijthsrev=0.01
+ ijthdrev=0.01             bvs=11.25                 bvd=11.25
+ xjbvs=1                   xjbvd=1                   pbs=0.6882682
+ pbd=0.6882682             cjs=1e-10                   cjd=1e-10
+ mjs=0.359                 mjd=0.359                 pbsws=0.32
+ pbswd=0.32                cjsws=1.185e-10               cjswd=1.185e-10
+ mjsws=0.202               mjswd=0.202               pbswgs=0.952
+ pbswgd=0.952              cjswgs=3.82e-10             cjswgd=3.82e-10
+ mjswgs=0.541              mjswgd=0.541              tpb=1.49e-3
+ tcj=9.05e-4               tpbsw=8.94e-04            tcjsw=8.09e-04
+ tpbswg=0.00133            tcjswg=0.00088            xtis=3
+ xtid=3                    jtsswgs=1.09e-009         jtsswgd=1.09e-009
+ njtsswg=11.6              xtsswgs=0.2886            xtsswgd=0.2886
+ tnjtsswg=1.08             vtsswgs=10                vtsswgd=10
+ dmcg=2.05e-007            dmci=3.15e-007            dmdg=0
+ dmcgt=0                   dwj=0                     xgw=0
+ xgl=-3.1e-008             rshg=8.23                 gbmin=1e-012
+ rbpb=50                   rbpd=50                   rbps=50
+ rbdb=50                   saref=1.00e-05            sbref=1.00e-05
+ rbsb=50                   ngcon=1                   wlod=5e-007
+ kvth0=2.2e-009            lkvth0=-1e-008            wkvth0=2.2e-006
+ pkvth0=-5e-014            llodvth=1                 wlodvth=1
+ stk2=2.5e-009             lodk2=1                   lodeta0=2
+ ku0=-3.2e-008             lku0=2e-007               wku0=7e-007
+ pku0=-5e-014              llodku0=1                 wlodku0=1
+ kvsat=0.4                 steta0=-1.1e-010          tku0=0.03
+ wvth0=0            pvth0=0            pcit=0
+ pvoff=0           leta0=0           peta0=0
+ pu0=0               pvsat=0           pa0=0
+ ppclm=0           ppdiblc2=0     fnoimod=1
+ noia=1.250e+42                noib=7.000e+23                noic=6.080e+7
+ em=3.00e7                 ef=0.904                  minr=1e-3
 
 
     4: type=n 
+ lmin=1.8e-07              lmax=5e-007 wmin=1.003e-005
+ wmax=90.003e-05           version=4.5               rgeomod=1
+ binunit=2                 paramchk=1                mobmod=0
+ capmod=2                  igcmod=0                  igbmod=0
+ diomod=1                  rdsmod=1                  rbodymod=0
+ rgatemod=0                permod=1                  acnqsmod=0
+ trnqsmod=0                tempmod=0                 wpemod=1
+ tnom=25                   toxe=3.981e-09       toxm=3.981e-09
+ dtox=5.958e-010           epsrox=3.9                wint=1.02e-008
+ lint=2.595e-008           ll=0                      wl=0
+ lln=1                     wln=1                     lw=0
+ ww=0                      lwn=1                     wwn=1
+ lwl=0                     wwl=0                     llc=0
+ wlc=0                     lwc=0                     wwc=0
+ lwlc=0                    wwlc=0                    xl=-1.5e-08
+ xw=0        dlc=2.595e-008       dwc=0
+ xpart=1                   toxref=3e-009             dlcig=2.5e-009
+ vth0=0.46146692                    lvth0=-3.4028302e-009
+ k1=0.448                  k2=0.039663073        lk2=4.3090269e-010
+ k3=-3.7                   k3b=1.2                   w0=0
+ dvt0=0.09708              dvt1=0.3053               dvt2=-0.6939
+ dvt0w=0                   dvt1w=0                   dvt2w=0
+ dsub=0.633                minv=-0.34                voffl=-1.22e-009
+ dvtp0=1.46e-006           dvtp1=0                   lpe0=9.921e-009
+ lpeb=2.178e-008           web=0                     wec=0
+ scref=1e-006              kvth0we=0.00349988        lkvth0we=-1.4284997e-010
+ wkvth0we=0                pkvth0we=0                k2we=0.0038
+ lk2we=0                   wk2we=0                   pk2we=0
+ xj=1.6e-007               ngate=9e+019              ndep=5.8e+017
+ nsd=1e+020                phin=0                    cdsc=0
+ cdscb=0                   cdscd=0                   cit=0.00061599596
+ lcit=3.7870453e-012                          voff=-0.14584802
+ tvoff=0.0013232813        ptvoff=0                  wtvoff=0
+ ltvoff=7.6536891e-11      lvoff=2.4721416e-009
+ nfactor=0.78346906        lnfactor=3.4397209e-008   eta0=0.28753
+ etab=-0.308               ud=0                      lud=0
+ wud=0                     pud=0                     ku0we=0
+ lku0we=0                  wku0we=0                  pku0we=0
+ u0=0.030914951       lu0=7.7700251e-010  ua=-7.1464787e-010
+ lua=-5.1817006e-017       ub=1.5421034e-018         lub=1.9489354e-025
+ uc=7.8458172e-011         luc=1.6891692e-017        vsat=61073.15
+ lvsat=0.0007881769                          a0=0.20832912
+ la0=7.8101305e-008  ags=0.31869166            lags=8.1127573e-008
+ a1=0                      a2=0.995                  b0=0
+ b1=0                      keta=-0.09467464          lketa=4.6240528e-009
+ dwg=0                     dwb=0                     pclm=0.64898747
+ lpclm=4.4100556e-009                        pdiblc1=0
+ pdiblc2=0.001415142                       lpdiblc2=4.5110843e-011
+ pdiblcb=0                 drout=0.5                 pvag=0.6279
+ delta=0.005               pscbe1=4.5e+008           pscbe2=1e-020
+ fprout=0                  pdits=0                   pditsd=0
+ pditsl=0                  rsh=7.28                  rdsw=200
+ rsw=90.88                 rdw=90.88                 prwg=0
+ prwb=0                    wr=1                      alpha0=1.454e-007
+ alpha1=2.295              beta0=17.8                agidl=2.593e-009
+ bgidl=1.8508e+009         cgidl=0.25                egidl=0.2624
+ aigbacc=0.01213           bigbacc=0.006537          cigbacc=0.2809
+ nigbacc=4.05              aigbinv=0.35              bigbinv=0.03
+ cigbinv=0.006             eigbinv=1.1               nigbinv=1
+ aigc=0.01                 bigc=0.00144              cigc=1.515e-005
+ aigsd=0.008379            bigsd=0.0002699           cigsd=3.925e-020
+ nigc=1                    poxedge=1                 pigcd=2.171
+ ntox=1                    xrcrg1=12                 xrcrg2=1
+ cgso=1e-10                 cgdo=1e-10                 cgbo=0
+ cgdl=1e-10                 cgsl=1e-10                 clc=1e-007
+ cle=0.6                   cf=1                    ckappas=0.6
+ ckappad=0.6               acde=0.4                  moin=5.346
+ noff=1.973                voffcv=-0.0904            kt1=-0.25288273
+ pkt1=0                    wkt1=0                    lkt1=-5.3606467e-09
+ kt1l=0                    kt2=-0.05510829           pkt2=0
+ wkt2=0                    lkt2=-1.543206e-11        ute=-1.2573881
+ lute=7.5736315e-010       ua1=2.6668279e-09         pua1=0
+ wua1=0                    lua1=7.6898481e-17        ub1=-3.2787121e-018
+ lub1=-1.0937304e-025      uc1=-2.214721e-12         puc1=0
+ wuc1=0                    luc1=7.4860548e-18        prt=0
+ at=15560.798              pat=0                     wat=0
+ lat=0.00050207373         jss=2.85e-07              jsd=2.85e-07
+ jsws=6.9e-13              jswd=6.9e-13              jswgs=6.9e-13
+ jswgd=6.9e-13             njs=1                     njd=1
+ ijthsfwd=0.01             ijthdfwd=0.01             ijthsrev=0.01
+ ijthdrev=0.01             bvs=11.25                 bvd=11.25
+ xjbvs=1                   xjbvd=1                   pbs=0.6882682
+ pbd=0.6882682             cjs=1e-10                   cjd=1e-10
+ mjs=0.359                 mjd=0.359                 pbsws=0.32
+ pbswd=0.32                cjsws=1.185e-10               cjswd=1.185e-10
+ mjsws=0.202               mjswd=0.202               pbswgs=0.952
+ pbswgd=0.952              cjswgs=3.82e-10             cjswgd=3.82e-10
+ mjswgs=0.541              mjswgd=0.541              tpb=1.49e-3
+ tcj=9.05e-4               tpbsw=8.94e-04            tcjsw=8.09e-04
+ tpbswg=0.00133            tcjswg=0.00088            xtis=3
+ xtid=3                    jtsswgs=1.09e-009         jtsswgd=1.09e-009
+ njtsswg=11.6              xtsswgs=0.2886            xtsswgd=0.2886
+ tnjtsswg=1.08             vtsswgs=10                vtsswgd=10
+ dmcg=2.05e-007            dmci=3.15e-007            dmdg=0
+ dmcgt=0                   dwj=0                     xgw=0
+ xgl=-3.1e-008             rshg=8.23                 gbmin=1e-012
+ rbpb=50                   rbpd=50                   rbps=50
+ rbdb=50                   saref=1.00e-05            sbref=1.00e-05
+ rbsb=50                   ngcon=1                   wlod=5e-007
+ kvth0=2.2e-009            lkvth0=-1e-008            wkvth0=2.2e-006
+ pkvth0=-5e-014            llodvth=1                 wlodvth=1
+ stk2=2.5e-009             lodk2=1                   lodeta0=2
+ ku0=-3.2e-008             lku0=2e-007               wku0=7e-007
+ pku0=-5e-014              llodku0=1                 wlodku0=1
+ kvsat=0.4                 steta0=-1.1e-010          tku0=0.03
+ wvth0=0            pvth0=0            pcit=0
+ pvoff=0           leta0=0           peta0=0
+ pu0=0               pvsat=0           pa0=0
+ ppclm=0           ppdiblc2=0     fnoimod=1
+ noia=1.250e+42                noib=7.000e+23                noic=6.080e+7
+ em=3.00e7                 ef=0.904                  minr=1e-3
 
 
     5: type=n 
+ lmin=1e-005 lmax=2e-05                wmin=1.23e-006
+ wmax=1.003e-005                       version=4.5
+ rgeomod=1                 binunit=2                 paramchk=1
+ mobmod=0                  capmod=2                  igcmod=0
+ igbmod=0                  diomod=1                  rdsmod=1
+ rbodymod=0                rgatemod=0                permod=1
+ acnqsmod=0                trnqsmod=0                tempmod=0
+ wpemod=1                  tnom=25                   toxe=3.981e-09
+ toxm=3.981e-09       dtox=5.958e-010           epsrox=3.9
+ wint=1.02e-008            lint=2.595e-008           ll=0
+ wl=0                      lln=1                     wln=1
+ lw=0                      ww=0                      lwn=1
+ wwn=1                     lwl=0                     wwl=0
+ llc=0                     wlc=0                     lwc=0
+ wwc=0                     lwlc=0                    wwlc=0
+ xl=-1.5e-08 xw=0        dlc=2.595e-008
+ dwc=0                     xpart=1                   toxref=3e-009
+ dlcig=2.5e-009            vth0=0.43767024
+ wvth0=1.8615454e-008                         k1=0.448
+ k2=0.044105166        wk2=2.3706154e-009        k3=-3.7
+ k3b=1.2                   w0=0                      dvt0=0.09708
+ dvt1=0.3053               dvt2=-0.6939              dvt0w=0
+ dvt1w=0                   dvt2w=0                   dsub=0.633
+ minv=-0.34                voffl=-1.22e-009          dvtp0=1.46e-006
+ dvtp1=0                   lpe0=9.921e-009           lpeb=2.178e-008
+ web=0                     wec=0                     scref=1e-006
+ kvth0we=0.0034939762      lkvth0we=0                wkvth0we=-1.2638696e-011
+ pkvth0we=0                k2we=0.0038               lk2we=0
+ wk2we=0                   pk2we=0                   xj=1.6e-007
+ ngate=9e+019              ndep=5.8e+017             nsd=1e+020
+ phin=0                    cdsc=0                    cdscb=0
+ cdscd=0                   cit=0.00079963881   wcit=2.8928938e-010
+ voff=-0.12992046   tvoff=1.500000e-03        wvoff=-6.3014618e-009
+ nfactor=0.88693351        wnfactor=6.2846762e-007   eta0=0.21639887
+ weta0=1.1321993e-007      etab=-0.308               ud=0
+ lud=0                     wud=0                     pud=0
+ ku0we=0                   lku0we=0                  wku0we=0
+ pku0we=0                  u0=0.02998869        wu0=5.3782564e-009
+ ua=-1.203133e-009         wua=9.1420727e-016        ub=2.4226144e-018
+ wub=-9.6406862e-025       uc=2.0880233e-010         wuc=-1.7148782e-016
+ vsat=73808.304     wvsat=-0.0047976413       a0=1.0648537
+ wa0=7.5534989e-008        ags=0.50587729            wags=-5.1622455e-008
+ a1=0                      a2=0.995                  b0=0
+ b1=0                      keta=-0.053402592         wketa=2.0295385e-008
+ dwg=0                     dwb=0                     pclm=0.72643962
+ wpclm=-7.5768887e-008     pdiblc1=0                 pdiblc2=0.00097154989
+ wpdiblc2=3.4534212e-011   pdiblcb=0                 drout=0.5
+ pvag=0.6279               delta=0.005               pscbe1=4.5e+008
+ pscbe2=1e-020             fprout=0                  pdits=0
+ pditsd=0                  pditsl=0                  rsh=7.28
+ rdsw=200                  rsw=90.88                 rdw=90.88
+ prwg=0                    prwb=0                    wr=1
+ alpha0=1.454e-007         alpha1=2.295              beta0=17.8
+ agidl=2.593e-009          bgidl=1.8508e+009         cgidl=0.25
+ egidl=0.2624              aigbacc=0.01213           bigbacc=0.006537
+ cigbacc=0.2809            nigbacc=4.05              aigbinv=0.35
+ bigbinv=0.03              cigbinv=0.006             eigbinv=1.1
+ nigbinv=1                 aigc=0.01                 bigc=0.00144
+ cigc=1.515e-005           aigsd=0.008379            bigsd=0.0002699
+ cigsd=3.925e-020          nigc=1                    poxedge=1
+ pigcd=2.171               ntox=1                    xrcrg1=12
+ xrcrg2=1                  cgso=1e-10                 cgdo=1e-10
+ cgbo=0                    cgdl=1e-10                 cgsl=1e-10
+ clc=1e-007                cle=0.6                   cf=1
+ ckappas=0.6               ckappad=0.6               acde=0.4
+ moin=5.346                noff=1.973                voffcv=-0.0904
+ kt1=-0.24969309           pkt1=0                    lkt1=0
+ wkt1=3.580664e-08         kt1l=0                    kt2=-0.055217703
+ pkt2=0                    lkt2=0                    wkt2=2.618748e-10
+ ute=-1.8450159            wute=3.3356664e-007       ua1=2.3109709e-09
+ pua1=0                    lua1=0                    wua1=3.0594354e-16
+ ub1=-4.4511878e-018       wub1=2.1333736e-025       uc1=-8.7610598e-011
+ wuc1=6.9172781e-017       prt=0                     at=117036.91
+ pat=0                     lat=0                     wat=0.008123733
+ jss=2.85e-07              jsd=2.85e-07              jsws=6.9e-13
+ jswd=6.9e-13              jswgs=6.9e-13             jswgd=6.9e-13
+ njs=1                     njd=1                     ijthsfwd=0.01
+ ijthdfwd=0.01             ijthsrev=0.01             ijthdrev=0.01
+ bvs=11.25                 bvd=11.25                 xjbvs=1
+ xjbvd=1                   pbs=0.6882682             pbd=0.6882682
+ cjs=1e-10                   cjd=1e-10                   mjs=0.359
+ mjd=0.359                 pbsws=0.32                pbswd=0.32
+ cjsws=1.185e-10               cjswd=1.185e-10               mjsws=0.202
+ mjswd=0.202               pbswgs=0.952              pbswgd=0.952
+ cjswgs=3.82e-10             cjswgd=3.82e-10             mjswgs=0.541
+ mjswgd=0.541              tpb=1.49e-3               tcj=9.05e-4
+ tpbsw=8.94e-04            tcjsw=8.09e-04            tpbswg=0.00133
+ tcjswg=0.00088            xtis=3                    xtid=3
+ jtsswgs=1.09e-009         jtsswgd=1.09e-009         njtsswg=11.6
+ xtsswgs=0.2886            xtsswgd=0.2886            tnjtsswg=1.08
+ vtsswgs=10                vtsswgd=10                dmcg=2.05e-007
+ dmci=3.15e-007            dmdg=0                    dmcgt=0
+ dwj=0                     xgw=0                     xgl=-3.1e-008
+ rshg=8.23                 gbmin=1e-012              rbpb=50
+ rbpd=50                   rbps=50                   rbdb=50
+ rbsb=50                   ngcon=1                   saref=1.00e-05
+ sbref=1.00e-05            wlod=5e-007               kvth0=2.2e-009
+ lkvth0=-1e-008            wkvth0=2.2e-006           pkvth0=-5e-014
+ llodvth=1                 wlodvth=1                 stk2=2.5e-009
+ lodk2=1                   lodeta0=2                 ku0=-3.2e-008
+ lku0=2e-007               wku0=7e-007               pku0=-5e-014
+ llodku0=1                 wlodku0=1                 kvsat=0.4
+ steta0=-1.1e-010          tku0=0.03                 lvth0=0
+ pvth0=0            lk2=0                lcit=0
+ pcit=0             lvoff=0           pvoff=0
+ leta0=0           peta0=0           lu0=0
+ pu0=0               lvsat=0           pvsat=0
+ la0=0               pa0=0               lpclm=0
+ ppclm=0           lpdiblc2=0     ppdiblc2=0
+ fnoimod=1                 noia=1.250e+42                noib=7.000e+23
+ noic=6.080e+7                em=3.00e7                 ef=0.904
+ minr=1e-3
 
 
     6: type=n 
+ lmin=1.2e-006                        lmax=1e-005
+ wmin=1.23e-006                        wmax=1.003e-005
+ version=4.5               rgeomod=1                 binunit=2
+ paramchk=1                mobmod=0                  capmod=2
+ igcmod=0                  igbmod=0                  diomod=1
+ rdsmod=1                  rbodymod=0                rgatemod=0
+ permod=1                  acnqsmod=0                trnqsmod=0
+ tempmod=0                 wpemod=1                  tnom=25
+ toxe=3.981e-09       toxm=3.981e-09       dtox=5.958e-010
+ epsrox=3.9                wint=1.02e-008            lint=2.595e-008
+ ll=0                      wl=0                      lln=1
+ wln=1                     lw=0                      ww=0
+ lwn=1                     wwn=1                     lwl=0
+ wwl=0                     llc=0                     wlc=0
+ lwc=0                     wwc=0                     lwlc=0
+ wwlc=0                    xl=-1.5e-08 xw=0
+ dlc=2.595e-008       dwc=0                     xpart=1
+ toxref=3e-009             dlcig=2.5e-009            vth0=0.43826899
+ lvth0=-5.9474128e-009                        wvth0=1.7352315e-008
+ pvth0=1.254688e-014                          k1=0.448
+ k2=0.044096635        lk2=8.473674e-011    wk2=3.2383366e-009
+ pk2=-8.6191608e-015       k3=-3.7                   k3b=1.2
+ w0=0                      dvt0=0.09708              dvt1=0.3053
+ dvt2=-0.6939              dvt0w=0                   dvt1w=0
+ dvt2w=0                   dsub=0.633                minv=-0.34
+ voffl=-1.22e-009          dvtp0=1.46e-006           dvtp1=0
+ lpe0=9.921e-009           lpeb=2.178e-008           web=0
+ wec=0                     scref=1e-006              kvth0we=0.0035094668
+ lkvth0we=-1.5387034e-010  wkvth0we=-1.4445197e-011  pkvth0we=1.794415e-017
+ k2we=0.0038               lk2we=0                   wk2we=0
+ pk2we=0                   xj=1.6e-007               ngate=9e+019
+ ndep=5.8e+017             nsd=1e+020                phin=0
+ cdsc=0                    cdscb=0                   cdscd=0
+ cit=0.00091692734   lcit=-1.1650387e-009
+ wcit=2.4691011e-010       pcit=4.2095749e-016
+ voff=-0.13043683   tvoff=1.500000e-03        lvoff=5.1291508e-009
+ wvoff=-4.4838181e-009     pvoff=-1.8054837e-014
+ nfactor=0.88311971        lnfactor=3.7882923e-008   wnfactor=6.4966815e-007
+ pnfactor=-2.1058697e-013  eta0=0.20763762    leta0=8.7026363e-008
+ weta0=1.2381754e-007      peta0=-1.0526709e-013
+ etab=-0.308               ud=0                      lud=0
+ wud=0                     pud=0                     ku0we=0
+ lku0we=0                  wku0we=0                  pku0we=0
+ u0=0.030734961       lu0=-7.4127816e-009 wu0=4.1245074e-009
+ pu0=1.2453614e-014  ua=-1.1100275e-009        lua=-9.2482661e-016
+ wua=7.489948e-016         pua=1.641072e-021         ub=2.3448197e-018
+ lub=7.727422e-025         wub=-8.2606234e-025       pub=-1.3708302e-030
+ uc=2.1675785e-010         luc=-7.9022914e-017       wuc=-1.8631596e-016
+ puc=1.4728946e-022        vsat=73706.519     lvsat=0.001011044
+ wvsat=-0.0048794884       pvsat=8.1299557e-010
+ a0=1.0494623         la0=1.5288501e-007  wa0=1.3847577e-007
+ pa0=-6.2519711e-013 ags=0.48226057            lags=2.3458734e-007
+ wags=-9.3890644e-008      pags=4.1985414e-013       a1=0
+ a2=0.995                  b0=0                      b1=0
+ keta=-0.046062599         lketa=-7.2908884e-008     wketa=1.5462685e-008
+ pketa=4.8003693e-014      dwg=0                     dwb=0
+ pclm=0.73944236    lpclm=-1.2915748e-007
+ wpclm=-9.1496997e-008     ppclm=1.5622889e-013
+ pdiblc1=0                 pdiblc2=0.00082255572
+ lpdiblc2=1.479974e-009                   wpdiblc2=1.2054455e-010
+ ppdiblc2=-8.5434924e-016                 pdiblcb=0
+ drout=0.5                 pvag=0.6279               delta=0.005
+ pscbe1=4.5e+008           pscbe2=1e-020             fprout=0
+ pdits=0                   pditsd=0                  pditsl=0
+ rsh=7.28                  rdsw=200                  rsw=90.88
+ rdw=90.88                 prwg=0                    prwb=0
+ wr=1                      alpha0=1.454e-007         alpha1=2.295
+ beta0=17.8                agidl=2.593e-009          bgidl=1.8508e+009
+ cgidl=0.25                egidl=0.2624              aigbacc=0.01213
+ bigbacc=0.006537          cigbacc=0.2809            nigbacc=4.05
+ aigbinv=0.35              bigbinv=0.03              cigbinv=0.006
+ eigbinv=1.1               nigbinv=1                 aigc=0.01
+ bigc=0.00144              cigc=1.515e-005           aigsd=0.008379
+ bigsd=0.0002699           cigsd=3.925e-020          nigc=1
+ poxedge=1                 pigcd=2.171               ntox=1
+ xrcrg1=12                 xrcrg2=1                  cgso=1e-10
+ cgdo=1e-10                 cgbo=0                    cgdl=1e-10
+ cgsl=1e-10                 clc=1e-007                cle=0.6
+ cf=1                    ckappas=0.6               ckappad=0.6
+ acde=0.4                  moin=5.346                noff=1.973
+ voffcv=-0.0904            kt1=-0.24727546           lkt1=-2.4014492e-08
+ wkt1=3.7260246e-08        pkt1=-1.4438818e-14       kt1l=0
+ kt2=-0.055269916          lkt2=5.1863176e-10        wkt2=3.326311e-10
+ pkt2=-7.02825e-16         ute=-1.9123217            lute=6.6855562e-007
+ wute=3.6556821e-007       pute=-3.1787476e-013      ua1=2.2105942e-09
+ lua1=9.9705133e-16        wua1=3.6924896e-16        pua1=-6.2881915e-22
+ ub1=-4.4301109e-018       lub1=-2.0935864e-025      wub1=9.8470839e-026
+ pub1=1.1409807e-030       uc1=-7.8971928e-11        luc1=-8.580875e-17
+ wuc1=4.7624082e-17        puc1=2.1404538e-22        prt=0
+ at=121701.61              lat=-0.04633491           wat=0.010823733
+ pat=-2.6819365e-08        jss=2.85e-07              jsd=2.85e-07
+ jsws=6.9e-13              jswd=6.9e-13              jswgs=6.9e-13
+ jswgd=6.9e-13             njs=1                     njd=1
+ ijthsfwd=0.01             ijthdfwd=0.01             ijthsrev=0.01
+ ijthdrev=0.01             bvs=11.25                 bvd=11.25
+ xjbvs=1                   xjbvd=1                   pbs=0.6882682
+ pbd=0.6882682             cjs=1e-10                   cjd=1e-10
+ mjs=0.359                 mjd=0.359                 pbsws=0.32
+ pbswd=0.32                cjsws=1.185e-10               cjswd=1.185e-10
+ mjsws=0.202               mjswd=0.202               pbswgs=0.952
+ pbswgd=0.952              cjswgs=3.82e-10             cjswgd=3.82e-10
+ mjswgs=0.541              mjswgd=0.541              tpb=1.49e-3
+ tcj=9.05e-4               tpbsw=8.94e-04            tcjsw=8.09e-04
+ tpbswg=0.00133            tcjswg=0.00088            xtis=3
+ xtid=3                    jtsswgs=1.09e-009         jtsswgd=1.09e-009
+ njtsswg=11.6              xtsswgs=0.2886            xtsswgd=0.2886
+ tnjtsswg=1.08             vtsswgs=10                vtsswgd=10
+ dmcg=2.05e-007            dmci=3.15e-007            dmdg=0
+ dmcgt=0                   dwj=0                     xgw=0
+ xgl=-3.1e-008             rshg=8.23                 gbmin=1e-012
+ rbpb=50                   rbpd=50                   rbps=50
+ rbdb=50                   rbsb=50                   saref=1.00e-05
+ sbref=1.00e-05            ngcon=1                   wlod=5e-007
+ kvth0=2.2e-009            lkvth0=-1e-008            wkvth0=2.2e-006
+ pkvth0=-5e-014            llodvth=1                 wlodvth=1
+ stk2=2.5e-009             lodk2=1                   lodeta0=2
+ ku0=-3.2e-008             lku0=2e-007               wku0=7e-007
+ pku0=-5e-014              llodku0=1                 wlodku0=1
+ kvsat=0.4                 steta0=-1.1e-010          tku0=0.03
+ fnoimod=1                 noia=1.250e+42                noib=7.000e+23
+ noic=6.080e+7                em=3.00e7                 ef=0.904
+ minr=1e-3
 
 
     7: type=n 
+ lmin=5e-007 lmax=1.2e-006
+ wmin=1.23e-006              wmax=1.003e-005
+ version=4.5               rgeomod=1                 binunit=2
+ paramchk=1                mobmod=0                  capmod=2
+ igcmod=0                  igbmod=0                  diomod=1
+ rdsmod=1                  rbodymod=0                rgatemod=0
+ permod=1                  acnqsmod=0                trnqsmod=0
+ tempmod=0                 wpemod=1                  tnom=25
+ toxe=3.981e-09       toxm=3.981e-09       dtox=5.958e-010
+ epsrox=3.9                wint=1.02e-008            lint=2.595e-008
+ ll=0                      wl=0                      lln=1
+ wln=1                     lw=0                      ww=0
+ lwn=1                     wwn=1                     lwl=0
+ wwl=0                     llc=0                     wlc=0
+ lwc=0                     wwc=0                     lwlc=0
+ wwlc=0                    xl=-1.5e-08 xw=0
+ dlc=2.595e-008       dwc=0                     xpart=1
+ toxref=3e-009             dlcig=2.5e-009            vth0=0.42037368
+ lvth0=1.4329762e-008                         wvth0=4.5084673e-008
+ pvth0=-1.8876655e-014                        k1=0.448
+ k2=0.046221224        lk2=-2.3226355e-009  wk2=-5.8299975e-009
+ pk2=1.6561685e-015        k3=-3.7                   k3b=1.2
+ w0=0                      dvt0=0.09708              dvt1=0.3053
+ dvt2=-0.6939              dvt0w=0                   dvt1w=0
+ dvt2w=0                   dsub=0.633                minv=-0.34
+ voffl=-1.22e-009          dvtp0=1.46e-006           dvtp1=0
+ lpe0=9.921e-009           lpeb=2.178e-008           web=0
+ wec=0                     scref=1e-006              kvth0we=0.0035012271
+ lkvth0we=-1.4453387e-010  wkvth0we=-1.3484334e-011  pkvth0we=1.6855396e-017
+ k2we=0.0038               lk2we=0                   wk2we=0
+ pk2we=0                   xj=1.6e-007               ngate=9e+019
+ ndep=5.8e+017             nsd=1e+020                phin=0
+ cdsc=0                    cdscb=0                   cdscd=0
+ cit=-0.00058574619  lcit=5.3764069e-010
+ wcit=1.1923586e-009       pcit=-6.5033018e-016
+ voff=-0.11697501   tvoff=0.0015255135        ptvoff=2.8937131e-16
+ wtvoff=-2.553802e-10      ltvoff=-2.8909378e-11     lvoff=-1.0124436e-008
+ wvoff=-3.4361596e-008     pvoff=1.5799673e-014
+ nfactor=0.97842413        lnfactor=-7.0106516e-008  wnfactor=4.6381786e-007
+ pnfactor=-3.6153196e-028  eta0=0.2857596     leta0=-1.4936512e-009
+ weta0=1.7721043e-008      peta0=1.4950851e-014
+ etab=-0.308               ud=0                      lud=0
+ wud=0                     pud=0                     ku0we=0
+ lku0we=0                  wku0we=0                  pku0we=0
+ u0=0.018994069       lu0=5.8908231e-009  wu0=2.3764981e-008
+ pu0=-9.8010062e-015 ua=-2.5857121e-009        lua=7.4727158e-016
+ wua=3.3956523e-015        pua=-1.3578556e-021       ub=3.6579891e-018
+ lub=-7.1521005e-025       wub=-3.2055939e-024       pub=1.325417e-030
+ uc=1.6778828e-010         luc=-2.3535502e-017       wuc=-1.1603581e-016
+ puc=6.7655012e-023        vsat=82472.125     lvsat=-0.0089212647
+ wvsat=-0.013050925        pvsat=1.0072051e-008
+ a0=1.7153328         la0=-6.016129e-007  wa0=-1.0555125e-006
+ pa0=7.2771096e-013  ags=0.8525523             lags=-1.8499023e-007
+ wags=-5.1280026e-008      pags=3.7157205e-013       a1=0
+ a2=0.995                  b0=0                      b1=0
+ keta=-0.12659406          lketa=1.8341317e-008      wketa=9.2075794e-008
+ pketa=-3.8806621e-014     dwg=0                     dwb=0
+ pclm=0.60499108    lpclm=2.3189257e-008
+ wpclm=7.1135264e-008      ppclm=-2.8049725e-014
+ pdiblc1=0                 pdiblc2=0.0025232125
+ lpdiblc2=-4.4704014e-010                 wpdiblc2=-1.2004774e-009
+ ppdiblc2=6.4250076e-016                  pdiblcb=0
+ drout=0.5                 pvag=0.6279               delta=0.005
+ pscbe1=4.5e+008           pscbe2=1e-020             fprout=0
+ pdits=0                   pditsd=0                  pditsl=0
+ rsh=7.28                  rdsw=200                  rsw=90.88
+ rdw=90.88                 prwg=0                    prwb=0
+ wr=1                      alpha0=1.454e-007         alpha1=2.295
+ beta0=17.8                agidl=2.593e-009          bgidl=1.8508e+009
+ cgidl=0.25                egidl=0.2624              aigbacc=0.01213
+ bigbacc=0.006537          cigbacc=0.2809            nigbacc=4.05
+ aigbinv=0.35              bigbinv=0.03              cigbinv=0.006
+ eigbinv=1.1               nigbinv=1                 aigc=0.01
+ bigc=0.00144              cigc=1.515e-005           aigsd=0.008379
+ bigsd=0.0002699           cigsd=3.925e-020          nigc=1
+ poxedge=1                 pigcd=2.171               ntox=1
+ xrcrg1=12                 xrcrg2=1                  cgso=1e-10
+ cgdo=1e-10                 cgbo=0                    cgdl=1e-10
+ cgsl=1e-10                 clc=1e-007                cle=0.6
+ cf=1                    ckappas=0.6               ckappad=0.6
+ acde=0.4                  moin=5.346                noff=1.973
+ voffcv=-0.0904            kt1=-0.27040689           lkt1=2.1957265e-09
+ wkt1=3.9210005e-08        pkt1=-1.6648091e-14       kt1l=0
+ kt2=-0.054513083          lkt2=-3.3893434e-10       wkt2=-1.4053344e-09
+ pkt2=1.2664632e-15        ute=-1.3645922            lute=4.7923298e-008
+ wute=1.4816586e-007       pute=-7.1536156e-014      ua1=3.2347934e-09
+ lua1=-1.634687e-16        wua1=-2.2026062e-16       pua1=3.915416e-23
+ ub1=-5.2851432e-018       lub1=7.594785e-025        wub1=1.7874554e-024
+ pub1=-7.7280775e-031      uc1=-2.5954626e-10        luc1=1.1880003e-16
+ wuc1=3.8091958e-16        puc1=-1.6361174e-22       prt=0
+ at=120571.33              lat=-0.045054185          wat=-0.021882427
+ pat=1.0239983e-08         jss=2.85e-07              jsd=2.85e-07
+ jsws=6.9e-13              jswd=6.9e-13              jswgs=6.9e-13
+ jswgd=6.9e-13             njs=1                     njd=1
+ ijthsfwd=0.01             ijthdfwd=0.01             ijthsrev=0.01
+ ijthdrev=0.01             bvs=11.25                 bvd=11.25
+ xjbvs=1                   xjbvd=1                   pbs=0.6882682
+ pbd=0.6882682             cjs=1e-10                   cjd=1e-10
+ mjs=0.359                 mjd=0.359                 pbsws=0.32
+ pbswd=0.32                cjsws=1.185e-10               cjswd=1.185e-10
+ mjsws=0.202               mjswd=0.202               pbswgs=0.952
+ pbswgd=0.952              cjswgs=3.82e-10             cjswgd=3.82e-10
+ mjswgs=0.541              mjswgd=0.541              tpb=1.49e-3
+ tcj=9.05e-4               tpbsw=8.94e-04            tcjsw=8.09e-04
+ tpbswg=0.00133            tcjswg=0.00088            xtis=3
+ xtid=3                    jtsswgs=1.09e-009         jtsswgd=1.09e-009
+ njtsswg=11.6              xtsswgs=0.2886            xtsswgd=0.2886
+ tnjtsswg=1.08             vtsswgs=10                vtsswgd=10
+ dmcg=2.05e-007            dmci=3.15e-007            dmdg=0
+ dmcgt=0                   dwj=0                     xgw=0
+ xgl=-3.1e-008             rshg=8.23                 gbmin=1e-012
+ rbpb=50                   rbpd=50                   rbps=50
+ rbdb=50                   rbsb=50                   saref=1.00e-05
+ sbref=1.00e-05            ngcon=1                   wlod=5e-007
+ kvth0=2.2e-009            lkvth0=-1e-008            wkvth0=2.2e-006
+ pkvth0=-5e-014            llodvth=1                 wlodvth=1
+ stk2=2.5e-009             lodk2=1                   lodeta0=2
+ ku0=-3.2e-008             lku0=2e-007               wku0=7e-007
+ pku0=-5e-014              llodku0=1                 wlodku0=1
+ kvsat=0.4                 steta0=-1.1e-010          tku0=0.03
+ fnoimod=1                 noia=1.250e+42                noib=7.000e+23
+ noic=6.080e+7                em=3.00e7                 ef=0.904
+ minr=1e-3
 
 
     8: type=n 
+ lmin=1.8e-07              lmax=5e-007 wmin=1.23e-006
+ wmax=1.003e-005                      version=4.5
+ rgeomod=1                 binunit=2                 paramchk=1
+ mobmod=0                  capmod=2                  igcmod=0
+ igbmod=0                  diomod=1                  rdsmod=1
+ rbodymod=0                rgatemod=0                permod=1
+ acnqsmod=0                trnqsmod=0                tempmod=0
+ wpemod=1                  tnom=25                   toxe=3.981e-09
+ toxm=3.981e-09       dtox=5.958e-010           epsrox=3.9
+ wint=1.02e-008            lint=2.595e-008           ll=0
+ wl=0                      lln=1                     wln=1
+ lw=0                      ww=0                      lwn=1
+ wwn=1                     lwl=0                     wwl=0
+ llc=0                     wlc=0                     lwc=0
+ wwc=0                     lwlc=0                    wwlc=0
+ xl=-1.5e-08 xw=0        dlc=2.595e-008
+ dwc=0                     xpart=1                   toxref=3e-009
+ dlcig=2.5e-009            vth0=0.46153716
+ lvth0=-3.4981445e-009                        wvth0=-7.0316591e-010
+ pvth0=9.5405814e-016                         k1=0.448
+ k2=0.04005708         lk2=3.4705556e-010   wk2=-3.9438461e-009
+ pk2=8.3927631e-016        k3=-3.7                   k3b=1.2
+ w0=0                      dvt0=0.09708              dvt1=0.3053
+ dvt2=-0.6939              dvt0w=0                   dvt1w=0
+ dvt2w=0                   dsub=0.633                minv=-0.34
+ voffl=-1.22e-009          dvtp0=1.46e-006           dvtp1=0
+ lpe0=9.921e-009           lpeb=2.178e-008           web=0
+ wec=0                     scref=1e-006              kvth0we=0.0035012271
+ lkvth0we=-1.4453389e-010  wkvth0we=-1.3484357e-011  pkvth0we=1.6855406e-017
+ k2we=0.0038               lk2we=0                   wk2we=0
+ pk2we=0                   xj=1.6e-007               ngate=9e+019
+ ndep=5.8e+017             nsd=1e+020                phin=0
+ cdsc=0                    cdscb=0                   cdscd=0
+ cit=0.00063596926   lcit=8.5157293e-012
+ wcit=-1.9992482e-010      pcit=-4.7332235e-017
+ voff=-0.14662081   tvoff=0.0012674705        ptvoff=-6.318266e-17
+ wtvoff=5.5864419e-10      ltvoff=8.2849096e-11      lvoff=2.7151615e-009
+ wvoff=7.7353926e-009      pvoff=-2.4325323e-015
+ nfactor=0.72621499        lnfactor=3.9125262e-008   wnfactor=5.7309035e-007
+ pnfactor=-4.7325917e-014  eta0=0.28035301    leta0=8.4793969e-010
+ weta0=7.1838771e-008      peta0=-8.4875371e-015
+ etab=-0.308               ud=0                      lud=0
+ wud=0                     pud=0                     ku0we=0
+ lku0we=0                  wku0we=0                  pku0we=0
+ u0=0.030600569       lu0=8.6404784e-010  wu0=3.1468385e-009
+ pu0=-8.7128886e-016 ua=-7.360552e-010         lua=-5.3814819e-017
+ wua=2.1427874e-016        pua=1.9997311e-023        ub=1.5214649e-018
+ lub=2.1011858e-025        wub=2.0658252e-025        pub=-1.5239657e-031
+ uc=7.1563125e-011         luc=1.8139615e-017        wuc=6.9016661e-017
+ puc=-1.2491212e-023       vsat=59837.656     lvsat=0.00088172379
+ wvsat=0.012366802         pvsat=-9.36367e-010
+ a0=0.12876526        la0=8.5529509e-008  wa0=7.9640237e-007
+ pa0=-7.4353352e-014 ags=0.19374941            lags=1.003373e-007
+ wags=1.2506219e-006       pags=-1.9228168e-013      a1=0
+ a2=0.995                  b0=0                      b1=0
+ keta=-0.094572384         lketa=4.4727282e-009      wketa=-1.0235369e-009
+ pketa=1.5146989e-015      dwg=0                     dwb=0
+ pclm=0.64375475    lpclm=6.400715e-009
+ wpclm=5.2377423e-008      ppclm=-1.9925704e-014
+ pdiblc1=0                 pdiblc2=0.0013400495
+ lpdiblc2=6.5387753e-011                  wpdiblc2=7.5164568e-010
+ ppdiblc2=-2.0296376e-016                 pdiblcb=0
+ drout=0.5                 pvag=0.6279               delta=0.005
+ pscbe1=4.5e+008           pscbe2=1e-020             fprout=0
+ pdits=0                   pditsd=0                  pditsl=0
+ rsh=7.28                  rdsw=200                  rsw=90.88
+ rdw=90.88                 prwg=0                    prwb=0
+ wr=1                      alpha0=1.454e-007         alpha1=2.295
+ beta0=17.8                agidl=2.593e-009          bgidl=1.8508e+009
+ cgidl=0.25                egidl=0.2624              aigbacc=0.01213
+ bigbacc=0.006537          cigbacc=0.2809            nigbacc=4.05
+ aigbinv=0.35              bigbinv=0.03              cigbinv=0.006
+ eigbinv=1.1               nigbinv=1                 aigc=0.01
+ bigc=0.00144              cigc=1.515e-005           aigsd=0.008379
+ bigsd=0.0002699           cigsd=3.925e-020          nigc=1
+ poxedge=1                 pigcd=2.171               ntox=1
+ xrcrg1=12                 xrcrg2=1                  cgso=1e-10
+ cgdo=1e-10                 cgbo=0                    cgdl=1e-10
+ cgsl=1e-10                 clc=1e-007                cle=0.6
+ cf=1                    ckappas=0.6               ckappad=0.6
+ acde=0.4                  moin=5.346                noff=1.973
+ voffcv=-0.0904            kt1=-0.25205998           lkt1=-5.7503208e-09
+ wkt1=-8.235319e-09        pkt1=3.900481e-15         kt1l=0
+ kt2=-0.055305172          lkt2=4.11855e-12          wkt2=1.9706945e-09
+ pkt2=-1.956946e-16        ute=-1.2578727            lute=1.7030936e-009
+ wute=4.8507534e-009       pute=-9.4663839e-015      ua1=2.64976e-09
+ lua1=8.9909248e-17        wua1=1.7084239e-16        pua1=-1.3023256e-22
+ ub1=-3.2377504e-018       lub1=-1.2724735e-025      wub1=-4.1001048e-025
+ pub1=1.7891473e-031       uc1=-5.2478553e-12        luc1=8.6633837e-18
+ wuc1=3.0360468e-17        puc1=-1.1784594e-23       prt=0
+ at=15225.518              lat=0.00057108617         wat=0.0033560168
+ pat=-6.907862e-10         jss=2.85e-07              jsd=2.85e-07
+ jsws=6.9e-13              jswd=6.9e-13              jswgs=6.9e-13
+ jswgd=6.9e-13             njs=1                     njd=1
+ ijthsfwd=0.01             ijthdfwd=0.01             ijthsrev=0.01
+ ijthdrev=0.01             bvs=11.25                 bvd=11.25
+ xjbvs=1                   xjbvd=1                   pbs=0.6882682
+ pbd=0.6882682             cjs=1e-10                   cjd=1e-10
+ mjs=0.359                 mjd=0.359                 pbsws=0.32
+ pbswd=0.32                cjsws=1.185e-10               cjswd=1.185e-10
+ mjsws=0.202               mjswd=0.202               pbswgs=0.952
+ pbswgd=0.952              cjswgs=3.82e-10             cjswgd=3.82e-10
+ mjswgs=0.541              mjswgd=0.541              tpb=1.49e-3
+ tcj=9.05e-4               tpbsw=8.94e-04            tcjsw=8.09e-04
+ tpbswg=0.00133            tcjswg=0.00088            xtis=3
+ xtid=3                    jtsswgs=1.09e-009         jtsswgd=1.09e-009
+ njtsswg=11.6              xtsswgs=0.2886            xtsswgd=0.2886
+ tnjtsswg=1.08             vtsswgs=10                vtsswgd=10
+ dmcg=2.05e-007            dmci=3.15e-007            dmdg=0
+ dmcgt=0                   dwj=0                     xgw=0
+ xgl=-3.1e-008             rshg=8.23                 gbmin=1e-012
+ rbpb=50                   rbpd=50                   rbps=50
+ rbdb=50                   rbsb=50                   saref=1.00e-05
+ sbref=1.00e-05            ngcon=1                   wlod=5e-007
+ kvth0=2.2e-009            lkvth0=-1e-008            wkvth0=2.2e-006
+ pkvth0=-5e-014            llodvth=1                 wlodvth=1
+ stk2=2.5e-009             lodk2=1                   lodeta0=2
+ ku0=-3.2e-008             lku0=2e-007               wku0=7e-007
+ pku0=-5e-014              llodku0=1                 wlodku0=1
+ kvsat=0.4                 steta0=-1.1e-010          tku0=0.03
+ fnoimod=1                 noia=1.250e+42                noib=7.000e+23
+ noic=6.080e+7                em=3.00e7                 ef=0.904
+ minr=1e-3
 
 
     9: type=n 
+ lmin=1e-005 lmax=2e-05                wmin=5.3e-007
+ wmax=1.23e-006                        version=4.5
+ rgeomod=1                 binunit=2                 paramchk=1
+ mobmod=0                  capmod=2                  igcmod=0
+ igbmod=0                  diomod=1                  rdsmod=1
+ rbodymod=0                rgatemod=0                permod=1
+ acnqsmod=0                trnqsmod=0                tempmod=0
+ wpemod=1                  tnom=25                   toxe=3.981e-09
+ toxm=3.981e-09       dtox=5.958e-010           epsrox=3.9
+ wint=1.02e-008            lint=2.595e-008           ll=0
+ wl=0                      lln=1                     wln=1
+ lw=0                      ww=0                      lwn=1
+ wwn=1                     lwl=0                     wwl=0
+ llc=0                     wlc=0                     lwc=0
+ wwc=0                     lwlc=0                    wwlc=0
+ xl=-1.5e-08 xw=0        dlc=2.595e-008
+ dwc=0                     xpart=1                   toxref=3e-009
+ dlcig=2.5e-009            vth0=0.45091968
+ wvth0=2.5889311e-009                         k1=0.448
+ k2=0.049658408        wk2=-4.3465863e-009       k3=-3.7
+ k3b=1.2                   w0=0                      dvt0=0.09708
+ dvt1=0.3053               dvt2=-0.6939              dvt0w=0
+ dvt1w=0                   dvt2w=0                   dsub=0.633
+ minv=-0.34                voffl=-1.22e-009          dvtp0=1.46e-006
+ dvtp1=0                   lpe0=9.921e-009           lpeb=2.178e-008
+ web=0                     wec=0                     scref=1e-006
+ kvth0we=0.003492826       lkvth0we=0                wkvth0we=-1.1247497e-011
+ pkvth0we=0                k2we=0.0038               lk2we=0
+ wk2we=0                   pk2we=0                   xj=1.6e-007
+ ngate=9e+019              ndep=5.8e+017             nsd=1e+020
+ phin=0                    cdsc=0                    cdscb=0
+ cdscd=0                   cit=0.0011644892    wcit=-1.5203366e-010
+ voff=-0.12502536   tvoff=1.500000e-03        wvoff=-1.2222573e-008
+ nfactor=1.3196496         wnfactor=1.0505424e-007   eta0=0.38866768
+ weta0=-9.5156426e-008     etab=-0.308               ud=0
+ lud=0                     wud=0                     pud=0
+ ku0we=0                   lku0we=0                  wku0we=0
+ pku0we=0                  u0=0.037683336       wu0=-3.9291872e-009
+ ua=-2.803732e-010         wua=-2.0196304e-016       ub=1.6975264e-018
+ wub=-8.7002173e-026       uc=5.6835816e-011         wuc=1.2330885e-017
+ vsat=56060.96      wvsat=0.016669546         a0=1.2341704
+ wa0=-1.2927044e-007       ags=0.49009232            wags=-3.252895e-008
+ a1=0                      a2=0.995                  b0=0
+ b1=0                      keta=-0.02910376          wketa=-9.0964823e-009
+ dwg=0                     dwb=0                     pclm=0.6638
+ pdiblc1=0                 pdiblc2=0.001072536
+ wpdiblc2=-8.7618586e-011  pdiblcb=0                 drout=0.5
+ pvag=0.6279               delta=0.005               pscbe1=4.5e+008
+ pscbe2=1e-020             fprout=0                  pdits=0
+ pditsd=0                  pditsl=0                  rsh=7.28
+ rdsw=200                  rsw=90.88                 rdw=90.88
+ prwg=0                    prwb=0                    wr=1
+ alpha0=1.454e-007         alpha1=2.295              beta0=17.8
+ agidl=2.593e-009          bgidl=1.8508e+009         cgidl=0.25
+ egidl=0.2624              aigbacc=0.01213           bigbacc=0.006537
+ cigbacc=0.2809            nigbacc=4.05              aigbinv=0.35
+ bigbinv=0.03              cigbinv=0.006             eigbinv=1.1
+ nigbinv=1                 aigc=0.01                 bigc=0.00144
+ cigc=1.515e-005           aigsd=0.008379            bigsd=0.0002699
+ cigsd=3.925e-020          nigc=1                    poxedge=1
+ pigcd=2.171               ntox=1                    xrcrg1=12
+ xrcrg2=1                  cgso=1e-10                 cgdo=1e-10
+ cgbo=0                    cgdl=1e-10                 cgsl=1e-10
+ clc=1e-007                cle=0.6                   cf=1
+ ckappas=0.6               ckappad=0.6               acde=0.4
+ moin=5.346                noff=1.973                voffcv=-0.0904
+ kt1=-0.21715589           pkt1=0                    lkt1=0
+ wkt1=-3.550358e-09        kt1l=0                    kt2=-0.054972169
+ pkt2=0                    lkt2=0                    wkt2=-3.51231e-11
+ ute=-1.6297245            wute=7.3150159e-008       ua1=2.7228749e-09
+ pua1=0                    lua1=0                    wua1=-1.9229558e-16
+ ub1=-4.6663733e-018       wub1=4.7362574e-025       uc1=-1.5828853e-011
+ wuc1=-1.7654419e-017      prt=0                     at=105690.22
+ pat=0                     lat=0                     wat=0.021848693
+ jss=2.85e-07              jsd=2.85e-07              jsws=6.9e-13
+ jswd=6.9e-13              jswgs=6.9e-13             jswgd=6.9e-13
+ njs=1                     njd=1                     ijthsfwd=0.01
+ ijthdfwd=0.01             ijthsrev=0.01             ijthdrev=0.01
+ bvs=11.25                 bvd=11.25                 xjbvs=1
+ xjbvd=1                   pbs=0.6882682             pbd=0.6882682
+ cjs=1e-10                   cjd=1e-10                   mjs=0.359
+ mjd=0.359                 pbsws=0.32                pbswd=0.32
+ cjsws=1.185e-10               cjswd=1.185e-10               mjsws=0.202
+ mjswd=0.202               pbswgs=0.952              pbswgd=0.952
+ cjswgs=3.82e-10             cjswgd=3.82e-10             mjswgs=0.541
+ mjswgd=0.541              tpb=1.49e-3               tcj=9.05e-4
+ tpbsw=8.94e-04            tcjsw=8.09e-04            tpbswg=0.00133
+ tcjswg=0.00088            xtis=3                    xtid=3
+ jtsswgs=1.09e-009         jtsswgd=1.09e-009         njtsswg=11.6
+ xtsswgs=0.2886            xtsswgd=0.2886            tnjtsswg=1.08
+ vtsswgs=10                vtsswgd=10                dmcg=2.05e-007
+ dmci=3.15e-007            dmdg=0                    dmcgt=0
+ dwj=0                     xgw=0                     xgl=-3.1e-008
+ rshg=8.23                 gbmin=1e-012              rbpb=50
+ rbpd=50                   rbps=50                   rbdb=50
+ rbsb=50                   ngcon=1                   saref=1.00e-05
+ sbref=1.00e-05            wlod=5e-007               kvth0=2.2e-009
+ lkvth0=-1e-008            wkvth0=2.2e-006           pkvth0=-5e-014
+ llodvth=1                 wlodvth=1                 stk2=2.5e-009
+ lodk2=1                   lodeta0=2                 ku0=-3.2e-008
+ lku0=2e-007               wku0=7e-007               pku0=-5e-014
+ llodku0=1                 wlodku0=1                 kvsat=0.4
+ steta0=-1.1e-010          tku0=0.03                 lvth0=0
+ pvth0=0            lk2=0                lcit=0
+ pcit=0             lvoff=0           pvoff=0
+ leta0=0           peta0=0           lu0=0
+ pu0=0               lvsat=0           pvsat=0
+ la0=0               pa0=0               lpclm=0
+ ppclm=0           lpdiblc2=0     ppdiblc2=0
+ fnoimod=1                 noia=1.250e+42                noib=7.000e+23
+ noic=6.080e+7                em=3.00e7                 ef=0.904
+ minr=1e-3
 
 
     10: type=n 
+ lmin=1.2e-006                        lmax=1e-005
+ wmin=5.3e-007                         wmax=1.23e-006
+ version=4.5               rgeomod=1                 binunit=2
+ paramchk=1                mobmod=0                  capmod=2
+ igcmod=0                  igbmod=0                  diomod=1
+ rdsmod=1                  rbodymod=0                rgatemod=0
+ permod=1                  acnqsmod=0                trnqsmod=0
+ tempmod=0                 wpemod=1                  tnom=25
+ toxe=3.981e-09       toxm=3.981e-09       dtox=5.958e-010
+ epsrox=3.9                wint=1.02e-008            lint=2.595e-008
+ ll=0                      wl=0                      lln=1
+ wln=1                     lw=0                      ww=0
+ lwn=1                     wwn=1                     lwl=0
+ wwl=0                     llc=0                     wlc=0
+ lwc=0                     wwc=0                     lwlc=0
+ wwlc=0                    xl=-1.5e-08 xw=0
+ dlc=2.595e-008       dwc=0                     xpart=1
+ toxref=3e-009             dlcig=2.5e-009            vth0=0.45009359
+ lvth0=8.2056515e-009                         wvth0=3.0492775e-009
+ pvth0=-4.5726669e-015                        k1=0.448
+ k2=0.0506837          lk2=-1.0184325e-008  wk2=-4.7293768e-009
+ pk2=3.8022964e-015        k3=-3.7                   k3b=1.2
+ w0=0                      dvt0=0.09708              dvt1=0.3053
+ dvt2=-0.6939              dvt0w=0                   dvt1w=0
+ dvt2w=0                   dsub=0.633                minv=-0.34
+ voffl=-1.22e-009          dvtp0=1.46e-006           dvtp1=0
+ lpe0=9.921e-009           lpeb=2.178e-008           web=0
+ wec=0                     scref=1e-006              kvth0we=0.0035081523
+ lkvth0we=-1.5223742e-010  wkvth0we=-1.2855149e-011  pkvth0we=1.5968969e-017
+ k2we=0.0038               lk2we=0                   wk2we=0
+ pk2we=0                   xj=1.6e-007               ngate=9e+019
+ ndep=5.8e+017             nsd=1e+020                phin=0
+ cdsc=0                    cdscb=0                   cdscd=0
+ cit=0.0012816735    lcit=-1.1640036e-009
+ wcit=-1.9428688e-010      pcit=4.197055e-016 voff=-0.12390125
+ tvoff=0.0014765654        ptvoff=-2.8156816e-16     wtvoff=2.8346454e-11
+ ltvoff=2.3277791e-10      lvoff=-1.116587e-008
+ wvoff=-1.238925e-008      pvoff=1.6556208e-015
+ nfactor=1.3034321         lnfactor=1.610905e-007    wnfactor=1.4125833e-007
+ pnfactor=-3.5961885e-013  eta0=0.38567368    leta0=2.9739706e-008
+ weta0=-9.1534883e-008     peta0=-3.5973148e-014
+ etab=-0.308               ud=0                      lud=0
+ wud=0                     pud=0                     ku0we=0
+ lku0we=0                  wku0we=0                  pku0we=0
+ u0=0.037135421       lu0=5.4424908e-009  wu0=-3.6174896e-009
+ pu0=-3.0961235e-015 ua=-3.4387548e-010        lua=6.3077452e-016
+ wua=-1.777427e-016        pua=-2.405831e-022        ub=1.7416045e-018
+ lub=-4.3783223e-025       wub=-9.6413196e-026       pub=9.3480629e-032
+ uc=5.2319544e-011         luc=4.486058e-017         wuc=1.2588611e-017
+ puc=-2.5600177e-024       vsat=54415.882     lvsat=0.016340723
+ wvsat=0.018454465         pvsat=-1.7729784e-008
+ a0=1.2658264         la0=-3.1444254e-007 wa0=-1.2323831e-007
+ pa0=-5.9917704e-014 ags=0.42466814            lags=6.4986497e-007
+ wags=-2.4226841e-008      pags=-8.2465682e-014      a1=0
+ a2=0.995                  b0=0                      b1=0
+ keta=-0.02494072          lketa=-4.1351896e-008     wketa=-1.008634e-008
+ pketa=9.8323601e-015      dwg=0                     dwb=0
+ pclm=0.6638        pdiblc1=0                 pdiblc2=0.0010118305
+ lpdiblc2=6.0299404e-010                  wpdiblc2=-1.0840221e-010
+ ppdiblc2=2.0644577e-016                  pdiblcb=0
+ drout=0.5                 pvag=0.6279               delta=0.005
+ pscbe1=4.5e+008           pscbe2=1e-020             fprout=0
+ pdits=0                   pditsd=0                  pditsl=0
+ rsh=7.28                  rdsw=200                  rsw=90.88
+ rdw=90.88                 prwg=0                    prwb=0
+ wr=1                      alpha0=1.454e-007         alpha1=2.295
+ beta0=17.8                agidl=2.593e-009          bgidl=1.8508e+009
+ cgidl=0.25                egidl=0.2624              aigbacc=0.01213
+ bigbacc=0.006537          cigbacc=0.2809            nigbacc=4.05
+ aigbinv=0.35              bigbinv=0.03              cigbinv=0.006
+ eigbinv=1.1               nigbinv=1                 aigc=0.01
+ bigc=0.00144              cigc=1.515e-005           aigsd=0.008379
+ bigsd=0.0002699           cigsd=3.925e-020          nigc=1
+ poxedge=1                 pigcd=2.171               ntox=1
+ xrcrg1=12                 xrcrg2=1                  cgso=1e-10
+ cgdo=1e-10                 cgbo=0                    cgdl=1e-10
+ cgsl=1e-10                 clc=1e-007                cle=0.6
+ cf=1                    ckappas=0.6               ckappad=0.6
+ acde=0.4                  moin=5.346                noff=1.973
+ voffcv=-0.0904            kt1=-0.21363667           lkt1=-3.4956736e-08
+ wkt1=-3.4292396e-09       pkt1=-1.203085e-15        kt1l=0
+ kt2=-0.054925589          lkt2=-4.626789e-10        wkt2=-8.386603e-11
+ pkt2=4.841688e-16         ute=-1.676861             lute=4.6821162e-007
+ wute=8.0754901e-008       pute=-7.5538655e-014      ua1=2.6804932e-09
+ lua1=4.2098151e-16        wua1=-1.9914087e-16       pua1=6.799488e-23
+ ub1=-4.7956442e-018       lub1=1.2840609e-024       wub1=5.4061989e-025
+ pub1=-6.6545954e-031      uc1=-2.6953883e-011       luc1=1.1050604e-016
+ wuc1=-1.5296949e-017      puc1=-2.3416982e-023      prt=0
+ at=110244.4               lat=-0.045237162          wat=0.02468237
+ pat=-2.8147196e-08        jss=2.85e-07              jsd=2.85e-07
+ jsws=6.9e-13              jswd=6.9e-13              jswgs=6.9e-13
+ jswgd=6.9e-13             njs=1                     njd=1
+ ijthsfwd=0.01             ijthdfwd=0.01             ijthsrev=0.01
+ ijthdrev=0.01             bvs=11.25                 bvd=11.25
+ xjbvs=1                   xjbvd=1                   pbs=0.6882682
+ pbd=0.6882682             cjs=1e-10                   cjd=1e-10
+ mjs=0.359                 mjd=0.359                 pbsws=0.32
+ pbswd=0.32                cjsws=1.185e-10               cjswd=1.185e-10
+ mjsws=0.202               mjswd=0.202               pbswgs=0.952
+ pbswgd=0.952              cjswgs=3.82e-10             cjswgd=3.82e-10
+ mjswgs=0.541              mjswgd=0.541              tpb=1.49e-3
+ tcj=9.05e-4               tpbsw=8.94e-04            tcjsw=8.09e-04
+ tpbswg=0.00133            tcjswg=0.00088            xtis=3
+ xtid=3                    jtsswgs=1.09e-009         jtsswgd=1.09e-009
+ njtsswg=11.6              xtsswgs=0.2886            xtsswgd=0.2886
+ tnjtsswg=1.08             vtsswgs=10                vtsswgd=10
+ dmcg=2.05e-007            dmci=3.15e-007            dmdg=0
+ dmcgt=0                   dwj=0                     xgw=0
+ xgl=-3.1e-008             rshg=8.23                 gbmin=1e-012
+ rbpb=50                   rbpd=50                   rbps=50
+ rbdb=50                   rbsb=50                   saref=1.00e-05
+ sbref=1.00e-05            ngcon=1                   wlod=5e-007
+ kvth0=2.2e-009            lkvth0=-1e-008            wkvth0=2.2e-006
+ pkvth0=-5e-014            llodvth=1                 wlodvth=1
+ stk2=2.5e-009             lodk2=1                   lodeta0=2
+ ku0=-3.2e-008             lku0=2e-007               wku0=7e-007
+ pku0=-5e-014              llodku0=1                 wlodku0=1
+ kvsat=0.4                 steta0=-1.1e-010          tku0=0.03
+ lpclm=0           ppclm=0           fnoimod=1
+ noia=1.250e+42                noib=7.000e+23                noic=6.080e+7
+ em=3.00e7                 ef=0.904                  minr=1e-3
 
 
     11: type=n 
+ lmin=5e-007 lmax=1.2e-006
+ wmin=5.3e-007                         wmax=1.23e-006
+ version=4.5               rgeomod=1                 binunit=2
+ paramchk=1                mobmod=0                  capmod=2
+ igcmod=0                  igbmod=0                  diomod=1
+ rdsmod=1                  rbodymod=0                rgatemod=0
+ permod=1                  acnqsmod=0                trnqsmod=0
+ tempmod=0                 wpemod=1                  tnom=25
+ toxe=3.981e-09       toxm=3.981e-09       dtox=5.958e-010
+ epsrox=3.9                wint=1.02e-008            lint=2.595e-008
+ ll=0                      wl=0                      lln=1
+ wln=1                     lw=0                      ww=0
+ lwn=1                     wwn=1                     lwl=0
+ wwl=0                     llc=0                     wlc=0
+ lwc=0                     wwc=0                     lwlc=0
+ wwlc=0                    xl=-1.5e-08 xw=0
+ dlc=2.595e-008       dwc=0                     xpart=1
+ toxref=3e-009             dlcig=2.5e-009            vth0=0.46386651
+ lvth0=-7.4004438e-009                        wvth0=-7.5242539e-009
+ pvth0=7.4082015e-015                         k1=0.448
+ k2=0.041798436        lk2=-1.164329e-010   wk2=-4.8019262e-010
+ pk2=-1.0124542e-015       k3=-3.7                   k3b=1.2
+ w0=0                      dvt0=0.09708              dvt1=0.3053
+ dvt2=-0.6939              dvt0w=0                   dvt1w=0
+ dvt2w=0                   dsub=0.633                minv=-0.34
+ voffl=-1.22e-009          dvtp0=1.46e-006           dvtp1=0
+ lpe0=9.921e-009           lpeb=2.178e-008           web=0
+ wec=0                     scref=1e-006              kvth0we=0.0034999999
+ lkvth0we=-1.4299998e-010  wkvth0we=-1.2000002e-011  pkvth0we=1.5000003e-017
+ k2we=0.0038               lk2we=0                   wk2we=0
+ pk2we=0                   xj=1.6e-007               ngate=9e+019
+ ndep=5.8e+017             nsd=1e+020                phin=0
+ cdsc=0                    cdscb=0                   cdscd=0
+ cit=0.0002093576    lcit=5.1037543e-011
+ wcit=2.3060105e-010       pcit=-6.1735013e-017
+ voff=-0.14158636   tvoff=0.0015639493        ptvoff=9.260252e-17
+ wtvoff=-3.0187213e-10     ltvoff=1.3376323e-10      lvoff=8.8731293e-009
+ wvoff=-4.5917007e-009     pvoff=-7.179782e-015
+ nfactor=1.5074714         lnfactor=-7.0106516e-008  wnfactor=-1.7611776e-007
+ pnfactor=-8.4625901e-029  eta0=0.444895      leta0=-3.7363969e-008
+ weta0=-1.7476914e-007     peta0=5.8339587e-014
+ etab=-0.308               ud=0                      lud=0
+ wud=0                     pud=0                     ku0we=0
+ lku0we=0                  wku0we=0                  pku0we=0
+ u0=0.047238653       lu0=-6.0054812e-009 wu0=-1.0399669e-008
+ pu0=4.5887635e-015  ua=7.1915788e-010         lua=-5.7374858e-016
+ wua=-6.0191843e-016       pua=2.4005042e-022        ub=1.1708869e-018
+ lub=2.0884787e-025        wub=-1.9719508e-025       pub=2.0767658e-031
+ uc=6.3459404e-011         luc=3.2238005e-017        wuc=1.0160408e-017
+ puc=1.9137854e-025        vsat=72259.383     lvsat=-0.0038777484
+ wvsat=-0.00069759276      pvsat=3.9714134e-009
+ a0=1.1074481         la0=-1.3498409e-007 wa0=-3.2021516e-007
+ pa0=1.6327676e-013  ags=1.0257791             lags=-3.1253821e-008
+ wags=-2.6081511e-007      pags=1.8561249e-013       a1=0
+ a2=0.995                  b0=0                      b1=0
+ keta=-0.044894245         lketa=-1.8742556e-008     wketa=-6.7483042e-009
+ pketa=6.0500312e-015      dwg=0                     dwb=0
+ pclm=0.74766895    lpclm=-9.5031906e-008
+ wpclm=-1.0144788e-007     ppclm=1.1495059e-013
+ pdiblc1=0                 pdiblc2=0.0014356508
+ lpdiblc2=1.2276324e-010                  wpdiblc2=1.1503719e-010
+ ppdiblc2=-4.6733404e-017                 pdiblcb=0
+ drout=0.5                 pvag=0.6279               delta=0.005
+ pscbe1=4.5e+008           pscbe2=1e-020             fprout=0
+ pdits=0                   pditsd=0                  pditsl=0
+ rsh=7.28                  rdsw=200                  rsw=90.88
+ rdw=90.88                 prwg=0                    prwb=0
+ wr=1                      alpha0=1.454e-007         alpha1=2.295
+ beta0=17.8                agidl=2.593e-009          bgidl=1.8508e+009
+ cgidl=0.25                egidl=0.2624              aigbacc=0.01213
+ bigbacc=0.006537          cigbacc=0.2809            nigbacc=4.05
+ aigbinv=0.35              bigbinv=0.03              cigbinv=0.006
+ eigbinv=1.1               nigbinv=1                 aigc=0.01
+ bigc=0.00144              cigc=1.515e-005           aigsd=0.008379
+ bigsd=0.0002699           cigsd=3.925e-020          nigc=1
+ poxedge=1                 pigcd=2.171               ntox=1
+ xrcrg1=12                 xrcrg2=1                  cgso=1e-10
+ cgdo=1e-10                 cgbo=0                    cgdl=1e-10
+ cgsl=1e-10                 clc=1e-007                cle=0.6
+ cf=1                    ckappas=0.6               ckappad=0.6
+ acde=0.4                  moin=5.346                noff=1.973
+ voffcv=-0.0904            kt1=-0.22414387           lkt1=-2.3051023e-08
+ wkt1=-1.6749742e-08       pkt1=1.3890378e-14        kt1l=0
+ kt2=-0.056575902          lkt2=1.4072901e-09        wkt2=1.0898507e-09
+ pkt2=-8.457698e-16        ute=-1.2217685            lute=-4.7453698e-008
+ wute=-2.4593713e-008      pute=4.3831859e-014       ua1=3.1519588e-09
+ lua1=-1.1323604e-16       wua1=-1.2006387e-16       pua1=-2.160726e-23
+ ub1=-3.4530876e-018       lub1=-2.3718997e-025      wub1=-4.2859905e-025
+ pub1=4.3276244e-031       uc1=1.2806939e-10         luc1=-6.5150827e-17
+ wuc1=-8.7940302e-17       puc1=5.8895201e-23        prt=0
+ at=96837.304              lat=-0.030045576          wat=0.006826252
+ pat=-7.914429e-09         jss=2.85e-07              jsd=2.85e-07
+ jsws=6.9e-13              jswd=6.9e-13              jswgs=6.9e-13
+ jswgd=6.9e-13             njs=1                     njd=1
+ ijthsfwd=0.01             ijthdfwd=0.01             ijthsrev=0.01
+ ijthdrev=0.01             bvs=11.25                 bvd=11.25
+ xjbvs=1                   xjbvd=1                   pbs=0.6882682
+ pbd=0.6882682             cjs=1e-10                   cjd=1e-10
+ mjs=0.359                 mjd=0.359                 pbsws=0.32
+ pbswd=0.32                cjsws=1.185e-10               cjswd=1.185e-10
+ mjsws=0.202               mjswd=0.202               pbswgs=0.952
+ pbswgd=0.952              cjswgs=3.82e-10             cjswgd=3.82e-10
+ mjswgs=0.541              mjswgd=0.541              tpb=1.49e-3
+ tcj=9.05e-4               tpbsw=8.94e-04            tcjsw=8.09e-04
+ tpbswg=0.00133            tcjswg=0.00088            xtis=3
+ xtid=3                    jtsswgs=1.09e-009         jtsswgd=1.09e-009
+ njtsswg=11.6              xtsswgs=0.2886            xtsswgd=0.2886
+ tnjtsswg=1.08             vtsswgs=10                vtsswgd=10
+ dmcg=2.05e-007            dmci=3.15e-007            dmdg=0
+ dmcgt=0                   dwj=0                     xgw=0
+ xgl=-3.1e-008             rshg=8.23                 gbmin=1e-012
+ rbpb=50                   rbpd=50                   rbps=50
+ rbdb=50                   rbsb=50                   saref=1.00e-05
+ sbref=1.00e-05            ngcon=1                   wlod=5e-007
+ kvth0=2.2e-009            lkvth0=-1e-008            wkvth0=2.2e-006
+ pkvth0=-5e-014            llodvth=1                 wlodvth=1
+ stk2=2.5e-009             lodk2=1                   lodeta0=2
+ ku0=-3.2e-008             lku0=2e-007               wku0=7e-007
+ pku0=-5e-014              llodku0=1                 wlodku0=1
+ kvsat=0.4                 steta0=-1.1e-010          tku0=0.03
+ fnoimod=1                 noia=1.250e+42                noib=7.000e+23
+ noic=6.080e+7                em=3.00e7                 ef=0.904
+ minr=1e-3
 
     12: type=n 
+ lmin=1.8e-07              lmax=5e-007 wmin=5.3e-007
+ wmax=1.23e-006                        version=4.5
+ rgeomod=1                 binunit=2                 paramchk=1
+ mobmod=0                  capmod=2                  igcmod=0
+ igbmod=0                  diomod=1                  rdsmod=1
+ rbodymod=0                rgatemod=0                permod=1
+ acnqsmod=0                trnqsmod=0                tempmod=0
+ wpemod=1                  tnom=25                   toxe=3.981e-09
+ toxm=3.981e-09       dtox=5.958e-010           epsrox=3.9
+ wint=1.02e-008            lint=2.595e-008           ll=0
+ wl=0                      lln=1                     wln=1
+ lw=0                      ww=0                      lwn=1
+ wwn=1                     lwl=0                     wwl=0
+ llc=0                     wlc=0                     lwc=0
+ wwc=0                     lwlc=0                    wwlc=0
+ xl=-1.5e-08 xw=0        dlc=2.595e-008
+ dwc=0                     xpart=1                   toxref=3e-009
+ dlcig=2.5e-009            vth0=0.45100766
+ lvth0=-1.8312768e-009                        wvth0=1.2033323e-008
+ pvth0=-1.0621851e-015                        k1=0.448
+ k2=0.038163914        lk2=1.4576788e-009   wk2=-1.6538724e-009
+ pk2=-5.0413351e-016       k3=-3.7                   k3b=1.2
+ w0=0                      dvt0=0.09708              dvt1=0.3053
+ dvt2=-0.6939              dvt0w=0                   dvt1w=0
+ dvt2w=0                   dsub=0.633                minv=-0.34
+ voffl=-1.22e-009          dvtp0=1.46e-006           dvtp1=0
+ lpe0=9.921e-009           lpeb=2.178e-008           web=0
+ wec=0                     scref=1e-006              kvth0we=0.0035
+ lkvth0we=-1.4299999e-010  wkvth0we=-1.1999982e-011  pkvth0we=1.4999994e-017
+ k2we=0.0038               lk2we=0                   wk2we=0
+ pk2we=0                   xj=1.6e-007               ngate=9e+019
+ ndep=5.8e+017             nsd=1e+020                phin=0
+ cdsc=0                    cdscb=0                   cdscd=0
+ cit=0.000449348     lcit=-5.2902299e-011
+ wcit=2.5812259e-011       pcit=2.6959011e-017
+ voff=-0.12170577   tvoff=0.001750652         ptvoff=-2.6959012e-17
+ wtvoff=-2.5812261e-11     ltvoff=5.2902302e-11      lvoff=2.6284605e-010
+ wvoff=-2.2401838e-008     pvoff=5.3378843e-016
+ nfactor=1.3456            wnfactor=-1.7611776e-007  eta0=0.34772908
+ leta0=4.7185912e-009                        weta0=-9.6593161e-009
+ peta0=-1.3169477e-014                       etab=-0.308
+ ud=0                      lud=0                     wud=0
+ pud=0                     ku0we=0                   lku0we=0
+ wku0we=0                  pku0we=0                  u0=0.03277883
+ lu0=2.5706843e-010  wu0=5.1201478e-010        pu0=-1.3708657e-016
+ ua=-4.8910711e-010        lua=-5.0449016e-017       wua=-8.4429657e-017
+ pua=1.5926036e-023        ub=1.3163084e-018         lub=1.4586584e-025
+ wub=4.5473991e-025        pub=-7.4676462e-032       uc=1.0368654e-010
+ luc=1.4815632e-017        wuc=3.0160177e-017        puc=-8.4705214e-024
+ vsat=61090.882     lvsat=0.00095932931
+ wvsat=0.010850899         pvsat=-1.0302386e-009
+ a0=0.75505102        la0=1.7639096e-008  wa0=3.8847114e-008
+ pa0=7.7668912e-015  ags=1.0232614             lags=-3.0163421e-008
+ wags=2.4724421e-007       pags=-3.4428006e-014      a1=0
+ a2=0.995                  b0=0                      b1=0
+ keta=-0.10179985          lketa=5.9032598e-009      wketa=7.7188011e-009
+ pketa=-2.1567209e-016     dwg=0                     dwb=0
+ pclm=0.56941084    lpclm=-1.782832e-008
+ wpclm=1.4230381e-007      ppclm=9.381736e-015
+ pdiblc1=0                 pdiblc2=0.0020754301
+ lpdiblc2=-1.5432519e-010                 wpdiblc2=-1.3787073e-010
+ ppdiblc2=6.2801017e-017                  pdiblcb=0
+ drout=0.5                 pvag=0.6279               delta=0.005
+ pscbe1=4.5e+008           pscbe2=1e-020             fprout=0
+ pdits=0                   pditsd=0                  pditsl=0
+ rsh=7.28                  rdsw=200                  rsw=90.88
+ rdw=90.88                 prwg=0                    prwb=0
+ wr=1                      alpha0=1.454e-007         alpha1=2.295
+ beta0=17.8                agidl=2.593e-009          bgidl=1.8508e+009
+ cgidl=0.25                egidl=0.2624              aigbacc=0.01213
+ bigbacc=0.006537          cigbacc=0.2809            nigbacc=4.05
+ aigbinv=0.35              bigbinv=0.03              cigbinv=0.006
+ eigbinv=1.1               nigbinv=1                 aigc=0.01
+ bigc=0.00144              cigc=1.515e-005           aigsd=0.008379
+ bigsd=0.0002699           cigsd=3.925e-020          nigc=1
+ poxedge=1                 pigcd=2.171               ntox=1
+ xrcrg1=12                 xrcrg2=1                  cgso=1e-10
+ cgdo=1e-10                 cgbo=0                    cgdl=1e-10
+ cgsl=1e-10                 clc=1e-007                cle=0.6
+ cf=1                    ckappas=0.6               ckappad=0.6
+ acde=0.4                  moin=5.346                noff=1.973
+ voffcv=-0.0904            kt1=-0.27320796           lkt1=-1.801372e-09
+ wkt1=1.734526e-08         pkt1=-8.761678e-16        kt1l=0
+ kt2=-0.052743813          lkt2=-2.523881e-10        wkt2=-1.1275252e-09
+ pkt2=1.145758e-16         ute=-1.3166839            lute=-6.3458267e-009
+ wute=7.5988759e-008       pute=2.6959011e-016       ua1=2.8231784e-09
+ lua1=2.9158718e-17        wua1=-3.8924501e-17       pua1=-5.6748718e-23
+ ub1=-3.9051406e-018       lub1=-4.1405846e-026      wub1=3.972647e-025
+ pub1=7.5080847e-032       uc1=-6.866448e-12         luc1=-6.710118e-18
+ wuc1=3.2318315e-17        puc1=6.8111944e-24        prt=0
+ at=30037.028              lat=-0.0011143775         wat=-0.014559985
+ pat=1.3479507e-09         jss=2.85e-07              jsd=2.85e-07
+ jsws=6.9e-13              jswd=6.9e-13              jswgs=6.9e-13
+ jswgd=6.9e-13             njs=1                     njd=1
+ ijthsfwd=0.01             ijthdfwd=0.01             ijthsrev=0.01
+ ijthdrev=0.01             bvs=11.25                 bvd=11.25
+ xjbvs=1                   xjbvd=1                   pbs=0.6882682
+ pbd=0.6882682             cjs=1e-10                   cjd=1e-10
+ mjs=0.359                 mjd=0.359                 pbsws=0.32
+ pbswd=0.32                cjsws=1.185e-10               cjswd=1.185e-10
+ mjsws=0.202               mjswd=0.202               pbswgs=0.952
+ pbswgd=0.952              cjswgs=3.82e-10             cjswgd=3.82e-10
+ mjswgs=0.541              mjswgd=0.541              tpb=1.49e-3
+ tcj=9.05e-4               tpbsw=8.94e-04            tcjsw=8.09e-04
+ tpbswg=0.00133            tcjswg=0.00088            xtis=3
+ xtid=3                    jtsswgs=1.09e-009         jtsswgd=1.09e-009
+ njtsswg=11.6              xtsswgs=0.2886            xtsswgd=0.2886
+ tnjtsswg=1.08             vtsswgs=10                vtsswgd=10
+ dmcg=2.05e-007            dmci=3.15e-007            dmdg=0
+ dmcgt=0                   dwj=0                     xgw=0
+ xgl=-3.1e-008             rshg=8.23                 gbmin=1e-012
+ rbpb=50                   rbpd=50                   rbps=50
+ rbdb=50                   rbsb=50                   saref=1.00e-05
+ sbref=1.00e-05            ngcon=1                   wlod=5e-007
+ kvth0=2.2e-009            lkvth0=-1e-008            wkvth0=2.2e-006
+ pkvth0=-5e-014            llodvth=1                 wlodvth=1
+ stk2=2.5e-009             lodk2=1                   lodeta0=2
+ ku0=-3.2e-008             lku0=2e-007               wku0=7e-007
+ pku0=-5e-014              llodku0=1                 wlodku0=1
+ kvsat=0.4                 steta0=-1.1e-010          tku0=0.03
+ fnoimod=1                 noia=1.250e+42                noib=7.000e+23
+ noic=6.080e+7                em=3.00e7                 ef=0.904
+ minr=1e-3
 
 
     13: type=n 
+ lmin=1e-005 lmax=2e-05                wmin=2.2e-07
+ wmax=5.3e-007                        version=4.5
+ rgeomod=1                 binunit=2                 paramchk=1
+ mobmod=0                  capmod=2                  igcmod=0
+ igbmod=0                  diomod=1                  rdsmod=1
+ rbodymod=0                rgatemod=0                permod=1
+ acnqsmod=0                trnqsmod=0                tempmod=0
+ wpemod=1                  tnom=25                   toxe=3.981e-09
+ toxm=3.981e-09       dtox=5.958e-010           epsrox=3.9
+ wint=1.02e-008            lint=2.595e-008           ll=0
+ wl=0                      lln=1                     wln=1
+ lw=0                      ww=0                      lwn=1
+ wwn=1                     lwl=0                     wwl=0
+ llc=0                     wlc=0                     lwc=0
+ wwc=0                     lwlc=0                    wwlc=0
+ xl=-1.5e-08 xw=0        dlc=2.595e-008
+ dwc=0                     xpart=1                   toxref=3e-009
+ dlcig=2.5e-009            vth0=0.45303175
+ wvth0=1.5126177e-009                         k1=0.448
+ k2=0.049498679        wk2=-4.2651883e-009       k3=-3.7
+ k3b=1.2                   w0=0                      dvt0=0.09708
+ dvt1=0.3053               dvt2=-0.6939              dvt0w=0
+ dvt1w=0                   dvt2w=0                   dsub=0.633
+ minv=-0.34                voffl=-1.22e-009          dvtp0=1.46e-006
+ dvtp1=0                   lpe0=9.921e-009           lpeb=2.178e-008
+ web=0                     wec=0                     scref=1e-006
+ kvth0we=0.003492826       lkvth0we=0                wkvth0we=-1.1247478e-011
+ pkvth0we=0                k2we=0.0038               lk2we=0
+ wk2we=0                   pk2we=0                   xj=1.6e-007
+ ngate=9e+019              ndep=5.8e+017             nsd=1e+020
+ phin=0                    cdsc=0                    cdscb=0
+ cdscd=0                   cit=0.00089942525   wcit=-1.6957068e-011
+ voff=-0.14737457   tvoff=0.0016931613        ptvoff=0
+ wtvoff=-9.8434994e-11     ltvoff=0                  wvoff=-8.3341628e-010
+ nfactor=1.658695          wnfactor=-6.7723276e-008  eta0=0.17743427
+ weta0=1.248812e-008       etab=-0.308               ud=0
+ lud=0                     wud=0                     pud=0
+ ku0we=0                   lku0we=0                  wku0we=0
+ pku0we=0                  u0=0.025695765       wu0=2.1796789e-009
+ ua=-7.1525143e-010        wua=1.9650906e-017        ub=9.9908335e-019
+ wub=2.689244e-025         uc=6.9611373e-011         wuc=5.8204612e-018
+ vsat=101331.99     wvsat=-0.0064005714       a0=0.96639923
+ wa0=7.1857545e-009        ags=0.29637191            wags=6.6190971e-008
+ a1=0                      a2=0.995                  b0=0
+ b1=0                      keta=-0.061694138         wketa=7.5115744e-009
+ dwg=0                     dwb=0                     pclm=0.69121603
+ wpclm=-1.3971207e-008     pdiblc1=0                 pdiblc2=0.00058465252
+ wpdiblc2=1.6100684e-010   pdiblcb=0                 drout=0.5
+ pvag=0.6279               delta=0.005               pscbe1=4.5e+008
+ pscbe2=1e-020             fprout=0                  pdits=0
+ pditsd=0                  pditsl=0                  rsh=7.28
+ rdsw=200                  rsw=90.88                 rdw=90.88
+ prwg=0                    prwb=0                    wr=1
+ alpha0=1.454e-007         alpha1=2.295              beta0=17.8
+ agidl=2.593e-009          bgidl=1.8508e+009         cgidl=0.25
+ egidl=0.2624              aigbacc=0.01213           bigbacc=0.006537
+ cigbacc=0.2809            nigbacc=4.05              aigbinv=0.35
+ bigbinv=0.03              cigbinv=0.006             eigbinv=1.1
+ nigbinv=1                 aigc=0.01                 bigc=0.00144
+ cigc=1.515e-005           aigsd=0.008379            bigsd=0.0002699
+ cigsd=3.925e-020          nigc=1                    poxedge=1
+ pigcd=2.171               ntox=1                    xrcrg1=12
+ xrcrg2=1                  cgso=1e-10                 cgdo=1e-10
+ cgbo=0                    cgdl=1e-10                 cgsl=1e-10
+ clc=1e-007                cle=0.6                   cf=1
+ ckappas=0.6               ckappad=0.6               acde=0.4
+ moin=5.346                noff=1.973                voffcv=-0.0904
+ kt1=-0.23457219           pkt1=0                    lkt1=0
+ wkt1=5.3249854e-09        kt1l=0                    kt2=-0.055036104
+ pkt2=0                    lkt2=0                    wkt2=-2.5423e-12
+ ute=-1.4386321            wute=-2.4230528e-008      ua1=2.8643697e-09
+ pua1=0                    lua1=0                    wua1=-2.6440135e-16
+ ub1=-4.2139758e-018       wub1=2.4308397e-025       uc1=-3.0422229e-011
+ wuc1=-1.0217634e-017      prt=0                     at=164968.73
+ pat=0                     lat=0                     wat=-0.008359635
+ jss=2.85e-07              jsd=2.85e-07              jsws=6.9e-13
+ jswd=6.9e-13              jswgs=6.9e-13             jswgd=6.9e-13
+ njs=1                     njd=1                     ijthsfwd=0.01
+ ijthdfwd=0.01             ijthsrev=0.01             ijthdrev=0.01
+ bvs=11.25                 bvd=11.25                 xjbvs=1
+ xjbvd=1                   pbs=0.6882682             pbd=0.6882682
+ cjs=1e-10                   cjd=1e-10                   mjs=0.359
+ mjd=0.359                 pbsws=0.32                pbswd=0.32
+ cjsws=1.185e-10               cjswd=1.185e-10               mjsws=0.202
+ mjswd=0.202               pbswgs=0.952              pbswgd=0.952
+ cjswgs=3.82e-10             cjswgd=3.82e-10             mjswgs=0.541
+ mjswgd=0.541              tpb=1.49e-3               tcj=9.05e-4
+ tpbsw=8.94e-04            tcjsw=8.09e-04            tpbswg=0.00133
+ tcjswg=0.00088            xtis=3                    xtid=3
+ jtsswgs=1.09e-009         jtsswgd=1.09e-009         njtsswg=11.6
+ xtsswgs=0.2886            xtsswgd=0.2886            tnjtsswg=1.08
+ vtsswgs=10                vtsswgd=10                dmcg=2.05e-007
+ dmci=3.15e-007            dmdg=0                    dmcgt=0
+ dwj=0                     xgw=0                     xgl=-3.1e-008
+ rshg=8.23                 gbmin=1e-012              rbpb=50
+ rbpd=50                   rbps=50                   rbdb=50
+ rbsb=50                   ngcon=1                   saref=1.00e-05
+ sbref=1.00e-05            wlod=5e-007               kvth0=2.2e-009
+ lkvth0=-1e-008            wkvth0=2.2e-006           pkvth0=-5e-014
+ llodvth=1                 wlodvth=1                 stk2=2.5e-009
+ lodk2=1                   lodeta0=2                 ku0=-3.2e-008
+ lku0=2e-007               wku0=7e-007               pku0=-5e-014
+ llodku0=1                 wlodku0=1                 kvsat=0.4
+ steta0=-1.1e-010          tku0=0.03                 lvth0=0
+ pvth0=0            lk2=0                lcit=0
+ pcit=0             lvoff=0           pvoff=0
+ leta0=0           peta0=0           lu0=0
+ pu0=0               lvsat=0           pvsat=0
+ la0=0               pa0=0               lpclm=0
+ ppclm=0           lpdiblc2=0     ppdiblc2=0
+ fnoimod=1                 noia=1.250e+42                noib=7.000e+23
+ noic=6.080e+7                em=3.00e7                 ef=0.904
+ minr=1e-3
 
 
     14: type=n 
+ lmin=1.2e-006                         lmax=1e-005
+ wmin=2.2e-07              wmax=5.3e-007
+ version=4.5               rgeomod=1                 binunit=2
+ paramchk=1                mobmod=0                  capmod=2
+ igcmod=0                  igbmod=0                  diomod=1
+ rdsmod=1                  rbodymod=0                rgatemod=0
+ permod=1                  acnqsmod=0                trnqsmod=0
+ tempmod=0                 wpemod=1                  tnom=25
+ toxe=3.981e-09       toxm=3.981e-09       dtox=5.958e-010
+ epsrox=3.9                wint=1.02e-008            lint=2.595e-008
+ ll=0                      wl=0                      lln=1
+ wln=1                     lw=0                      ww=0
+ lwn=1                     wwn=1                     lwl=0
+ wwl=0                     llc=0                     wlc=0
+ lwc=0                     wwc=0                     lwlc=0
+ wwlc=0                    xl=-1.5e-08 xw=0
+ dlc=2.595e-008       dwc=0                     xpart=1
+ toxref=3e-009             dlcig=2.5e-009            vth0=0.45234877
+ lvth0=6.7841929e-009                         wvth0=1.9000387e-009
+ pvth0=-3.8482916e-015                        k1=0.448
+ k2=0.049708891        lk2=-2.0880632e-009  wk2=-4.2326145e-009
+ pk2=-3.2355865e-016       k3=-3.7                   k3b=1.2
+ w0=0                      dvt0=0.09708              dvt1=0.3053
+ dvt2=-0.6939              dvt0w=0                   dvt1w=0
+ dvt2w=0                   dsub=0.633                minv=-0.34
+ voffl=-1.22e-009          dvtp0=1.46e-006           dvtp1=0
+ lpe0=9.921e-009           lpeb=2.178e-008           web=0
+ wec=0                     scref=1e-006              kvth0we=0.0035081523
+ lkvth0we=-1.5223736e-010  wkvth0we=-1.2855127e-011  pkvth0we=1.5968941e-017
+ k2we=0.0038               lk2we=0                   wk2we=0
+ pk2we=0                   xj=1.6e-007               ngate=9e+019
+ ndep=5.8e+017             nsd=1e+020                phin=0
+ cdsc=0                    cdscb=0                   cdscd=0
+ cit=0.00093598992   lcit=-3.6320049e-010
+ wcit=-1.8126514e-011      pcit=1.1616217e-017
+ voff=-0.14627576   tvoff=0.0017294969        ptvoff=2.098306e-17
+ wtvoff=-1.0054744e-10     ltvoff=-3.6092541e-10     lvoff=-1.0914586e-008
+ wvoff=-9.8720172e-010     pvoff=1.5275661e-015
+ nfactor=1.7223427         lnfactor=-6.3221952e-007  wnfactor=-7.2218542e-008
+ pnfactor=4.4651933e-014   eta0=0.18419492    leta0=-6.7154174e-008
+ weta0=1.1138695e-008      peta0=1.3403973e-014
+ etab=-0.308               ud=0                      lud=0
+ wud=0                     pud=0                     ku0we=0
+ lku0we=0                  wku0we=0                  pku0we=0
+ u0=0.025734547       lu0=-3.8522805e-010 wu0=2.1923957e-009
+ pu0=-1.2631797e-016 ua=-7.4834311e-010        lua=3.2870292e-016
+ wua=2.8374005e-017        pua=-8.6647412e-023       ub=1.0002368e-018
+ lub=-1.145736e-026        wub=2.8138778e-025        pub=-1.238e-031
+ uc=6.3534915e-011         luc=6.0358059e-017        wuc=6.8732577e-018
+ puc=-1.0457533e-023       vsat=104447.26     lvsat=-0.030944327
+ wvsat=-0.0070415271       pvsat=6.3666774e-009
+ a0=1.0509621         la0=-8.3997116e-007 wa0=-1.374343e-008
+ pa0=2.0789168e-013  ags=0.23996998            lags=5.6024604e-007
+ wags=6.9895341e-008       pags=-3.6795879e-014      a1=0
+ a2=0.995                  b0=0                      b1=0
+ keta=-0.061786008         lketa=9.1255707e-010      wketa=8.6900186e-009
+ pketa=-1.1705605e-014     dwg=0                     dwb=0
+ pclm=0.69474615    lpclm=-3.5065083e-008
+ wpclm=-1.5770158e-008     ppclm=1.7869166e-014
+ pdiblc1=0                 pdiblc2=0.0004881786
+ lpdiblc2=9.5828501e-010                  wpdiblc2=1.5845079e-010
+ ppdiblc2=2.5389492e-017                  pdiblcb=0
+ drout=0.5                 pvag=0.6279               delta=0.005
+ pscbe1=4.5e+008           pscbe2=1e-020             fprout=0
+ pdits=0                   pditsd=0                  pditsl=0
+ rsh=7.28                  rdsw=200                  rsw=90.88
+ rdw=90.88                 prwg=0                    prwb=0
+ wr=1                      alpha0=1.454e-007         alpha1=2.295
+ beta0=17.8                agidl=2.593e-009          bgidl=1.8508e+009
+ cgidl=0.25                egidl=0.2624              aigbacc=0.01213
+ bigbacc=0.006537          cigbacc=0.2809            nigbacc=4.05
+ aigbinv=0.35              bigbinv=0.03              cigbinv=0.006
+ eigbinv=1.1               nigbinv=1                 aigc=0.01
+ bigc=0.00144              cigc=1.515e-005           aigsd=0.008379
+ bigsd=0.0002699           cigsd=3.925e-020          nigc=1
+ poxedge=1                 pigcd=2.171               ntox=1
+ xrcrg1=12                 xrcrg2=1                  cgso=1e-10
+ cgdo=1e-10                 cgbo=0                    cgdl=1e-10
+ cgsl=1e-10                 clc=1e-007                cle=0.6
+ cf=1                    ckappas=0.6               ckappad=0.6
+ acde=0.4                  moin=5.346                noff=1.973
+ voffcv=-0.0904            kt1=-0.23046948           lkt1=-4.0752482e-08
+ wkt1=5.1487626e-09        pkt1=1.750431e-15         kt1l=0
+ kt2=-0.055121839          lkt2=8.516152e-10         wkt2=1.614237e-11
+ pkt2=-1.855959e-16        ute=-1.4614899            lute=2.270494e-007
+ wute=-2.8998185e-008      pute=4.7357614e-014       ua1=2.8633408e-09
+ lua1=1.022118e-17         wua1=-2.9231996e-16       pua1=2.7731835e-22
+ ub1=-4.2552952e-018       lub1=4.1043047e-025       wub1=2.6525806e-025
+ pub1=-2.2025749e-031      uc1=-3.4311091e-011       luc1=3.8628462e-017
+ wuc1=-1.1547715e-017      puc1=1.321183e-023        prt=0
+ at=177197.4               lat=-0.12146865           wat=-0.0094368784
+ pat=1.0700365e-08         jss=2.85e-07              jsd=2.85e-07
+ jsws=6.9e-13              jswd=6.9e-13              jswgs=6.9e-13
+ jswgd=6.9e-13             njs=1                     njd=1
+ ijthsfwd=0.01             ijthdfwd=0.01             ijthsrev=0.01
+ ijthdrev=0.01             bvs=11.25                 bvd=11.25
+ xjbvs=1                   xjbvd=1                   pbs=0.6882682
+ pbd=0.6882682             cjs=1e-10                   cjd=1e-10
+ mjs=0.359                 mjd=0.359                 pbsws=0.32
+ pbswd=0.32                cjsws=1.185e-10               cjswd=1.185e-10
+ mjsws=0.202               mjswd=0.202               pbswgs=0.952
+ pbswgd=0.952              cjswgs=3.82e-10             cjswgd=3.82e-10
+ mjswgs=0.541              mjswgd=0.541              tpb=1.49e-3
+ tcj=9.05e-4               tpbsw=8.94e-04            tcjsw=8.09e-04
+ tpbswg=0.00133            tcjswg=0.00088            xtis=3
+ xtid=3                    jtsswgs=1.09e-009         jtsswgd=1.09e-009
+ njtsswg=11.6              xtsswgs=0.2886            xtsswgd=0.2886
+ tnjtsswg=1.08             vtsswgs=10                vtsswgd=10
+ dmcg=2.05e-007            dmci=3.15e-007            dmdg=0
+ dmcgt=0                   dwj=0                     xgw=0
+ xgl=-3.1e-008             rshg=8.23                 gbmin=1e-012
+ rbpb=50                   rbpd=50                   rbps=50
+ rbdb=50                   rbsb=50                   saref=1.00e-05
+ sbref=1.00e-05            ngcon=1                   wlod=5e-007
+ kvth0=2.2e-009            lkvth0=-1e-008            wkvth0=2.2e-006
+ pkvth0=-5e-014            llodvth=1                 wlodvth=1
+ stk2=2.5e-009             lodk2=1                   lodeta0=2
+ ku0=-3.2e-008             lku0=2e-007               wku0=7e-007
+ pku0=-5e-014              llodku0=1                 wlodku0=1
+ kvsat=0.4                 steta0=-1.1e-010          tku0=0.03
+ fnoimod=1                 noia=1.250e+42                noib=7.000e+23
+ noic=6.080e+7                em=3.00e7                 ef=0.904
+ minr=1e-3
 
 
     15: type=n 
+ lmin=5e-007 lmax=1.2e-006
+ wmin=2.2e-07              wmax=5.3e-007
+ version=4.5               rgeomod=1                 binunit=2
+ paramchk=1                mobmod=0                  capmod=2
+ igcmod=0                  igbmod=0                  diomod=1
+ rdsmod=1                  rbodymod=0                rgatemod=0
+ permod=1                  acnqsmod=0                trnqsmod=0
+ tempmod=0                 wpemod=1                  tnom=25
+ toxe=3.981e-09       toxm=3.981e-09       dtox=5.958e-010
+ epsrox=3.9                wint=1.02e-008            lint=2.595e-008
+ ll=0                      wl=0                      lln=1
+ wln=1                     lw=0                      ww=0
+ lwn=1                     wwn=1                     lwl=0
+ wwl=0                     llc=0                     wlc=0
+ lwc=0                     wwc=0                     lwlc=0
+ wwlc=0                    xl=-1.5e-08 xw=0
+ dlc=2.595e-008       dwc=0                     xpart=1
+ toxref=3e-009             dlcig=2.5e-009            vth0=0.44828089
+ lvth0=1.1393503e-008                         wvth0=4.181767e-010
+ pvth0=-2.1691937e-015                        k1=0.448
+ k2=0.048140709        lk2=-3.1115533e-010  wk2=-3.7122147e-009
+ pk2=-9.1322366e-016       k3=-3.7                   k3b=1.2
+ w0=0                      dvt0=0.09708              dvt1=0.3053
+ dvt2=-0.6939              dvt0w=0                   dvt1w=0
+ dvt2w=0                   dsub=0.633                minv=-0.34
+ voffl=-1.22e-009          dvtp0=1.46e-006           dvtp1=0
+ lpe0=9.921e-009           lpeb=2.178e-008           web=0
+ wec=0                     scref=1e-006              kvth0we=0.0035
+ lkvth0we=-1.4299999e-010  wkvth0we=-1.2000011e-011  pkvth0we=1.5000009e-017
+ k2we=0.0038               lk2we=0                   wk2we=0
+ pk2we=0                   xj=1.6e-007               ngate=9e+019
+ ndep=5.8e+017             nsd=1e+020                phin=0
+ cdsc=0                    cdscb=0                   cdscd=0
+ cit=0.00048769918   lcit=1.4475774e-010
+ wcit=8.8758178e-011       pcit=-1.0949483e-016
+ voff=-0.14850048   tvoff=0.00095327882       ptvoff=-1.0351402e-16
+ wtvoff=9.32555e-12        ltvoff=5.1860729e-10      lvoff=-8.3937491e-009
+ wvoff=-1.0682653e-009     pvoff=1.6194193e-015
+ nfactor=1.305933          lnfactor=-1.6038562e-007  wnfactor=-7.3413756e-008
+ pnfactor=4.6006229e-014   eta0=0.0092251498  leta0=1.3110407e-007
+ weta0=4.7248216e-008      peta0=-2.7511725e-014
+ etab=-0.308               ud=0                      lud=0
+ wud=0                     pud=0                     ku0we=0
+ lku0we=0                  wku0we=0                  pku0we=0
+ u0=0.020914402       lu0=5.0764788e-009  wu0=3.0151699e-009
+ pu0=-1.0586033e-015 ua=-4.7450936e-010        lua=1.8421903e-017
+ wua=6.3743975e-018        pua=-6.1719657e-023       ub=3.3755544e-019
+ lub=7.394269e-025         wub=2.2747064e-025        pub=-6.2706491e-032
+ uc=4.6796853e-011         luc=7.9323958e-017        wuc=1.8651644e-017
+ puc=-2.3803623e-023       vsat=77860.433     lvsat=-0.00081878711
+ wvsat=-0.0035518874       pvsat=2.4125667e-009
+ a0=-0.10275458       la0=4.6730518e-007  wa0=2.9650415e-007
+ pa0=-1.4364985e-013 ags=0.3065495             lags=4.8480478e-007
+ wags=1.0570427e-007       pags=-7.7370976e-014      a1=0
+ a2=0.995                  b0=0                      b1=0
+ keta=-0.044479894         lketa=-1.8697001e-008     wketa=-6.9594572e-009
+ pketa=6.0268161e-015      dwg=0                     dwb=0
+ pclm=0.4744185     lpclm=2.1458817e-007
+ wpclm=3.7800547e-008      ppclm=-4.28318e-014
+ pdiblc1=0                 pdiblc2=0.0015597345
+ lpdiblc2=-2.5589493e-010                 wpdiblc2=5.1804148e-011
+ ppdiblc2=1.462308e-016                   pdiblcb=0
+ drout=0.5                 pvag=0.6279               delta=0.005
+ pscbe1=4.5e+008           pscbe2=1e-020             fprout=0
+ pdits=0                   pditsd=0                  pditsl=0
+ rsh=7.28                  rdsw=200                  rsw=90.88
+ rdw=90.88                 prwg=0                    prwb=0
+ wr=1                      alpha0=1.454e-007         alpha1=2.295
+ beta0=17.8                agidl=2.593e-009          bgidl=1.8508e+009
+ cgidl=0.25                egidl=0.2624              aigbacc=0.01213
+ bigbacc=0.006537          cigbacc=0.2809            nigbacc=4.05
+ aigbinv=0.35              bigbinv=0.03              cigbinv=0.006
+ eigbinv=1.1               nigbinv=1                 aigc=0.01
+ bigc=0.00144              cigc=1.515e-005           aigsd=0.008379
+ bigsd=0.0002699           cigsd=3.925e-020          nigc=1
+ poxedge=1                 pigcd=2.171               ntox=1
+ xrcrg1=12                 xrcrg2=1                  cgso=1e-10
+ cgdo=1e-10                 cgbo=0                    cgdl=1e-10
+ cgsl=1e-10                 clc=1e-007                cle=0.6
+ cf=1                    ckappas=0.6               ckappad=0.6
+ acde=0.4                  moin=5.346                noff=1.973
+ voffcv=-0.0904            kt1=-0.27879193           lkt1=1.4001673e-08
+ wkt1=1.1098907e-08        pkt1=-4.991675e-15        kt1l=0
+ kt2=-0.053872644          lkt2=-5.638463e-10        wkt2=-2.877297e-10
+ pkt2=1.587215e-16         ute=-1.3891561            lute=1.4508792e-007
+ wute=6.0707017e-008       pute=-5.4287351e-014      ua1=2.6364413e-09
+ lua1=2.6732108e-16        wua1=1.4264386e-16        pua1=-2.1553916e-22
+ ub1=-4.1547516e-018       lub1=2.9650447e-025       wub1=-7.1031093e-026
+ pub1=1.6079175e-031       uc1=-4.151591e-011        luc1=4.6792241e-017
+ wuc1=-1.519636e-018       puc1=1.8490137e-024       prt=0
+ at=114195.88              lat=-0.050081619          wat=-0.0020196821
+ pat=2.2959393e-09         jss=2.85e-07              jsd=2.85e-07
+ jsws=6.9e-13              jswd=6.9e-13              jswgs=6.9e-13
+ jswgd=6.9e-13             njs=1                     njd=1
+ ijthsfwd=0.01             ijthdfwd=0.01             ijthsrev=0.01
+ ijthdrev=0.01             bvs=11.25                 bvd=11.25
+ xjbvs=1                   xjbvd=1                   pbs=0.6882682
+ pbd=0.6882682             cjs=1e-10                   cjd=1e-10
+ mjs=0.359                 mjd=0.359                 pbsws=0.32
+ pbswd=0.32                cjsws=1.185e-10               cjswd=1.185e-10
+ mjsws=0.202               mjswd=0.202               pbswgs=0.952
+ pbswgd=0.952              cjswgs=3.82e-10             cjswgd=3.82e-10
+ mjswgs=0.541              mjswgd=0.541              tpb=1.49e-3
+ tcj=9.05e-4               tpbsw=8.94e-04            tcjsw=8.09e-04
+ tpbswg=0.00133            tcjswg=0.00088            xtis=3
+ xtid=3                    jtsswgs=1.09e-009         jtsswgd=1.09e-009
+ njtsswg=11.6              xtsswgs=0.2886            xtsswgd=0.2886
+ tnjtsswg=1.08             vtsswgs=10                vtsswgd=10
+ dmcg=2.05e-007            dmci=3.15e-007            dmdg=0
+ dmcgt=0                   dwj=0                     xgw=0
+ xgl=-3.1e-008             rshg=8.23                 gbmin=1e-012
+ rbpb=50                   rbpd=50                   rbps=50
+ rbdb=50                   rbsb=50                   saref=1.00e-05
+ sbref=1.00e-05            ngcon=1                   wlod=5e-007
+ kvth0=2.2e-009            lkvth0=-1e-008            wkvth0=2.2e-006
+ pkvth0=-5e-014            llodvth=1                 wlodvth=1
+ stk2=2.5e-009             lodk2=1                   lodeta0=2
+ ku0=-3.2e-008             lku0=2e-007               wku0=7e-007
+ pku0=-5e-014              llodku0=1                 wlodku0=1
+ kvsat=0.4                 steta0=-1.1e-010          tku0=0.03
+ fnoimod=1                 noia=1.250e+42                noib=7.000e+23
+ noic=6.080e+7                em=3.00e7                 ef=0.904
+ minr=1e-3
 
 
     16: type=n 
+ lmin=1.8e-07              lmax=5e-007 wmin=2.2e-07
+ wmax=5.3e-007                         version=4.5
+ rgeomod=1                 binunit=2                 paramchk=1
+ mobmod=0                  capmod=2                  igcmod=0
+ igbmod=0                  diomod=1                  rdsmod=1
+ rbodymod=0                rgatemod=0                permod=1
+ acnqsmod=0                trnqsmod=0                tempmod=0
+ wpemod=1                  tnom=25                   toxe=3.981e-09
+ toxm=3.981e-09       dtox=5.958e-010           epsrox=3.9
+ wint=1.02e-008            lint=2.595e-008           ll=0
+ wl=0                      lln=1                     wln=1
+ lw=0                      ww=0                      lwn=1
+ wwn=1                     lwl=0                     wwl=0
+ llc=0                     wlc=0                     lwc=0
+ wwc=0                     lwlc=0                    wwlc=0
+ xl=-1.5e-08 xw=0        dlc=2.595e-008
+ dwc=0                     xpart=1                   toxref=3e-009
+ dlcig=2.5e-009            vth0=0.48719013
+ lvth0=-5.4580876e-009                        wvth0=-6.4052624e-009
+ pvth0=7.8603777e-016                         k1=0.448
+ k2=0.04626793         lk2=4.9994489e-010   wk2=-5.7836793e-009
+ pk2=-1.6072338e-017       k3=-3.7                   k3b=1.2
+ w0=0                      dvt0=0.09708              dvt1=0.3053
+ dvt2=-0.6939              dvt0w=0                   dvt1w=0
+ dvt2w=0                   dsub=0.633                minv=-0.34
+ voffl=-1.22e-009          dvtp0=1.46e-006           dvtp1=0
+ lpe0=9.921e-009           lpeb=2.178e-008           web=0
+ wec=0                     scref=1e-006              kvth0we=0.0035
+ lkvth0we=-1.4299999e-010  wkvth0we=-1.1999981e-011  pkvth0we=1.4999996e-017
+ k2we=0.0038               lk2we=0                   wk2we=0
+ pk2we=0                   xj=1.6e-007               ngate=9e+019
+ ndep=5.8e+017             nsd=1e+020                phin=0
+ cdsc=0                    cdscb=0                   cdscd=0
+ cit=0.00082193549   lcit=-1.2910146e-018
+ wcit=-1.6405833e-010      pcit=6.5790105e-025
+ voff=-0.17614288   tvoff=0.0021962234        ptvoff=1.0045211e-17
+ wtvoff=-2.528754e-10      ltvoff=-1.9711953e-11     lvoff=3.5781717e-009
+ wvoff=5.3393099e-009      pvoff=-1.1557015e-015
+ nfactor=0.85596405        lnfactor=3.4495917e-008   wnfactor=7.3400719e-008
+ pnfactor=-1.7579119e-014  eta0=0.39703025    leta0=-3.685432e-008
+ weta0=-3.4783194e-008     peta0=8.0160785e-015
+ etab=-0.24211447          letab=-2.8535023e-008     wetab=-3.3575266e-008
+ petab=1.4541448e-014      ud=0                      lud=0
+ wud=0                     pud=0                     ku0we=0
+ lku0we=0                  wku0we=0                  pku0we=0
+ u0=0.033118824       lu0=-2.092564e-010  wu0=3.3875357e-010
+ pu0=1.0055256e-016  ua=-3.335318e-010         lua=-4.263548e-017
+ wua=-1.6371084e-016       pua=1.1944258e-023        ub=1.9040785e-018
+ lub=6.0965752e-026        wub=1.5521224e-025        pub=-3.1411375e-032
+ uc=2.2466359e-010         luc=2.2898732e-018        wuc=-3.1489728e-017
+ puc=-2.0873949e-024       vsat=81637.162     lvsat=-0.0024544887
+ wvsat=0.00038051534       pvsat=7.0944303e-010
+ a0=0.85142296        la0=5.4050885e-008  wa0=-1.0264022e-008
+ pa0=-1.0788557e-014 ags=1.7021554             lags=-1.1963214e-007
+ wags=-9.8720178e-008      pags=1.1165252e-014       a1=0
+ a2=0.995                  b0=0                      b1=0
+ keta=-0.10549168          lketa=7.727204e-009       wketa=9.6001598e-009
+ pketa=-1.1451541e-015     dwg=0                     dwb=0
+ pclm=0.93788546    lpclm=1.3860637e-008
+ wpclm=-4.5470853e-008     ppclm=-6.7669565e-015
+ pdiblc1=0                 pdiblc2=0.00072159941
+ lpdiblc2=1.0710136e-010                  wpdiblc2=5.520414e-010
+ ppdiblc2=-7.0421953e-017                 pdiblcb=0
+ drout=0.5                 pvag=0.6279               delta=0.005
+ pscbe1=4.5e+008           pscbe2=1e-020             fprout=0
+ pdits=0                   pditsd=0                  pditsl=0
+ rsh=7.28                  rdsw=200                  rsw=90.88
+ rdw=90.88                 prwg=0                    prwb=0
+ wr=1                      alpha0=1.454e-007         alpha1=2.295
+ beta0=17.8                agidl=2.593e-009          bgidl=1.8508e+009
+ cgidl=0.25                egidl=0.2624              aigbacc=0.01213
+ bigbacc=0.006537          cigbacc=0.2809            nigbacc=4.05
+ aigbinv=0.35              bigbinv=0.03              cigbinv=0.006
+ eigbinv=1.1               nigbinv=1                 aigc=0.01
+ bigc=0.00144              cigc=1.515e-005           aigsd=0.008379
+ bigsd=0.0002699           cigsd=3.925e-020          nigc=1
+ poxedge=1                 pigcd=2.171               ntox=1
+ xrcrg1=12                 xrcrg2=1                  cgso=1e-10
+ cgdo=1e-10                 cgbo=0                    cgdl=1e-10
+ cgsl=1e-10                 clc=1e-007                cle=0.6
+ cf=1                    ckappas=0.6               ckappad=0.6
+ acde=0.4                  moin=5.346                noff=1.973
+ voffcv=-0.0904            kt1=-0.23125654           lkt1=-6.5859059e-09
+ wkt1=-4.0331791e-09       pkt1=1.5620304e-15        kt1l=0
+ kt2=-0.055033537          lkt2=-6.10637e-11         wkt2=3.93187e-11
+ pkt2=1.707685e-17         ute=-0.98679314           lute=-2.9175468e-008
+ wute=-9.2123567e-008      pute=1.1903575e-014       ua1=3.5950246e-09
+ lua1=-1.478414e-16        wua1=-4.3225733e-16       pua1=3.3450547e-23
+ ub1=-3.6926465e-018       lub1=9.636675e-026        wub1=2.8897772e-025
+ pub1=4.8719324e-033       uc1=5.5143893e-011        luc1=4.9288809e-018
+ wuc1=7.1784539e-019       puc1=8.7996049e-025       prt=0
+ at=-6339.3589             lat=0.0021221942          wat=0.0039774212
+ pat=-3.0140637e-10        jss=2.85e-07              jsd=2.85e-07
+ jsws=6.9e-13              jswd=6.9e-13              jswgs=6.9e-13
+ jswgd=6.9e-13             njs=1                     njd=1
+ ijthsfwd=0.01             ijthdfwd=0.01             ijthsrev=0.01
+ ijthdrev=0.01             bvs=11.25                 bvd=11.25
+ xjbvs=1                   xjbvd=1                   pbs=0.6882682
+ pbd=0.6882682             cjs=1e-10                   cjd=1e-10
+ mjs=0.359                 mjd=0.359                 pbsws=0.32
+ pbswd=0.32                cjsws=1.185e-10               cjswd=1.185e-10
+ mjsws=0.202               mjswd=0.202               pbswgs=0.952
+ pbswgd=0.952              cjswgs=3.82e-10             cjswgd=3.82e-10
+ mjswgs=0.541              mjswgd=0.541              tpb=1.49e-3
+ tcj=9.05e-4               tpbsw=8.94e-04            tcjsw=8.09e-04
+ tpbswg=0.00133            tcjswg=0.00088            xtis=3
+ xtid=3                    jtsswgs=1.09e-009         jtsswgd=1.09e-009
+ njtsswg=11.6              xtsswgs=0.2886            xtsswgd=0.2886
+ tnjtsswg=1.08             vtsswgs=10                vtsswgd=10
+ dmcg=2.05e-007            dmci=3.15e-007            dmdg=0
+ dmcgt=0                   dwj=0                     xgw=0
+ xgl=-3.1e-008             rshg=8.23                 gbmin=1e-012
+ rbpb=50                   rbpd=50                   rbps=50
+ rbdb=50                   rbsb=50                   saref=1.00e-05
+ sbref=1.00e-05            ngcon=1                   wlod=5e-007
+ kvth0=2.2e-009            lkvth0=-1e-008            wkvth0=2.2e-006
+ pkvth0=-5e-014            llodvth=1                 wlodvth=1
+ stk2=2.5e-009             lodk2=1                   lodeta0=2
+ ku0=-3.2e-008             lku0=2e-007               wku0=7e-007
+ pku0=-5e-014              llodku0=1                 wlodku0=1
+ kvsat=0.4                 steta0=-1.1e-010          tku0=0.03
+ fnoimod=1                 noia=1.250e+42                noib=7.000e+23
+ noic=6.080e+7                em=3.00e7                 ef=0.904
+ minr=1e-3
}