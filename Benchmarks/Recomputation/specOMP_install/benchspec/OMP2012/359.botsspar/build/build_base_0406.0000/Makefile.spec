TUNE=base
EXT=0406
NUMBER=359
NAME=botsspar
SOURCES= common/bots_main.c common/bots_common.c \
	 omp-tasks/sparselu/sparselu_single/my_include.c \
	 omp-tasks/sparselu/sparselu_single/sparselu.c
EXEBASE=bots-sparselu
NEED_MATH=yes
BENCHLANG=C
ONESTEP=
CONESTEP=

BENCH_FLAGS      = -I. -I./omp-tasks/sparselu/sparselu_single -I./common
CC               = /usr/bin/gcc
COPTIMIZE        = -fopenmp
FPBASE           = yes
OPTIMIZE         = -O2
OS               = unix
PORTABILITY      = -DSPEC_LP64
absolutely_no_locking = 0
abstol           = 1e-07
action           = build
allow_extension_override = 0
backup_config    = 1
baseexe          = bots-sparselu
basepeak         = 0
benchdir         = benchspec
benchmark        = 359.botsspar
binary           = 
bindir           = exe
build_in_build_dir = 1
builddir         = build
bundleaction     = 
bundlename       = 
calctol          = 0
changedmd5       = 0
check_integrity  = 1
check_md5        = 0
check_version    = 1
clean_between_builds = no
command_add_redirect = 0
commanderrfile   = speccmds.err
commandexe       = bots-sparselu_base.0406
commandfile      = speccmds.cmd
commandoutfile   = speccmds.out
commandstdoutfile = speccmds.stdout
compareerrfile   = compare.err
comparefile      = compare.cmd
compareoutfile   = compare.out
comparestdoutfile = compare.stdout
compile_error    = 0
compwhite        = 
configdir        = config
configpath       = /home/cc/specOMP_install/config/dave.cfg
copies           = 1
current_range    = 
datadir          = data
default_size     = ref
delay            = 0
deletebinaries   = 0
deletework       = 0
dependent_workloads = 0
device           = 
difflines        = 10
dirprot          = 511
discard_power_samples = 1
endian           = 12345678
env_vars         = 0
exitvals         = spec_exit
expand_notes     = 0
expid            = 
ext              = 0406
fake             = 0
feedback         = 1
flag_url_base    = http://www.spec.org/auto/omp2012/flags/
floatcompare     = 
help             = 0
http_proxy       = 
http_timeout     = 30
hw_cpu_name      = Intel Xeon E5-2670 v3
hw_disk          = 219 GB  add more disk info here
hw_memory001     = 125.687 GB fixme: If using DDR3, format is:
hw_memory002     = 'N GB (M x N GB nRxn PCn-nnnnnR-n, ECC)'
hw_nchips        = 2
idle_current_range = 
idledelay        = 10
idleduration     = 60
ignore_errors    = 0
ignore_sigint    = 0
ignorecase       = 
info_wrap_columns = 50
inputdir         = input
iteration        = -1
iterations       = 1
keeptmp          = 0
line_width       = 0
locking          = 1
log              = OMP2012
log_line_width   = 0
log_timestamp    = 0
logname          = /home/cc/specOMP_install/result/OMP2012.183.log
lognum           = 183
mach             = default
mail_reports     = all
mailcompress     = 0
mailmethod       = smtp
mailport         = 25
mailserver       = 127.0.0.1
mailto           = 
make             = specmake
make_no_clobber  = 0
makeflags        = 
max_active_compares = 0
max_average_uncertainty = 1
max_hum_limit    = 0
max_unknown_uncertainty = 1
mean_anyway      = 0
meter_connect_timeout = 30
meter_errors_default = 0.1
meter_errors_percentage = 0.1
min_report_runs  = 3
min_temp_limit   = 20
minimize_builddirs = 0
minimize_rundirs = 0
name             = botsspar
need_math        = yes
no_input_handler = close
no_monitor       = 
note_preenv      = 0
notes_plat_sysinfo_000 =  Sysinfo program /home/cc/specOMP_install/Docs/sysinfo
notes_plat_sysinfo_005 =  $Rev: 395 $ $Date:: 2012-07-25 \#$ 8f8c0fe9e19c658963a1e67685e50647
notes_plat_sysinfo_010 =  running on crash-test6 Thu Oct 18 06:41:10 2018
notes_plat_sysinfo_015 = 
notes_plat_sysinfo_020 =  This section contains SUT (System Under Test) info as seen by
notes_plat_sysinfo_025 =  some common utilities.  To remove or add to this section, see:
notes_plat_sysinfo_030 =    http://www.spec.org/omp2012/Docs/config.html\#sysinfo
notes_plat_sysinfo_035 = 
notes_plat_sysinfo_040 =  From /proc/cpuinfo
notes_plat_sysinfo_045 =     model name : Intel(R) Xeon(R) CPU E5-2670 v3 @ 2.30GHz
notes_plat_sysinfo_050 =        2 "physical id"s (chips)
notes_plat_sysinfo_055 =        48 "processors"
notes_plat_sysinfo_060 =     cores, siblings (Caution: counting these is hw and system dependent.  The
notes_plat_sysinfo_065 =     following excerpts from /proc/cpuinfo might not be reliable.  Use with
notes_plat_sysinfo_070 =     caution.)
notes_plat_sysinfo_075 =        cpu cores : 12
notes_plat_sysinfo_080 =        siblings  : 24
notes_plat_sysinfo_085 =        physical 0: cores 0 1 2 3 4 5 8 9 10 11 12 13
notes_plat_sysinfo_090 =        physical 1: cores 0 1 2 3 4 5 8 9 10 11 12 13
notes_plat_sysinfo_095 =     cache size : 30720 KB
notes_plat_sysinfo_100 = 
notes_plat_sysinfo_105 =  From /proc/meminfo
notes_plat_sysinfo_110 =     MemTotal:       131791880 kB
notes_plat_sysinfo_115 =     HugePages_Total:       0
notes_plat_sysinfo_120 =     Hugepagesize:       2048 kB
notes_plat_sysinfo_125 = 
notes_plat_sysinfo_130 =  /usr/bin/lsb_release -d
notes_plat_sysinfo_135 =     Ubuntu 14.04.5 LTS
notes_plat_sysinfo_140 = 
notes_plat_sysinfo_145 =  From /etc/*release* /etc/*version*
notes_plat_sysinfo_150 =     debian_version: jessie/sid
notes_plat_sysinfo_155 =     ec2_version: Ubuntu 14.04 LTS (Trusty Tahr)
notes_plat_sysinfo_160 =     os-release:
notes_plat_sysinfo_165 =        NAME="Ubuntu"
notes_plat_sysinfo_170 =        VERSION="14.04.5 LTS, Trusty Tahr"
notes_plat_sysinfo_175 =        ID=ubuntu
notes_plat_sysinfo_180 =        ID_LIKE=debian
notes_plat_sysinfo_185 =        PRETTY_NAME="Ubuntu 14.04.5 LTS"
notes_plat_sysinfo_190 =        VERSION_ID="14.04"
notes_plat_sysinfo_195 =        HOME_URL="http://www.ubuntu.com/"
notes_plat_sysinfo_200 =        SUPPORT_URL="http://help.ubuntu.com/"
notes_plat_sysinfo_205 = 
notes_plat_sysinfo_210 =  uname -a:
notes_plat_sysinfo_215 =     Linux crash-test6 3.13.0-145-generic \#194-Ubuntu SMP Thu Apr 5 15:20:44 UTC
notes_plat_sysinfo_220 =     2018 x86_64 x86_64 x86_64 GNU/Linux
notes_plat_sysinfo_225 = 
notes_plat_sysinfo_230 =  run-level 2 Oct 14 06:52
notes_plat_sysinfo_235 = 
notes_plat_sysinfo_240 =  SPEC is set to: /home/cc/specOMP_install
notes_plat_sysinfo_245 =     Filesystem     Type  Size  Used Avail Use% Mounted on
notes_plat_sysinfo_250 =     /dev/sda1      ext4  219G   15G  196G   7% /
notes_plat_sysinfo_255 = 
notes_plat_sysinfo_260 =  Cannot run dmidecode; consider saying 'chmod +s /usr/sbin/dmidecode'
notes_plat_sysinfo_265 = 
notes_plat_sysinfo_270 =  (End of data from sysinfo program)
notes_wrap_columns = 0
notes_wrap_indent =   
num              = 359
obiwan           = 
os_exe_ext       = 
output           = asc
output_format    = text,config
output_root      = 
outputdir        = output
parallel_setup   = 1
parallel_setup_prefork = 
parallel_setup_type = fork
parallel_test    = 0
parallel_test_submit = 0
parallel_test_workloads = 
path             = /home/cc/specOMP_install/benchspec/OMP2012/359.botsspar
plain_train      = 0
platform         = 
power            = 0
preenv           = 1
prefix           = 
prepared_by      = cc  (is never output, only tags rawfile)
ranks            = -1
rate             = 0
realuser         = your name here
rebuild          = 0
reftime          = reftime
reltol           = 1e-07
reportable       = 0
resultdir        = result
review           = 0
run              = all
rundir           = run
runspec          = /home/cc/specOMP_install/bin/runspec --config=dave.cfg --action=build --tune=base 359.botsspar
safe_eval        = 1
section_specifier_fatal = 1
sendmail         = /usr/sbin/sendmail
setpgrp_enabled  = 1
setprocgroup     = 1
setup_error      = 0
shrate           = 0
sigint           = 2
size             = test
size_class       = test
skipabstol       = 
skipobiwan       = 
skipreltol       = 
skiptol          = 
smarttune        = base
specdiff         = specdiff
specmake         = Makefile.YYYtArGeTYYYspec
specrun          = specinvoke
speed            = 0
srcalt           = 
srcdir           = src
srcsource        = /home/cc/specOMP_install/benchspec/OMP2012/359.botsspar/src
stagger          = 10
strict_rundir_verify = 0
sw_file          = ext4
sw_os001         = Ubuntu 14.04.5 LTS
sw_os002         = 3.13.0-145-generic
sw_state         = Run level 2 (add definition here)
sysinfo_program  = specperl /home/cc/specOMP_install/Docs/sysinfo
table            = 1
teeout           = 0
test_date        = Oct-2018
threads          = -1
top              = /home/cc/specOMP_install
train_with       = train
tune             = base
uid              = 1000
unbuffer         = 1
uncertainty_exception = 5
update-flags     = 0
use_submit_for_speed = 1
username         = cc
vendor           = anon
vendor_makefiles = 0
verbose          = 5
version          = 20
version_url      = http://www.spec.org/auto/omp2012/current_version
voltage_range    = 
worklist         = list
OUTPUT_RMFILES   = botsspar.out
