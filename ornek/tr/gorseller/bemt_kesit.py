"""Pal elemanı kesiti ve hız üçgeni: ornek/tr/sunum.md, "5 · Yöntem: BEMT askı modeli" slaydı.

Kullanım: python3 bemt_kesit.py [çıktı.png]   (varsayılan: bu klasördeki bemt_kesit.png)
Gerekli paket: matplotlib. Slayttaki metin_gorsel kutusu ölçüsünde (6,1 inç) çizilir; bütün yazılar 16 pt,
matematik gerçek yazımla (alt indis, eğik değişken, dik diferansiyel d). Etiketler çizgilerin üstüne binmez.
"""
import os, sys, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Polygon, Arc

PT = 16                                   # bütün yazılar tek punto (slaytta 6,1 inç genişlikte gösterilir)
plt.rcParams.update({"font.family": "Helvetica", "font.size": PT, "mathtext.fontset": "stix"})
NAVY, GREY, DARK, FILL = "#022756", "#6E7380", "#1F2433", "#D6DDE9"
W, H = 1220, 730                           # eski görselin piksel ölçüsü; 200 dpi → 6,1 × 3,65 inç
fig = plt.figure(figsize=(W / 200, H / 200), dpi=200)
ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, W); ax.set_ylim(H, 0); ax.axis("off")

def ok(p, q, c, lw=2.2):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>", mutation_scale=22, color=c, lw=lw, shrinkA=0, shrinkB=0))

# hız üçgeni
ok((195, 192), (195, 297), NAVY)                       # U_P, aşağı
ok((195, 297), (470, 297), NAVY)                       # U_T, sağa
ok((195, 192), (470, 297), GREY)                       # U, bileşke
ax.text(180, 233, r"$U_P \;=\; v_i$", ha="right", va="center", color=DARK)
ax.text(330, 325, r"$U_T \;=\; \Omega r$", ha="center", va="center", color=DARK)
ax.text(363, 205, r"$U$", ha="center", va="center", color=GREY)
phi = np.degrees(np.arctan2(105, 275))
ax.add_patch(Arc((470, 297), 340, 340, theta1=180, theta2=180 + phi, color=DARK, lw=1.4))   # y ekseni ters: açı yönü
ax.text(338, 272, r"$\phi$", ha="center", va="center", color=DARK)

# dönme düzlemi
ax.plot([472, 1205], [320, 320], ls=(0, (1, 2.2)), color=GREY, lw=1.6)
ax.text(1203, 296, "dönme düzlemi", ha="right", va="center", color=GREY)

# kesit: NACA 0012, veter (600,296) → (915,383)
le, te = np.array([600.0, 296.0]), np.array([915.0, 383.0])
c = np.linalg.norm(te - le); ang = np.arctan2(te[1] - le[1], te[0] - le[0])
x = (1 - np.cos(np.linspace(0, np.pi, 120))) / 2
t = 5 * 0.12 * (0.2969 * np.sqrt(x) - 0.1260 * x - 0.3516 * x**2 + 0.2843 * x**3 - 0.1036 * x**4)
pts = np.concatenate([np.c_[x, t], np.c_[x[::-1], -t[::-1]]]) * c
R = np.array([[np.cos(ang), -np.sin(ang)], [np.sin(ang), np.cos(ang)]])
ax.add_patch(Polygon(pts @ R.T + le, closed=True, fc=FILL, ec=NAVY, lw=2))
u = (te - le) / c
ax.plot(*np.c_[le - 130 * u, te + 50 * u], ls=(0, (4, 3)), color=GREY, lw=1.5)    # veter doğrultusu
# θ: veter doğrultusu ile dönme düzlemi arasındaki açı; tepe noktası iki çizginin kesiştiği yer
vx = le[0] + (320 - le[1]) / u[1] * u[0]
ax.add_patch(Arc((vx, 320), 2 * (vx - 583), 2 * (vx - 583), theta1=180, theta2=180 + np.degrees(ang), color=DARK, lw=1.4))
ax.text(548, 304, r"$\theta$", ha="center", va="center", color=DARK)

# kuvvetler: dL ⟂ U, dD ∥ U
ok((680, 320), (740, 170), NAVY)
ax.text(768, 155, r"$\mathrm{d}L$", ha="center", va="center", color=DARK)
ok((680, 320), (777, 357), GREY)
ax.text(768, 402, r"$\mathrm{d}D$", ha="center", va="center", color=GREY)

ax.text(1048, 108, r"$\alpha \;=\; \theta \;-\; \phi$", ha="center", va="center", color=DARK)
ax.text(18, 545, "Her $r$ kesitinde d$L$ ve d$D$ hesaplanır; momentum teorisi $v_i$'yi\n"
        "verir; yarıçap boyunca integral askı itkisini ve gücünü verir.", ha="left", va="center", color=DARK, linespacing=1.5)
out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "bemt_kesit.png")
fig.savefig(out, dpi=200, transparent=False, facecolor="white")
