import pandas as pd
import matplotlib.pyplot as plt
import io

# --- 1. Corrected Data String (The source data) ---
# NOTE: This multi-line string structure is essential for pandas to read the data correctly.
data_string = """id,role,company,location,salary_lpa,experience
1,Data Analyst,Company 26,Bengaluru,22.1,1-2 yrs
2,Web Developer,Company 31,Bengaluru,14.5,1-2 yrs
3,Backend Developer,Company 7,Bengaluru,22.1,2-4 yrs
4,Web Developer,Company 48,Remote,4.1,2-4 yrs
5,Software Engineer,Company 14,Mumbai,7.7,Fresher
6,Backend Developer,Company 31,Remote,10.8,1-2 yrs
7,ML Engineer,Company 41,Mumbai,12.9,1-2 yrs
8,Data Analyst,Company 48,Hyderabad,15.0,4-6 yrs
9,Backend Developer,Company 3,Hyderabad,14.5,1-2 yrs
10,Backend Developer,Company 32,Mumbai,19.7,4-6 yrs
11,Web Developer,Company 38,Chennai,18.2,2-4 yrs
12,Software Engineer,Company 6,Chennai,22.7,2-4 yrs
13,Web Developer,Company 32,Remote,6.3,2-4 yrs
14,Web Developer,Company 23,Bengaluru,10.7,Fresher
15,Backend Developer,Company 18,Chennai,9.5,1-2 yrs
16,ML Engineer,Company 6,Remote,23.9,2-4 yrs
17,Software Engineer,Company 28,Chennai,8.4,2-4 yrs
18,Backend Developer,Company 7,Remote,20.6,4-6 yrs
19,Backend Developer,Company 13,Bengaluru,21.2,4-6 yrs
20,Backend Developer,Company 18,Remote,5.9,4-6 yrs
21,Backend Developer,Company 44,Remote,23.6,2-4 yrs
22,Web Developer,Company 16,Hyderabad,18.6,4-6 yrs
23,Backend Developer,Company 24,Hyderabad,21.2,2-4 yrs
24,Web Developer,Company 29,Remote,18.2,4-6 yrs
25,Backend Developer,Company 2,Chennai,23.9,2-4 yrs
26,Data Analyst,Company 36,Chennai,13.6,Fresher
27,Backend Developer,Company 5,Remote,7.1,Fresher
28,Web Developer,Company 45,Bengaluru,11.7,1-2 yrs
29,Web Developer,Company 13,Chennai,21.3,2-4 yrs
30,Software Engineer,Company 41,Chennai,13.1,4-6 yrs
31,Backend Developer,Company 15,Chennai,10.0,4-6 yrs
32,Data Analyst,Company 25,Chennai,3.4,1-2 yrs
33,Software Engineer,Company 3,Hyderabad,10.4,Fresher
34,Software Engineer,Company 29,Remote,11.8,1-2 yrs
35,Backend Developer,Company 21,Hyderabad,15.2,2-4 yrs
36,Web Developer,Company 14,Remote,24.0,2-4 yrs
37,Web Developer,Company 34,Remote,18.7,2-4 yrs
38,Backend Developer,Company 11,Hyderabad,6.3,1-2 yrs
39,Backend Developer,Company 3,Mumbai,16.9,Fresher
40,Backend Developer,Company 41,Hyderabad,12.3,Fresher
41,Web Developer,Company 6,Chennai,20.1,4-6 yrs
42,Software Engineer,Company 5,Bengaluru,22.4,4-6 yrs
43,Software Engineer,Company 18,Hyderabad,14.7,Fresher
44,Backend Developer,Company 10,Mumbai,16.8,Fresher
45,Web Developer,Company 48,Remote,3.2,4-6 yrs
46,Software Engineer,Company 40,Mumbai,23.2,Fresher
47,Data Analyst,Company 36,Chennai,15.8,2-4 yrs
48,Software Engineer,Company 8,Chennai,16.2,2-4 yrs
49,Data Analyst,Company 12,Mumbai,15.8,4-6 yrs
50,Data Analyst,Company 26,Hyderabad,15.8,2-4 yrs
51,ML Engineer,Company 33,Bengaluru,14.5,2-4 yrs
52,Web Developer,Company 1,Hyderabad,4.2,4-6 yrs
53,Web Developer,Company 44,Hyderabad,9.4,2-4 yrs
54,ML Engineer,Company 2,Chennai,24.2,2-4 yrs
55,Software Engineer,Company 9,Chennai,24.2,Fresher
56,Backend Developer,Company 15,Chennai,11.0,2-4 yrs
57,Web Developer,Company 48,Remote,16.0,1-2 yrs
58,ML Engineer,Company 11,Chennai,12.6,4-6 yrs
59,Software Engineer,Company 5,Hyderabad,11.7,2-4 yrs
60,Web Developer,Company 13,Chennai,11.7,1-2 yrs
61,Backend Developer,Company 14,Chennai,5.6,2-4 yrs
62,Software Engineer,Company 19,Bengaluru,11.8,2-4 yrs
63,ML Engineer,Company 11,Mumbai,14.6,2-4 yrs
64,Web Developer,Company 37,Remote,24.8,Fresher
65,Web Developer,Company 32,Hyderabad,18.9,Fresher
66,ML Engineer,Company 3,Bengaluru,9.4,Fresher
67,Software Engineer,Company 41,Mumbai,23.2,Fresher
68,ML Engineer,Company 19,Hyderabad,21.0,1-2 yrs
69,Web Developer,Company 13,Remote,18.4,Fresher
70,Backend Developer,Company 13,Hyderabad,24.6,Fresher
71,ML Engineer,Company 2,Chennai,14.7,1-2 yrs
72,Web Developer,Company 39,Chennai,22.7,2-4 yrs
73,Data Analyst,Company 13,Mumbai,11.7,2-4 yrs
74,ML Engineer,Company 25,Chennai,17.7,Fresher
75,Backend Developer,Company 33,Remote,23.1,2-4 yrs
76,Backend Developer,Company 21,Chennai,19.0,4-6 yrs
77,Software Engineer,Company 18,Mumbai,11.2,4-6 yrs
78,Web Developer,Company 31,Mumbai,21.6,1-2 yrs
79,Backend Developer,Company 12,Mumbai,15.9,2-4 yrs
80,Software Engineer,Company 7,Remote,16.6,1-2 yrs
81,Software Engineer,Company 29,Mumbai,13.7,2-4 yrs
82,Software Engineer,Company 31,Mumbai,10.6,1-2 yrs
83,Web Developer,Company 19,Mumbai,13.3,1-2 yrs
84,Web Developer,Company 26,Bengaluru,11.9,2-4 yrs
85,Web Developer,Company 41,Mumbai,12.3,4-6 yrs
86,Data Analyst,Company 33,Remote,6.7,2-4 yrs
87,Software Engineer,Company 23,Remote,7.7,2-4 yrs
88,ML Engineer,Company 22,Hyderabad,10.7,1-2 yrs
89,Web Developer,Company 48,Chennai,17.6,2-4 yrs
90,ML Engineer,Company 48,Mumbai,6.2,Fresher
91,ML Engineer,Company 46,Hyderabad,21.1,4-6 yrs
92,ML Engineer,Company 38,Mumbai,7.5,1-2 yrs
93,Software Engineer,Company 7,Remote,20.2,4-6 yrs
94,ML Engineer,Company 5,Chennai,3.8,2-4 yrs
95,Web Developer,Company 27,Hyderabad,9.6,Fresher
96,ML Engineer,Company 24,Hyderabad,4.6,4-6 yrs
97,Web Developer,Company 15,Bengaluru,18.3,4-6 yrs
98,Data Analyst,Company 17,Bengaluru,11.1,1-2 yrs
99,Data Analyst,Company 32,Hyderabad,15.2,1-2 yrs
100,Backend Developer,Company 4,Remote,24.1,4-6 yrs
101,ML Engineer,Company 40,Remote,22.5,1-2 yrs
102,Backend Developer,Company 14,Bengaluru,14.1,Fresher
103,Web Developer,Company 23,Mumbai,4.3,4-6 yrs
104,Web Developer,Company 27,Remote,5.5,1-2 yrs
105,Data Analyst,Company 14,Hyderabad,12.1,1-2 yrs
106,Backend Developer,Company 41,Bengaluru,9.9,2-4 yrs
107,Web Developer,Company 20,Remote,4.2,4-6 yrs
108,ML Engineer,Company 47,Remote,9.6,Fresher
109,Data Analyst,Company 47,Remote,24.5,2-4 yrs
110,Backend Developer,Company 37,Remote,5.4,1-2 yrs
111,Software Engineer,Company 28,Bengaluru,21.2,1-2 yrs
112,Data Analyst,Company 7,Remote,4.7,2-4 yrs
113,Backend Developer,Company 20,Chennai,22.3,4-6 yrs
114,Software Engineer,Company 20,Hyderabad,3.0,1-2 yrs
115,Backend Developer,Company 4,Mumbai,15.4,1-2 yrs
116,ML Engineer,Company 17,Chennai,11.4,1-2 yrs
117,Data Analyst,Company 6,Bengaluru,6.0,Fresher
118,Backend Developer,Company 15,Hyderabad,23.3,2-4 yrs
119,ML Engineer,Company 4,Bengaluru,18.4,Fresher
120,Backend Developer,Company 49,Mumbai,8.6,1-2 yrs
121,Software Engineer,Company 19,Hyderabad,16.3,2-4 yrs
122,Backend Developer,Company 18,Mumbai,10.8,2-4 yrs
123,Backend Developer,Company 23,Remote,9.9,1-2 yrs
124,Software Engineer,Company 44,Chennai,4.9,Fresher
125,Backend Developer,Company 37,Bengaluru,23.8,2-4 yrs
126,ML Engineer,Company 20,Bengaluru,3.4,1-2 yrs
127,Backend Developer,Company 45,Chennai,14.9,1-2 yrs
128,Backend Developer,Company 49,Hyderabad,12.0,1-2 yrs
129,Software Engineer,Company 41,Remote,9.4,Fresher
130,Backend Developer,Company 50,Mumbai,10.7,1-2 yrs
131,Data Analyst,Company 23,Hyderabad,12.4,Fresher
132,Data Analyst,Company 41,Mumbai,20.5,Fresher
133,Web Developer,Company 26,Bengaluru,5.6,Fresher
134,Web Developer,Company 15,Chennai,6.5,1-2 yrs
135,Data Analyst,Company 48,Hyderabad,20.3,2-4 yrs
136,Data Analyst,Company 1,Bengaluru,9.9,1-2 yrs
137,Data Analyst,Company 24,Bengaluru,19.3,Fresher
138,Software Engineer,Company 7,Chennai,13.0,Fresher
139,ML Engineer,Company 5,Mumbai,19.6,2-4 yrs
140,Backend Developer,Company 36,Bengaluru,6.3,2-4 yrs
141,Software Engineer,Company 17,Remote,14.6,Fresher
142,Software Engineer,Company 42,Remote,16.0,1-2 yrs
143,Backend Developer,Company 49,Remote,15.0,Fresher
144,Web Developer,Company 6,Hyderabad,23.5,Fresher
145,Data Analyst,Company 40,Bengaluru,3.6,Fresher
146,Software Engineer,Company 4,Mumbai,6.3,4-6 yrs
147,Backend Developer,Company 16,Hyderabad,15.4,2-4 yrs
148,Data Analyst,Company 38,Bengaluru,14.8,Fresher
149,Data Analyst,Company 14,Chennai,11.5,4-6 yrs
150,Data Analyst,Company 33,Remote,24.9,1-2 yrs
151,ML Engineer,Company 43,Chennai,6.9,2-4 yrs
152,Backend Developer,Company 49,Chennai,4.0,4-6 yrs
153,Software Engineer,Company 4,Hyderabad,20.1,2-4 yrs
154,Software Engineer,Company 30,Remote,12.0,1-2 yrs
155,Data Analyst,Company 5,Remote,20.9,4-6 yrs
156,Web Developer,Company 12,Remote,16.4,4-6 yrs
157,ML Engineer,Company 14,Remote,20.1,Fresher
158,Software Engineer,Company 20,Bengaluru,18.6,4-6 yrs
159,Software Engineer,Company 13,Chennai,18.2,1-2 yrs
160,Web Developer,Company 28,Remote,6.1,1-2 yrs
161,ML Engineer,Company 39,Bengaluru,24.8,Fresher
162,Backend Developer,Company 6,Hyderabad,9.3,1-2 yrs
163,Data Analyst,Company 43,Hyderabad,8.9,4-6 yrs
164,Software Engineer,Company 38,Remote,12.6,2-4 yrs
165,Data Analyst,Company 25,Remote,11.0,4-6 yrs
166,Software Engineer,Company 25,Remote,5.1,4-6 yrs
167,ML Engineer,Company 2,Mumbai,16.7,4-6 yrs
168,ML Engineer,Company 29,Mumbai,9.8,4-6 yrs
169,ML Engineer,Company 1,Bengaluru,18.4,Fresher
170,ML Engineer,Company 13,Hyderabad,10.3,Fresher
171,ML Engineer,Company 37,Remote,13.6,Fresher
172,Web Developer,Company 34,Hyderabad,15.7,Fresher
173,Software Engineer,Company 40,Hyderabad,3.2,4-6 yrs
174,Backend Developer,Company 24,Hyderabad,19.2,2-4 yrs
175,Software Engineer,Company 3,Chennai,23.7,2-4 yrs
176,ML Engineer,Company 42,Hyderabad,15.2,2-4 yrs
177,Software Engineer,Company 19,Hyderabad,18.9,4-6 yrs
178,Data Analyst,Company 8,Mumbai,9.9,4-6 yrs
179,Backend Developer,Company 35,Remote,21.2,4-6 yrs
180,Backend Developer,Company 27,Remote,18.4,4-6 yrs
181,Data Analyst,Company 11,Remote,24.8,Fresher
182,Backend Developer,Company 41,Bengaluru,19.1,2-4 yrs
183,Backend Developer,Company 17,Remote,16.5,Fresher
184,Data Analyst,Company 14,Chennai,16.8,4-6 yrs
185,ML Engineer,Company 38,Hyderabad,6.9,Fresher
186,Software Engineer,Company 31,Bengaluru,6.7,Fresher
187,Software Engineer,Company 10,Chennai,16.4,1-2 yrs
188,Web Developer,Company 42,Chennai,7.7,4-6 yrs
189,ML Engineer,Company 9,Mumbai,20.4,2-4 yrs
190,Data Analyst,Company 29,Bengaluru,15.0,4-6 yrs
191,Data Analyst,Company 18,Bengaluru,3.7,2-4 yrs
192,Web Developer,Company 43,Bengaluru,13.9,1-2 yrs
193,Backend Developer,Company 13,Mumbai,18.4,1-2 yrs
194,Software Engineer,Company 48,Remote,24.9,1-2 yrs
195,ML Engineer,Company 33,Mumbai,10.2,4-6 yrs
196,Backend Developer,Company 44,Bengaluru,9.3,4-6 yrs
197,Data Analyst,Company 40,Chennai,22.3,2-4 yrs
198,Data Analyst,Company 11,Hyderabad,3.3,1-2 yrs
199,Data Analyst,Company 23,Bengaluru,22.7,Fresher
200,Software Engineer,Company 49,Bengaluru,6.9,2-4 yrs
"""

