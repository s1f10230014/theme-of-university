# ジュースにする野菜(と果物)のリスト
vegetables = ['apple', 'tomato', 'orange']

# トマトをリストから削除

vegetables.pop((vegetables.index('tomato') ))

# vegetablesに入った野菜をジュースにして表示
for s in vegetables:
    print(s + ' juice')