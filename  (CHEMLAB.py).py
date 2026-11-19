# Easy Chem Lab | Low-memory TI-84 Evo build
import gc as _gc
_console = print
try:
 exec('''from math import log,log10,exp,sqrt
DIG="0123456789"
ABC="abcdefg"
aa=False
U={
 "v":("L mL uL cm3 m3",(1,.001,.000001,.001,1000)),
 "p":("atm kPa Pa bar mmHg torr",(1,.009869232667,.000009869232667,
 .9869232667,.001315789474,.001315789474)),
 "t":("K C F",(1,1,5/9)),
 "d":("C K F",(1,1,5/9)),
 "m":("g mg kg ug",(1,.001,1000,.000001)),
 "n":("mol mmol umol",(1,.001,.000001)),
 "c":("mol/L mmol/L",(1,.001)),
 "b":("mol/kg",(1,)),
 "w":("g/mol kg/mol",(1,1000)),
 "q":("J kJ cal",(1,1000,4.184)),
 "h":("J/mol kJ/mol",(1,1000)),
 "s":("J/mol/K kJ/mol/K",(1,1000)),
 "j":("J/g/K",(1,)),
 "C":("J/K kJ/K",(1,1000)),
 "D":("g/mL g/L kg/m3",(1,.001,.001)),
 "G":("g/L g/mL kg/m3",(1,1000,1)),
 "l":("m nm um cm",(1,1e-9,1e-6,.01)),
 "f":("Hz kHz MHz GHz",(1,1000,1e6,1e9)),
 "z":("s min h day yr",(1,60,3600,86400,31557600)),
 "V":("V mV",(1,.001)),
 "I":("A mA",(1,.001)),
 "Q":("Coulomb",(1,)),
 "L":("L/mol/cm",(1,)),
 "B":("cm mm m",(1,.1,100)),
 "%":("%",(1,)),
 "X":("entities",(1,)),
 "P":("ppm ppb",(1,.001)),
 "0":("",(1,))
 }
ab={
 "R":.08205736608,"RJ":8.314462618,"NA":6.02214076e23,
 "H":6.62607015e-34,"LIGHT":299792458,"F":96485.33212,
 "L2":.69314718056
 }
''',globals())
 _gc.collect()
 exec('''GAS=(
 ("Charles: V and T","V1 V2 T1 T2","!v !v !t !t","a/c=b/d",
 "Pressure and moles stay fixed. State 1 is before; state 2 is after. Temperatures are converted to K."),
 ("Boyle: P and V","P1 P2 V1 V2","!p !p !v !v","ac=bd",
 "Temperature and moles stay fixed. State 1 is before; state 2 is after. Enter absolute pressure."),
 ("Gay-Lussac: P and T","P1 P2 T1 T2","!p !p !t !t","a/c=b/d",
 "Volume and moles stay fixed. Also called Amontons\'s law. Use absolute pressure and kelvin temperatures."),
 ("Combined gas law","P1 P2 V1 V2 T1 T2","!p !p !v !v !t !t","ac/e=bd/f",
 "Use for two states of the SAME amount of gas. Absolute pressure and kelvin temperatures are required."),
 ("Ideal gas law","P V n T","!p !v !n !t","ab=cRd",
 "Use absolute P, gas volume V, amount n and temperature T. R is 0.08205737 L*atm/(mol*K)."),
 ("Avogadro: V and n","V1 V2 n1 n2","!v !v !n !n","a/c=b/d",
 "Pressure and temperature stay fixed; V is volume and n is moles."),
 ("Dalton: add pressures","","","",
 ""),
 ("Partial pressure","Ppart X Ptotal","+p &0 !p","a=bc",
 "Ppart is the gas\'s partial pressure; X is its mole fraction (0 to 1). Ptotal is absolute total pressure."),
 ("Gas density","d P MM T","!G !p !w !t","a=bc/Rd",
 "Ideal gas only. d is density and MM is molar mass. R uses L, atm, mol and K."),
 ("Graham: effusion","rateA/B MMA MMB","!0 !w !w",
 ("rateA/B = sqrt(MMB / MMA)","c b / sqrt","c a a * /","b a a * *"),
 "Use the rate of A divided by the rate of B. MMA and MMB are molar masses; compare at the same temperature."),
 ("Gas molar mass","P V mass T MM","!p !v !m !t !w","ab=Rcd/e",
 "Ideal gas only. Uses absolute pressure, volume, mass and temperature. R uses L, atm, mol and K.")
 )
''',globals())
 _gc.collect()
 exec('''ab["N"]=ab["NA"]
ab["U"]=1000
ab["P"]=100
ab["M"]=1000000
ab["L"]=ab["L2"]
ab["T"]=2
ab["I"]=1
ab["S"]=ab["LIGHT"]
ab["W"]=10
def wrapped(txt):
 ac=[]
 ad=""
 for ae in txt.split(" "):
  if not ae:
   continue
  if ad and len(ad)+len(ae)>=26:
   ac.append(ad)
   ad=""
  while len(ae)>26:
   ac.append(ae[:26])
   ae=ae[26:]
  if ad:
   ad+=" "
  ad+=ae
 if ad:
  ac.append(ad)
 return ac
def digits(txt):
 if not txt:
  return False
 for x in txt:
  if x not in DIG:
   return False
 return True
def af(text):
 t=text.strip().lower().replace("*10^","e")
 if not t or len(t)>72:
  raise ValueError()
 neg=""
 if t[0]in"+-":
  if t[0]=="-":
   neg="-"
  t=t[1:]
 ag=t.split("e")
 if len(ag)>2:
  raise ValueError()
 power=0
 if len(ag)==2:
  e=ag[1]
  test=e
  if e and e[0]in"+-":
   test=e[1:]
  if not digits(test)or len(test)>4:
   raise ValueError()
  power=int(e)
  if abs(power)>999:
   raise ValueError()
 ag=ag[0].split(".")
 if len(ag)>2:
  raise ValueError()
 a=ag[0]
 b=ag[1]if len(ag)==2 else""
 ah=a+b
 if not digits(ah):
  raise ValueError()
 ai=ah.lstrip("0")
 if not ai:
  return("","",0,0)
 aj=power+len(a)-(len(ah)-len(ai))-1
 marked="."in t or"e"in t
 ak=len(ai)if marked else len(ai.rstrip("0"))
 return(neg,ai,aj,ak)
''',globals())
 _gc.collect()
 exec('''def al(ai,aj,am):
 if am<0 or not ai:
  return("0",0)
 if not am:
  if an(ai,0):
   return("1",aj+1)
  return("0",0)
 cut=ai[:am]
 if len(cut)<am:
  cut+="0"*(am-len(cut))
 elif len(ai)>am and an(ai,am):
  carry=1
  ao=""
  for i in range(am-1,-1,-1):
   ap=int(cut[i])+carry
   ao=DIG[ap%10]+ao
   carry=ap//10
  if carry:
   return("1"+"0"*(am-1),aj+1)
  cut=ao
 return(cut,aj)
def an(ai,aq):
 ar=ai[aq]
 if ar!="5":
  return ar>"5"
 if not aa or ai[aq+1:].strip("0"):
  return True
 return aq>0 and int(ai[aq-1])%2==1
def au(ai,aj):
 aq=aj+1
 if aq<=0:
  return"0."+"0"*(-aq)+ai
 if aq>=len(ai):
  return ai+"0"*(aq-len(ai))
 return ai[:aq]+"."+ai[aq:]
def sci(ai,aj):
 av=ai[0]
 if len(ai)>1:
  av+="."+ai[1:]
 return av+"e"+str(aj)
def aw(az,n,aA=False):
 neg,ai,aj,ak=az
 if not ai:
  if aA:
   return sci("0"*n,0)
  return"0"if n==1 else"0."+"0"*(n-1)
 ai,aj=al(ai,aj,n)
 if aA or aj<-4 or aj>7:
  return neg+sci(ai,aj)
 aq=aj+1
 if aq>len(ai)or(aq==len(ai)and ai[-1]=="0"):
  return neg+sci(ai,aj)
 return neg+au(ai,aj)
''',globals())
 _gc.collect()
 exec('''def aB(az,n):
 neg,ai,aj,ak=az
 if not ai:
  return au("0"*(1+n),0)
 out,e=al(ai,aj,aj+1+n)
 if out=="0":
  return au("0"*(1+n),0)
 aC=len(out)-e-1
 if aC<n:
  out+="0"*(n-aC)
 if e<-300 or e+n>60:
  return neg+sci(out.rstrip("0"),e)
 return neg+au(out,e)
def approx(x,sf=7):
 p=af("{:.8e}".format(x))
 if not p[1]:
  return"0"
 ai,e=al(p[1],p[2],sf)
 ai=ai.rstrip("0")
 if e<-4 or e>7:
  return p[0]+sci(ai,e)
 return p[0]+au(ai,e)
def value(x):
 return x-x==0
def aD(aE):
 if aE[0]in"!+#@&":
  return aE[0],aE[1:]
 return"",aE
def check(x,aE):
 if not value(x):
  return"Number out of range."
 flag,aF=aD(aE)
 if aF=="t"and x<0:
  return"Below absolute zero."
 if flag=="#"and(x<.99999 or x>10000.00001 or abs(x-int(x+.5))>.00001):
  return"Need a whole number 1-10000."
 if flag=="!"and x<=0:
  return"Must be greater than zero."
 if flag in("+","@","&")and x<0:
  return"Must not be negative."
 if flag=="@"and x>100:
  return"Must be 0 to 100 percent."
 if flag=="&"and x>1:
  return"Must be between 0 and 1."
 if aF=="P"and x>1000000:
  return"Mass ratio exceeds 100%."
 return""
def aG(aE,ix=0):
 return U[aD(aE)[1]][0].split(" ")[ix]
''',globals())
 _gc.collect()
 exec('''def scale(x,aE,ix,out=False):
 aF=aD(aE)[1]
 fac=U[aF][1][ix]
 if aF=="t"and ix:
  if ix==1:
   return x-273.15 if out else x+273.15
  return x/fac-459.67 if out else(x+459.67)*fac
 return x/fac if out else x*fac
def aH(aI):
 if not aI:
  return"1"
 ans=aI[0]
 for x in aI[1:]:
  ans+=" "+x+" *"
 return ans
def law_rpn(eq,target):
 aJ,aK=eq.replace(" ","").split("=")
 ap=[]
 den=[]
 sign=0
 for pair in((aJ,1),(aK,-1)):
  aL=pair[1]
  for x in pair[0]:
   if x=="/":
    aL=-aL
   elif x==target:
    sign=aL
   elif aL>0:
    ap.append(x)
   else:
    den.append(x)
 if sign>0:
  ap,den=den,ap
 ans=aH(ap)
 if den:
  ans+=" "+aH(den)+" /"
 return ans
def aM(eq,aN):
 if not isinstance(eq,str):
  return eq[0]
 sides=[]
 for side in eq.replace(" ","").split("="):
  parts=side.split("/")
  aO=[]
  for term in parts:
   fs=[]
   for x in term:
    fs.append(aN[ABC.index(x)]if x in ABC else("NA"if x=="N"else x))
   aO.append(" * ".join(fs))
  if len(parts)==2 and len(parts[1])>1:
   aO[1]="("+aO[1]+")"
  sides.append(" / ".join(aO))
 return" = ".join(sides)
''',globals())
 _gc.collect()
 exec('''def aP(aF,aQ,aN,aR=0):
 aS=[]
 for aT in aF.split():
  if aT in("+","-","*","/","^"):
   b=aS.pop()
   a=aS.pop()
   if aR:
    p=1 if aT in("+","-")else(3 if aT=="^"else 2)
    sa=a[0]
    sb=b[0]
    if a[1]<p or(aT=="^"and a[1]==p):
     sa="("+sa+")"
    if b[1]<p or(aT in("-","/","^")and b[1]==p):
     sb="("+sb+")"
    aS.append((sa+" "+aT+" "+sb,p))
   else:
    if aT=="+":
     x=a+b
    elif aT=="-":
     x=a-b
    elif aT=="*":
     x=a*b
    elif aT=="/":
     x=a/b
    else:
     x=a**b
    aS.append(x)
  elif aT in("ln","lg","neg","exp","sqrt"):
   a=aS.pop()
   if aR:
    if aT=="neg":
     aU="-"
    else:
     aU="log10"if aT=="lg"else aT
    aS.append((aU+"("+a[0]+")",4))
   else:
    if aT=="ln":
     x=log(a)
    elif aT=="lg":
     x=log10(a)
    elif aT=="exp":
     x=exp(a)
    elif aT=="sqrt":
     x=sqrt(a)
    else:
     x=-a
    aS.append(x)
  else:
   if aT in ABC and len(aT)==1:
    i=ABC.index(aT)
    x=aQ[i][0]
    label=aN[i]
   else:
    x=ab[aT]if aT in ab else float(aT)
    label="NA"if aT=="N"else aT
   if aR==2:
    label=approx(x)
    if x<0:
     label="("+label+")"
   aS.append((label,4)if aR else x)
 return aS[0][0]if aR else aS[0]
''',globals())
 _gc.collect()
 exec('''def solve(tool):
 aV,labels,units,eq,note=tool
 aN=labels.split()
 aW=units.split()
 while True:
  i=aX(aV,aN,aW,eq,note)
  if i<0:
   return
  aQ=collection("Enter knowns",aN,aW,i)
  if aQ is None:
   continue
  aF=law_rpn(eq,ABC[i])if isinstance(eq,str)else eq[i+1]
  aY=None
  try:
   x=aP(aF,aQ,aN)
   if aV=="Formula multiplier"and i==0 and value(x)and.97<=x<=10000.03:
    aY=x
    x=int(x+.5)
    aZ=check(x,aW[i])
    if abs(aY-x)>.03:
     aZ="Mass ratio is not close to a whole number."
   else:
    aZ=check(x,aW[i])
  except(ZeroDivisionError,ValueError,OverflowError,TypeError):
   aZ="No unique real answer. Check for zero divisors or invalid input."
  if aZ:
   page("Check your values")
   notice(aZ)
   continue
  if aW[i][0]=="#":
   x=int(x+.5)
  ix=pickunit("Answer unit",aN[i],aW[i])
  if ix<0:
   continue
  f=aN[i]+" = "+aP(aF,aQ,aN,1)
  sub=aN[i]+" = "+aP(aF,aQ,aN,2)
  ba=wrapped("1. "+aM(eq,aN))+wrapped("2. "+f)
  ba+=wrapped("3. "+sub)
  if aY is not None and aY!=x:
   ba+=wrapped("Raw mass ratio: "+approx(aY))
  label=aG(aW[i])
  ba+=wrapped("4. "+aN[i]+" = "+approx(x)+" "+label)
  ba+=["","Knowns in formula units:"]
  for j in range(len(aN)):
   if j!=i:
    y,ah,at=aQ[j]
    txt=aN[j]+" = "+approx(y)+" "+aG(aW[j])
    if at:
     txt+=" from "+approx(ah)+" "+aG(aW[j],at)
    ba+=wrapped(txt)
  bb=gas_points(aV,aQ,i,x)
  if not answer(aN[i],aW[i],x,ix,f,ba,bb):
   return
''',globals())
 _gc.collect()
 exec('''def dalton():
 page("Dalton: add pressures")
 print("How many gases? (2-6)")
 print("Blank Enter = Back")
 n=bc("Gases: ",2,6)
 if n is None:
  return
 aN=["Ptotal"]+["P"+str(j)for j in range(1,n+1)]
 allparts=" + ".join(aN[1:])
 f=["Ptotal = "+allparts]
 for j in range(n+1):
  if j==0:
   s="b"
   for k in range(2,n+1):
    s+=" "+ABC[k]+" +"
  else:
   s="a"
   for k in range(1,n+1):
    if j!=k:
     s+=" "+ABC[k]+" -"
  f.append(s)
 solve(("Dalton: add pressures"," ".join(aN),"!p "+"+p "*n,f,
  "Total pressure equals the sum of the partial pressures. The tool can also solve for one missing partial pressure."))
''',globals())
 _gc.collect()
 exec('''def convert():
 bd=(
  ("Temperature","t"),("Temperature change","d"),("Volume","v"),
  ("Pressure","p"),("Mass","m"),("Amount","n"),("Energy","q"),
  ("Molar energy","h"),("Molarity","c"),("Time","z"),("Length","l"),
  ("Density","D"),("Molar mass","w"),("Voltage","V")
  )
 at=0
 while True:
  i=be("Unit conversions",[a[0]for a in bd],at)
  if i<0:
   return
  at=i
  aU,aE=bd[i]
  if aE not in"dtqhV":
   aE="+"+aE
  while True:
   d=field("Convert / input",aU,aE)
   if d is None:
    break
   x,ah,i=d
   to=pickunit("Convert / output",aU,aE)
   if to<0:
    continue
   ba=wrapped("Input = "+approx(ah)+" "+aG(aE,i))
   ba+=wrapped("Base = "+approx(x)+" "+aG(aE))
   if not answer(aU,aE,x,to,"",ba):
    break
''',globals())
 _gc.collect()
 exec('''def bf():
 global aa
 aN=("Round to sig figs","Round decimal places","Count sig figs",
  "Scientific notation","Convert units","Rounding guide","Tie rounding rule")
 while True:
  i=be("Sig figs and units",aN)
  if i<0:
   return
  if i<4:
   bg(i)
  elif i==4:
   convert()
  elif i==6:
   page("Tie rounding rule")
   print("Now: "+("even"if aa else"away from zero"))
   print("1 Half away from zero")
   print("2 Half to even")
   print("0 Keep current")
   s=select(("0","1","2"))
   if s!="0":
    aa=s=="2"
  else:
   pages("Rounding / guide",wrapped(
    "Enter a decimal or scientific notation such as 2.50e-3. "
    "Enter requested digits. Exact ties round away from zero by default. "
    "Use Tie rounding rule for half to even, if your class uses it. "
    "1200 counts as 2 sig figs; 1200. and 1.200e3 count as 4. "
    "For multiply/divide, use the fewest sig figs. For add/subtract, use the fewest decimal places. "
    "Keep guard digits until the final result. For log problems, use your class\'s log precision rule."))
bh=print
bi=input
try:
 import ti_draw as dr
 import ti_graphics as gr
 import ti_system as sy
 bj=True
except ImportError:
 bj=False
BG=(8,17,29)
HEAD=(13,27,43)
PANEL=(19,35,53)
ACTIVE=(29,54,75)
bk=(49,74,99)
''',globals())
 _gc.collect()
 exec('''WHITE=(240,247,252)
MUTED=(166,188,207)
DIM=(117,148,176)
INK=(7,23,33)
RED=(255,133,132)
bl=((92,234,205),(249,192,112),(120,190,255),
 (255,143,128),(184,157,253),(248,218,113),
 (128,222,151),(113,218,252))
ACC=bl[0]
UP,DOWN,LEFT,RIGHT,ENTER,CLEAR,DELETE,SECOND=25,34,24,26,105,45,23,21
NUM={102:"0",92:"1",93:"2",94:"3",82:"4",83:"5",84:"6",72:"7",73:"8",74:"9"}
INPUT_CHARS={103:".",104:"-",75:"-",85:"+",25:"e"}
bm=""
bn=[]
FONT=-1
TOPICS=("Gas laws","Moles & reactions","Solutions & pH","Heat & energy",
 "Rates & equilibrium","Light & electrochem","Sig figs & units","Periodic table")
TILES=("Gas laws","Reactions","Solutions","Heat","Rates","Light & e-","Sig figs","Elements")
SUB=("P / V / n / T","Moles & yields","pH & molarity","Energy & entropy",
 "Kinetics & K","Photons & cells","Round & convert","118 element cards")
def bo(c):
 dr.set_color(c[0],c[1],c[2])
def rect(x,y,w,h,c):
 bo(c)
 dr.fill_rect(x-1,y-1,w+1,h+1)
def ad(x,y,x2,y2,c):
 bo(c)
 dr.draw_line(x,y,x2,y2)
def dot(x,y,r,c):
 bo(c)
 dr.fill_circle(x,y,r)
def width(s,f=0):
 return gr.string_size(s,f)[0]if s else 0
''',globals())
 _gc.collect()
 exec('''def text(x,y,s,c=WHITE,f=0,align=0):
 global FONT
 if not s:
  return
 if align:
  w=width(s,f)
  x-=w//2 if align==1 else w
 if f!=FONT:
  gr.setFont(f)
  FONT=f
 bo(c)
 dr.draw_text(x,y+(14,18,21)[f],s)
def fit(s,w,f=0):
 if width(s,f)<=w:
  return s
 while s and width(s+"...",f)>w:
  s=s[:-1]
 return s+"..."
def bp(s,w,f=0):
 ans=[]
 bq=""
 for ae in s.split():
  test=bq+" "+ae if bq else ae
  if width(test,f)>w and bq:
   ans.append(bq)
   bq=""
  while width(ae,f)>w:
   k=len(ae)-1
   while width(ae[:k],f)>w:
    k-=1
   ans.append(ae[:k])
   ae=ae[k:]
  bq=bq+" "+ae if bq else ae
 ans.append(bq)
 return ans
def label(x,y,s,c=WHITE,f=0,w=290,align=0):
 text(x,y,fit(s,w,f),c,f,align)
def footer(aJ,aK=""):
 rect(0,187,320,23,HEAD)
 rect(0,187,320,1,bk)
 label(11,192,aJ,MUTED,w=195 if aK else 294)
 if aK:
  label(309,192,aK,ACC,w=106,align=2)
def frame(tag,aV,badge=""):
 rect(0,0,320,210,BG)
 rect(0,0,320,49,HEAD)
 rect(0,48,320,1,bk)
 rect(0,0,3,49,ACC)
 label(12,5,tag.upper(),ACC,w=280)
 label(12,23,aV,WHITE,1,295)
 if badge:
  label(307,5,badge,MUTED,w=98,align=2)
def chip(x,y,w,s,br=False):
 rect(x,y,w,21,ACC if br else PANEL)
 label(x+w//2,y+3,s,INK if br else WHITE,w=w-8,align=1)
''',globals())
 _gc.collect()
 exec('''def barsteps(a,b):
 for i in range(b):
  rect(220+i*11,12,8,3,ACC if i<a else bk)
''',globals())
 _gc.collect()
 exec('''def pick(tag,aV,bs,at=0,bt="",bu=False,hot=None):
 if not bs:
  return-1
 p=min(max(at,0),len(bs)-1)
 bv=4 if bt else 5
 bw=min(max(0,p-bv+1),max(0,len(bs)-bv))
 while True:
  frame(tag,aV,str(p+1)+" / "+str(len(bs)))
  y0=56
  if bt:
   rect(10,55,299,31,PANEL)
   for j,s in enumerate(bp(bt,282)[:2]):
    label(17,56+j*13,s,MUTED,w=282)
   y0=91
  for j in range(bw,min(bw+bv,len(bs))):
   y=y0+(j-bw)*23
   on=j==p
   rect(11,y,289,21,ACTIVE if on else PANEL)
   if on:
    rect(11,y,3,21,ACC)
   if hot is None:
    glyph=str(j+1)if j<9 else">"
   else:
    glyph=hot[j]
   label(23,y+3,glyph,ACC if on else DIM,w=20,align=1)
   label(37,y+2,bs[j],WHITE if on else MUTED,1,250)
  if len(bs)>bv:
   span=23*bv-2
   bx=max(10,span*bv//len(bs))
   offset=(span-bx)*bw//(len(bs)-bv)
   rect(306,y0,3,span,PANEL)
   rect(306,y0+offset,3,bx,ACC)
  footer("UP/DOWN Move   ENTER Open","2ND Guide"if bu else"CLEAR Back")
  k=sy.wait_key()
  if k==CLEAR or(hot is None and NUM.get(k)=="0"):
   return-1
  if k==SECOND and bu:
   return-2
  if k==ENTER:
   return p
  if k in NUM:
   ap=NUM[k]
   if hot is not None:
    for j in range(len(hot)):
     if hot[j]==ap:
      return j
   elif int(ap)<=len(bs):
    return int(ap)-1
  elif k in(UP,DOWN,LEFT,RIGHT):
   step={UP:-1,DOWN:1,LEFT:-bv,RIGHT:bv}[k]
   p=min(max(p+step,0),len(bs)-1)
   if p<bw:
    bw=p
   if p>=bw+bv:
    bw=p-bv+1
''',globals())
 _gc.collect()
 exec('''def page(aV):
 global bm,bn
 bm,bn=aV,[]
def print(s=""):
 bn.append(str(s))
def show(s):
 bn.append(str(s))
def select(valid,by="Pick: "):
 bz=[]
 bA=[]
 bB=[]
 for s in bn:
  for bit in s.split("   "):
   if len(bit)>2 and bit[1]==" "and bit[0]in valid:
    if bit[0]not in("0","8"):
     bz.append(bit[0])
     bA.append(bit[2:])
   elif bit:
    bB.append(bit)
 if bA:
  i=pick("Tool settings",bm,bA,bt=" / ".join(bB),
   bu="8"in valid,hot=bz)
  return"0"if i==-1 else("8"if i==-2 else bz[i])
 return"0"
def pages(aV,ac):
 bA=[]
 for s in ac:
  bA+=bp(s,282)
 if not bA:
  bA=[""]
 bC=(len(bA)+6)//7
 i=0
 while True:
  frame("Reference"if aV!="Worked solution"else"Calculation trace",aV,
   str(i+1)+" / "+str(bC))
  rect(10,55,300,125,PANEL)
  for j,s in enumerate(bA[7*i:7*i+7]):
   label(19,59+j*16,s,ACC if s[:2]in("1.","2.","3.","4.")else WHITE,w=283)
  footer("ARROWS Page   ENTER Next","CLEAR Back")
  k=sy.wait_key()
  if k==CLEAR or(k==ENTER and i==bC-1):
   return
  if k in(LEFT,UP)and i:
   i-=1
  if k in(RIGHT,DOWN,ENTER)and i<bC-1:
   i+=1
''',globals())
 _gc.collect()
 exec('''def notice(bD):
 frame("Needs attention",bm or"Check your values")
 rect(10,62,300,100,PANEL)
 rect(10,62,3,100,RED)
 for j,s in enumerate(bp(bD,276)[:5]):
  label(22,70+j*16,s,WHITE,w=276)
 footer("ENTER Continue","CLEAR Back")
 while sy.wait_key()not in(ENTER,CLEAR):
  pass
def be(aV,aN,at=0):
 return pick("Tools",aV,aN,at)
def aX(aV,aN,aW,eq,note):
 f=aM(eq,aN)
 bd=[]
 for i in range(len(aN)):
  u=aG(aW[i])
  bd.append(aN[i]+("  ["+u+"]"if u else""))
 while True:
  i=pick("Solve for an unknown",aV,bd,bt=f,bu=True)
  if i!=-2:
   return i
  info=["Formula:"]+wrapped(f)+[""]+wrapped(note)+[""]
  for j in range(len(aN)):
   if aG(aW[j]):
    info.append(aN[j]+": "+aG(aW[j]))
  pages("Equation guide",info)
def bE(aE):
 return U[aD(aE)[1]][0].split(" ")
def pickunit(aV,aU,aE,ix=0):
 bF=bE(aE)
 if len(bF)==1:
  return 0
 if aD(aE)[1]=="t":
  bF=("K  Kelvin","C  Celsius","F  Fahrenheit")
 elif aD(aE)[1]=="d":
  bF=("C  Celsius change","K  Kelvin change","F  Fahrenheit change")
 return pick("Unit selector",aV,bF,ix,bt=aU)
''',globals())
 _gc.collect()
 exec('''def bG(bH,aU,bB,u,ak,bD):
 frame(bH,aU)
 if ak:
  barsteps(ak[0],ak[1])
  label(307,51,str(ak[0])+" of "+str(ak[1]),ACC,w=80,align=2)
 label(12,53,bB,MUTED,w=197 if ak else 290)
 rect(11,72,298,43,PANEL)
 rect(11,113,298,2,ACC)
 if u:
  label(13,124,"INPUT UNIT",DIM,w=112)
  label(13,140,u,WHITE,1,138)
 if bD:
  rect(10,160,300,22,PANEL)
  label(17,163,bD,RED,w=286)
 else:
  label(12,163,"LEFT/RIGHT Edit   DEL Delete   UP: exponent (e)",MUTED,w=292)
 footer("ENTER Confirm"+("   DOWN Unit"if u else""),"CLEAR Back")
''',globals())
 _gc.collect()
 exec('''def bI(bH,aU,bB,aE="",ix=0,bJ="",ak=None,bD=""):
 s=bJ
 aq=len(s)
 bK=aE and len(bE(aE))>1
 bG(bH,aU,bB,aG(aE,ix)if bK else"",ak,bD)
 while True:
  rect(15,78,289,31,PANEL)
  start=max(0,aq-19)
  bL=s[start:start+22]
  label(21,84,bL or"Type a value",WHITE if bL else DIM,1,273)
  rect(21+10*(aq-start),106,9,2,ACC)
  k=sy.wait_key()
  if k==ENTER:
   return(s,ix)
  if k==CLEAR:
   return("",ix)
  if k==DOWN and bK:
   j=pickunit("Input unit",aU,aE,ix)
   if j>=0:
    ix=j
   bG(bH,aU,bB,aG(aE,ix),ak,bD)
  elif k==LEFT:
   aq=max(0,aq-1)
  elif k==RIGHT:
   aq=min(len(s),aq+1)
  elif k==DELETE and aq:
   s=s[:aq-1]+s[aq:]
   aq-=1
  elif k in NUM or k in INPUT_CHARS:
   if len(s)<68:
    ch=NUM[k]if k in NUM else INPUT_CHARS[k]
    s=s[:aq]+ch+s[aq:]
    aq+=1
''',globals())
 _gc.collect()
 exec('''def field(bH,aU,aE,bM="",bN=None):
 bD=""
 ah=bN[3]if bN else""
 ix=bN[2]if bN else 0
 bB="Enter the known value"
 if len(bE(aE))==1 and aG(aE):
  bB+=" ["+aG(aE)+"]"
 while True:
  ah,ix=bI(bH,aU,bB,aE,ix,ah,bM,bD)
  if not ah:
   return None
  try:
   p=af(ah)
   x=float(ah)
   if not value(x)or(x==0 and p[1]):
    raise ValueError()
   y=scale(x,aE,ix)
   bD=check(y,aE)
   if not bD:
    if aE[0]=="#":
     y=int(y+.5)
    return(y,x,ix,ah)if bM else(y,x,ix)
  except(ValueError,OverflowError):
   bD="Try a number such as -3.2 or 2.5e-3."
def collection(aV,aN,aW,skip=-1):
 ids=[i for i in range(len(aN))if i!=skip]
 aQ=[None]*len(aN)
 cache=[None]*len(aN)
 aq=0
 while aq<len(ids):
  i=ids[aq]
  got=field(aV,aN[i],aW[i],(aq+1,len(ids)),cache[i])
  if got is None:
   if not aq:
    return None
   aq-=1
  else:
   cache[i]=got
   aQ[i]=got[:3]
   aq+=1
 return aQ
def bc(by,low,high):
 bF=[str(x)for x in range(low,high+1)]
 bO="Choose "+str(low)+" to "+str(high)
 if low==0 and bm=="Round the answer":
  bF[0]="0  Normal display"
  bO="0 restores normal display"
 i=pick("Number settings",bm or by.strip(),bF,bt=bO,
  hot=[str(x)if x<10 else">"for x in range(low,high+1)])
 return None if i<0 else low+i
''',globals())
 _gc.collect()
 exec('''def input(by=""):
 if"Formula"in by:
  sy.disp_clr()
  bh("EASY CHEM LAB / FORMULA")
  bh("Try Ca(OH)2 or CuSO4.5H2O.")
  bh("Case matters. Blank = Back.")
  return bi(by)
 ah,_=bI("Number entry",bm or by.strip(),by.strip())
 return ah
def report(aV,ac,ba):
 while True:
  frame("Complete",aV)
  rect(10,56,300,78,PANEL)
  rect(10,56,3,78,ACC)
  j=0
  for s in ac:
   for q in bp(s,284):
    label(20,61+j*16,q,ACC if not j else WHITE,w=284)
    j+=1
  chip(12,153,139,"1  Again")
  chip(161,153,147,"2  Work",True)
  footer("1 Again   2 Work","CLEAR Back")
  k=sy.wait_key()
  if k==CLEAR:
   return False
  if NUM.get(k)=="1":
   return True
  if NUM.get(k)=="2"or k==ENTER:
   pages("Worked solution",ba)
def gas_points(aV,aQ,missing,x):
 if aV.startswith("Charles"):
  ax,ay,inv="T (K)","V (L)",False
 elif aV.startswith("Boyle"):
  ax,ay,inv="V (L)","P (atm)",True
 elif aV.startswith("Gay-Lussac"):
  ax,ay,inv="T (K)","P (atm)",False
 else:
  return None
 vals=[x if i==missing else aQ[i][0]for i in(2,0,3,1)]
 return(aV.split(":")[0],ax,ay,tuple(vals[:2]),tuple(vals[2:]),inv)
''',globals())
 _gc.collect()
 exec('''def plot_gas(bb):
 aV,ax,ay,a,b,inv=bb
 mx,my=max(a[0],b[0]),max(a[1],b[1])
 aJ,aK,bP,top=48,291,143,65
 w,h=aK-aJ,bP-top
 a0,a1=.86*(a[0]/mx),.86*(a[1]/my)
 b0,b1=.86*(b[0]/mx),.86*(b[1]/my)
 while True:
  frame("Model plot / two states",aV,"IDEAL GAS")
  rect(10,53,300,107,PANEL)
  for i in range(1,5):
   y=bP-i*h//4
   xx=aJ+i*w//4
   ad(aJ,y,aK,y,bk)
   ad(xx,top,xx,bP,bk)
  ad(aJ,top,aJ,bP,DIM)
  ad(aJ,bP,aK,bP,DIM)
  label(15,57,ay,MUTED,w=50)
  label(291,143,ax,MUTED,w=62,align=2)
  label(aJ-4,134,"0",DIM,w=12,align=2)
  if inv:
   k=a0*a1 if a0>=b0 else b0*b1
   prev=None
   for j in range(1,49):
    xn=j/48
    yn=k/xn
    if yn<=1:
     pt=(aJ+int(xn*w),bP-int(yn*h))
     if prev:
      ad(prev[0],prev[1],pt[0],pt[1],ACC)
     prev=pt
  else:
   rx,ry=(a0,a1)if a0>=b0 else(b0,b1)
   if ry:
    endx=min(1,rx/ry)
    endy=(endx/rx)*ry
    ad(aJ,bP,aJ+int(endx*w),bP-min(h,int(endy*h)),ACC)
  dot(aJ+int(a0*w),bP-int(a1*h),5,bl[1])
  dot(aJ+int(b0*w),bP-int(b1*h),3,bl[2])
  dot(20,173,4,bl[1])
  label(31,165,"1  Initial",WHITE,w=104)
  dot(144,173,4,bl[2])
  label(155,165,"2  Final",WHITE,w=130)
  footer("ENTER State values","CLEAR Back")
  k=sy.wait_key()
  if k==CLEAR:
   return
  if k==ENTER:
   pages("State values",["State 1",ax+" = "+approx(a[0]),ay+" = "+approx(a[1]),"",
    "State 2",ax+" = "+approx(b[0]),ay+" = "+approx(b[1])])
''',globals())
 _gc.collect()
 exec('''def answer(aU,aE,x,ix,bQ,ba,bb=None):
 sf=0
 at=1
 bz=["1","2","3"]
 bR=["New","Work","Round"]
 if len(bE(aE))>1:
  bz.append("4")
  bR.append("Units")
 if bb:
  bz.append("5")
  bR.append("Plot")
 while True:
  frame("Result / solved",aU,str(sf)+" SIG FIGS"if sf else"NORMAL")
  u=aG(aE,ix)
  try:
   y=scale(x,aE,ix,True)
   ap="Out of range"
   if value(y):
    p=af("{:.8e}".format(y))
    ap=aw(p,sf)if sf else approx(y)
  except(ValueError,OverflowError):
   ap="Out of range"
  rect(10,56,300,54,PANEL)
  rect(10,56,3,54,ACC)
  label(21,60,"ANSWER",MUTED,w=120)
  label(21,78,ap,ACC,2,267)
  if u:
   label(298,61,u,WHITE,w=128,align=2)
  if bQ:
   for j,s in enumerate(bp(bQ,284)[:2]):
    label(18,114+j*14,s,WHITE,w=284)
  else:
   label(18,120,"Open Work for the calculation.",MUTED,w=284)
  w=296//len(bz)
  for i in range(len(bz)):
   chip(12+i*w,151,w-4,bz[i]+" "+bR[i],i==at)
  footer("ARROWS Select   ENTER Open","CLEAR Back")
  k=sy.wait_key()
  c=bz[at]if k==ENTER else NUM.get(k,"")
  if k==CLEAR or c=="0":
   return False
  if k in(LEFT,RIGHT):
   at=(at+(-1 if k==LEFT else 1))%len(bz)
  if c=="1":
   return True
  if c=="2":
   pages("Worked solution",ba)
  if c=="3":
   page("Round the answer")
   n=bc("Digits",0,7)
   if n is not None:
    sf=n
  if c=="4"and"4"in bz:
   br=pickunit("Answer unit",aU,aE,ix)
   if br>=0:
    ix=br
  if c=="5"and bb:
   plot_gas(bb)
''',globals())
 _gc.collect()
 exec('''def bg(aR):
 aV=("Round to sig figs","Round decimal places","Count sig figs","Scientific notation")[aR]
 ah=""
 bD=""
 while True:
  ah,_=bI("Numbers / precision",aV,"Enter a decimal or use UP for e",bJ=ah,bD=bD)
  if not ah:
   return
  try:
   p=af(ah)
  except ValueError:
   bD="Try -1.245 or 2.5e-3."
   continue
  bD=""
  if aR==2:
   ap=str(p[3])if p[1]else"Zero"
   bS="Significant figures in your entry."if p[1]else"Zero: decimal places show precision."
  else:
   low,high=(0,12)if aR==1 else(1,15)
   page("Decimal places"if aR==1 else"Significant figures")
   n=bc("Digits",low,high)
   if n is None:
    continue
   ap=aB(p,n)if aR==1 else aw(p,n,aR==3)
   bS=str(n)+(" decimal places"if aR==1 else" significant figures")
   if aR==1 and"e"in ap:
    bS="Scientific display (fixed was too long)."
  frame("Precision / result",aV)
  rect(10,60,300,77,PANEL)
  rect(10,60,3,77,ACC)
  label(20,63,bS,MUTED,w=280)
  if width(ap,2)<=280:
   label(20,87,ap,ACC,2,280)
  else:
   for i,q in enumerate(bp(ap,277)):
    label(20,85+i*12,q,ACC,w=279)
  label(13,150,"Tie rule: "+("Half to even"if aa else"Half away from zero"),WHITE,w=290)
  footer("ENTER Edit number","CLEAR Back")
  k=sy.wait_key()
  while k not in(ENTER,CLEAR):
   k=sy.wait_key()
  if k==CLEAR:
   return
''',globals())
 _gc.collect()
 exec('''def bT(i,bU):
 x=11+(i%2)*151
 y=52+(i//2)*33
 c=bl[i]
 rect(x,y,146,30,ACTIVE if bU else PANEL)
 if bU:
  rect(x,y,146,1,c)
  rect(x,y+29,146,1,c)
 rect(x+6,y+6,19,18,c if bU else BG)
 label(x+15,y+7,str(i+1),INK if bU else c,w=17,align=1)
 label(x+30,y,TILES[i],WHITE,1,112)
 label(x+30,y+15,SUB[i],MUTED,w=111)
def bV():
 ad(272,17,295,12,bk)
 ad(272,17,281,33,bk)
 ad(295,12,303,29,bk)
 ad(281,33,303,29,bk)
 dot(272,17,4,bl[0])
 dot(281,33,5,bl[3])
 dot(295,12,3,bl[2])
 dot(303,29,4,bl[1])
def help_lab():
 pages("Quick start",[
  "HOME: Use arrows or press a tile number.",
  "LISTS: UP/DOWN moves one item. LEFT/RIGHT jumps a page. ENTER opens.",
  "SOLVE: Choose the missing value. 2ND opens its equation guide.",
  "ENTRY: Type digits. DOWN changes units. UP inserts e, as in 2.5e-3.",
  "LEFT/RIGHT moves the cursor. DEL deletes. CLEAR goes back.",
  "RESULT: Use Work to see the algebra. Units and Round change display only.",
  "PLOT: Charles, Boyle and Gay-Lussac show the two gas states.",
  "ELEMENTS: Move on the grid and press ENTER for the element profile.",
  "To quit the app, press CLEAR from the home screen."
  ])
import gc
import sys
''',globals())
 _gc.collect()
 exec('''def unload(aU):
 try:
  del sys.modules[aU]
 except(AttributeError,KeyError,TypeError):
  pass
 gc.collect()
def bW(i):
 aU="CHEMREF"if i==7 else"CHEMBOOK"
 gc.collect()
 try:
  if i==7:
   import CHEMREF
   CHEMREF.open_table(globals())
  else:
   import CHEMBOOK
   CHEMBOOK.open_topic(i-1,TOPICS[i],globals())
 except ImportError:
  page("Optional add-on")
  notice("Send "+aU+".py to enable this tile. Gas laws and Sig figs work without it.")
 except MemoryError:
  gc.collect()
  page("Low Python memory")
  notice("Restart the Python App and remove old copies only after backing them up.")
 unload(aU)
def gas_menu():
 at=0
 titles=[item[0]for item in GAS]
 while True:
  j=pick("Equation library","Gas laws",titles,at)
  if j<0:
   return
  at=j
  if GAS[j][0]=="Dalton: add pressures":
   dalton()
  else:
   solve(GAS[j])
''',globals())
 _gc.collect()
 exec('''def launch():
 global ACC
 if not bj:
  bh("Easy Chem Lab needs TI-84 Evo graphics.")
  return
 sz=dr.get_screen_dim()
 if sz[0]<319 or sz[1]<209:
  bh("Easy Chem Lab needs the Evo canvas.")
  return
 dr.set_window()
 p=0
 old=-1
 while True:
  ACC=bl[0]
  if old<0:
   frame("EVO / LOW-MEMORY EDITION","Easy Chem Lab")
   bV()
   for i in range(8):
    bT(i,i==p)
   footer("ARROWS Move   ENTER Open","2ND Help")
  elif old!=p:
   bT(old,False)
   bT(p,True)
  k=sy.wait_key()
  old=p
  if k==CLEAR or NUM.get(k)=="0":
   gr.setFont(1)
   sy.disp_clr()
   return
  if k==SECOND:
   help_lab()
   old=-1
  if k in(UP,DOWN):
   p=(p+(2 if k==DOWN else-2))%8
  if k in(LEFT,RIGHT):
   p=p+1 if p%2==0 else p-1
  if k==ENTER or(k in NUM and"1"<=NUM[k]<="8"):
   if k!=ENTER:
    p=int(NUM[k])-1
   ACC=bl[p]
   gc.collect()
   try:
    if p==0:
     gas_menu()
    elif p==6:
     bf()
    else:
     bW(p)
   except MemoryError:
    gc.collect()
    page("Low Python memory")
    notice("Quit and reopen Python. Back up and remove unused copies if needed.")
   gc.collect()
   old=-1
''',globals())
 _gc.collect()
 launch()
except MemoryError:
 _console('Low Python memory. Back up old programs and restart Python.')
