鐵達尼號生存數據多維度分析系統
本專案利用經典的鐵達尼號數據集（Titanic Dataset），透過 Python 進行資料清洗、邏輯篩選以及多樣化的資料視覺化分析，藉此探討影響生存率的關鍵因素。

核心技術
資料處理：使用 Pandas 進行數據清洗（處理缺失值）與結構化篩選。

資料視覺化：整合 Matplotlib 與 Seaborn 繪製圓餅圖、長條圖及小提琴圖。

開發邏輯：採用模組化函式（Functional Programming）設計，確保程式碼的可讀性與擴展性。

主要功能
精確名單篩選：自動區分並列印成年男性與女性的存活及死亡詳細名單，並排除不必要的冗餘欄位。

多維度視覺化洞察：

結構分析：透過圓餅圖呈現不同性別群體的生存與遇難比例。

社會階層關聯：分析不同船艙等級（Pclass）與生存率之間的強相關性。

分佈密度分析：利用小提琴圖揭示年齡、性別與生存機率的機率分佈情況。

數據觀察結論
性別與年齡：女性存活率顯著高於男性；男性在 20 歲左右的遇難風險最高。

社會經濟地位：三等艙乘客雖然人數最多，但其遇難人數亦遠超其他等級，反映出逃生機會與艙等之間的聯繫。


Titanic Survival Multi-dimensional Analysis System
This project analyzes the classic Titanic dataset using Python to perform data cleaning, logical filtering, and various data visualizations. The goal is to identify key factors influencing passenger survival rates.

Tech Stack
Data Processing: Pandas for data cleaning (handling missing values) and structured filtering.

Data Visualization: Matplotlib and Seaborn for generating Pie Charts, Bar Charts, and Violin Plots.

Programming Logic: Modular functional design to ensure code readability and scalability.

Key Features
Precise List Filtering: Automatically categorizes and prints detailed lists of survivors and deceased passengers (stratified by adult males/females) while removing redundant data columns.

Multi-dimensional Visualization:

Composition Analysis: Pie charts illustrating the survival vs. mortality ratio across different gender groups.

Social Class Correlation: Analyzing the strong correlation between passenger class (Pclass) and survival outcomes.

Distribution Density: Violin plots revealing the probability distribution of survival based on age and sex.

Data Insights
Gender & Age: Female survival rates were significantly higher than males; males around age 20 faced the highest mortality risk.

Socio-economic Status: Passengers in 3rd class had the highest number of fatalities, significantly exceeding the combined total of 1st and 2nd class, highlighting the link
