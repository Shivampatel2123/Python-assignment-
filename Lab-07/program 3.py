def dept_salary_stats(emp_data):
    salaries = {}
    for emp_id, info in emp_data.items():
        d = info['dept']
        s = info['salary']
        if d not in salaries:
            salaries[d] = []
        salaries[d].append(s)

    stats = {}
    for d, sal in salaries.items():
        stats[d] = {'min': min(sal), 'max': max(sal)}
    return stats

emp_data = {
    101: {'dept': 'Sales', 'salary': 50000},
    102: {'dept': 'Marketing', 'salary': 60000},
    103: {'dept': 'Sales', 'salary': 45000},
    104: {'dept': 'Marketing', 'salary': 70000},
    105: {'dept': 'HR', 'salary': 55000}
}

stats = dept_salary_stats(emp_data)
print(stats)
