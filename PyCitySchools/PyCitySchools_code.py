# Code for Pandas Challenge

# Dependencies and Setup
import pandas as pd

# File to Load
sch_data = "Resources/schools_complete.csv"
stu_data = "Resources/students_complete.csv"

# Read School and Student Data File and store into Pandas Data Frames
sch_df = pd.read_csv(sch_data)
stu_df = pd.read_csv(stu_data)


# Combine the data into a single dataset
sch_stu_merged = pd.merge(stu_df, sch_df, how="left", on=["school_name", "school_name"])
sch_stu_merged.head

renamed_sch_stu_merged_df = sch_stu_merged.rename(columns={"school_name":"School Name", "student_name":"Student Name", 
                                                           "reading_score":"Reading Score", "math_score":"Math Score",
                                                          "budget":"Budget", "type":"Type", "size":"Size", "grade":"Grade",
                                                          "gender":"Gender",})

# stu_df

renamed_sch_stu_merged_df["School Name"].unique()

Tot_Schs = len(renamed_sch_stu_merged_df["School Name"].unique())
Tot_Stus = len(renamed_sch_stu_merged_df["Student ID"].unique())
Tot_Bud = float((sch_df["budget"]).sum())
# Calculate the average math score
# Calculate the average reading score
AveReadScor = (renamed_sch_stu_merged_df["Reading Score"].mean())
AveMathScor = (renamed_sch_stu_merged_df["Math Score"].mean())

# print(Tot_Schs, Tot_Stus,Tot_Bud, AveMathScor, AveReadScor)
"""15 39170 24649428.0 78.98537145774827 81.87784018381414"""

# print(AveMathScor,AveReadScor)
"""78.98537145774827 81.87784018381414"""

# Calculate the overall passing rate (overall average score), i.e. (avg. math score + avg. reading score)/2
Tot_Pass_rt = (AveReadScor + AveMathScor)/2
Tot_Pass_rt

# Calculate the percentage of students with a passing math score (70 or greater)

MathPass = len(renamed_sch_stu_merged_df.loc[renamed_sch_stu_merged_df["Math Score"] >= 70]["Student ID"])
MathPass

PerMathPass = (MathPass/Tot_Stus)
PerMathPass

# Calculate the percentage of students with a passing reading score (70 or greater)
ReadPass = len(renamed_sch_stu_merged_df.loc[renamed_sch_stu_merged_df["Reading Score"] >= 70]["Student ID"])
ReadPass

PerReadPass = (ReadPass/Tot_Stus)
PerReadPass


# print(Tot_Pass_rt, MathPass, PerMathPass, ReadPass, PerReadPass)
'''80.43160582078121   29370   0.749808526933878   33610   0.8580546336482001'''

# Create a dataframe to hold the above results

Dist_Sum = pd.DataFrame([
    {"Total Schools": Tot_Schs, "Total Students": Tot_Stus, "Total Budget": Tot_Bud, "Ave. Match Score": AveMathScor, 
     "Ave. Reading Score": AveReadScor, "% Passing Math": PerMathPass, "% Passing Reading": PerReadPass, 
     "% Overall Passing Rate": Tot_Pass_rt}
])

Dist_Sum  # Output for District Summary


# ====================================================================================

'''# Goup by School Name to Generate a SUMMARY by SCHOOL'''

SchSum_df = renamed_sch_stu_merged_df.groupby("School Name")

School_Sum = pd.DataFrame({"School Name":sch_df["school_name"], "School Type":sch_df["type"],
                             "Total Budget":sch_df["budget"]})

# .set_index("School Name").sort_values("School Name")
School_Sum = School_Sum.set_index("School Name")
School_Sum = School_Sum.sort_values("School Name")

# School_Sum ["Grade"] = SchSum_df["Grade"]
School_Sum ["Total Students"] = SchSum_df["Student ID"].count()
School_Sum ["Budget/Student"] = School_Sum["Total Budget"]/School_Sum["Total Students"]
School_Sum ["Ave. Reading Score"] = round(SchSum_df["Reading Score"].mean(),2)
School_Sum ["Ave. Math Score"] = round(SchSum_df["Math Score"].mean(),2)

"""## Tried using my code below from earlier calcuation but it returned the incorrect numbers for the % Passing and Overall Passing
# AveReadScor1 = (School_Sum["Ave. Reading Score"])
# AveMathScor1 = (School_Sum["Ave. Math Score"])
# Sch_Tot_Pass_rt = (AveReadScor1 + AveMathScor1)/2
# School_Sum ["% Overall Passing Rate"] = Sch_Tot_Pass_rt
"""

### This code below using lambda works but is NOT my creation. My method returned an average that was incorrect:
School_Sum["% Passing Math"] = round((SchSum_df.apply(lambda x: (x["Math Score"] >= 70).sum()) / 
                                          School_Sum["Total Students"]) * 100, 2)
School_Sum["% Passing Reading"] = round((SchSum_df.apply(lambda x: (x["Reading Score"] >= 70).sum()) / 
                                          School_Sum["Total Students"]) * 100, 2)

School_Sum["Overall Passing Rate"] = round((School_Sum["% Passing Math"] + 
                                               School_Sum["% Passing Reading"]) / 2, 2)

School_Sum

#===========================================================================================================================

# ****** Top Five Performing Schools by Overall Passing Rate *******
School_Sum.sort_values(("Overall Passing Rate"), ascending=False).head()

# ****** Bottom Five Performing Schools by Overall Passing Rate *******
School_Sum.sort_values(("Overall Passing Rate"), ascending=True).head()

# ==========================================================================================================================

"""The following produces the Ave Reading and Math Scores by School and by Grade however I could not figure out _
how to get it into the requested format"""
#Math and Reading scores by School and Grade

import numpy as np
newtest1 = renamed_sch_stu_merged_df.set_index("School Name")
newtest2 = newtest1.groupby(["School Name", "Grade"]).agg(['mean'])
newtest3 = newtest2.sort_values(["School Name", "Grade"], ascending=[True, True])

# newtest3.iloc[:,1:3].reset_index()
AveReadMathScoreBySchandGrd = newtest3.iloc[:,1:3].reset_index()
AveReadMathScoreBySchandGrd

