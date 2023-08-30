#--- define groups
variable xxlo	equal xlo
variable x0		equal ${xxlo}+${buff}
#
variable xxhi	equal xhi 
variable x1		equal ${xxhi}-${buff}
#
variable yylo	equal ylo
variable y0	equal ${yylo}+${buffy}

variable yyhi	equal yhi
variable y1		equal ${yyhi}-${buffy}
#
variable zzlo	equal zlo
variable z0		equal ${zzlo}+${buffz}
#
variable zzhi	equal zhi 
variable z1		equal ${zzhi}-${buffz}
#
region top    block INF INF INF INF ${z1} INF
region bottom block INF INF INF INF INF ${z0}
#
region up block INF INF ${y1} INF INF INF
region down block INF INF INF ${y0} INF INF
#
region right block ${x1} INF INF INF INF INF
region left block INF ${x0} INF INF INF INF

group topp region top
group bottomm region bottom
#
group upp region up
group downn region down
#
group lg region left
group rg region right
#
#--- fix walls
fix 1 upp setforce 0.0 0.0 0.0
fix 2 downn setforce 0.0 0.0 0.0
#
fix 11 lg setforce 0.0 0.0 0.0
fix 22 rg setforce 0.0 0.0 0.0
#
fix 111 topp setforce 0.0 0.0 0.0
fix 222 bottomm setforce 0.0 0.0 0.0
#

velocity topp set 0 0 0
velocity bottomm set 0 0 0
velocity upp set 0 0 0
velocity downn set 0 0 0
velocity lg set 0 0 0
velocity rg set 0 0 0

group boundary union upp downn lg rg topp bottomm
group bulk subtract all boundary

