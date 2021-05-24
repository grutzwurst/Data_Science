# Load data into data frame
df <- data.frame(datasets::esoph)

# Get overview
summary(df)

# Get first 6 rows
head(df)

# Get number of rows and columns
dim(df)

# Get number of cases for age 75+
sum(df[df['agegp'] == '75+', 'ncases'])

# Get number of cases for age 25-34
sum(df[df['agegp'] == '25-34', 'ncases'])

# Get number of cases for people who 
# do not smoke nor drink (or just casually)
sum(df[(df['tobgp'] == '0-9g/day') 
       & (df['alcgp'] =='0-39g/day'), 'ncases'])

# Get number of cases for people who 
# smoke and/or drink
sum(df[(df['tobgp'] != '0-9g/day') 
       & (df['alcgp'] !='0-39g/day'), 'ncases'])

# Do analysis of variance
model1 <- aov(ncases ~ alcgp*tobgp, data = df)
anova(model1)
plot(model1)

# Do analysis of variance
df['a'] = 1
df['a'][df['agegp'] == '35-44'] = 2
df['a'][df['agegp'] == '45-54'] = 3
df['a'][df['agegp'] == '55-64'] = 4
df['a'][df['agegp'] == '65-74'] = 5
df['a'][df['agegp'] == '75+'] = 6

modelLM = lm(ncases ~ a, data = df)
print(modelLM)
anova(modelLM)
plot(modelLM)
