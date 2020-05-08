The resources for this dataset can be found at https://www.openml.org/d/1067

Author: Mike Chapman, NASA  
Source: [tera-PROMISE](http://openscience.us/repo/defect/mccabehalsted/kc1.html) - 2004  
Please cite: Sayyad Shirabad, J. and Menzies, T.J. (2005) The PROMISE Repository of Software Engineering Databases. School of Information Technology and Engineering, University of Ottawa, Canada.  
  
KC1 Software defect prediction  
One of the NASA Metrics Data Program defect data sets. Data from software for storage management for receiving and processing ground data. Data comes from McCabe and Halstead features extractors of source code.  These features were defined in the 70s in an attempt to objectively characterize code features that are associated with software quality.

### Attribute Information  

1. loc             : numeric % McCabe's line count of code
2. v(g)            : numeric % McCabe "cyclomatic complexity"
3. ev(g)           : numeric % McCabe "essential complexity"
4. iv(g)           : numeric % McCabe "design complexity"
5. n               : numeric % Halstead total operators + operands
6. v               : numeric % Halstead "volume"
7. l               : numeric % Halstead "program length"
8. d               : numeric % Halstead "difficulty"
9. i               : numeric % Halstead "intelligence"
10. e               : numeric % Halstead "effort"
11. b               : numeric % Halstead 
12. t               : numeric % Halstead's time estimator
13. lOCode          : numeric % Halstead's line count
14. lOComment       : numeric % Halstead's count of lines of comments
15. lOBlank         : numeric % Halstead's count of blank lines
16. lOCodeAndComment: numeric
17. uniq_Op         : numeric % unique operators
18. uniq_Opnd       : numeric % unique operands
19. total_Op        : numeric % total operators
20. total_Opnd      : numeric % total operands
21. branchCount     : numeric % of the flow graph
22. problems        : {false,true} % module has/has not one or more reported defects

### Relevant papers  

- Shepperd, M. and Qinbao Song and Zhongbin Sun and Mair, C. (2013)
Data Quality: Some Comments on the NASA Software Defect Datasets, IEEE Transactions on Software Engineering, 39.

- Tim Menzies and Justin S. Di Stefano (2004) How Good is Your Blind Spot Sampling Policy? 2004 IEEE Conference on High Assurance
Software Engineering.

- T. Menzies and J. DiStefano and A. Orrego and R. Chapman (2004) Assessing Predictors of Software Defects", Workshop on Predictive Software Models, Chicago
