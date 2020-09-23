from bokeh.plotting import figure, output_file, show


if __name__ == "__main__":
    output_file('grafic_simple.html')
    fig = figure()

    total_vals = int(input('Cuantos valores quieres graficar: '))
    x_val = list(range(total_vals))
    y_val = []

    for i in x_val:
        val = int(input(f'Valor Y para { i }: '))
        y_val.append(val)

    
    fig.line(x_val, y_val, line_width = 2)
    show(fig)



