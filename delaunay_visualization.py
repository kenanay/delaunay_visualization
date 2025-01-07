import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay
import matplotlib.animation as animation
from IPython.display import HTML

class DelaunayVisualizer:
    def __init__(self, num_points=20):
        self.num_points = num_points
        # Rastgele noktaları oluştur
        np.random.seed(42)  # Tekrar üretilebilirlik için
        self.points = np.random.rand(num_points, 2)
        # Delaunay üçgenlemesi hesapla
        self.tri = Delaunay(self.points)
        
        # Figure ve axes'i oluştur
        plt.style.use('default')
        self.fig, self.ax = plt.subplots(figsize=(10, 10))
        self.ax.set_title('Delaunay Üçgenlemesi Görselleştirme\nHazırlayan: Kenan AY')
        
    def plot_points(self):
        self.ax.plot(self.points[:,0], self.points[:,1], 'o')
        
    def plot_triangle(self, triangle, color='blue', alpha=0.2):
        vertices = self.points[triangle]
        self.ax.fill(vertices[:,0], vertices[:,1], color=color, alpha=alpha)
        
    def check_delaunay_property(self, triangle):
        vertices = self.points[triangle]
        A = vertices[0]
        B = vertices[1]
        C = vertices[2]
        
        D = 2 * (A[0]*(B[1] - C[1]) + B[0]*(C[1] - A[1]) + C[0]*(A[1] - B[1]))
        if abs(D) < 1e-10:  # Numerik kararlılık için
            return True
            
        center_x = ((A[0]*A[0] + A[1]*A[1])*(B[1] - C[1]) + 
                   (B[0]*B[0] + B[1]*B[1])*(C[1] - A[1]) + 
                   (C[0]*C[0] + C[1]*C[1])*(A[1] - B[1])) / D
        
        center_y = ((A[0]*A[0] + A[1]*A[1])*(C[0] - B[0]) + 
                   (B[0]*B[0] + B[1]*B[1])*(A[0] - C[0]) + 
                   (C[0]*C[0] + C[1]*C[1])*(B[0] - A[0])) / D
        
        center = np.array([center_x, center_y])
        radius = np.linalg.norm(A - center)
        
        # Numerik tolerans ekle
        tolerance = 1e-10
        for i, point in enumerate(self.points):
            if i not in triangle:
                if np.linalg.norm(point - center) < radius - tolerance:
                    return False
        return True
    
    def animate(self, frame):
        self.ax.clear()
        self.ax.set_title('Delaunay Üçgenlemesi Görselleştirme\nHazırlayan: Kenan AY')
        
        # Tüm noktaları çiz
        self.plot_points()
        
        # frame sayısına kadar olan üçgenleri çiz
        for i in range(min(frame + 1, len(self.tri.simplices))):
            triangle = self.tri.simplices[i]
            is_delaunay = self.check_delaunay_property(triangle)
            color = 'green' if is_delaunay else 'red'
            self.plot_triangle(triangle, color=color)
            
            # Üçgenin kenarlarını çiz
            for j in range(3):
                start = self.points[triangle[j]]
                end = self.points[triangle[(j+1)%3]]
                self.ax.plot([start[0], end[0]], [start[1], end[1]], 'k-')
        
        self.ax.set_xlim(-0.1, 1.1)
        self.ax.set_ylim(-0.1, 1.1)
        
        info_text = f'Üçgen {min(frame+1, len(self.tri.simplices))}/{len(self.tri.simplices)}\n'
        info_text += 'Yeşil: Delaunay özelliği sağlanıyor\n'
        info_text += 'Kırmızı: Delaunay özelliği sağlanmıyor'
        self.ax.text(0.02, 0.98, info_text, transform=self.ax.transAxes, 
                    verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    def run_animation(self):
        anim = animation.FuncAnimation(
            self.fig, 
            self.animate,
            frames=len(self.tri.simplices) + 1,
            interval=500,
            repeat=False,
        )
        # Colab için HTML olarak döndür
        return HTML(anim.to_jshtml())

# Çalıştırma kodu
viz = DelaunayVisualizer(num_points=15)
viz.run_animation()
