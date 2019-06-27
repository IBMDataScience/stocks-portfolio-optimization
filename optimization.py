mdl = Model(name='stocks_portfolio')
df_stocks['frac'] = mdl.continuous_var_list(df_stocks.index, name='frac', ub=1)

# sum of fractions equal 100%
mdl.add_constraint(mdl.sum(df_stocks.frac) == 1);

# ensure minimal return on investment
target_return = .09
actual_return = mdl.dot(df_stocks.frac, df_stocks['ret'])
mdl.add_kpi(actual_return, 'ROI')
ct_return = mdl.add_constraint(actual_return >= target_return)

# KPIs
fracs = df_stocks.frac
variance = mdl.sum(float(df_var[s1][s2]) * fracs[s1] * fracs[s2] for s1 in df_stocks.index for s2 in df_stocks.index)
mdl.add_kpi(variance, 'Variance')

# finally the objective function
mdl.minimize(variance)

# solve the quadratic problem
mdl.solve(url=None, key=None)
mdl.report()
