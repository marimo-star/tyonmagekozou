import streamlit as st
import math

# Streamlitアプリケーションのタイトルを設定
st.title("衛星の軌道計算アプリ")

# ユーザーに衛星の初期高度と燃料の残量を入力してもらう
initial_altitude = st.number_input("初期高度 (km)", min_value=0.0)
remaining_fuel = st.number_input("残りの燃料量 (kg)", min_value=0.0)

# ユーザーが「計算」ボタンをクリックしたときの処理
if st.button("計算"):
    # 地球の半径 (km)
    earth_radius = 6371.0

    # 衛星の初期高度 (km) を地球の半径に加える
    initial_altitude_km = earth_radius + initial_altitude

    # 衛星の速度を計算する関数
    def calculate_velocity(altitude_km):
        # 地球上の引力定数 (m^3/s^2/kg)
        gravitational_constant = 6.67430e-11

        # 地球の質量 (kg)
        earth_mass = 5.972e24

        # 衛星の高度 (m)
        altitude_m = altitude_km * 1000

        # 衛星の速度を計算 (m/s)
        velocity = math.sqrt(gravitational_constant * earth_mass / (earth_radius + altitude_m))

        return velocity

    # 衛星の速度を計算
    initial_velocity = calculate_velocity(initial_altitude_km)

    # 衛星の軌道周回時間を計算 (秒)
    orbital_period = (2 * math.pi * (earth_radius + initial_altitude_km)) / initial_velocity

    # 衛星が燃料切れまでの時間を計算 (秒)
    burnout_time = remaining_fuel / (orbital_period / 2)

    # 結果を表示
    st.subheader("結果")
    st.write(f"初期高度: {initial_altitude} km")
    st.write(f"残りの燃料量: {remaining_fuel} kg")
    st.write(f"衛星の軌道周回時間: {orbital_period} 秒")
    st.write(f"燃料切れまでの時間: {burnout_time} 秒")
