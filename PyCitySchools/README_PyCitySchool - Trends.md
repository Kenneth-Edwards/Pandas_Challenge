# Pandas for PyCitySchools

## Trends 

1.There appears to be a significant trend toward lower over-all passing rates once the total number of students surpasses 2283 regardless of the fact that the budget per student is larger.
2. The second trend is that the Charter Schools all have significantly across the board higher math and reading scores and higher over-all passing rates with smaller budgets per student.

I did not get to the following sections:
•	Scores by School Spending
•	Scores by School Size
•	Scores by School Type


### NOTE: ### This code using the lambda to compute the % Passing Math and % Reading does work BUT it is NOT my creation. I had help with this part. I had used the code from my District summary but my method returned  percentages that were incorrect:
School_Sum["% Passing Math"] = round((SchSum_df.apply(lambda x: (x["Math Score"] >= 70).sum()) / 
                                          School_Sum["Total Students"]) * 100, 2)
School_Sum["% Passing Reading"] = round((SchSum_df.apply(lambda x: (x["Reading Score"] >= 70).sum()) / 
                                          School_Sum["Total Students"]) * 100, 2)

School_Sum["Overall Passing Rate"] = round((School_Sum["% Passing Math"] + 
                                               School_Sum["% Passing Reading"]) / 2, 2)





