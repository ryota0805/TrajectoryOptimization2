from param import Parameter as p
import GenerateInitialPath
import util
import constraints
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as optimize
import objective_function 
import plot
import time
import animation

####手動でヤコビアンを計算しSQPを実行するプログラム

# 計測開始
start_time = time.time()

#WayPointから設計変数の初期値を計算する
#cubicX, cubicY = GenerateInitialPath.cubic_spline()
cubicX, cubicY = GenerateInitialPath.cubic_spline_by_waypoint(p.WayPoint)
x, y, theta, phi, v = GenerateInitialPath.generate_initialpath2(cubicX, cubicY)
#x, y, theta, phi, v = GenerateInitialPath.generate_initialpath_randomly(cubicX, cubicY)
xs, ys, thetas, phi, v = GenerateInitialPath.initial_zero(0.1)
trajectory_matrix = np.array([x, y, theta, phi, v])
trajectory_vector = util.matrix_to_vector(trajectory_matrix)

#目的関数の設定
func = objective_function.objective_function2
jac_of_objective_function = objective_function.jac_of_objective_function2

args = (1, 1)

#制約条件の設定
cons = constraints.generate_cons_with_jac()

#変数の範囲の設定
bounds = constraints.generate_bounds()

#オプションの設定
options = {'maxiter':10000, 'ftol': 1e-6}


#最適化を実行
result = optimize.minimize(func, trajectory_vector, args = args, method='SLSQP', jac = jac_of_objective_function, constraints=cons, bounds=bounds, options=options)

# 計測終了
end_time = time.time()

#最適化結果の表示
print(result)
plot.vis_env()
#plot.vis_path(trajectory_vector)
plot.compare_path(trajectory_vector, result.x)
plot.compare_history_theta(trajectory_vector, result.x, range_flag = True)
plot.compare_history_phi(trajectory_vector, result.x, range_flag = True)
plot.compare_history_v(trajectory_vector, result.x, range_flag = True)
#plot.vis_history_theta(result.x, range_flag=True)
#plot.vis_history_phi(result.x, range_flag=True)
#plot.vis_history_v(result.x, range_flag = True)
#plot.compare_path_rec(trajectory_vector, result.x)

# 経過時間を計算
elapsed_time = end_time - start_time
print(f"実行時間: {elapsed_time}秒")
xs, ys, thetas, _, _ = util.generate_result(result.x)
print(list(xs), list(ys))
animation.gen_movie(xs, ys, thetas)

sum1, sum2, sum3, sum4 = objective_function.check_objective_function2(result.x, *args)
print('steer:{},speed:{},forward:{},backward:{}'.format(sum1, sum2, sum3, sum4))