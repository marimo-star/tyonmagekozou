import streamlit as st
import math

# Streamlitアプリケーションのタイトルを設定
st.title("宇宙から大気圏への落下時間計算アプリ")

# ユーザーに物体の情報を入力してもらう
mass = st.number_input("物体の質量 (kg)", min_value=0.0)
cross_sectional_area = st.number_input("物体の断面積 (m^2)", min_value=0.0)
initial_altitude = st.number_input("初期高度 (km)", min_value=0.0)
initial_velocity = st.number_input("初速度 (m/s)", min_value=0.0)
drag_coefficient = st.number_input("抗力係数 (0から2の間の値)", min_value=0.0, max_value=2.0)

# ユーザーが「計算」ボタンをクリックしたときの処理
if st.button("計算"):
    # 定数
    gravitational_acceleration = 9.81  # 重力加速度 (m/s^2)
    earth_radius = 6371.0  # 地球の半径 (km)

    # 初期高度 (m) を設定
    initial_altitude_m = initial_altitude * 1000.0

    # 大気密度 (kg/m^3) のモデル化
    air_density = 1.225 * math.exp(-initial_altitude_m / 8500.0)

    # 落下時間を計算
    time_to_fall = 0.0
    while initial_altitude_m > 0:
        # 物体にかかる重力と抗力の計算
        gravitational_force = mass * gravitational_acceleration
        drag_force = 0.5 * air_density * initial_velocity**2 * cross_sectional_area * drag_coefficient

        # 速度の変化を計算
        acceleration = (gravitational_force - drag_force) / mass
        initial_velocity += acceleration
        initial_altitude_m -= initial_velocity

        # 時間を更新
        time_to_fall += 1  # 1秒ごとに更新

    # 結果を表示
    st.subheader("結果")
    st.write(f"物体の質量: {mass} kg")
    st.write(f"物体の断面積: {cross_sectional_area} m^2")
    st.write(f"初期高度: {initial_altitude} km")
    st.write(f"初速度: {initial_velocity} m/s")
    st.write(f"抗力係数: {drag_coefficient}")
    st.write(f"落下時間: {time_to_fall} 秒")

