

SCHR="/opt/schrodinger2018-2/"

MACCS_EXPLANATION = "A : Any valid periodic table element symbol\n \
Q : Hetro atoms; any non-C or non-H atom\n \
X : Halogens; F, Cl, Br, I\n \
Z : Others; other than H, C, N, O, Si, P, S, F, Cl, Br, I\n \
"

MACCS_VOC = {
1: "ISOTOPE",
2: "103 < ATOMIC NO. < 256",
3: "GROUP IVA,VA,VIA PERIODS 4-6 (Ge...)",
4: "ACTINIDE",
5: "GROUP IIIB,IVB (Sc...)",
6: "LANTHANIDE",
7: "GROUP VB,VIB,VIIB (V...)",
8: "QAAA@1",
9: "GROUP VIII (Fe...)",
10: "GROUP IIA (ALKALINE EARTH)",
11: "4M RING",
12: "GROUP IB,IIB (Cu...)",
13: "ON(C)C",
14: "S-S",
15: "OC(O)O",
16: "QAA@1",
17: "CTC",
18: "GROUP IIIA (B...)",
19: "7M RING",
20: "SI",
21: "C=C(Q)Q",
22: "3M RING",
23: "NC(O)O",
24: "N-O",
25: "NC(N)N",
26: "C$=C($A)$A",
27: "I",
28: "QCH2Q",
29: "P",
30: "CQ(C)(C)A",
31: "QX",
32: "CSN",
33: "NS",
34: "CH2=A",
35: "GROUP IA (ALKALI METAL)",
36: "S HETEROCYCLE",
37: "NC(O)N",
38: "NC(C)N",
39: "OS(O)O",
40: "S-O",
41: "CTN",
42: "F",
43: "QHAQH",
44: "OTHER",
45: "C=CN",
46: "BR",
47: "SAN",
48: "OQ(O)O",
49: "CHARGE",
50: "C=C(C)C",
51: "CSO",
52: "NN",
53: "QHAAAQH",
54: "QHAAQH",
55: "OSO",
56: "ON(O)C",
57: "O HETEROCYCLE",
58: "QSQ",
59: "Snot%A%A",
60: "S=O",
61: "AS(A)A",
62: "A$A!A$A",
63: "N=O",
64: "A$A!S",
65: "C%N",
66: "CC(C)(C)A",
67: "QS",
68: "QHQH (&...)",
69: "QQH",
70: "QNQ",
71: "NO",
72: "OAAO",
73: "S=A",
74: "CH3ACH3",
75: "A!N$A",
76: "C=C(A)A",
77: "NAN",
78: "C=N",
79: "NAAN",
80: "NAAAN",
81: "SA(A)A",
82: "ACH2QH",
83: "QAAAA@1",
84: "NH2",
85: "CN(C)C",
86: "CH2QCH2",
87: "X!A$A",
88: "S",
89: "OAAAO",
90: "QHAACH2A",
91: "QHAAACH2A",
92: "OC(N)C",
93: "QCH3",
94: "QN",
95: "NAAO",
96: "5M RING",
97: "NAAAO",
98: "QAAAAA@1",
99: "C=C",
100: "ACH2N",
101: "8M RING",
102: "QO",
103: "CL",
104: "QHACH2A",
105: "A$A($A)$A",
106: "QA(Q)Q",
107: "XA(A)A",
108: "CH3AAACH2A",
109: "ACH2O",
110: "NCO",
111: "NACH2A",
112: "AA(A)(A)A",
113: "Onot%A%A",
114: "CH3CH2A",
115: "CH3ACH2A",
116: "CH3AACH2A",
117: "NAO",
118: "ACH2CH2A > 1",
119: "N=A",
120: "HETEROCYCLIC ATOM > 1 (&...)",
121: "N HETEROCYCLE",
122: "AN(A)A",
123: "OCO",
124: "QQ",
125: "AROMATIC RING > 1",
126: "A!O!A",
127: "A$A!O > 1 (&...)",
128: "ACH2AAACH2A",
129: "ACH2AACH2A",
130: "QQ > 1 (&...)",
131: "QH > 1",
132: "OACH2A",
133: "A$A!N",
134: "X (HALOGEN)",
135: "Nnot%A%A",
136: "O=A > 1",
137: "HETEROCYCLE",
138: "QCH2A > 1 (&...)",
139: "OH",
140: "O > 3 (&...)",
141: "CH3 > 2 (&...)",
142: "N > 1",
143: "A$A!O",
144: "Anot%A%Anot%A",
145: "6M RING > 1",
146: "O > 2",
147: "ACH2CH2A",
148: "AQ(A)A",
149: "CH3 > 1",
150: "A!A$A!A",
151: "NH",
152: "OC(C)C",
153: "QCH2A",
154: "C=O",
155: "A!CH2!A",
156: "NA(A)A",
157: "C-O",
158: "C-N",
159: "O > 1",
160: "CH3",
161: "N",
162: "AROMATIC",
163: "6M RING",
164: "O",
165: "RING",
166: "FRAGMENTS"
}