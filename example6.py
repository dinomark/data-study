#%%
import matplotlib.pyplot as plt

plt.plot([1,2,3,4], [12,43,25,15])

plt.show()
#%%
plt.title("plotting")
plt.plot([10,20,30,40])
plt.show()
# %%
plt.title("legend")
plt.plot([10,20,30,40], label="asc")
plt.plot([40,30,20,10], label="desc")
plt.legend()
plt.show()
# %%
# 제목이 color인 그래프를 생성
plt.title("color")
# 그래프 생성(데이터, 색깔, 범례)
plt.plot([10,20,30,40], color='skyblue', label='skyblue')
plt.plot([40,30,20,10], 'pink', label="pink")
#범례 생성
plt.legend()
plt.show()
# %%

plt.title("linestyle")

# 빨간색 dashed 그래프
plt.plot([10, 20, 30, 40], color='r', linestyle='--', label='dashed')
# 초록색 dotted 그래프
plt.plot([40,30,20,10], color='g', ls=':', label="dotted")
# 범례 표시
plt.legend()
plt.show()
# %%
plt.title("marker")
# 빨간색 원형 마커 + 라인 출력 ( 선모양도 같이 출력하고 싶을때는, 색상, 마커모양, 선모양 순으로 사용)
plt.plot([10, 20, 30, 40], 'r.:', label='circle')
# 초록색 삼각형 마커
plt.plot([40, 30, 20, 10], 'g^', label='triangle up')
plt.legend()
plt.show()

# %%
