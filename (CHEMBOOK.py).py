# Easy Chem Lab | Low-memory TI-84 Evo build
import gc as _gc
exec('''MOLES=(
 ("Mass and moles","mass n MM","+m +n !w","a=bc",
 "Enter sample mass, amount in moles or molar mass MM. Use Molar mass formula if needed."),
 ("Moles and particles","N n","+X +n","a=bN",
 "N is number of specified entities (atoms, molecules, ions or formula units). NA is Avogadro\'s constant."),
 ("Density","density mass V","!D !m !v","a=b/Uc",
 "Density uses g/mL internally; U = 1000 mL/L. Enter mass and the volume of the same sample."),
 ("Mole ratio","nA nB coefA coefB","+n +n #0 #0","a/c=b/d",
 "A and B are two substances. Use their whole-number coefficients from a balanced reaction."),
 ("Grams to grams","massA massB MMA MMB coefA coefB","+m +m !w !w #0 #0",
 "a/ce=b/df",
 "Use a balanced equation. MM is molar mass. Assumes complete reaction; use Limiting reactant if both reactant amounts are given."),
 ("Limiting reactant","","","",""),
 ("Percent yield","yield% actual theory","+% +m !m","a=Pb/c",
 "Actual and theoretical yields must describe the same product. Values over 100% are possible for impure or wet product."),
 ("Mass composition","% part total","@% +m !m","a=Pb/c",
 "Part is the mass of the element or component. Total is the mass of the entire compound or sample."),
 ("Molar mass formula","","","",""),
 ("Formula multiplier","factor molecular empirical","#0 !w !w","a=b/c",
 "Factor multiplies every empirical-formula subscript. Checks that the mass ratio is within 0.03 of a whole number.")
 )
''',globals())
_gc.collect()
exec('''SOLN=(
 ("Molarity","M n V","+c +n !v","a=b/c",
 "Use moles of solute and TOTAL solution volume, not solvent volume."),
 ("Dilution","M1 M2 V1 V2","!c !c !v !v","ac=bd",
 "Solute amount stays constant. 1 is stock; 2 is final solution. V2 is final volume, NOT solvent added."),
 ("Titration","MA MB VA VB coefA coefB","!c !c !v !v #0 #0","ac/e=bd/f",
 "At equivalence, moles divided by coefficients are equal. Use the balanced reaction, not M1V1 = M2V2 unless the ratio is 1:1."),
 ("pH and H3O+","pH H3O+","0 !c",("pH = -log10(H3O+)","b lg neg","10 a neg ^"),
 "Enter hydronium concentration (mol/L in the formula). This classroom calculation uses concentration in place of activity."),
 ("pOH and OH-","pOH OH-","0 !c",("pOH = -log10(OH-)","b lg neg","10 a neg ^"),
 "Enter hydroxide concentration (mol/L in the formula)."),
 ("pH + pOH = 14","pH pOH","0 0",("pH + pOH = 14","14 b -","14 a -"),
 "For water at 25 C. At other temperatures use the actual pKw in pH + pOH = pKw."),
 ("Buffer pH","pH pKa base acid","0 0 !c !c",
 ("pH = pKa + log10(base/acid)","b c d / lg +","a c d / lg -",
 "d 10 a b - ^ *","c 10 a b - ^ /"),
 "Henderson-Hasselbalch: base and acid are a conjugate pair. Use amounts AFTER any neutralization, as molarity."),
 ("Molality","b n solvent","+b +n !m","a=Ub/c",
 "b is mol/kg, n is moles of solute, solvent is mass of SOLVENT only. U = 1000 g/kg."),
 ("Mole fraction","X nPart nTotal","&0 +n !n","a=b/c",
 "Use moles of the component divided by total moles of all components."),
 ("Mass percent","% solute solution","@% +m !m","a=Pb/c",
 "Use mass of solute and total mass of solution."),
 ("Volume percent","% solute solution","@% +v !v","a=Pb/c",
 "Use solute volume and final solution volume (not a sum of separate volumes unless stated)."),
 ("Mass ppm / ppb","ppm solute solution","+P +m !m","a=Mb/c",
 "Mass ratio, not mg/L. M = 1000000 for ppm. Can enter or display ppb."),
 ("Ka, Kb and Kw","Ka Kb Kw","!0 !0 !0","ab=c",
 "Ka and Kb must be for a conjugate acid-base pair. Enter Kw for your temperature (1e-14 at 25 C)."),
 ("pKa and Ka","pKa Ka","0 !0",("pKa = -log10(Ka)","b lg neg","10 a neg ^"),
 "Also works for pKb and Kb: use the same relationship with the base constant."),
 ("Weak acid (1 proton)","","","",""),
 ("Mass/volume percent","% solute solution","+% +m !v","a=b/Wc",
 "Grams of solute per 100 mL of total solution. W = 10 for converting solution volume from L to units of 100 mL."),
 ("pH + pOH = pKw","pH pOH pKw","0 0 0",
 ("pH + pOH = pKw","c b -","c a -","a b +"),
 "Use pKw for your temperature. If given Kw, use pKw = -log10(Kw). At 25 C, pKw is about 14."),
 )
''',globals())
_gc.collect()
exec('''HEAT=(
 ("Heat: q = mc*dT","q mass c dT","q !m !j d","a=bcd",
 "No phase change. c is specific heat. dT is final minus initial. Heating q > 0; cooling q < 0."),
 ("Change in temperature","dT Tfinal Tstart","d t t",("dT = Tfinal - Tstart","b c -","a c +","b a -"),
 "Enter absolute start/end temperatures. dT is a change, so do not add 273.15 to it."),
 ("Heat capacity","q C dT","q !C d","a=bc",
 "C is heat capacity of the entire sample or calorimeter, not specific heat per gram."),
 ("Phase change / mol","q n dH","q +n h","a=bc",
 "No temperature change during the phase step. Enter signed molar enthalpy for the direction: melting +, freezing -."),
 ("Gibbs free energy","dG dH T dS","h h !t s",
 ("dG = dH - T * dS","b c d * -","a c d * +","b a - d /","b a - c /"),
 "Use values for the same reaction basis. Entropy is normalized to J/mol/K; energies to J/mol."),
 ("Entropy: qrev / T","dS qrev T","s h !t","a=b/c",
 "Reversible isothermal heat per mole divided by kelvin temperature. Keep the same molar basis."),
 ("First law: dU = q+w","dU q w","q q q",("dU = q + w","b c +","a c -","a b -"),
 "Use the chemistry sign convention: q positive into the system, w positive for work ON the system."),
 ("Pressure-volume work","work Pext dV","q !p v",
 ("work = -101.325*Pext*dV","101.325 neg b * c *","a 101.325 c * neg /","a 101.325 b * neg /"),
 "Constant external pressure only. dV is Vfinal - Vinitial. Uses 101.325 J per L*atm."),
 ("Bond energy estimate","dH broken formed","h +h +h",
 ("dH = broken - formed","b c -","a c +","b a -"),
 "Enter the sums of bond energies for bonds broken and formed per mole of reaction. Gas-phase estimate.")
 )
''',globals())
_gc.collect()
exec('''RATE=(
 ("Zero-order rate","At A0 k time","+c !c +0 +z",
 ("At = A0 - k * time","b c d * -","a c d * +","b a - d /","b a - c /"),
 "One reactant, zero order. Concentrations in mol/L, k in mol/L/s. Use only before or at depletion."),
 ("First-order rate","At A0 k time","!c !c +0 +z",
 ("ln(At/A0) = -k * time","b c d * neg exp *","a c d * exp *",
 "b a / ln d /","b a / ln c /"),
 "One reactant, first order. Concentrations in mol/L, k in 1/s."),
 ("Second-order rate","At A0 k time","!c !c +0 +z",
 ("1/At = 1/A0 + k * time","1 1 b / c d * + /","1 1 a / c d * - /",
 "1 a / 1 b / - d /","1 a / 1 b / - c /"),
 "One reactant with rate k[A]^2. Concentrations in mol/L, k in L/mol/s."),
 ("Half-life: 1st order","tHalf k","!z !0","ab=L",
 "First-order process, including basic radioactive decay. Enter k in 1/s. L = ln(2)."),
 ("Half-life: 0 order","tHalf A0 k","!z !c !0","a= b/Tc",
 "Zero order. Use initial A0 in mol/L and k in mol/L/s. T is the factor 2."),
 ("Half-life: 2nd order","tHalf A0 k","!z !c !0","abc=I",
 "Second order with rate k[A]^2. A0 is in mol/L, k in L/mol/s. I is the number 1."),
 ("Arrhenius","k A Ea T","!0 !0 h !t",
 ("k = A * exp(-Ea/(RJ*T))","b c RJ d * / neg exp *","a c RJ d * / exp *",
 "b a / ln RJ d * *","c RJ b a / ln * /"),
 "k and pre-factor A use the same units. Ea is activation energy. RJ = 8.314462618 J/mol/K."),
 ("Kp and Kc","Kp Kc T dnGas","!0 !0 !t 0",
 ("Kp = Kc * (R*T)^dnGas","b R c * d ^ *","a R c * d ^ /",
 "a b / 1 d / ^ R /","a b / ln R c * ln /"),
 "dnGas is gaseous product coefficients minus gaseous reactant coefficients. Use classroom atm and mol/L convention."),
 ("Gibbs and equilibrium","dG0 K T","h !0 !t",
 ("dG0 = -RJ * T * ln(K)","RJ c * b ln * neg","a RJ c * / neg exp","a RJ b ln * / neg"),
 "Standard Gibbs free energy and equilibrium constant K, at the same temperature. Use natural log."),
 ("Compare Q and K","","","",""),
 ("Ksp and solubility","","","","")
 )
''',globals())
_gc.collect()
exec('''MORE=(
 ("Light: wavelength/freq","wave freq","!l !f","ab=S",
 "For light in vacuum. S = 299792458 m/s. Wavelength and frequency are inversely proportional."),
 ("Photon energy","E freq","!q !f","a=Hb",
 "Use energy per photon, not energy per mole. H is Planck\'s constant in J*s."),
 ("Photon E/wavelength","E wave","!q !l","ab=HS",
 "For light in vacuum. Energy is per photon. H is Planck\'s constant; S is the speed of light."),
 ("Beer-Lambert","Abs eps path conc","+0 !L !B +c","a=bcd",
 "Abs is absorbance. eps is molar absorptivity in L/mol/cm, path is cuvette path length and conc is molarity."),
 ("Cell voltage","Ecell Ecath Ean","V V V",("Ecell = Ecath - Ean","b c -","a c +","b a -"),
 "Enter both half-cell values as reduction potentials. Do NOT multiply the potentials by coefficients."),
 ("Cell free energy","dG n E","h #0 V",
 ("dG = -n * F * E","b F * c * neg","a F c * / neg","a F b * / neg"),
 "n is electrons transferred in the balanced reaction. F is Faraday\'s constant in C/mol. Consistent standard/nonstandard states."),
 ("Nernst equation","E E0 n T Q","V V #0 !t !0",
 ("E = E0 - RJ*T*ln(Q)/(n*F)","b RJ d * e ln * c F * / -",
 "a RJ d * e ln * c F * / +","RJ d * e ln * b a - F * /",
 "b a - c F * * RJ e ln * /","b a - c F * * RJ d * / exp"),
 "Q is reaction quotient, n is electrons transferred, E0 is standard cell potential. Uses natural log and kelvin."),
 ("Electric charge","Q current time","+Q +I +z","a=bc",
 "Q is charge, current in amperes and time in seconds in the formula. Use magnitudes."),
 ("Electrons from charge","Q nElec","+Q +n","a=Fb",
 "Q is charge magnitude, nElec is moles of electrons. F is 96485.33212 C/mol.")
 )
''',globals())
_gc.collect()
exec('''def limiting():
 while True:
  page("Limiting reactant")
  print("Two reactants, one product")
  print("1 Given reactant moles")
  print("2 Given reactant masses")
  print("8 Guide   0 Back")
  s=select(("0","1","2","8"))
  if s=="0":
   return
  if s=="8":
   pages("Limiting / guide",wrapped(
    "Use a balanced equation. A and B are reactants; P is your product. "
    "Enter the three whole-number coefficients. In mass mode also enter their molar masses. "
    "The smaller moles/coefficient ratio determines the product. Assumes complete reaction."))
   continue
  names=["molA","molB","coefA","coefB","coefP"]
  kinds=["+n","+n","#0","#0","#0"]
  if s=="2":
   names=["massA","massB"]+names[2:]+["MMA","MMB","MMP"]
   kinds=["+m","+m"]+kinds[2:]+["!w","!w","!w"]
  data=collection("Limiting / knowns",names,kinds)
  if data is None:
   continue
  d=[x[0]for x in data]
  a=d[0]if s=="1"else d[0]/d[5]
  b=d[1]if s=="1"else d[1]/d[6]
  ra=a/d[2]
  rb=b/d[3]
  prod=min(ra,rb)*d[4]
  g=prod*d[7]if s=="2"else 0
  if not value(prod)or not value(g):
   page("Check your values")
   notice("Result out of range.")
   continue
  who="A"if ra<rb else"B"
  if abs(ra-rb)<=1e-7*max(ra,rb):
   who="A and B (tie)"
  aa=["Limiting: "+who,"Product: "+approx(prod)+" mol"]
  ab=wrapped("molA = "+approx(a)+", molB = "+approx(b))
  if s=="2":
   ab=["mol = mass / molar mass"]+ab
   aa+=["Product: "+approx(g)+" g"]
  ab+=wrapped("molA / coefA = "+approx(ra))
  ab+=wrapped("molB / coefB = "+approx(rb))
  ab+=wrapped("molP = min(ratios) * coefP")
  if s=="2":
   ab+=wrapped("massP = molP * MMP")
  if not report("Limiting / answer",aa,ab):
   return
''',globals())
_gc.collect()
exec('''def q_vs_k():
 while True:
  page("Compare Q and K")
  print("Q = reaction quotient")
  print("K = equilibrium constant")
  print("Use the same convention.")
  print("1 Enter Q and K   0 Back")
  if select(("0","1"))=="0":
   return
  d=collection("Equilibrium / knowns",["Q","K"],["+0","!0"])
  if d is None:
   continue
  q,k=[a[0]for a in d]
  if q<k:
   rule="Q < K"
   ac="Net shift: toward products"
  elif q>k:
   rule="Q > K"
   ac="Net shift: toward reactants"
  else:
   rule="Q = K"
   ac="At equilibrium"
  ab=["Q = "+approx(q),"K = "+approx(k)]
  ab+=wrapped("Compare the reaction quotient with the equilibrium constant at the same temperature.")
  if not report("Equilibrium / answer",[rule,ac],ab):
   return
''',globals())
_gc.collect()
exec('''def ad():
 while True:
  page("Weak acid / monoprotic")
  print("HA in water, no added salt")
  print("Input Ka and initial [HA].")
  print("1 Calculate pH   0 Back")
  if select(("0","1"))=="0":
   return
  d=collection("Weak acid / knowns",["Ka","Initial [HA]"],["!0","!c"])
  if d is None:
   continue
  ka,c=[a[0]for a in d]
  try:
   x=c/(.5+sqrt(.25+c/ka))
   ph=-log10(x)
   pct=100*(x/c)
  except(ValueError,OverflowError,ZeroDivisionError):
   page("Check your values")
   notice("Result out of range.")
   continue
  ab=wrapped("Ka = x^2 / (C0 - x)")+wrapped("x = C0 / (0.5 + sqrt(0.25 + C0 / Ka))")
  ab+=wrapped("pH = -log10(x). Ion% = 100 * x / C0. Ignores water\'s own ionization; avoid near neutral or very dilute solutions.")
  aa=["pH = "+approx(ph),"[H3O+] = "+approx(x)+" mol/L","Ionized = "+approx(pct)+"%"]
  if x<1e-6:
   aa.append("Caution: near water pH")
  if not report("Weak acid / answer",aa,ab):
   return
''',globals())
_gc.collect()
exec('''def ksp():
 while True:
  page("Ksp and solubility")
  print("Pure water; two ions.")
  print("Solid -> a A + b B")
  print("1 Find molar solubility")
  print("2 Find Ksp")
  print("8 Guide   0 Back")
  s=select(("0","1","2","8"))
  if s=="0":
   return
  if s=="8":
   pages("Ksp / guide",wrapped(
    "Use a and b from the balanced dissolution. Example: CaF2 gives a=1 and b=2. "
    "Use s in mol/L. No preexisting common ions, pH effects or complex formation."))
   continue
  d=collection("Ksp / knowns",["a","b","Ksp"if s=="1"else"Solubility s"],
   ["#0","#0","!0"if s=="1"else"!c"])
  if d is None:
   continue
  a,b,x=[i[0]for i in d]
  name="Solubility"if s=="1"else"Ksp"
  kind="!c"if s=="1"else"!0"
  f="ln(s) = (ln(Ksp) - a*ln(a) - b*ln(b)) / (a + b)"if s=="1"else"Ksp = (a*s)^a * (b*s)^b"
  try:
   if s=="1":
    y=exp((log(x)-a*log(a)-b*log(b))/(a+b))
   else:
    y=exp(a*(log(a)+log(x))+b*(log(b)+log(x)))
  except(ValueError,OverflowError):
   y=0
  if not value(y)or y<=0:
   page("Check your values")
   notice("Result out of range.")
   continue
  ix=pickunit("Answer unit",name,kind)
  if ix<0:
   continue
  ab=wrapped("Ksp = (a*s)^a * (b*s)^b")+wrapped(f)
  ab+=wrapped("a = "+approx(a)+", b = "+approx(b))
  ab+=wrapped(("Ksp = "if s=="1"else"s (mol/L) = ")+approx(x))
  if not answer(name,kind,y,ix,f,ab):
   return
''',globals())
_gc.collect()
exec('''def atom_weights():
 ac=(
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
 ae={}
 for pair in ac.split():
  af,mass=pair.split(":")
  ae[af]=0 if mass=="-"else float(mass)
 return ae
''',globals())
_gc.collect()
exec('''def ag(s,i):
 j=i
 while j<len(s)and s[j]in DIG:
  j+=1
 if i==j:
  return 1,j
 if j-i>4 or s[i]=="0":
  raise ValueError("Use subscripts 1-9999.")
 return int(s[i:j]),j
def ah(dest,src,ai):
 for af in src:
  dest[af]=dest.get(af,0)+src[af]*ai
  if dest[af]>1000000:
   raise ValueError("Atom count too large.")
''',globals())
_gc.collect()
exec('''def aj(ac,ak):
 ac=ac.strip()
 if not ac or len(ac)>54:
  raise ValueError("Use 1-54 characters.")
 ae={}
 parts=ac.split(".")
 for al in range(len(parts)):
  s=parts[al]
  m,i=ag(s,0)
  if(not al and i)or i==len(s):
   raise ValueError("Use a formula, e.g. H2O.")
  am=[{}]
  an=[]
  while i<len(s):
   c=s[i]
   if c in"([":
    am.append({})
    an.append(c)
    i+=1
   elif c in")]":
    if not an or not am[-1]or an[-1]!=("("if c==")"else"["):
     raise ValueError("Check group brackets.")
    an.pop()
    g=am.pop()
    factor,i=ag(s,i+1)
    ah(am[-1],g,factor)
   elif"A"<=c<="Z":
    sym=c
    i+=1
    if i<len(s)and"a"<=s[i]<="z":
     sym+=s[i]
     i+=1
    if sym not in ak:
     raise ValueError("Unknown element: "+sym)
    if not ak[sym]:
     raise ValueError("No standard weight for "+sym+". Use an isotope mass.")
    n,i=ag(s,i)
    ah(am[-1],{sym:n},1)
   else:
    raise ValueError("Check case and formula.")
  if an or not am[0]:
   raise ValueError("Check group brackets.")
  ah(ae,am[0],m)
 return ae
''',globals())
_gc.collect()
exec('''def ao():
 ak=atom_weights()
 while True:
  page("Molar mass / formula")
  print("Use correct letter case.")
  print("Try H2O or Ca(OH)2")
  print("Hydrates: CuSO4.5H2O")
  print("Blank Enter = Back")
  txt=input("Formula: ").strip()
  if not txt:
   return
  try:
   atoms=aj(txt,ak)
  except ValueError as e:
   notice(str(e))
   continue
  total=0
  ab=["Mass = sum(count * weight)"]
  for af in sorted(atoms):
   amt=atoms[af]*ak[af]
   total+=amt
   ab+=wrapped(af+": "+str(atoms[af])+" * "+
    approx(ak[af])+" = "+approx(amt))
  ab+=wrapped("Total = "+approx(total)+" g/mol")
  if not answer("Molar mass","!w",total,0,"",ab):
   return
ap=\'page print select pages wrapped collection value approx report notice log log10 sqrt exp pickunit answer input solve pick DIG\'
aq={"Limiting reactant":limiting,"Molar mass formula":ao,
 "Weak acid (1 proton)":ad,"Compare Q and K":q_vs_k,
 "Ksp and solubility":ksp}
def open_topic(i,title,api):
 for k in ap.split():
  globals()[k]=api[k]
 group=(MOLES,SOLN,HEAT,RATE,MORE)[i]
 titles=[tool[0]for tool in group]
 at=0
 while True:
  j=pick("Equation library",title,titles,at)
  if j<0:
   return
  at=j
  item=group[j]
  if item[0]in aq:
   aq[item[0]]()
  else:
   solve(item)
''',globals())
_gc.collect()