# -----------------------------
# 2. DataFrame Creation and Cleaning
# -----------------------------
# Read the string data into the DataFrame
df = pd.read_csv(io.StringIO(data_string))

# Convert 'salary_lpa' to numeric (float)
df['salary_lpa'] = pd.to_numeric(df['salary_lpa'], errors='coerce')

# Convert 'id' to integer type
df['id'] = df['id'].astype(int)

# Set categorical order for experience (used in Box Plot)
exp_order = ['Fresher', '1-2 yrs', '2-4 yrs', '4-6 yrs']
df['experience'] = pd.Categorical(df['experience'], categories=exp_order, ordered=True)
df.sort_values('experience', inplace=True)


# -----------------------------
# 3. Data Preparation for Plotting
# -----------------------------

# Average salary by role for Bar Chart
avg_salary_by_role = df.groupby('role')['salary_lpa'].mean().sort_values(ascending=False)

# Overall salary distribution for Histogram
salary_distribution = df['salary_lpa']

# -----------------------------
# 4. Plotting Commands (CORRECTED TO USE EXISTING COLUMNS)
# -----------------------------

# Plot 1: Average Salary by Role (Bar Chart)
plt.figure(figsize=(10, 6))
avg_salary_by_role.plot(kind='bar', color='skyblue')
plt.title("Average Salary (LPA) by Job Role", fontsize=14)
plt.xlabel("Job Role", fontsize=12)
plt.ylabel("Average Salary (LPA)", fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show() # Use plt.show() to display the plot

# Plot 2: Salary Distribution by Experience Level (Box Plot)
# 
plt.figure(figsize=(12, 6))
df.boxplot(column='salary_lpa', by='experience', grid=True, rot=45)
plt.title("Salary (LPA) Distribution by Experience Level", fontsize=14)
plt.suptitle('') # Suppress automatic suptitle
plt.xlabel("Experience Level", fontsize=12)
plt.ylabel("Salary (LPA)", fontsize=12)
plt.tight_layout()
plt.show()

# Plot 3: Salary Distribution (Histogram)
# 
plt.figure(figsize=(8, 5))
salary_distribution.plot(kind='hist', bins=10, edgecolor='black', color='lightcoral')
plt.title("Distribution of Salaries (LPA)", fontsize=14)
plt.xlabel("Salary (LPA)", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
