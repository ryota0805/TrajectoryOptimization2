#パラメータ管理class
import numpy as np

class Parameter:
    N = 50                                                      #系列データの長さ
    M = 5                                                       #設計変数の種類の個数
    WayPoint = np.array([[0, 0], [9, 5], [19, 5], [29, 0]])    #初期パス　[x, y]

    #初期状態と終端状態
    initial_x = 0                                               #x[m]
    terminal_x = 29                                             #x[m]
    initial_y = 0                                               #y[m]
    terminal_y = 0                                              #y[m] 
    initial_theta = 0                                           #theta[rad]
    terminal_theta = 0                                          #theta[rad]
    initial_phi = 0                                             #phi[rad]
    terminal_phi = 0                                            #phi[rad]
    initial_v = 0                                               #v[m/s]
    terminal_v = 0                                              #v[m/s]
    
    
    #変数の範囲
    x_min = -3                                                  #x[m]
    x_max = 32                                                  #x[m]
    y_min = -10                                                 #y[m]
    y_max = 10                                                  #y[m]
    theta_min = -np.pi                                          #theta[rad]
    theta_max = np.pi                                           #tehta[rad]
    phi_min = -np.pi/4                                          #phi[rad]
    phi_max = np.pi/4                                           #phi[rad]
    v_min = 0                                                   #v[m/s]
    v_max = 3                                                   #v[m/s]


    dt = 1                                                      #刻み幅[s]                                             
    L = 1.5                                                     #前輪と後輪の距離[m]

    #障害物のパラメータ 
    #　(x, y, r)
    #　x　: 円の中心座標
    #　y　: 円の中心座標
    #　r　: 半径 
    obstacle_list = [(7, 1, 2), (14, 1, 2), (21, 1, 2)]                   #障害物のパラメータが格納されたリスト
    
    
    #wallのパラメータ
    wall_thick = 1                                #wallの厚さ
    margin = 2
