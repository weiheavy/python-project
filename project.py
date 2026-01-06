import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



tit1 = pd.read_csv("titanic_train.csv")
cleandata = tit1.dropna(subset=["Age"])

def survivedlist():  #function1 存活名單

    global survmale,survfmale
   
    survmale = cleandata[(cleandata["Sex"] == 'male') & (cleandata["Age"] > 20) & (cleandata["Survived"] == 1)]

    survfmale = cleandata[(cleandata["Sex"] == 'female') & (cleandata["Age"] > 20) & (cleandata["Survived"] == 1)]
    
    print("鐵達尼號成年男性存活名單 : \n")
    columns_to_drop = ["PassengerId", "Survived", "Pclass", "SibSp", "Parch", 'Ticket', 'Fare', 'Cabin', 'Embarked']
    survmale = survmale.drop(labels=columns_to_drop, axis=1)
    
    for n in survmale.iloc():
        print("姓名:{} , 性別:{} ,年紀:{}".format(n["Name"], n["Sex"], n["Age"]))
    
    print("鐵達尼號成年女性存活名單 : \n")
    columns_to_drop = ["PassengerId", "Survived", "Pclass", "SibSp", "Parch", 'Ticket', 'Fare', 'Cabin', 'Embarked']
    survfmale = survfmale.drop(labels=columns_to_drop, axis=1)
    
    for n in survfmale.iloc():
        print("姓名:{} , 性別:{} ,年紀:{}".format(n["Name"], n["Sex"], n["Age"]))
     
   

    
        
def deceasedlist():  #function2 死亡名單

    global deceasedmale,deceasedfmale
    
  
    deceasedmale = cleandata[(cleandata["Sex"] == 'male') & (cleandata["Age"] > 20) & (cleandata["Survived"] == 0)]
    
    deceasedfmale = cleandata[(cleandata["Sex"] == 'female') & (cleandata["Age"] > 20) & (cleandata["Survived"] == 0)]
    
    print("鐵達尼號成年男性死亡名單 : \n")
    columns_to_drop = ["PassengerId", "Survived", "Pclass", "SibSp", "Parch", 'Ticket', 'Fare', 'Cabin', 'Embarked']
    deceasedmale = deceasedmale.drop(labels=columns_to_drop, axis=1)
    
    for n in deceasedfmale.iloc():
        print("姓名:{} , 性別:{} ,年紀:{}".format(n["Name"], n["Sex"], n["Age"]))
    
    print("鐵達尼號成年女性死亡名單 : \n")
    columns_to_drop = ["PassengerId", "Survived", "Pclass", "SibSp", "Parch", 'Ticket', 'Fare', 'Cabin', 'Embarked']
    deceasedfmale = deceasedfmale.drop(labels=columns_to_drop, axis=1)
    
    for n in deceasedfmale.iloc():
        print("姓名:{} , 性別:{} ,年紀:{}".format(n["Name"], n["Sex"], n["Age"]))
        
    

    
        
def pie_chart1(num_survmale, num_deceasedmale, num_survfmale, num_deceasedfmale): #function3 圖表1製作


    labels = ['Survived Adult Males', 'Deceased Adult Males', 'Survived Adult Females', 'Deceased Adult Females']
    sizes = [num_survmale, num_deceasedmale, num_survfmale, num_deceasedfmale]
    separated = (0, 0, 0, 0)  
    
    plt.pie(sizes, labels=labels, shadow=True, autopct='%0.0f%%', explode=separated)
    plt.axis('equal')  
    plt.show()
    
    
    # 此圖結論 : 事件中成年男性死亡率明顯最高，而死亡成年女性及存活成年男性數值差異相對小，為另一特點
    
def pie_chart2(): #function4 圖表2製作

   
    pclass_survival = cleandata.groupby(['Pclass', 'Survived']).size().unstack()

    pclass_survival.plot(kind='bar', stacked=False, color=['orange', 'blue'])
    
    plt.title('Survival Counts by Passenger Class')
    
    plt.xlabel('Pclass')
    
    plt.xticks(rotation=90)
    
    plt.ylabel('Count')
    
    plt.legend(title='Survived', labels=['0', '1'], loc='upper right',bbox_to_anchor=(1.01, 1))
    
    plt.show()

    
    # 此圖結論 : 三等艙乘客死亡數超越頭等及二等艙總和，三個等級船艙的存活率卻差不多，足以顯見三等艙人數最多，死亡率也最高
    
    
def pie_chart3(): #function5 圖表3製作
    
    plt.figure(figsize=(10, 6))
    
    
    sns.violinplot(x='Sex', y='Age', hue='Survived', data=cleandata, split=True, palette='muted')
    
    plt.title('Age Distribution by Sex and Survival')
    
    plt.xlabel('Sex')
    
    plt.ylabel('Age')
    

    
    plt.show()

 
    # 此圖結論 : 男性20歲上下死亡率極高，存活年齡則不一定。而女性存活率明顯高於男性。
    
        

def final_result():# 總匯整
    
    survivedlist()
    
    deceasedlist()
    
    num_survmale = len(survmale)
    num_deceasedmale = len(deceasedmale)
    num_survfmale = len(survfmale)
    num_deceasedfmale = len(deceasedfmale)
    
    pie_chart1(num_survmale, num_deceasedmale, num_survfmale, num_deceasedfmale)
    
    pie_chart2()
    
    pie_chart3()
    
    
    
   
    
    
    
    
    
final_result()
    

    
   
    
    
    
    

        
    
    
    
        











#survivedlist("titanic_train.csv")        