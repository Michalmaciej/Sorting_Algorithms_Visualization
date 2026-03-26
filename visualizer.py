import matplotlib.pyplot as plt
import matplotlib.animation as animation

def visualize(gen, size, max_val, elapsed, name, time_complexity, space_complexity):
    fig, ax = plt.subplots(facecolor="#2b2b2b")
    ax.set_facecolor("#2b2b2b")
    bars = ax.bar(range(size), [0] * size, color="#c0c0c0", edgecolor="#1a1a1a", linewidth=0.5)
    ax.set_ylim(0, max_val * 1.05)
    ax.set_title(name, color="white")
    ax.tick_params(colors="white")

    for spine in ax.spines.values():
        spine.set_edgecolor("#444")

    info = f"Czas: {elapsed:.10f}s  |  Złożoność czasowa: {time_complexity}  |  Złożoność miejsca: {space_complexity}"
    fig.text(0.5, 0.01, info, ha="center", color="white", fontsize=9)

    def update(frame):
        arr, i, j, sorted_info = frame
        n = len(arr)
        for idx, (bar, val) in enumerate(zip(bars, arr)):
            bar.set_height(val)
            if idx == i:
                bar.set_facecolor("#87ceeb")
            elif idx == j:
                bar.set_facecolor("#ff6b6b")
            elif isinstance(sorted_info, frozenset):
                bar.set_facecolor("#50c878" if idx in sorted_info else "#c0c0c0")
            else:
                sorted_left, sorted_right = sorted_info
                bar.set_facecolor("#50c878" if idx < sorted_left or idx >= n - sorted_right else "#c0c0c0")
            bar.set_edgecolor("#1a1a1a")

    first_frame = next(gen)
    update(first_frame)
    plt.show(block=False)
    plt.pause(3)

    ani = animation.FuncAnimation(
        fig, update,
        frames=gen,
        interval=10,
        repeat=False,
        cache_frame_data=False
    )
    plt.show(block=True)
    return ani
