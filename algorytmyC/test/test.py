import matplotlib.pyplot as plt 
import sys
def plot_graph(coords_file, edges_file, output_image="graph_result.png"):
 nodes = {}
 try:
    with open(coords_file, 'r') as f:
        for line in f:
            parts = line.split()
            if len(parts) == 3:
                node_id = int(parts[0])
                x, y = float(parts[1]), float(parts[2])
                nodes[node_id] = (x, y) 
 except Exception as e:
    print(f"Błąd odczytu współrzędnych: {e}")
    return

 plt.figure(figsize=(10, 10))

 try:
    with open(edges_file, 'r') as f:
        for line in f:
            parts = line.split()
            if len(parts) >= 2:
                try:
                    u, v = int(parts[0]), int(parts[1])
                except ValueError:
                    u, v = int(parts[1]), int(parts[2])

                if u in nodes and v in nodes:
                    x_values = [nodes[u][0], nodes[v][0]]
                    y_values = [nodes[u][1], nodes[v][1]]
                    # Rysowanie linii łączącej dwa węzły
                    plt.plot(x_values, y_values, color='skyblue', zorder=1, alpha=0.6)
 except Exception as e:
  print(f"Błąd odczytu krawędzi: {e}")


x_coords = [n[0] for n in nodes.values()]
y_coords = [n[1] for n in nodes.values()]

plt.scatter(x_coords, y_coords, color='navy', zorder=2, s=100)

for node_id, (x, y) in nodes.items():
    plt.text(x, y, f" {node_id}", fontsize=9, verticalalignment='bottom')

plt.title("Wizualizacja grafu - Weryfikacja algorytmu layoutu")
plt.grid(True, linestyle='--', alpha=0.7)
plt.axis('equal') 
plt.savefig(output_image)
print(f"Sukces! Wizualizacja została zapisana w pliku: {output_image}")
 
if __name__ == "__main__":
 if len(sys.argv) < 3:
  print("Użycie: python visualize_graph.py <wspolrzedne.txt> <krawedzie.txt>") 
 else: 
  plot_graph(sys.argv[1], sys.argv[2])
