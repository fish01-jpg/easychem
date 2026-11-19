# Easy Chem Lab | Low-memory TI-84 Evo build
import gc as _gc
exec('''def element_weight(symbol):
 text=(
  "H:1.008 He:4.0026 Li:6.94 Be:9.0122 B:10.81 C:12.011 N:14.007 O:15.999 F:18.998 Ne:20.180 "
  "Na:22.990 Mg:24.305 Al:26.982 Si:28.085 P:30.974 S:32.06 Cl:35.45 Ar:39.95 K:39.098 Ca:40.078 "
  "Sc:44.956 Ti:47.867 V:50.942 Cr:51.996 Mn:54.938 Fe:55.845 Co:58.933 Ni:58.693 Cu:63.546 Zn:65.38 "
  "Ga:69.723 Ge:72.630 As:74.922 Se:78.971 Br:79.904 Kr:83.798 Rb:85.468 Sr:87.62 Y:88.906 Zr:91.222 "
  "Nb:92.906 Mo:95.95 Tc:- Ru:101.07 Rh:102.91 Pd:106.42 Ag:107.87 Cd:112.41 In:114.82 Sn:118.71 "
  "Sb:121.76 Te:127.60 I:126.90 Xe:131.29 Cs:132.91 Ba:137.33 La:138.91 Ce:140.12 Pr:140.91 Nd:144.24 "
  "Pm:- Sm:150.36 Eu:151.96 Gd:157.25 Tb:158.93 Dy:162.50 Ho:164.93 Er:167.26 Tm:168.93 Yb:173.05 "
  "Lu:174.97 Hf:178.49 Ta:180.95 W:183.84 Re:186.21 Os:190.23 Ir:192.22 Pt:195.08 Au:196.97 Hg:200.59 "
  "Tl:204.38 Pb:207.2 Bi:208.98 Po:- At:- Rn:- Fr:- Ra:- Ac:- Th:232.04 Pa:231.04 U:238.03 "
  "Np:- Pu:- Am:- Cm:- Bk:- Cf:- Es:- Fm:- Md:- No:- Lr:- Rf:- Db:- Sg:- Bh:- Hs:- Mt:- Ds:- "
  "Rg:- Cn:- Nh:- Fl:- Mc:- Lv:- Ts:- Og:-"
  )
 key=" "+symbol+":"
 text=" "+text+" "
 i=text.index(key)+len(key)
 aa=text[i:text.index(" ",i)]
 return 0 if aa=="-"else float(aa)
''',globals())
_gc.collect()
exec('''SYMBOLS=(
 "H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn "
 "Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba "
 "La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn Fr Ra "
 "Ac Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og"
 )
ab=(
 "Hydrogen Helium Lithium Beryllium Boron Carbon Nitrogen Oxygen Fluorine Neon "
 "Sodium Magnesium Aluminum Silicon Phosphorus Sulfur Chlorine Argon Potassium Calcium "
 "Scandium Titanium Vanadium Chromium Manganese Iron Cobalt Nickel Copper Zinc "
 "Gallium Germanium Arsenic Selenium Bromine Krypton Rubidium Strontium Yttrium Zirconium "
 "Niobium Molybdenum Technetium Ruthenium Rhodium Palladium Silver Cadmium Indium Tin "
 "Antimony Tellurium Iodine Xenon Cesium Barium Lanthanum Cerium Praseodymium Neodymium "
 )
''',globals())
_gc.collect()
exec('''ac=(
 "Promethium Samarium Europium Gadolinium Terbium Dysprosium Holmium Erbium Thulium Ytterbium "
 "Lutetium Hafnium Tantalum Tungsten Rhenium Osmium Iridium Platinum Gold Mercury Thallium Lead "
 "Bismuth Polonium Astatine Radon Francium Radium Actinium Thorium "
 "Protactinium Uranium Neptunium Plutonium Americium Curium "
 "Berkelium Californium Einsteinium Fermium Mendelevium Nobelium Lawrencium "
 )
ad="Rutherfordium Dubnium Seaborgium Bohrium Hassium Meitnerium Darmstadtium "
ae="Roentgenium Copernicium Nihonium Flerovium Moscovium Livermorium Tennessine Oganesson"
BLOCKS=((40,72,99),(49,87,83),(87,63,112),(104,67,60),(58,88,114))
def table_grid():
 af=[0]*162
 for r,c,a,b in((0,0,1,1),(0,17,2,2),
  (1,0,3,4),(1,12,5,10),(2,0,11,12),(2,12,13,18),
  (3,0,19,36),(4,0,37,54),(5,0,55,56),(5,3,72,86),
  (6,0,87,88),(6,3,104,118),(7,2,57,71),(8,2,89,103)):
  start=r*18+c
  for n in range(a,b+1):
   af[start+n-a]=n
 return af
''',globals())
_gc.collect()
exec('''def family(r,c,n):
 if r==7:
  return("Lanthanide series",2)
 if r==8:
  return("Actinide series",3)
 if c==17:
  return("Noble gas group",4)
 if c==16:
  return("Halogen group",0)
 if c==0 and n!=1:
  return("Alkali metal group",0)
 if c==1:
  return("Alkaline earth group",0)
 if 2<=c<=11:
  return("d-block",1)
 return("Main group",0)
def ag(pos,z,ah,ai=False):
 r,c=pos//18,pos%18
 if not z:
  return
 if r>=7:
  x,y,w=11+(c-2)*20,57+r*14,18
 else:
  x,y,w=8+c*17,53+r*14,16
 rect(x,y,w,13,ACC if ai else BLOCKS[family(r,c,z)[1]])
 sym=ah[z-1]
 label(x+w//2,y,sym if width(sym)<=w+1 else str(z),
  INK if ai else WHITE,w=w+1,align=1)
def step_element(af,pos,key):
 r,c=pos//18,pos%18
 if key in(LEFT,RIGHT):
  for i in range(1,18):
   j=r*18+(c+i*(1 if key==RIGHT else-1))%18
   if af[j]:
    return j
 else:
  rr=r+(-1 if key==UP else 1)
  if 0<=rr<9:
   j=-1
   for cc in range(18):
    if af[rr*18+cc]and(j<0 or abs(cc-c)<abs(j-c)):
     j=cc
   if j>=0:
    return rr*18+j
 return pos
''',globals())
_gc.collect()
exec('''def element_details(af,pos,ah,aj):
 n=af[pos]
 while True:
  pos=af.index(n)
  sym=ah[n-1]
  r,c=pos//18,pos%18
  fam,_=family(r,c,n)
  p=(6 if r==7 else 7)if r>=7 else r+1
  frame("Element profile",aj[n-1],"Z "+str(n))
  rect(11,57,83,97,ACTIVE)
  rect(11,57,83,3,ACC)
  label(53,67,str(n),MUTED,w=70,align=1)
  label(53,91,sym,ACC,2,71,1)
  label(53,130,"ATOMIC NO.",MUTED,w=74,align=1)
  rect(102,57,207,97,PANEL)
  label(113,63,"MOLAR MASS (g/mol)",MUTED,w=182)
  aa=element_weight(sym)
  label(113,81,approx(aa)if aa else"Not defined",WHITE,1,184)
  s="Period "+str(p)
  if r<7:
   s+="  |  Group "+str(c+1)
  label(113,111,s,WHITE,w=186)
  label(113,132,fam,ACC,w=186)
  label(11,162,"No standard atomic weight; use isotope mass."if not aa else
   "Standard-weight estimate for normal material.",MUTED,w=298)
  footer("LEFT/RIGHT Atomic number","CLEAR Table")
  k=sy.wait_key()
  if k in(CLEAR,ENTER):
   return pos
  if k in(LEFT,RIGHT):
   n=min(118,max(1,n+(1 if k==RIGHT else-1)))
''',globals())
_gc.collect()
exec('''def periodic():
 af=table_grid()
 ah=SYMBOLS.split()
 aj=(ab+ac+ad+ae).split()
 p=0
 old=-1
 while True:
  n=af[p]
  if old<0:
   frame("Reference / 118 elements","Periodic table")
   for i in range(len(af)):
    ag(i,af[i],ah,i==p)
   footer("ARROWS Move   ENTER Details","CLEAR Back")
  elif old!=p:
   ag(old,af[old],ah)
   ag(p,n,ah,True)
  chip(162,22,147,str(n)+"  "+aj[n-1],True)
  k=sy.wait_key()
  old=p
  if k==CLEAR:
   return
  if k==ENTER:
   p=element_details(af,p,ah,aj)
   old=-1
  if k in(LEFT,RIGHT,UP,DOWN):
   p=step_element(af,p,k)
ak=\'frame footer rect label width chip ACC WHITE INK MUTED ACTIVE PANEL UP DOWN LEFT RIGHT ENTER CLEAR approx sy\'
def open_table(api):
 for k in ak.split():
  globals()[k]=api[k]
 periodic()
''',globals())
_gc.collect()
