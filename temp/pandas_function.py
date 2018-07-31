# --------------------dropna(axis=1)去掉有缺失值的行------------------------------------------
drop_na_columns = titanic_survival.dropna(axis=1)
new_titanic_survival = titanic_survival.dropna(axis=0,subset=["Age", "Sex"])    #在age和sex列进行dropna操作
print(new_titanic_survival)

# ---------------------------打印83行age列的值和766行pclass列的值-------------------------------
row_index_83_age = titanic_survival.loc[83,"Age"]
row_index_1000_pclass = titanic_survival.loc[766,"Pclass"]
print(row_index_83_age)
print(row_index_1000_pclass)

#---------------------sort_values函数是排序，表示已age列为准进行降序排列---------------------------
new_titanic_survival = titanic_survival.sort_values("Age",ascending=False)
print(new_titanic_survival[0:10])
# -------------------------------重新定义序号------------------------------------------
itanic_reindexed = new_titanic_survival.reset_index(drop=True)
print(titanic_reindexed.iloc[0:10])

# --------------------------------------找出第100行------------------------------------------------
def hundredth_row(column):
    hundredth_item = column.loc[99]
    return hundredth_item
hundredth_row = titanic_survival.apply(hundredth_row)
print(hundredth_row)

# ---------------------------------打印出每行空值的个数----------------------------------------------
def not_null_count(column):
    column_null = pd.isnull(column)
    null = column[column_null]
    return len(null)
column_null_count = titanic_survival.apply(not_null_count)
print(column_null_count)

def which_class(row):
    pclass = row['Pclass']
    if pd.isnull(pclass):
        return "Unknown"
    elif pclass == 1:
        return "First Class"
    elif pclass == 2:
        return "Second Class"
    elif pclass == 3:
        return "Third Class"
classes = titanic_survival.apply(which_class, axis=1)
print(classes)

def is_minor(row):
    if row["Age"] < 18:
        return True
    else:
        return False

minors = titanic_survival.apply(is_minor, axis=1)
#print minors

def generate_age_label(row):
    age = row["Age"]
    if pd.isnull(age):
        return "unknown"
    elif age < 18:
        return "minor"
    else:
        return "adult"

age_labels = titanic_survival.apply(generate_age_label, axis=1)
print(age_labels)

titanic_survival['age_labels'] = age_labels
age_group_survival = titanic_survival.pivot_table(index="age_labels", values="Survived")
print(age_group_survival)
