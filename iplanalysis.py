import matplotlib.pyplot as plt
import pandas as pd

# Load datasets
matches = pd.read_csv("matches.csv")
deliveries = pd.read_csv("deliveries.csv")
# 1 plt bar 
wins = matches['match_winner'].value_counts()#ksi colm m uniqe value count krna
plt.figure(figsize=(10,5))#figure ka size batana
plt.bar(wins.index,wins.values)#bar graphbanega,x-team,y-win
plt.title("Team Wise Wins")
plt.xticks(rotation=90) #for rotation
plt.show()
# 2 histogram
plt.hist(matches['first_ings_score'].dropna(),bins='auto')#dropna missing value hata deta h,bins kitne group m data divide krna hai bins ki range select bhi kar sakte hai bins(range(100,120,170))
plt.title("first innings score")
plt.show()
# 3 pie chart
toss=matches['toss_decision'].value_counts()
plt.pie(toss.values,labels=toss.index,autopct="%1.2f%%")# toss value degi number ki toss bat ya ball kitni bar choose hua ,toss index toss bat ya ball h,autopct percent show karta hai
plt.title("Toss Decision")
plt.show()
# 4 line graph
runs_per_over=deliveries.groupby('over')['runs_of_bat'].sum()#.sum() data add karna groupby se over ka hisab hoga aur bad m isliye.sum() use kiya hai kyuki groupby inke sath use hota
plt.plot(runs_per_over.index,runs_per_over.values)#index-xaxis aur .valuess-yaxis
plt.title("Runs per Over")
plt.show()
#5 bar graph
top=matches[['top_scorer','highscore']].dropna()
top=top.groupby('top_scorer')['highscore'].max().sort_values(ascending=False).head(10)# groupby se top scorer ke hisab se group krna h aur bad m unka highscore aur sort krna aur ascending order m dena true ascending false descendinh
plt.figure(figsize=(10,5))
plt.barh(top.index,top.values)
plt.title("Top 10")
plt.gca().invert_yaxis()#invert y axis pr krne ko
plt.show()
#box plot 
plt.boxplot(matches['first_ings_score'].dropna())
plt.title('First Innings Score Distribution')
plt.show()
#subplots
wins = matches['match_winner'].value_counts()
toss = matches['toss_decision'].value_counts()

fig, ax = plt.subplots(1,3, figsize=(15,4))

ax[0].bar(wins.index, wins.values)
ax[0].set_title("Wins")

ax[1].pie(toss.values, labels=toss.index)
ax[1].set_title("Toss")

ax[2].hist(matches['first_ings_score'].dropna())
ax[2].set_title("Score")

plt.tight_layout()
plt.show()
# OO Api 
# wins = matches['match_winner'].value_counts()
# toss = matches['toss_decision'].value_counts()

fig, ax = plt.subplots()
ax.bar(wins.index, wins.values)
ax.set_title("Team Wins")
ax.set_xlabel("Teams")
ax.set_ylabel("wins")
plt.xticks(rotation=90)

plt.show()
